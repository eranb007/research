"""Invented offline analogues. No original source, eval, network or model output."""
import json
def textual_gate(text): return 'obsolete_read(' not in text
def narrow_admission(operation, target): return target=='record'
def reference(value): return [value, value+1]
def mutant(value): return [] if value==2 else reference(value)
def require(condition):
    if not condition:
        raise ValueError("invented boundary control failed")

def demo():
    # Same invented local behavior; comment-only text changes admission.
    plain='fetch_current(value)'
    commented=plain+' # obsolete_read(value)'
    local=lambda value:[value,value+1]
    require(textual_gate(plain) and not textual_gate(commented))
    require(local(4)==reference(4))
    # A target-only gate cannot establish a read-only task contract.
    require(narrow_admission('read','record'))
    require(narrow_admission('write','record'))
    allowed=lambda operation: operation=='read'
    require(allowed('read') and not allowed('write'))
    require(not narrow_admission('read','unrelated'))
    # Finite checked inputs miss the intentionally excluded branch.
    require(all(mutant(i)==reference(i) for i in [0,1]))
    require(mutant(2)!=reference(2) and reference(2)==[2,3])
    return {'status':'PASS','invented_boundary_examples':3,'counterpart_controls_present':True,'historical_results_reproduced':False,'model_observations':0}
if __name__=='__main__':print(json.dumps(demo(),sort_keys=True))
