import sys, importlib.abc
class Block(importlib.abc.MetaPathFinder):
    def find_spec(self, name, path, target=None):
        if name.split('.')[0] in ('gemmi','rdkit'):
            raise ImportError(f'blocked {name}')
        return None
if sys.argv[1]=='block': sys.meta_path.insert(0, Block())
import molecular.receptor_materialization as rm
print('after domain import gemmi loaded:', 'gemmi' in sys.modules)
import molecular.receptor_parsing as rp
print('after adapter import gemmi loaded:', 'gemmi' in sys.modules, 'rdkit' in sys.modules)
try:
    rp.parse_receptor_cif_dom021(b'data_x\n_a.b 1\n')
    print('parse ok; gemmi', rp.gemmi.__version__)
except rm.MaterializationConfigurationError as e:
    print('config error', getattr(e,'code',None))
