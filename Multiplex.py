#file created: 11/11/2021 02:50:33 PM

import pandas as pd
from io import StringIO

#dataframe String
inputString = """       Volume  StartPlate StartPosition EndPosition
0   16.046307           1            A1          A1
1    3.286709           1            B1          A1
2    4.484029           1            C1          A1
3    3.989652           1            D1          A1
4    3.452516           1            E1          A1
5    3.252540           1            F1          A1
6    3.680920           1            G1          A1
7    3.695080           1            H1          A1
8    3.879127           1            A2          B1
9    3.317177           1            B2          B1
10   3.511416           1            C2          B1
11   3.598423           1            D2          B1
12   3.816129           1            E2          B1
13   3.838873           1            F2          B1
14   3.577496           1            G2          B1
15   4.361160           1            H2          C1
16   3.213028           1            A3          C1
17   3.163277           1            B3          C1
18   3.530664           1            C3          C1
19   3.313162           1            D3          C1
20   3.291056           1            E3          C1
21   3.481938           1            F3          C1
22   3.834839           1            G3          C1
23   2.358999           1            H3          D1
24   2.546630           1            A4          D1
25   3.509840           1            B4          D1
26   3.505570           1            C4          D1
27   2.524321           1            D4          D1
28   2.639445           1            E4          D1
29   2.515391           1            F4          D1
30   2.346160           1            G4          D1
31   3.139515           2            A1          G1
32   7.552766           2            B1          G1
33   6.865204           2            C1          G1
34   5.485422           2            D1          G1
35   3.877753           2            E1          G1
36   7.403651           2            F1          G1
37   2.737226           2            G1          G1
38   4.403958           2            H1          H1
39   2.935027           2            A2          H1
40   6.154451           2            B2          H1
41   4.150557           2            C2          H1
42   3.026869           2            D2          H1
43   2.841351           2            E2          H1
44   6.403509           2            F2          H1
45   4.010989           2            G2          H1
46   5.509157           2            H2          A2
47   3.984136           2            A3          A2
48   3.847235           2            B3          A2
49   4.352838           2            C3          A2
50   4.493598           2            D3          A2
51   7.205844           2            E3          A2
52   6.956554           2            F3          A2
53   4.526471           2            G3          B2
54   8.949003           2            H3          B2
55   5.658915           2            A4          B2
56   5.247269           2            B4          B2
57   4.253088           2            C4          B2
58   6.758425           2            D4          B2
59   3.372136           3            A1          E1
60   6.303972           3            C1          E1
61   3.448384           3            D1          E1
62   2.905897           3            E1          E1
63   2.887658           3            F1          E1
64   2.927181           3            B2          F1
65   3.037448           3            E2          F1
66   7.620042           3            F2          F1
67   2.789667           3            G2          F1"""

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
  
'''
volume = []
for index, row in inputTable.iterrows():
  volume.append(row['Volume'])

inputTable.to_string()
'''