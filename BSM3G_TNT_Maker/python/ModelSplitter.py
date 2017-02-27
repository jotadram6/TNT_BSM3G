import ROOT
##########################
#Loading full tree to read
##########################
MainChain=ROOT.TChain("TNT/BOOM")
MainChain.Add("root://cmsxrootd.fnal.gov//store/user/jruizalv/VBF-C1N2_leptonicDecays_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/VBF_SUSY_signal/170227_004332/0000/OutTreeModelInfo_1.root")
MainChain.Add("root://cmsxrootd.fnal.gov//store/user/jruizalv/VBF-C1N2_leptonicDecays_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/VBF_SUSY_signal/170227_004332/0000/OutTreeModelInfo_2.root")
MainChain.Add("root://cmsxrootd.fnal.gov//store/user/jruizalv/VBF-C1N2_leptonicDecays_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/VBF_SUSY_signal/170227_004332/0000/OutTreeModelInfo_3.root")
MainChain.Add("root://cmsxrootd.fnal.gov//store/user/jruizalv/VBF-C1N2_leptonicDecays_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/VBF_SUSY_signal/170227_004332/0000/OutTreeModelInfo_4.root")
MainChain.Add("root://cmsxrootd.fnal.gov//store/user/jruizalv/VBF-C1N2_leptonicDecays_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/VBF_SUSY_signal/170227_004332/0000/OutTreeModelInfo_5.root")
MainChain.Add("root://cmsxrootd.fnal.gov//store/user/jruizalv/VBF-C1N2_leptonicDecays_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/VBF_SUSY_signal/170227_004332/0000/OutTreeModelInfo_6.root")
MainChain.Add("root://cmsxrootd.fnal.gov//store/user/jruizalv/VBF-C1N2_leptonicDecays_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/VBF_SUSY_signal/170227_004332/0000/OutTreeModelInfo_7.root")
MainChain.Add("root://cmsxrootd.fnal.gov//store/user/jruizalv/VBF-C1N2_leptonicDecays_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/VBF_SUSY_signal/170227_004332/0000/OutTreeModelInfo_8.root")
MainChain.Add("root://cmsxrootd.fnal.gov//store/user/jruizalv/VBF-C1N2_leptonicDecays_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/VBF_SUSY_signal/170227_004332/0000/OutTreeModelInfo_9.root")
MainChain.Add("root://cmsxrootd.fnal.gov//store/user/jruizalv/VBF-C1N2_leptonicDecays_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/VBF_SUSY_signal/170227_004332/0000/OutTreeModelInfo_10.root")
#MainChain.Add("/home/jose/VBF_DM_ROOT_FILES/OutTreeModelInfo.root")
MainChain.LoadTree(0)
#MainChain.Print("p")
##########################
#Creating skimmed tree
##########################
SkimmedTree = MainChain.GetTree().CloneTree(0)
#SkimmedTree.Print("p")
MainChain.CopyAddresses(SkimmedTree)
##########################
#Geetting models histogram
##########################
#MainChain.Draw("configmodel.c_str() >> SignalModels","")
#ModelsHisto=ROOT.gDirectory.Get("SignalModels")
#ModelsHisto.Draw("")
#TotalBins=ModelsHisto.GetNbinsX()
#print "Total of models:", TotalBins
#BASEOUTPUT="root://cmsxrootd.fnal.gov//store/user/jruizalv/VBF-C1N2_leptonicDecays_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/VBF_SUSY_signal/170227_004332/0000/"
BASEOUTPUT=""
NumberOfEntries=MainChain.GetEntries()
SkimmedTree.Reset()
for j in xrange(NumberOfEntries):
    MainChain.GetEntry(j)
    if j==0: 
        print MainChain.configmodel.c_str()
        CurrentModel = MainChain.configmodel.c_str()
        output = ROOT.TFile.Open(BASEOUTPUT+CurrentModel+".root","RECREATE")
        output.mkdir("TNT"); output.cd("TNT")
    if CurrentModel==MainChain.configmodel.c_str():
        #print "Same model:", MainChain.configmodel.c_str()
        SkimmedTree.Fill()
    else:
        print MainChain.configmodel.c_str()
        SkimmedTree.Write()
        output.Close()
        SkimmedTree.Reset()
        CurrentModel = MainChain.configmodel.c_str()
        output = ROOT.TFile.Open(BASEOUTPUT+CurrentModel+".root","RECREATE")
        output.mkdir("TNT"); output.cd("TNT")
        print "Next model:", MainChain.configmodel.c_str()
        SkimmedTree.Fill()

SkimmedTree.Write()
output.Close()
