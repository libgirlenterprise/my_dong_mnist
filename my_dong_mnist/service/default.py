from __future__ import division
import json
import numpy
import dong.framework
from ..model.init.defaultload import DefaultloadModelInit


class DefaultService(DefaultloadModelInit, dong.framework.Service):

    @dong.framework.request_handler
    def inference(self, request_body, mime_type='application/json'):

        data = json.loads(request_body)
        x = numpy.array(data) / 255.0
        return json.dumps(self.predict(x).tolist())

    @dong.framework.request_handler
    def hello(self, request_body, mime_type='application/json'):

        return json.dumps('hello')
