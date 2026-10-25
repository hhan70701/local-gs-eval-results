"""Run the unmodified metric pipeline for one setup, capturing summary inputs for exact merging."""
import inspect,json,os,sys
from pathlib import Path
import numpy as np
ROOT=Path(__file__).resolve().parents[2];sys.path.insert(0,str(ROOT))
from scripts import evaluate
original=evaluate.write_summary
def encode(v):
 if isinstance(v,np.generic):return v.item()
 if isinstance(v,np.ndarray):return v.tolist()
 if isinstance(v,Path):return str(v)
 raise TypeError(type(v).__name__)
def capture(*args,**kwargs):
 b=inspect.signature(original).bind(*args,**kwargs);b.apply_defaults();data=dict(b.arguments);path=Path(data.pop('path'))
 path.parent.mkdir(parents=True,exist_ok=True)
 (path.parent/'summary_payload.json').write_text(json.dumps(data,default=encode))
 return original(*args,**kwargs)
evaluate.write_summary=capture
evaluate.main()
