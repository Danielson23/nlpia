""" File utilities comparable to similarly named bash utils: rm_rf(), rm_f(), and mkdir_p() """
import os
from pugnlp.futil import expand_path, mkdir_p  # noqa


def ls(path, force=False):
    """ bash `ls -a`: List both file paths or directory contents (files and directories)

    >>> ls('.')
    [...]
    >>> ls('~/')
    [...]
    >>> ls(os.path.join('.', __name__))).endswith(os.path.join('nlpia', 'futil.py'))
    True
    """
    path = expand_path(path)
    if os.path.isfile(path):
        return path
    elif os.path.isdir(path):
        return os.listdir(path)
    elif not force:
        return os.listdir(path)
    try:
        return os.listdir(path)
    except:
        pass


def ls_a(path, force=False):
    """ bash `ls -a`: List both file paths or directory contents (files and directories)

    >>> path = ls(os.path.join('.', __name__)))
    >>> path.endswith(os.path.join('nlpia', 'futil.py'))
    True
    """
    return ls(path, force=force)


def rm_r(path, force=False):
    """ bash `rm -r`: Recursively remove dirpath. If `force==True`, don't raise exception if path doesn't exist.

    >>> rm_r('/tmp/nlpia_dir_that_doesnt_exist_3.141591234/', force=True)
    >>> rm_r('/tmp/nlpia_dir_that_doesnt_exist_3.141591234/')
    Traceback (most recent call last):
      ...
    """
    paths = ls(path, force=force)
    if isinstance(paths, list):
        for p in paths:
            rm_r(p, force=force)
    elif isinstance(paths, str):
        rm_r(paths, force=force)
    if force:
        return None
    return os.removedir(path)


def rm_rf(path):
    """ bash `rm -rf`: Recursively remove dirpath. Don't raise exception if path doesn't exist.

    >>> rm_rf('/tmp/nlpia_dir_that_doesnt_exist_3.141591234/')
    """
    return rm_r(path, force=True)

