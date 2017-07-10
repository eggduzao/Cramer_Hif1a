
# export PATH=/home/egg/Installation/HINT/bin:$PATH
# export PYTHONPATH=/home/eg474423/Installation/HINT/lib/python2.7/site-packages:$PYTHONPATH

# Import
import os

# Direction Loop
extBothList = [True]
for eb in extBothList:

  # Extension Loop
  extList = ["3"]
  for ext in extList:

    # Parameters
    if(eb):
      ext_both_directions = "--ext-both-directions"
      oname = "twoside"
    else:
      ext_both_directions = ""
      oname = "oneside"
    dnase_norm_per = "--dnase-norm-per=99"
    dnase_slope_per = "--dnase-slope-per=99"
    dnase_frag_ext = "--dnase-frag-ext="+ext
    hmm_file = "--hmm-file=/work/eg474423/eg474423_Projects/trunk/TfbsPrediction/Results/ATAC/HMM/Models_ATAC/K562/Model/regular.hmm"
    inputMatrix = "/home/egg/Projects/Thorsten/Results/thorsten/large_intestine/footprints/exp_mat/InputMatrix.txt"
    organism = "--organism=mm9"
    outLoc = "/home/egg/Projects/Thorsten/Results/thorsten/large_intestine/footprints/results/"
    os.system("mkdir -p "+outLoc)
    output_location = "--output-location="+outLoc

    # Execution
    clusterCommand = "rgt-hint "+organism+" "+output_location+" "+ext_both_directions+" "+hmm_file+" "
    clusterCommand += dnase_norm_per+" "+dnase_slope_per+" "+dnase_frag_ext+" "+inputMatrix
    os.system(clusterCommand)

    #myL = "_".join(["ATAC"])
    #clusterCommand = "bsub -J "+myL+" -o "+myL+"_out.txt -e "+myL+"_err.txt "
    #clusterCommand += "-W 100:00 -M 12000 -S 100 -P izkf -R \"select[hpcwork]\" ./hint_pipeline.zsh "
    #clusterCommand += organism+" "+output_location+" "+ext_both_directions+" "+hmm_file+" "
    #clusterCommand += dnase_norm_per+" "+dnase_slope_per+" "+dnase_frag_ext+" "+inputMatrix
    #os.system(clusterCommand)


