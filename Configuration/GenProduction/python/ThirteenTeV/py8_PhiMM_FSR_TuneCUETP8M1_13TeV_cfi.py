import FWCore.ParameterSet.Config as cms
from Configuration.Generator.Pythia8CommonSettings_cfi import *
from Configuration.Generator.Pythia8CUEP8M1Settings_cfi import *

generator = cms.EDFilter("Pythia8GeneratorFilter",
    pythiaPylistVerbosity = cms.untracked.int32(0),
    filterEfficiency = cms.untracked.double(0.026),
    pythiaHepMCVerbosity = cms.untracked.bool(False),
    crossSection = cms.untracked.double(30560000.0),
    comEnergy = cms.double(13000.0),
    maxEventsToPrint = cms.untracked.int32(0),
    PythiaParameters = cms.PSet(
         pythia8CommonSettingsBlock,
         pythia8CUEP8M1SettingsBlock,
         processParameters = cms.vstring(
             'SoftQCD:all = on',                          
             '333:onMode = off',                          # Turn off phi decays
             '333:onIfMatch = 13 -13',                    # just let phi -> mu+ mu-
            # 'PhaseSpace:pTHatMin = 2.'                   # be aware of this ckin(3) equivalent
         ),
         parameterSets = cms.vstring(
             'pythia8CommonSettings',
             'pythia8CUEP8M1Settings',
             'processParameters',
         )
    )
)

#filter two muons in the phi(1020) mass region
mumugenfilter = cms.EDFilter("MCParticlePairFilter",
    Status = cms.untracked.vint32(1, 1),
    MinPt = cms.untracked.vdouble(0.5, 0.5),
    MinP = cms.untracked.vdouble(0., 0.),
    MaxEta = cms.untracked.vdouble(2.5, 2.5),
    MinEta = cms.untracked.vdouble(-2.5, -2.5),
    MinInvMass = cms.untracked.double(0.5),
    MaxInvMass = cms.untracked.double(1.5),
    ParticleCharge = cms.untracked.int32(-1),
    ParticleID1 = cms.untracked.vint32(13),
    ParticleID2 = cms.untracked.vint32(13)
)

oniafilter = cms.EDFilter("PythiaFilter",
    Status = cms.untracked.int32(2),
    MaxEta = cms.untracked.double(1000.0),
    MinEta = cms.untracked.double(-1000.0),
    MinPt = cms.untracked.double(5.0),
    ParticleID = cms.untracked.int32(333)
)

ProductionFilterSequence = cms.Sequence(generator*oniafilter*mumugenfilter)
