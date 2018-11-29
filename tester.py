from mmdnn.conversion.pytorch.pytorch_parser import PytorchParser

parser = PytorchParser('/media/slomkarafa/HDD0/Projects/android/py_to_tf/model.pth',[3,224,224])
# parser = PytorchParser(dens,(3,224,224))
parser.run('out/sen')