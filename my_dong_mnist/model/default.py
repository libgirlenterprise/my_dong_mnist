from .init.default import DefaultModelInit
import dong.framework

class DefaultModel(DefaultModelInit, dong.framework.Model):

    from .train.default import train
    from .serializer.default import write
