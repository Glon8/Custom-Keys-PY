import os
import time
import shutil

from .values import op
from .helpers import switch, dir_mtime, files_count
from .visuals import render


# ===================================< SAVES SNATCHER
def snt_switch():
    ks = op[1]['stat']
    snt = op[5]

    switch(op[5], 'stat')

    if ks:
        if snt['stat'] and snt['backup_time'] == -1 and snt['dir_files'] == 0:
            if isinstance(snt['path_to'], str) and os.path.exists(snt['path_to']):
                # raw dst name
                dst_name = os.path.basename(snt['path_from'].rstrip('\\/'))
                # edited destination
                dst_path = os.path.join(snt['path_to'], dst_name)
                # recover backup specks
                mtime = dir_mtime(dst_path)
                snt['backup_time'] = mtime if mtime != 0 else -1
                snt['dir_files'] = files_count(dst_path)

        render()


def snt_prot():
    snt = op[5]

    if snt['stat']:
        p_from = snt['path_from']
        p_to = snt['path_to']
        # raw dst name
        dst_name = os.path.basename(p_from.rstrip('\\/'))
        # edited destination
        dst_path = os.path.join(p_to, dst_name)

        if isinstance(p_from, str) and isinstance(p_to, str):
            if os.path.exists(p_from) and os.path.exists(p_to):
                # mtime of the origins
                new_time = dir_mtime(p_from)
                # inner files check
                new_count = files_count(p_from)

                if new_time > snt['backup_time'] and new_count > snt['dir_files']:
                    # slight delay < game has a delay between ~0 to 3 seconds to overwrite
                    time.sleep(3)
                    # delete old backed file
                    if os.path.exists(dst_path):
                        shutil.rmtree(dst_path)
                    # copy creation
                    shutil.copytree(p_from, dst_path, dirs_exist_ok=True)
                    # time update
                    snt['backup_time'] = new_time
                    snt['dir_files'] = new_count
                    render()

            # self_replace - ll replace the backed up, in to original folder
            if snt['self_replace']:
                # check if backup has files
                backup = files_count(dst_path)
                # files count in original folder
                origin = files_count(p_from)
                # mtime check may break, flag may be needed!
                if (not os.path.exists(p_from) or origin == 0 or origin < backup) and (
                        os.path.exists(dst_path) and backup > 0):
                    # slight delay < game may delete files to rewrite < may trigger a loop
                    time.sleep(0.3)
                    # double check files count in original folder
                    origin_del = files_count(p_from)
                    # if folder size stays the same then copy
                    if origin == origin_del:
                        # copy creation
                        shutil.copytree(dst_path, p_from, dirs_exist_ok=True)
