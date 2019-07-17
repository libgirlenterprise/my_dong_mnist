from dong.framework import HyperParameterConfig, HyperParameterTuner
import copy

class DefaultTune(HyperParameterTuner):

    def get_hyper_parameter_config_list(self):

        return []
        
