"""Regenerate the aggregate curation figure; no model performance comparison."""
import pathlib
from check import read_csv, validate_coverage, COVERAGE_COLUMNS
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
R=pathlib.Path(__file__).resolve().parents[1]
def plot():
    rows=validate_coverage(read_csv(R/'results/reconciliation-coverage.csv', COVERAGE_COLUMNS))
    reviewed=[int(x['reviewed_fields']) for x in rows]
    remaining=[int(x['unreviewed_fields']) for x in rows]
    fig,ax=plt.subplots(figsize=(10,5.5))
    fig.subplots_adjust(left=.10,right=.98,bottom=.26,top=.82)
    ax.barh(range(3),reviewed,color='#245b78',label='Reviewed selected fields')
    ax.barh(range(3),remaining,left=reviewed,color='#d8a343',label='Unreviewed selected fields')
    for i,(a,b) in enumerate(zip(reviewed,remaining)):
        ax.text(a/2,i,str(a),ha='center',va='center',color='white',weight='bold')
        if b:ax.text(a+b/2,i,str(b),ha='center',va='center',color='#252525')
    ax.set_yticks(range(3),[x['checkpoint'] for x in rows]);ax.invert_yaxis()
    ax.set_xlim(0,585);ax.set_xticks([0,100,200,300,400,500,585])
    ax.set_xlabel('Selected disagreement fields (fixed denominator: 585)')
    ax.set_title('Review coverage of the selected ledger',loc='left',weight='bold')
    ax.spines[['top','right']].set_visible(False)
    ax.legend(loc='upper center',bbox_to_anchor=(.5,-.30),ncol=2,frameon=False)
    fig.suptitle('Curation progress, not model performance or complete historical adjudication',fontsize=10,y=.97)
    out=R/'figures';out.mkdir(exist_ok=True)
    with matplotlib.rc_context({'svg.hashsalt':'research-preview-coverage', 'svg.fonttype':'none'}):
        fig.savefig(out/'reconciliation-coverage.svg',metadata={'Date':None})
        fig.savefig(out/'reconciliation-coverage.png',dpi=160,metadata={'Software':'Research preview figure generator'})
    plt.close(fig)
if __name__=='__main__':plot()
