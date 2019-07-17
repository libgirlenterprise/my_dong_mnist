

def write(self, save_dir):
    export_path = save_dir + 'my_model_weights.hdf5'
    self.save_weights(export_path)
    
def read(self, save_dir):
    export_path = save_dir + 'my_model_weights.hdf5'
    self.load_weights(export_path)
