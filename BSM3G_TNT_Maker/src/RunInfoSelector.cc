// Authors:  Alfredo Gurrola (Vanderbilt University)
// Andres Florez: Universidad de los Andes, Colombia.
// kaur amandeepkalsi: Panjab University, India.

#include "NtupleMaker/BSM3G_TNT_Maker/interface/RunInfoSelector.h"

RunInfoSelector::RunInfoSelector(std::string name, TTree* tree, bool debug, const pset& iConfig):baseTree(name,tree,debug) {
  if(debug) std::cout << "BSM3G TNT Maker: In the RunInfoSelector Constructor --> calling SetBranches()." << std::endl;
  /*
  edm::Handle<GenEventInfoProduct> genEvt;
  iEvent.getByToken(generatorToken_,genEvt);
  weightevt = genEvt->weight();
 
  if(debug_) std::cout << "     GenEventWeightSelector: Extracted the event weight." << std::endl;
  
  edm::Handle<GenLumiInfoHeader> gen_header;
  iLumi.getByToken(genLumiHeader_, gen_header);
  string model = gen_header->configDescription();
  std::cout << model << std::endl;
  */
  SetBranches();
}

RunInfoSelector::~RunInfoSelector(){
  delete tree_;
}

void RunInfoSelector::Fill(const edm::Event& iEvent){
  Clear(); 

  if(debug_) std::cout << "     RunInfoSelector: Re-initialized the variables and extracting the run number, event number, and lumi block." << std::endl;

  runNumber = iEvent.id().run();
  eventNumber = iEvent.id().event();
  if( iEvent.isRealData() ) {
    lumiBlock = iEvent.luminosityBlock();
  } else {
    lumiBlock = -1;
  }
  
}

void RunInfoSelector::SetBranches(){
  if(debug_) std::cout << "     RunInfoSelector: Setting branches by calling AddBranch of baseTree." << std::endl;

  AddBranch(&runNumber            ,"runNumber");
  AddBranch(&eventNumber          ,"eventNumber");
  AddBranch(&lumiBlock            ,"lumiBlock");

  if(debug_) std::cout << "     RunInfoSelector: Finished setting branches." << std::endl;
}

void RunInfoSelector::Clear(){
  runNumber = -1;
  eventNumber = -1;
  lumiBlock = -1;
}

/*void beginLuminosityBlock(edm::LuminosityBlock const& iLumi, edm::EventSetup const& iEventSetup){
  genLumiHeader_ = iCC.consumes<GenLumiInfoHeader>(iConfig.getParameter<edm::InputTag>("genmodelinfo"));
  edm::Handle<GenLumiInfoHeader> gen_header;
  iLumi.getByToken(genLumiHeader_, gen_header);
  string model = gen_header->configDescription();
  std::cout << model << std::endl;  // prints, e.g. T1tttt_1500_100
  }*/

