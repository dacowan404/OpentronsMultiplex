
inputTable = pd.read_csv(StringIO(inputString), sep='\s+')

metadata = {
    'protocolName': '96wellPlateToPlate',
    'author': 'David Cowan <dcowan2@emory.edu>',
    'source': 'Protocol Library',
    'apiLevel': '2.3'
    }

tiprack_slots = ['7', '8', '9']

def run(protocol):

  wellheight = 0.9
  finishPlate = protocol.load_labware('biorad_96_wellplate_200ul_pcr', 2, 'Finish Plate')
  startPlate1 = protocol.load_labware('biorad_96_wellplate_200ul_pcr', 4, 'Start Plate 1')
  startPlate2 = protocol.load_labware('biorad_96_wellplate_200ul_pcr', 5, 'Start Plate 2')
  startPlate3 = protocol.load_labware('biorad_96_wellplate_200ul_pcr', 6, 'Start Plate 3')
  startPlates = [startPlate1, startPlate2, startPlate3]

  tip_name = 'opentrons_96_tiprack_20ul'
  tipracks = [protocol.load_labware(tip_name, slot) for slot in tiprack_slots]
  pipette = protocol.load_instrument("p20_single_gen2", "left", tip_racks=tipracks)
   
  #transfers samples to plate, pauses to allow user to change out samples
  for index, row in inputTable.iterrows():
    currentVolume = row['Volume']
    if currentVolume <= 0:
      continue
    currentPlate = startPlates[(row['StartPlate']-1)]

    pipette.transfer(currentVolume, 
      currentPlate[row['StartPosition']].bottom(z=wellheight), 
      finishPlate[row['EndPosition']].bottom(z=wellheight), 
      new_tip="always")

  protocol.home()
  
