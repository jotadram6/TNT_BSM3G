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
MainChain.LoadTree(0)
#MainChain.Print("p")
##########################
#Geetting models histogram
##########################
MainChain.Draw("configmodel.c_str() >> SignalModels","")
ModelsHisto=ROOT.gDirectory.Get("SignalModels")
#ModelsHisto.Draw("")
NumberOfModels=ModelsHisto.GetNbinsX()
print "Total of models:", NumberOfModels
Models=[]
print "Entries per bin"
for i in xrange(NumberOfModels):
    Models.append(ModelsHisto.GetXaxis().GetBinLabel(i+1))
    print ModelsHisto.GetXaxis().GetBinLabel(i+1), ModelsHisto.GetBinContent(i+1)
print Models
del(ModelsHisto)
for i in Models:
    #print "Processing ... "+i
    #if Models.index(i)<1 or Models.index(i)>=11: continue
    output = ROOT.TFile.Open(i+".root","RECREATE")
    output.mkdir("TNT"); output.cd("TNT")
    SkimmedTree = MainChain.CopyTree('strstr(configmodel.c_str(),\"'+i+'\")')
    output = SkimmedTree.GetCurrentFile()
    output.Write()
    print "Total entries for", i, SkimmedTree.GetEntries() 
    output.Close()
    del(SkimmedTree); del(output)
