'''Media file class'''
import os


class MediaFile:
    '''General media object, has methods for general I/O'''

    def __init__(self, fpath):
        if not os.path.exists(fpath):
            raise IOError('{} does not exist'.format(fpath))
        if not os.path.isfile(fpath):
            raise IOError('{} is not a file'.format(fpath))
        self._fullpath = fpath

    def __repr__(self):
        return '{} Object: {}'.format(self.__class__.__name__, self._fullpath)

    @property
    def exists(self):
        '''Whether the mediafile exists or not'''
        return os.path.exists(self._fullpath)

    @property
    def filename(self):
        '''Filename of mediafile'''
        _, filename = os.path.split(self._fullpath)
        return filename

    @property
    def filepath(self):
        '''Filepath of mediafile'''
        return self._fullpath

    @property
    def dirpath(self):
        '''Directory path mediafile is contained within'''
        mdir, _ = os.path.split(self._fullpath)
        return mdir

    @property
    def ext(self):
        '''Extension of mediafile'''
        _, ext = os.path.splitext(self._fullpath)
        return ext

    @property
    def file_prefix(self):
        '''Filename without extension'''
        fprefix, _ = os.path.splitext(self.filename)
        return fprefix

    @property
    def size(self):
        '''Filesize of mediafile'''
        return os.path.getsize(self._fullpath)
