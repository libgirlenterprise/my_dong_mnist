from .default import DefaultModelInit
from ...data.default import DefaultData


class DefaultloadModelInit(DefaultModelInit):

    from ..serializer.default import read

    def __init__(self, config={}, data_params=None, save_dir=None):

        data = DefaultData()
        super().__init__(config,
                         data_params=data.get_data_params(),
                         save_dir=save_dir)
        self.read(save_dir)
