from typing import List, Any, Union

import numpy as np

gd = {'data': 'file'}

# setting up the data for the first gas (CF4)


gd['gas1/Sym'] = "CF4"

XENG1 = [np.float32(0.0), np.float32(.001), np.float32(.002), np.float32(.003), np.float32(.004), np.float32(.005),
         np.float32(.006), np.float32(.007), np.float32(.008), np.float32(.009),
         np.float32(0.01), np.float32(.012), np.float32(.014), np.float32(.016), np.float32(.018), np.float32(0.02),
         np.float32(.025), np.float32(0.03), np.float32(.035), np.float32(0.04),
         np.float32(.045), np.float32(0.05), np.float32(.055), np.float32(0.06), np.float32(.065), np.float32(0.07),
         np.float32(.075), np.float32(0.08), np.float32(.085), np.float32(0.09),
         np.float32(0.10), np.float32(0.12), np.float32(0.14), np.float32(0.17), np.float32(0.20), np.float32(0.24),
         np.float32(0.30), np.float32(0.40), np.float32(0.50), np.float32(0.60),
         np.float32(0.80), np.float32(1.00), np.float32(1.20), np.float32(1.40), np.float32(1.70), np.float32(2.00),
         np.float32(3.00), np.float32(5.00), np.float32(6.00), np.float32(7.00),
         np.float32(8.00), np.float32(9.00), np.float32(10.0), np.float32(12.0), np.float32(15.0), np.float32(20.0),
         np.float32(25.0), np.float32(30.0), np.float32(40.0), np.float32(50.0),
         np.float32(60.0), np.float32(80.0), np.float32(100.), np.float32(125.), np.float32(150.), np.float32(200.),
         np.float32(250.), np.float32(300.), np.float32(400.), np.float32(500.),
         np.float32(600.), np.float32(700.), np.float32(800.), np.float32(1000.), np.float32(1250.), np.float32(1500.),
         np.float32(1750.), np.float32(2000.), np.float32(2500.), np.float32(3000.),
         np.float32(3500.), np.float32(4000.), np.float32(5000.), np.float32(6000.), np.float32(7000.),
         np.float32(8000.), np.float32(9000.), np.float32(10000.), 1.25e4, 1.50e4,
         1.75e4, 2.0e4, 2.5e4, 3.0e4, 3.5e4, 4.0e4, 4.5e4, 5.0e4, 6.0e4, 7.0e4,
         8.0e4, 9.0e4, 1.0e5, 1.25e5, 1.5e5, 1.75e5, 2.0e5, 2.5e5, 3.0e5, 3.5e5,
         4.0e5, 4.5e5, 5.0e5, 6.0e5, 7.0e5, 8.0e5, 9.0e5, 1.0e6, 1.25e6, 1.5e6,
         1.75e6, 2.0e6, 2.5e6, 3.0e6, 3.5e6, 4.0e6, 4.5e6, 5.0e6, 6.0e6, 7.0e6,
         8.0e6, 9.0e6, 1.0e7, 1.25e7, 1.5e7, 1.75e7, 2.0e7, 2.5e7, 3.0e7, 3.5e7,
         4.0e7, 4.5e7, 5.0e7, 6.0e7, 7.0e7, 8.0e7, 9.0e7, 1.0e8, 1.25e8, 1.5e8,
         1.75e8, 2.0e8, 2.5e8, 3.0e8, 3.5e8, 4.0e8, 4.5e8, 5.0e8, 6.0e8, 7.0e8,
         8.0e8, 9.0e8, 1.0e9,
         ]
# ELASTIC MOMENTUM TRANSFER X-SECTION

YELMG1 = [np.float32(12.5), np.float32(8.70), np.float32(7.00), np.float32(5.95), np.float32(5.20), np.float32(4.70),
          np.float32(4.30), np.float32(3.95), np.float32(3.65), np.float32(3.40),
          np.float32(3.20), np.float32(2.85), np.float32(2.58), np.float32(2.37), np.float32(2.19), np.float32(2.04),
          np.float32(1.77), np.float32(1.57), np.float32(1.41), np.float32(1.30),
          np.float32(1.20), np.float32(1.12), np.float32(1.05), np.float32(0.99), np.float32(0.93), np.float32(0.88),
          np.float32(0.84), np.float32(0.80), np.float32(0.76), np.float32(0.72),
          np.float32(0.65), np.float32(0.48), np.float32(0.35), np.float32(0.29), np.float32(0.29), np.float32(0.34),
          np.float32(0.47), np.float32(0.87), np.float32(1.35), np.float32(1.85),
          np.float32(2.95), np.float32(4.00), np.float32(4.75), np.float32(5.15), np.float32(5.45), np.float32(5.65),
          np.float32(5.80), np.float32(6.00), np.float32(6.10), np.float32(6.30),
          np.float32(6.50), np.float32(6.80), np.float32(7.20), np.float32(8.30), np.float32(9.50), np.float32(10.1),
          np.float32(9.60), np.float32(8.80), np.float32(7.85), np.float32(6.72),
          np.float32(5.90), np.float32(5.06), np.float32(4.16), np.float32(3.57), np.float32(2.99), np.float32(1.92),
          np.float32(1.53), np.float32(1.20), np.float32(0.88), np.float32(0.66),
          np.float32(.525), np.float32(0.43), np.float32(0.37), np.float32(0.30), np.float32(.228), np.float32(.169),
          np.float32(.131), np.float32(.104), np.float32(.0711), np.float32(.0519),
          np.float32(.0397), np.float32(.0314), np.float32(.0212), np.float32(.0153), np.float32(.0117),
          np.float32(.00918), np.float32(.00743), np.float32(.00615), np.float32(.00412), np.float32(.00297),
          2.25e-3, 1.77e-3, 1.18e-3, 8.51e-4, 6.45e-4, 5.08e-4, 4.12e-4, 3.41e-4,
          2.47e-4, 1.88e-4,
          1.49e-4, 1.21e-4, 1.01e-4, 6.88e-5, 5.05e-5, 3.90e-5, 3.13e-5, 2.17e-5,
          1.62e-5, 1.27e-5,
          1.03e-5, 8.56e-6, 7.27e-6, 5.49e-6, 4.34e-6, 3.54e-6, 2.96e-6, 2.52e-6,
          1.81e-6, 1.36e-6,
          1.07e-6, 8.68e-7, 6.08e-7, 4.53e-7, 3.51e-7, 2.82e-7, 2.31e-7, 1.93e-7,
          1.42e-7, 1.08e-7,
          8.59e-8, 6.98e-8, 5.79e-8, 3.89e-8, 2.80e-8, 2.12e-8, 1.66e-8, 1.10e-8,
          7.86e-9, 5.90e-9,
          4.59e-9, 3.68e-9, 3.01e-9, 2.13e-9, 1.58e-9, 1.22e-9, 9.75e-10, 7.92e-10,
          5.10e-10, 3.56e-10,
          2.62e-10, 2.01e-10, 1.29e-10, 8.95e-11, 6.58e-11, 5.04e-11, 3.98e-11,
          3.23e-11, 2.24e-11, 1.65e-11,
          1.26e-11, 9.96e-12, 8.07e-12,
          ]
# ELASTIC X-SECTION ASSUMED ISOTROPIC BELOW 0.6 EV

YELTG1 = [np.float32(12.5), np.float32(8.70), np.float32(7.00), np.float32(5.95), np.float32(5.20), np.float32(4.70),
          np.float32(4.30), np.float32(3.95), np.float32(3.65), np.float32(3.40),
          np.float32(3.20), np.float32(2.85), np.float32(2.58), np.float32(2.37), np.float32(2.19), np.float32(2.04),
          np.float32(1.77), np.float32(1.57), np.float32(1.41), np.float32(1.30),
          np.float32(1.20), np.float32(1.12), np.float32(1.05), np.float32(0.99), np.float32(0.93), np.float32(0.88),
          np.float32(0.84), np.float32(0.80), np.float32(0.76), np.float32(0.72),
          np.float32(0.65), np.float32(0.48), np.float32(0.35), np.float32(0.29), np.float32(0.29), np.float32(0.34),
          np.float32(0.47), np.float32(0.87), np.float32(1.35), np.float32(1.85),
          np.float32(3.77), np.float32(4.89), np.float32(5.66), np.float32(6.43), np.float32(7.43), np.float32(8.34),
          np.float32(10.6), np.float32(12.5), np.float32(11.6), np.float32(11.0),
          np.float32(11.0), np.float32(11.7), np.float32(12.9), np.float32(14.5), np.float32(16.8), np.float32(17.6),
          np.float32(18.1), np.float32(17.2), np.float32(15.9), np.float32(14.9),
          np.float32(14.3), np.float32(13.0), np.float32(11.7), np.float32(10.5), np.float32(9.65), np.float32(8.10),
          np.float32(6.83), np.float32(6.02), np.float32(5.02), np.float32(4.36),
          np.float32(3.83), np.float32(3.40), np.float32(3.08), np.float32(2.65), np.float32(2.17), np.float32(1.89),
          np.float32(1.55), np.float32(1.40), np.float32(1.19), np.float32(1.11),
          np.float32(.921), np.float32(.822), np.float32(.696), np.float32(.568), np.float32(.492), np.float32(.435),
          np.float32(.390), np.float32(.353), np.float32(.286), np.float32(.241),
          np.float32(.209), np.float32(.185), np.float32(.150), np.float32(.127), np.float32(.111), np.float32(.0984),
          np.float32(.0888), np.float32(.0810), np.float32(.0694), np.float32(.0611),
          np.float32(.0522), np.float32(.050), np.float32(.0461), np.float32(.0391), np.float32(.0344),
          np.float32(.0311), np.float32(.0287), np.float32(.0253), np.float32(.0230), np.float32(.0214),
          np.float32(.0202), np.float32(.0193), np.float32(.0186), np.float32(.0176), np.float32(.0169),
          np.float32(.0164), np.float32(.0160), np.float32(.0157), np.float32(.0152), np.float32(.0148),
          np.float32(.0146), np.float32(.0145), np.float32(.0143), np.float32(.0142), np.float32(.0141),
          np.float32(.0141), np.float32(.0140), np.float32(.0140), np.float32(.0140), np.float32(.0139),
          np.float32(.0139), np.float32(.0139), np.float32(.0139), np.float32(.0139), np.float32(.01389),
          np.float32(.01389), np.float32(.01389), np.float32(.01388), np.float32(.01388), np.float32(.01388),
          np.float32(.01388), np.float32(.01388), np.float32(.01388), np.float32(.01388), np.float32(.01388),
          np.float32(.01388), np.float32(.01388), np.float32(.01388), np.float32(.01388), np.float32(.01388),
          np.float32(.01388), np.float32(.01388), np.float32(.01388), np.float32(.01388), np.float32(.01388),
          np.float32(.01388), np.float32(.01388), np.float32(.01388), np.float32(.01388), np.float32(.01388),
          np.float32(.01388), np.float32(.01388), np.float32(.01388),
          ]
# EPSILON FOR ELASTIC ANGULAR DISTRIBUTION

# EPSILON =1-YEPS

YEPSG1 = [np.float32(1.0), np.float32(1.0), np.float32(1.0), np.float32(1.0), np.float32(1.0), np.float32(1.0),
          np.float32(1.0), np.float32(1.0), np.float32(1.0), np.float32(1.0), np.float32(1.0), np.float32(1.0),
          np.float32(1.0), np.float32(1.0), np.float32(1.0), np.float32(1.0), np.float32(1.0), np.float32(1.0),
          np.float32(1.0), np.float32(1.0), np.float32(1.0), np.float32(1.0), np.float32(1.0), np.float32(1.0),
          np.float32(1.0), np.float32(1.0), np.float32(1.0), np.float32(1.0), np.float32(1.0), np.float32(1.0),
          np.float32(1.0), np.float32(1.0), np.float32(1.0), np.float32(1.0), np.float32(1.0), np.float32(1.0),
          np.float32(1.0), np.float32(1.0), np.float32(1.0), np.float32(1.0),
          np.float32(.68056), np.float32(.73101), np.float32(.76161), np.float32(.70664), np.float32(.61270),
          np.float32(.53797), np.float32(.37888), np.float32(.30604), np.float32(.35505),
          np.float32(.40830),
          np.float32(.42979), np.float32(.41826), np.float32(.39140), np.float32(.40794), np.float32(.39986),
          np.float32(.40963), np.float32(.36006), np.float32(.33951), np.float32(.32037),
          np.float32(.27671),
          np.float32(.23985), np.float32(.21859), np.float32(.18948), np.float32(.17666), np.float32(.15292),
          np.float32(.10180), np.float32(.09358), np.float32(.07880), np.float32(.06538),
          np.float32(.05301),
          np.float32(.04608), np.float32(.04117), np.float32(.03833), np.float32(.03532), np.float32(.03188),
          np.float32(.02561), np.float32(.02374), np.float32(.019986), np.float32(.015005),
          np.float32(.010925),
          np.float32(.009845), np.float32(.008442), np.float32(.006348), np.float32(.005446), np.float32(.004667),
          np.float32(.004028), np.float32(.003554), np.float32(.003186),
          np.float32(.002530), np.float32(.002096),
          np.float32(.001783), np.float32(.001549), np.float32(.001228), np.float32(.001016), np.float32(.000859),
          np.float32(.000749), np.float32(.000661), np.float32(.000590),
          np.float32(.000486), np.float32(.000411),
          3.53e-4, 3.12e-4, 2.78e-4, 2.17e-4, 1.76e-4, 1.47e-4, 1.26e-4, 9.61e-5,
          7.68e-5, 6.32e-5,
          5.32e-5, 4.56e-5, 3.97e-5, 3.10e-5, 2.30e-5, 2.07e-5, 1.74e-5, 1.49e-5,
          1.07e-5, 8.04e-6,
          6.28e-6, 5.05e-6, 3.47e-6, 2.54e-6, 1.94e-6, 1.53e-6, 1.24e-6, 1.02e-6,
          7.33e-7, 5.51e-7,
          4.30e-7, 3.44e-7, 2.82e-7, 1.84e-7, 1.30e-7, 9.62e-8, 7.42e-8, 4.80e-8,
          3.35e-8, 2.47e-8,
          1.89e-8, 1.50e-8, 1.21e-8, 8.388e-9, 6.133e-9, 4.669e-9, 3.666e-9,
          2.950e-9, 1.858e-9, 1.271e-9,
          9.21e-10, 6.97e-10, 4.37e-10, 2.98e-10, 2.16e-10, 1.63e-10, 1.28e-10,
          1.02e-10, 7.00e-11, 5.10e-11,
          3.80e-11, 3.00e-11, 2.40e-11,
          ]
#  VIBRATION V4 (RESONANCE ONLY) SCALED BY 1/E**3 ABOVE 50EV

XVBV4G1 = [np.float32(0.0783), np.float32(4.00), np.float32(5.00), np.float32(6.00), np.float32(7.00), np.float32(8.00),
           np.float32(9.00), np.float32(10.0), np.float32(15.0), np.float32(20.0),
           np.float32(50.0),
           ]
YVBV4G1 = [np.float32(0.0), np.float32(0.0), np.float32(0.05), np.float32(0.35), np.float32(1.06), np.float32(1.40),
           np.float32(1.26), np.float32(0.97), np.float32(0.07), np.float32(.022),
           1.e-3,
           ]
#  VIBRATION V1 (RESONANCE ONLY) SCALED BY 1/E**3 ABOVE 50EV

XVBV1G1 = [np.float32(0.1126), np.float32(4.00), np.float32(5.00), np.float32(6.00), np.float32(7.00), np.float32(8.00),
           np.float32(9.00), np.float32(10.0), np.float32(15.0), np.float32(20.0),
           np.float32(50.0),
           ]
YVBV1G1 = [np.float32(0.0), np.float32(0.0), np.float32(.016), np.float32(.118), np.float32(0.36), np.float32(0.47),
           np.float32(0.42), np.float32(0.33), np.float32(.023), np.float32(.007),
           3.e-4,
           ]
#  VIBRATION V3 (RESONANCE ONLY) SCALED BY 1/E**3 ABOVE 50EV

XVBV3G1 = [np.float32(0.1588), np.float32(4.00), np.float32(5.00), np.float32(6.00), np.float32(7.00), np.float32(8.00),
           np.float32(9.00), np.float32(10.0), np.float32(15.0), np.float32(20.0),
           np.float32(50.0),
           ]
YVBV3G1 = [np.float32(0.0), np.float32(0.0), np.float32(0.15), np.float32(1.05), np.float32(3.19), np.float32(4.20),
           np.float32(3.78), np.float32(2.90), np.float32(0.20), np.float32(.067),
           3.e-3,
           ]
#  VIBRATION HARMONIC 2(V3) SCALED BY 1/E ABOVE 50EV

XVIB5G1 = [np.float32(0.3176), np.float32(1.00), np.float32(4.00), np.float32(5.00), np.float32(6.00), np.float32(7.00),
           np.float32(8.00), np.float32(9.00), np.float32(10.0), np.float32(15.0),
           np.float32(20.0), np.float32(50.0),
           ]
YVIB5G1 = [np.float32(0.0), np.float32(.001), np.float32(0.01), np.float32(.031), np.float32(0.23), np.float32(0.67),
           np.float32(0.87), np.float32(0.79), np.float32(0.60), np.float32(.042),
           np.float32(.014), np.float32(.0006),
           ]
# VIBRATION HARMONIC (3(V3) + ALL OTHER HARMONICS)

#  SCALED BY 1/E ABOVE 50 EV

XVIB6G1 = [np.float32(0.4764), np.float32(1.00), np.float32(4.00), np.float32(5.00), np.float32(6.00), np.float32(7.00),
           np.float32(8.00), np.float32(9.00), np.float32(10.0), np.float32(15.0),
           np.float32(20.0), np.float32(50.0),
           ]
YVIB6G1 = [np.float32(0.0), np.float32(.0009), np.float32(.045), np.float32(.117), np.float32(.774), np.float32(2.32),
           np.float32(3.06), np.float32(2.75), np.float32(2.12), np.float32(.138),
           np.float32(.037), np.float32(.0018),
           ]
#

#  DISSOCATIVE IONISATION :

#  WEIGHTED AVERAGE OF SIEGLAFF AND NISHIMURA FOR SINGLE IONISATION AND

#  DOUBLE IONISATION.

#  FOR DOUBLE IONISATION WITH BREAKUP :  BRUCE ET AL CPL 190(1992)285

#  NB.  (USED NISHIMURA ONLY BELOW 30EV)

#

# CF3 +

XCF3G1 = [np.float32(15.7), np.float32(16.0), np.float32(17.0), np.float32(18.0), np.float32(19.0), np.float32(20.0),
          np.float32(22.0), np.float32(24.0), np.float32(26.0), np.float32(28.0),
          np.float32(30.0), np.float32(35.0), np.float32(40.0), np.float32(45.0), np.float32(50.0), np.float32(60.0),
          np.float32(70.0), np.float32(80.0), np.float32(90.0), np.float32(100.),
          np.float32(120.), np.float32(140.), np.float32(160.), np.float32(200.), np.float32(250.), np.float32(300.),
          np.float32(400.), np.float32(500.), np.float32(600.), np.float32(800.),
          np.float32(1000.), np.float32(1250.), np.float32(1500.), np.float32(1750.), np.float32(2000.),
          np.float32(2500.), np.float32(3000.),
          ]
YCF3G1 = [np.float32(0.0), np.float32(.032), np.float32(.075), np.float32(.128), np.float32(.191), np.float32(.276),
          np.float32(.448), np.float32(.610), np.float32(.866), np.float32(1.08),
          np.float32(1.26), np.float32(1.72), np.float32(2.05), np.float32(2.35), np.float32(2.62), np.float32(2.94),
          np.float32(3.13), np.float32(3.24), np.float32(3.32), np.float32(3.35),
          np.float32(3.38), np.float32(3.34), np.float32(3.27), np.float32(3.17), np.float32(3.00), np.float32(2.81),
          np.float32(2.54), np.float32(2.28), np.float32(2.09), np.float32(1.77),
          np.float32(1.56), np.float32(1.32), np.float32(1.15), np.float32(1.05), np.float32(.937), np.float32(.804),
          np.float32(.692),
          ]
# CF2+

XCF2G1 = [np.float32(21.47), np.float32(24.0), np.float32(26.0), np.float32(28.0),
          np.float32(30.0), np.float32(35.0), np.float32(40.0), np.float32(45.0), np.float32(50.0), np.float32(60.0),
          np.float32(70.0), np.float32(80.0), np.float32(90.0), np.float32(100.),
          np.float32(120.), np.float32(140.), np.float32(160.), np.float32(200.), np.float32(250.), np.float32(300.),
          np.float32(400.), np.float32(500.), np.float32(600.), np.float32(800.),
          np.float32(1000.), np.float32(1250.), np.float32(1500.), np.float32(1750.), np.float32(2000.),
          np.float32(2500.), np.float32(3000.),
          ]
YCF2G1 = [np.float32(0.00), np.float32(.003), np.float32(.010), np.float32(.032),
          np.float32(.060), np.float32(.131), np.float32(.148), np.float32(.162), np.float32(.192), np.float32(.221),
          np.float32(.234), np.float32(.243), np.float32(.256), np.float32(.263),
          np.float32(.266), np.float32(.260), np.float32(.257), np.float32(.240), np.float32(.233), np.float32(.212),
          np.float32(.186), np.float32(.169), np.float32(.152), np.float32(.131),
          np.float32(.113), np.float32(.0961), np.float32(.0834), np.float32(.0763), np.float32(.0681),
          np.float32(.0585), np.float32(.0503),
          ]
# CF+

XCF1G1 = [np.float32(29.14),
          np.float32(30.0), np.float32(35.0), np.float32(40.0), np.float32(45.0), np.float32(50.0), np.float32(60.0),
          np.float32(70.0), np.float32(80.0), np.float32(90.0), np.float32(100.),
          np.float32(120.), np.float32(140.), np.float32(160.), np.float32(200.), np.float32(250.), np.float32(300.),
          np.float32(400.), np.float32(500.), np.float32(600.), np.float32(800.),
          np.float32(1000.), np.float32(1250.), np.float32(1500.), np.float32(1750.), np.float32(2000.),
          np.float32(2500.), np.float32(3000.),
          ]
YCF1G1 = [np.float32(0.00),
          np.float32(.0024), np.float32(.0145), np.float32(.0583), np.float32(.107), np.float32(.156), np.float32(.185),
          np.float32(.226), np.float32(.239), np.float32(.238), np.float32(.266),
          np.float32(.274), np.float32(.259), np.float32(.261), np.float32(.234), np.float32(.227), np.float32(.186),
          np.float32(.146), np.float32(.122), np.float32(.113), np.float32(.0909),
          np.float32(.0820), np.float32(.0695), np.float32(.0603), np.float32(.0552), np.float32(.0493),
          np.float32(.0423), np.float32(.0364),
          ]
# DATA CF3 2+

XCF32G1 = [np.float32(41.0), np.float32(45.0), np.float32(50.0), np.float32(60.0), np.float32(70.0), np.float32(80.0),
           np.float32(90.0), np.float32(100.), np.float32(120.), np.float32(140.),
           np.float32(160.), np.float32(200.), np.float32(250.), np.float32(300.), np.float32(400.), np.float32(500.),
           np.float32(600.), np.float32(800.), np.float32(1000.), np.float32(1250.),
           np.float32(1500.), np.float32(1750.), np.float32(2000.), np.float32(2500.), np.float32(3000.),
           ]
YCF32G1 = [np.float32(0.00), np.float32(.0053), np.float32(.0083), np.float32(.0104), np.float32(.0135),
           np.float32(.0154), np.float32(.0164), np.float32(.0187), np.float32(.0208),
           np.float32(.0198),
           np.float32(.0208), np.float32(.0198), np.float32(.0187), np.float32(.0167), np.float32(.0135),
           np.float32(.0114), np.float32(.0101), np.float32(.0079), np.float32(.0065), np.float32(.0055),
           np.float32(.0048), np.float32(.0044), np.float32(.0039), np.float32(.0033), np.float32(.0029),
           ]
# C+

XCF0G1 = [np.float32(34.77), np.float32(35.0), np.float32(40.0), np.float32(45.0), np.float32(50.0), np.float32(60.0),
          np.float32(70.0), np.float32(80.0), np.float32(90.0), np.float32(100.),
          np.float32(120.), np.float32(140.), np.float32(160.), np.float32(200.), np.float32(250.), np.float32(300.),
          np.float32(400.), np.float32(500.), np.float32(600.), np.float32(800.),
          np.float32(1000.), np.float32(1250.), np.float32(1500.), np.float32(1750.), np.float32(2000.),
          np.float32(2500.), np.float32(3000.),
          ]
YCF0G1 = [np.float32(0.0), np.float32(.0005), np.float32(.0093), np.float32(.0426), np.float32(.0884), np.float32(.134),
          np.float32(.172), np.float32(.193), np.float32(.207), np.float32(.228),
          np.float32(.245), np.float32(.246), np.float32(.249), np.float32(.236), np.float32(.222), np.float32(.191),
          np.float32(.166), np.float32(.144), np.float32(.134), np.float32(.104),
          np.float32(.0895), np.float32(.0759), np.float32(.0658), np.float32(.0602), np.float32(.0538),
          np.float32(.0462), np.float32(.0397),
          ]
# F+

XC0FG1 = [np.float32(34.5), np.float32(35.0), np.float32(40.0), np.float32(45.0), np.float32(50.0), np.float32(60.0),
          np.float32(70.0), np.float32(80.0), np.float32(90.0), np.float32(100.),
          np.float32(120.), np.float32(140.), np.float32(160.), np.float32(200.), np.float32(250.), np.float32(300.),
          np.float32(400.), np.float32(500.), np.float32(600.), np.float32(800.),
          np.float32(1000.), np.float32(1250.), np.float32(1500.), np.float32(1750.), np.float32(2000.),
          np.float32(2500.), np.float32(3000.),
          ]
YC0FG1 = [np.float32(0.0), np.float32(.0019), np.float32(.0085), np.float32(.0271), np.float32(.0561),
          np.float32(.1051), np.float32(.154), np.float32(.1937), np.float32(.212), np.float32(.289),
          np.float32(.363), np.float32(.408), np.float32(.439), np.float32(.461), np.float32(.440), np.float32(.378),
          np.float32(.316), np.float32(.264), np.float32(.227), np.float32(.174),
          np.float32(.170), np.float32(.144), np.float32(.125), np.float32(.114), np.float32(.102), np.float32(.0874),
          np.float32(.0753),
          ]
# CF2 2+

XCF22G1 = [np.float32(42.0), np.float32(45.0), np.float32(50.0), np.float32(60.0), np.float32(70.0), np.float32(80.0),
           np.float32(90.0), np.float32(100.), np.float32(120.), np.float32(140.),
           np.float32(160.), np.float32(200.), np.float32(250.), np.float32(300.), np.float32(400.), np.float32(500.),
           np.float32(600.), np.float32(800.), np.float32(1000.), np.float32(1250.),
           np.float32(1500.), np.float32(1750.), np.float32(2000.), np.float32(2500.), np.float32(3000.),
           ]
YCF22G1 = [np.float32(0.0), np.float32(.0002), np.float32(.0033), np.float32(.0095), np.float32(.0194),
           np.float32(.0287), np.float32(.0348), np.float32(.0409), np.float32(.0483),
           np.float32(.0521),
           np.float32(.0522), np.float32(.0517), np.float32(.0467), np.float32(.0458), np.float32(.0367),
           np.float32(.0303), np.float32(.0280), np.float32(.0218), np.float32(.0164), np.float32(.0139),
           np.float32(.0120), np.float32(.0110), np.float32(.0098), np.float32(.0084), np.float32(.0073),
           ]
# ION PAIRS:

#   (C+ , F+)

XCFG1 = [np.float32(63.0), np.float32(70.0), np.float32(80.0), np.float32(90.0), np.float32(100.), np.float32(120.),
         np.float32(140.), np.float32(160.), np.float32(200.), np.float32(250.),
         np.float32(300.), np.float32(400.), np.float32(500.), np.float32(600.), np.float32(800.), np.float32(1000.),
         np.float32(1250.), np.float32(1500.), np.float32(1750.), np.float32(2000.),
         np.float32(2500.), np.float32(3000.),
         ]
YCFG1 = [np.float32(0.0), np.float32(.002), np.float32(.009), np.float32(.020), np.float32(.025), np.float32(.038),
         np.float32(.048), np.float32(.056), np.float32(.062), np.float32(.059),
         np.float32(.068), np.float32(.049), np.float32(.043), np.float32(.036), np.float32(.025), np.float32(.019),
         np.float32(.016), np.float32(.014), np.float32(.012), np.float32(.011),
         np.float32(.0096), np.float32(.0082),
         ]
#   (CF+ , F+)

XCFFG1 = [np.float32(43.0), np.float32(50.0), np.float32(60.0), np.float32(70.0), np.float32(80.0), np.float32(90.0),
          np.float32(100.), np.float32(120.), np.float32(140.), np.float32(160.),
          np.float32(200.), np.float32(250.), np.float32(300.), np.float32(400.), np.float32(500.), np.float32(600.),
          np.float32(800.), np.float32(1000.), np.float32(1250.), np.float32(1500.),
          np.float32(1750.), np.float32(2000.), np.float32(2500.), np.float32(3000.),
          ]
YCFFG1 = [np.float32(0.0), np.float32(.001), np.float32(.009), np.float32(.028), np.float32(.049), np.float32(.077),
          np.float32(.084), np.float32(.111), np.float32(.125), np.float32(.136),
          np.float32(.139), np.float32(.126), np.float32(.133), np.float32(.109), np.float32(.095), np.float32(.078),
          np.float32(.059), np.float32(.040), np.float32(.034), np.float32(.030),
          np.float32(.027), np.float32(.024), np.float32(.021), np.float32(.018),
          ]
#   (CF2 + , F+)

XCF2FG1 = [np.float32(40.0), np.float32(45.0), np.float32(50.0), np.float32(60.0), np.float32(70.0), np.float32(80.0),
           np.float32(90.0), np.float32(100.), np.float32(120.), np.float32(140.),
           np.float32(160.), np.float32(200.), np.float32(250.), np.float32(300.), np.float32(400.), np.float32(500.),
           np.float32(600.), np.float32(800.), np.float32(1000.), np.float32(1250.),
           np.float32(1500.), np.float32(1750.), np.float32(2000.), np.float32(2500.), np.float32(3000.),
           ]
YCF2FG1 = [np.float32(0.0), np.float32(.001), np.float32(.004), np.float32(.013), np.float32(.024), np.float32(.034),
           np.float32(.043), np.float32(.046), np.float32(.053), np.float32(.054),
           np.float32(.057), np.float32(.056), np.float32(.049), np.float32(.050), np.float32(.042), np.float32(.036),
           np.float32(.030), np.float32(.023), np.float32(.015), np.float32(.013),
           np.float32(.011), np.float32(.0104), np.float32(.0093), np.float32(.0080), np.float32(.0069),
           ]
#   (CF3 + , F+)

XCF3FG1 = [np.float32(36.0), np.float32(40.0), np.float32(45.0), np.float32(50.0), np.float32(60.0), np.float32(70.0),
           np.float32(80.0), np.float32(90.0), np.float32(100.), np.float32(120.),
           np.float32(140.), np.float32(160.), np.float32(200.), np.float32(250.), np.float32(300.), np.float32(400.),
           np.float32(500.), np.float32(600.), np.float32(800.), np.float32(1000.),
           np.float32(1250.), np.float32(1500.), np.float32(1750.), np.float32(2000.), np.float32(2500.),
           np.float32(3000.),
           ]
YCF3FG1 = [np.float32(0.0), np.float32(.001), np.float32(.003), np.float32(.006), np.float32(.014), np.float32(.023),
           np.float32(.030), np.float32(.037), np.float32(.038), np.float32(.042),
           np.float32(.041), np.float32(.044), np.float32(.045), np.float32(.040), np.float32(.038), np.float32(.033),
           np.float32(.028), np.float32(.023), np.float32(.018), np.float32(.012),
           np.float32(.0105), np.float32(.0091), np.float32(.0083), np.float32(.0074), np.float32(.0064),
           np.float32(.0055),
           ]
# CARBON K-SHELL IONISATION X-SECTION

XKSHCG1 = [np.float32(285.), np.float32(298.), np.float32(307.), np.float32(316.), np.float32(325.), np.float32(335.),
           np.float32(345.), np.float32(365.), np.float32(398.), np.float32(422.),
           np.float32(447.), np.float32(473.), np.float32(501.), np.float32(531.), np.float32(613.), np.float32(668.),
           np.float32(708.), np.float32(750.), np.float32(817.), np.float32(917.),
           np.float32(1000.), np.float32(1122.), np.float32(1296.), np.float32(1496.), np.float32(1679.),
           np.float32(1884.), np.float32(2054.), np.float32(2238.), np.float32(2512.), np.float32(2985.),
           np.float32(3981.), np.float32(5012.), np.float32(7079.), 1.0e4, 1.50e4, 2.05e4, 2.51e4, 3.07e4, 4.10e4,
           5.01e4,
           6.13e4, 7.08e4, 8.18e4, 1.0e5, 1.54e5, 2.05e5, 2.99e5, 4.10e5, 5.01e5,
           6.13e5,
           7.08e5, 8.18e5, 1.0e6, 1.25e6, 1.5e6, 2.05e6, 3.07e6, 4.10e6, 5.01e6,
           6.13e6,
           7.08e6, 8.18e6, 1.0e7, 1.5e7, 2.05e7, 3.07e7, 4.10e7, 5.01e7, 6.13e7,
           7.08e7,
           8.18e7, 1.0e8, 1.5e8, 2.05e8, 3.07e8, 4.10e8, 5.01e8, 6.13e8, 7.08e8,
           8.18e8,
           1.0e9,
           ]
YKSHCG1 = [np.float32(0.00), 1.66e-4, 3.48e-4, 5.25e-4, 6.96e-4, 8.63e-4, 1.02e-3,
           1.33e-3, 1.75e-3, 2.01e-3,
           2.24e-3, 2.46e-3, 2.66e-3, 2.84e-3, 3.21e-3, 3.38e-3, 3.47e-3, 3.55e-3,
           3.65e-3, 3.72e-3,
           3.75e-3, 3.74e-3, 3.68e-3, 3.57e-3, 3.45e-3, 3.31e-3, 3.19e-3, 3.07e-3,
           2.91e-3, 2.66e-3,
           2.25e-3, 1.95e-3, 1.55e-3, 1.21e-3, 8.97e-4, 7.07e-4, 6.07e-4, 5.21e-4,
           4.21e-4, 3.63e-4,
           3.14e-4, 2.84e-4, 2.57e-4, 2.25e-4, 1.74e-4, 1.50e-4, 1.28e-4, 1.15e-4,
           1.09e-4, 1.05e-4,
           1.03e-4, 1.02e-4, 1.01e-4, 1.005e-4, 1.01e-4, 1.03e-4, 1.07e-4, 1.11e-4,
           1.14e-4, 1.17e-4,
           1.20e-4, 1.22e-4, 1.25e-4, 1.32e-4, 1.38e-4, 1.45e-4, 1.50e-4, 1.54e-4,
           1.58e-4, 1.60e-4,
           1.63e-4, 1.67e-4, 1.74e-4, 1.80e-4, 1.87e-4, 1.92e-4, 1.96e-4, 2.00e-4,
           2.02e-4, 2.05e-4,
           2.09e-4,
           ]
# FLUORINE K-SHELL IONISATION X-SECTION

XKSHFG1 = [np.float32(685.4), np.float32(705.), np.float32(726.), np.float32(747.), np.float32(770.), np.float32(792.),
           np.float32(816.), np.float32(840.), np.float32(865.), np.float32(890.),
           np.float32(916.), np.float32(944.), np.float32(1000.), np.float32(1090.), np.float32(1188.),
           np.float32(1296.), np.float32(1496.), np.float32(1679.), np.float32(1884.), np.float32(2054.),
           np.float32(2238.), np.float32(2512.), np.float32(2985.), np.float32(3758.), np.float32(4467.),
           np.float32(5158.), np.float32(5957.), np.float32(7079.), 1.0e4, 1.26e4,
           1.50e4, 2.05e4, 2.51e4, 3.07e4, 4.10e4, 5.01e4, 6.13e4, 7.08e4, 8.18e4,
           1.0e5,
           1.50e5, 2.05e5, 2.99e5, 4.10e5, 5.01e5, 6.13e5, 7.08e5, 8.18e5, 1.00e6,
           1.26e6,
           1.50e6, 2.05e6, 3.07e6, 4.10e6, 5.01e6, 6.13e6, 7.08e6, 8.18e6, 1.00e7,
           1.26e7,
           1.50e7, 2.05e7, 3.07e7, 4.10e7, 5.01e7, 6.13e7, 7.08e7, 8.18e7, 1.00e8,
           1.26e8,
           1.50e8, 2.05e8, 3.07e8, 4.10e8, 5.01e8, 6.13e8, 7.08e8, 8.18e8, 1.00e9,
           ]
YKSHFG1 = [np.float32(0.00), 3.39e-5, 6.77e-5, 1.00e-4, 1.32e-4, 1.63e-4, 1.92e-4,
           2.21e-4, 2.48e-4, 2.75e-4,
           3.00e-4, 3.25e-4, 3.71e-4, 4.33e-4, 4.87e-4, 5.34e-4, 5.96e-4, 6.32e-4,
           6.57e-4, 6.69e-4,
           6.77e-4, 6.79e-4, 6.68e-4, 6.33e-4, 5.97e-4, 5.62e-4, 5.25e-4, 4.80e-4,
           3.93e-4, 3.41e-4,
           3.04e-4, 2.45e-4, 2.13e-4, 1.85e-4, 1.51e-4, 1.31e-4, 1.14e-4, 1.04e-4,
           9.46e-5, 8.32e-5,
           6.58e-5, 5.60e-5, 4.80e-5, 4.35e-5, 4.15e-5, 4.00e-5, 3.93e-5, 3.89e-5,
           3.85e-5, 3.86e-5,
           3.89e-5, 3.98e-5, 4.17e-5, 4.33e-5, 4.45e-5, 4.58e-5, 4.68e-5, 4.78e-5,
           4.92e-5, 5.09e-5,
           5.21e-5, 5.45e-5, 5.75e-5, 5.96e-5, 6.12e-5, 6.27e-5, 6.38e-5, 6.49e-5,
           6.64e-5, 6.82e-5,
           6.95e-5, 7.19e-5, 7.50e-5, 7.72e-5, 7.88e-5, 8.03e-5, 8.14e-5, 8.25e-5,
           8.40e-5,
           ]
# ATTACHMENT

XATTG1 = [np.float32(4.00), np.float32(4.10), np.float32(5.00), np.float32(6.00), np.float32(7.00), np.float32(8.00),
          np.float32(9.00), np.float32(10.0), np.float32(11.0),
          np.float32(12.0), np.float32(100.),
          ]
YATTG1 = [np.float32(.0), np.float32(.00001), np.float32(.00087), np.float32(.0062), np.float32(.0125),
          np.float32(.0134), np.float32(.0047), np.float32(.0009), np.float32(.0004),
          np.float32(.00001), np.float32(.0000001),
          ]
#

#  NEUTRAL DISSOCIATION

#      DIPOLE NEUTRAL DISSOCIATION GIVEN ANALYTICALLY

#      NON-DIPOLE  NEUTRAL DISSOCIATION :

XTR1G1 = [np.float32(11.5), np.float32(12.5), np.float32(14.0), np.float32(15.0), np.float32(16.0), np.float32(17.0),
          np.float32(19.0), np.float32(21.0), np.float32(24.0), np.float32(27.0),
          np.float32(31.0), np.float32(34.0),
          ]
YTR1G1 = [np.float32(0.00), np.float32(.005), np.float32(.017), np.float32(.026), np.float32(.029), np.float32(.031),
          np.float32(.035), np.float32(.035), np.float32(.031), np.float32(.026),
          np.float32(.019), np.float32(.015),
          ]
XTR2G1 = [np.float32(12.5), np.float32(14.0), np.float32(15.0), np.float32(16.0), np.float32(17.0), np.float32(19.0),
          np.float32(21.0), np.float32(24.0), np.float32(27.0), np.float32(31.0),
          np.float32(34.0),
          ]
YTR2G1 = [np.float32(0.00), np.float32(.030), np.float32(.056), np.float32(.064), np.float32(.068), np.float32(.075),
          np.float32(.077), np.float32(.068), np.float32(.057), np.float32(.042),
          np.float32(.033),
          ]
XTR3G1 = [np.float32(14.0), np.float32(15.0), np.float32(16.0), np.float32(17.0), np.float32(19.0), np.float32(21.0),
          np.float32(24.0), np.float32(27.0), np.float32(31.0), np.float32(34.0),
          np.float32(39.0),
          ]
YTR3G1 = [np.float32(0.00), np.float32(.087), np.float32(.180), np.float32(.210), np.float32(.237), np.float32(.250),
          np.float32(.250), np.float32(.237), np.float32(.187), np.float32(.145),
          np.float32(.107),
          ]
# BREMSTRAHLUNG X-SECTION WITH CUT OFF

Z6TG1 = [np.float32(298.), np.float32(178.), np.float32(85.2), np.float32(47.5), np.float32(26.3), np.float32(12.2),
         np.float32(7.06), np.float32(4.45), np.float32(3.06), np.float32(2.82),
         np.float32(2.89), np.float32(2.99), np.float32(3.08), np.float32(3.13), np.float32(3.18), np.float32(3.25),
         np.float32(3.31), np.float32(3.39), np.float32(3.44), np.float32(3.49),
         np.float32(3.52), np.float32(3.54), np.float32(3.55), np.float32(3.57), np.float32(3.57),
         ]
Z9TG1 = [np.float32(573.), np.float32(358.), np.float32(179.), np.float32(101.6), np.float32(57.3), np.float32(26.5),
         np.float32(15.4), np.float32(9.63), np.float32(6.52), np.float32(5.92),
         np.float32(6.01), np.float32(6.18), np.float32(6.35), np.float32(6.43), np.float32(6.52), np.float32(6.65),
         np.float32(6.75), np.float32(6.87), np.float32(6.95), np.float32(7.02),
         np.float32(7.07), np.float32(7.10), np.float32(7.12), np.float32(7.13), np.float32(7.14),
         ]
EBRMG1 = [np.float32(1000.), np.float32(2000.), np.float32(5000.), np.float32(1.E4), np.float32(2.E4), np.float32(5.E4),
          np.float32(1.E5), np.float32(2.E5), np.float32(5.E5), np.float32(1.E6),
          np.float32(2.E6), np.float32(3.E6), np.float32(4.E6), np.float32(5.E6), np.float32(6.E6), np.float32(8.E6),
          np.float32(1.E7), np.float32(1.5E7), np.float32(2.E7), np.float32(3.E7),
          np.float32(4.E7), np.float32(5.E7), np.float32(6.E7), np.float32(8.E7), np.float32(1.E8),
          ]
XENG1 = [np.float32(0.0), np.float32(.001), np.float32(.002), np.float32(.003), np.float32(.004), np.float32(.005),
         np.float32(.006), np.float32(.007), np.float32(.008), np.float32(.009),
         np.float32(0.01), np.float32(.012), np.float32(.014), np.float32(.016), np.float32(.018), np.float32(0.02),
         np.float32(.025), np.float32(0.03), np.float32(.035), np.float32(0.04),
         np.float32(.045), np.float32(0.05), np.float32(.055), np.float32(0.06), np.float32(.065), np.float32(0.07),
         np.float32(.075), np.float32(0.08), np.float32(.085), np.float32(0.09),
         np.float32(0.10), np.float32(0.12), np.float32(0.14), np.float32(0.17), np.float32(0.20), np.float32(0.24),
         np.float32(0.30), np.float32(0.40), np.float32(0.50), np.float32(0.60),
         np.float32(0.80), np.float32(1.00), np.float32(1.20), np.float32(1.40), np.float32(1.70), np.float32(2.00),
         np.float32(3.00), np.float32(5.00), np.float32(6.00), np.float32(7.00),
         np.float32(8.00), np.float32(9.00), np.float32(10.0), np.float32(12.0), np.float32(15.0), np.float32(20.0),
         np.float32(25.0), np.float32(30.0), np.float32(40.0), np.float32(50.0),
         np.float32(60.0), np.float32(80.0), np.float32(100.), np.float32(125.), np.float32(150.), np.float32(200.),
         np.float32(250.), np.float32(300.), np.float32(400.), np.float32(500.),
         np.float32(600.), np.float32(700.), np.float32(800.), np.float32(1000.), np.float32(1250.), np.float32(1500.),
         np.float32(1750.), np.float32(2000.), np.float32(2500.), np.float32(3000.),
         np.float32(3500.), np.float32(4000.), np.float32(5000.), np.float32(6000.), np.float32(7000.),
         np.float32(8000.), np.float32(9000.), np.float32(10000.), 1.25e4, 1.50e4,
         1.75e4, 2.0e4, 2.5e4, 3.0e4, 3.5e4, 4.0e4, 4.5e4, 5.0e4, 6.0e4, 7.0e4,
         8.0e4, 9.0e4, 1.0e5, 1.25e5, 1.5e5, 1.75e5, 2.0e5, 2.5e5, 3.0e5, 3.5e5,
         4.0e5, 4.5e5, 5.0e5, 6.0e5, 7.0e5, 8.0e5, 9.0e5, 1.0e6, 1.25e6, 1.5e6,
         1.75e6, 2.0e6, 2.5e6, 3.0e6, 3.5e6, 4.0e6, 4.5e6, 5.0e6, 6.0e6, 7.0e6,
         8.0e6, 9.0e6, 1.0e7, 1.25e7, 1.5e7, 1.75e7, 2.0e7, 2.5e7, 3.0e7, 3.5e7,
         4.0e7, 4.5e7, 5.0e7, 6.0e7, 7.0e7, 8.0e7, 9.0e7, 1.0e8, 1.25e8, 1.5e8,
         1.75e8, 2.0e8, 2.5e8, 3.0e8, 3.5e8, 4.0e8, 4.5e8, 5.0e8, 6.0e8, 7.0e8,
         8.0e8, 9.0e8, 1.0e9,
         ]
# ELASTIC MOMENTUM TRANSFER X-SECTION

YELMG1 = [np.float32(12.5), np.float32(8.70), np.float32(7.00), np.float32(5.95), np.float32(5.20), np.float32(4.70),
          np.float32(4.30), np.float32(3.95), np.float32(3.65), np.float32(3.40),
          np.float32(3.20), np.float32(2.85), np.float32(2.58), np.float32(2.37), np.float32(2.19), np.float32(2.04),
          np.float32(1.77), np.float32(1.57), np.float32(1.41), np.float32(1.30),
          np.float32(1.20), np.float32(1.12), np.float32(1.05), np.float32(0.99), np.float32(0.93), np.float32(0.88),
          np.float32(0.84), np.float32(0.80), np.float32(0.76), np.float32(0.72),
          np.float32(0.65), np.float32(0.48), np.float32(0.35), np.float32(0.29), np.float32(0.29), np.float32(0.34),
          np.float32(0.47), np.float32(0.87), np.float32(1.35), np.float32(1.85),
          np.float32(2.95), np.float32(4.00), np.float32(4.75), np.float32(5.15), np.float32(5.45), np.float32(5.65),
          np.float32(5.80), np.float32(6.00), np.float32(6.10), np.float32(6.30),
          np.float32(6.50), np.float32(6.80), np.float32(7.20), np.float32(8.30), np.float32(9.50), np.float32(10.1),
          np.float32(9.60), np.float32(8.80), np.float32(7.85), np.float32(6.72),
          np.float32(5.90), np.float32(5.06), np.float32(4.16), np.float32(3.57), np.float32(2.99), np.float32(1.92),
          np.float32(1.53), np.float32(1.20), np.float32(0.88), np.float32(0.66),
          np.float32(.525), np.float32(0.43), np.float32(0.37), np.float32(0.30), np.float32(.228), np.float32(.169),
          np.float32(.131), np.float32(.104), np.float32(.0711), np.float32(.0519),
          np.float32(.0397), np.float32(.0314), np.float32(.0212), np.float32(.0153), np.float32(.0117),
          np.float32(.00918), np.float32(.00743), np.float32(.00615), np.float32(.00412), np.float32(.00297),
          2.25e-3, 1.77e-3, 1.18e-3, 8.51e-4, 6.45e-4, 5.08e-4, 4.12e-4, 3.41e-4,
          2.47e-4, 1.88e-4,
          1.49e-4, 1.21e-4, 1.01e-4, 6.88e-5, 5.05e-5, 3.90e-5, 3.13e-5, 2.17e-5,
          1.62e-5, 1.27e-5,
          1.03e-5, 8.56e-6, 7.27e-6, 5.49e-6, 4.34e-6, 3.54e-6, 2.96e-6, 2.52e-6,
          1.81e-6, 1.36e-6,
          1.07e-6, 8.68e-7, 6.08e-7, 4.53e-7, 3.51e-7, 2.82e-7, 2.31e-7, 1.93e-7,
          1.42e-7, 1.08e-7,
          8.59e-8, 6.98e-8, 5.79e-8, 3.89e-8, 2.80e-8, 2.12e-8, 1.66e-8, 1.10e-8,
          7.86e-9, 5.90e-9,
          4.59e-9, 3.68e-9, 3.01e-9, 2.13e-9, 1.58e-9, 1.22e-9, 9.75e-10, 7.92e-10,
          5.10e-10, 3.56e-10,
          2.62e-10, 2.01e-10, 1.29e-10, 8.95e-11, 6.58e-11, 5.04e-11, 3.98e-11,
          3.23e-11, 2.24e-11, 1.65e-11,
          1.26e-11, 9.96e-12, 8.07e-12,
          ]
# ELASTIC X-SECTION ASSUMED ISOTROPIC BELOW 0.6 EV

YELTG1 = [np.float32(12.5), np.float32(8.70), np.float32(7.00), np.float32(5.95), np.float32(5.20), np.float32(4.70),
          np.float32(4.30), np.float32(3.95), np.float32(3.65), np.float32(3.40),
          np.float32(3.20), np.float32(2.85), np.float32(2.58), np.float32(2.37), np.float32(2.19), np.float32(2.04),
          np.float32(1.77), np.float32(1.57), np.float32(1.41), np.float32(1.30),
          np.float32(1.20), np.float32(1.12), np.float32(1.05), np.float32(0.99), np.float32(0.93), np.float32(0.88),
          np.float32(0.84), np.float32(0.80), np.float32(0.76), np.float32(0.72),
          np.float32(0.65), np.float32(0.48), np.float32(0.35), np.float32(0.29), np.float32(0.29), np.float32(0.34),
          np.float32(0.47), np.float32(0.87), np.float32(1.35), np.float32(1.85),
          np.float32(3.77), np.float32(4.89), np.float32(5.66), np.float32(6.43), np.float32(7.43), np.float32(8.34),
          np.float32(10.6), np.float32(12.5), np.float32(11.6), np.float32(11.0),
          np.float32(11.0), np.float32(11.7), np.float32(12.9), np.float32(14.5), np.float32(16.8), np.float32(17.6),
          np.float32(18.1), np.float32(17.2), np.float32(15.9), np.float32(14.9),
          np.float32(14.3), np.float32(13.0), np.float32(11.7), np.float32(10.5), np.float32(9.65), np.float32(8.10),
          np.float32(6.83), np.float32(6.02), np.float32(5.02), np.float32(4.36),
          np.float32(3.83), np.float32(3.40), np.float32(3.08), np.float32(2.65), np.float32(2.17), np.float32(1.89),
          np.float32(1.55), np.float32(1.40), np.float32(1.19), np.float32(1.11),
          np.float32(.921), np.float32(.822), np.float32(.696), np.float32(.568), np.float32(.492), np.float32(.435),
          np.float32(.390), np.float32(.353), np.float32(.286), np.float32(.241),
          np.float32(.209), np.float32(.185), np.float32(.150), np.float32(.127), np.float32(.111), np.float32(.0984),
          np.float32(.0888), np.float32(.0810), np.float32(.0694), np.float32(.0611),
          np.float32(.0522), np.float32(.050), np.float32(.0461), np.float32(.0391), np.float32(.0344),
          np.float32(.0311), np.float32(.0287), np.float32(.0253), np.float32(.0230), np.float32(.0214),
          np.float32(.0202), np.float32(.0193), np.float32(.0186), np.float32(.0176), np.float32(.0169),
          np.float32(.0164), np.float32(.0160), np.float32(.0157), np.float32(.0152), np.float32(.0148),
          np.float32(.0146), np.float32(.0145), np.float32(.0143), np.float32(.0142), np.float32(.0141),
          np.float32(.0141), np.float32(.0140), np.float32(.0140), np.float32(.0140), np.float32(.0139),
          np.float32(.0139), np.float32(.0139), np.float32(.0139), np.float32(.0139), np.float32(.01389),
          np.float32(.01389), np.float32(.01389), np.float32(.01388), np.float32(.01388), np.float32(.01388),
          np.float32(.01388), np.float32(.01388), np.float32(.01388), np.float32(.01388), np.float32(.01388),
          np.float32(.01388), np.float32(.01388), np.float32(.01388), np.float32(.01388), np.float32(.01388),
          np.float32(.01388), np.float32(.01388), np.float32(.01388), np.float32(.01388), np.float32(.01388),
          np.float32(.01388), np.float32(.01388), np.float32(.01388), np.float32(.01388), np.float32(.01388),
          np.float32(.01388), np.float32(.01388), np.float32(.01388),
          ]
# EPSILON FOR ELASTIC ANGULAR DISTRIBUTION

# EPSILON =1-YEPS

YEPSG1 = [np.float32(1.0), np.float32(1.0), np.float32(1.0), np.float32(1.0), np.float32(1.0), np.float32(1.0),
          np.float32(1.0), np.float32(1.0), np.float32(1.0), np.float32(1.0), np.float32(1.0), np.float32(1.0),
          np.float32(1.0), np.float32(1.0), np.float32(1.0), np.float32(1.0), np.float32(1.0), np.float32(1.0),
          np.float32(1.0), np.float32(1.0), np.float32(1.0), np.float32(1.0), np.float32(1.0), np.float32(1.0),
          np.float32(1.0), np.float32(1.0), np.float32(1.0), np.float32(1.0), np.float32(1.0), np.float32(1.0),
          np.float32(1.0), np.float32(1.0), np.float32(1.0), np.float32(1.0), np.float32(1.0), np.float32(1.0),
          np.float32(1.0), np.float32(1.0), np.float32(1.0), np.float32(1.0),
          np.float32(.68056), np.float32(.73101), np.float32(.76161), np.float32(.70664), np.float32(.61270),
          np.float32(.53797), np.float32(.37888), np.float32(.30604), np.float32(.35505),
          np.float32(.40830),
          np.float32(.42979), np.float32(.41826), np.float32(.39140), np.float32(.40794), np.float32(.39986),
          np.float32(.40963), np.float32(.36006), np.float32(.33951), np.float32(.32037),
          np.float32(.27671),
          np.float32(.23985), np.float32(.21859), np.float32(.18948), np.float32(.17666), np.float32(.15292),
          np.float32(.10180), np.float32(.09358), np.float32(.07880), np.float32(.06538),
          np.float32(.05301),
          np.float32(.04608), np.float32(.04117), np.float32(.03833), np.float32(.03532), np.float32(.03188),
          np.float32(.02561), np.float32(.02374), np.float32(.019986), np.float32(.015005),
          np.float32(.010925),
          np.float32(.009845), np.float32(.008442), np.float32(.006348), np.float32(.005446), np.float32(.004667),
          np.float32(.004028), np.float32(.003554), np.float32(.003186),
          np.float32(.002530), np.float32(.002096),
          np.float32(.001783), np.float32(.001549), np.float32(.001228), np.float32(.001016), np.float32(.000859),
          np.float32(.000749), np.float32(.000661), np.float32(.000590),
          np.float32(.000486), np.float32(.000411),
          3.53e-4, 3.12e-4, 2.78e-4, 2.17e-4, 1.76e-4, 1.47e-4, 1.26e-4, 9.61e-5,
          7.68e-5, 6.32e-5,
          5.32e-5, 4.56e-5, 3.97e-5, 3.10e-5, 2.30e-5, 2.07e-5, 1.74e-5, 1.49e-5,
          1.07e-5, 8.04e-6,
          6.28e-6, 5.05e-6, 3.47e-6, 2.54e-6, 1.94e-6, 1.53e-6, 1.24e-6, 1.02e-6,
          7.33e-7, 5.51e-7,
          4.30e-7, 3.44e-7, 2.82e-7, 1.84e-7, 1.30e-7, 9.62e-8, 7.42e-8, 4.80e-8,
          3.35e-8, 2.47e-8,
          1.89e-8, 1.50e-8, 1.21e-8, 8.388e-9, 6.133e-9, 4.669e-9, 3.666e-9,
          2.950e-9, 1.858e-9, 1.271e-9,
          9.21e-10, 6.97e-10, 4.37e-10, 2.98e-10, 2.16e-10, 1.63e-10, 1.28e-10,
          1.02e-10, 7.00e-11, 5.10e-11,
          3.80e-11, 3.00e-11, 2.40e-11,
          ]
#  VIBRATION V4 (RESONANCE ONLY) SCALED BY 1/E**3 ABOVE 50EV

XVBV4G1 = [np.float32(0.0783), np.float32(4.00), np.float32(5.00), np.float32(6.00), np.float32(7.00), np.float32(8.00),
           np.float32(9.00), np.float32(10.0), np.float32(15.0), np.float32(20.0),
           np.float32(50.0),
           ]
YVBV4G1 = [np.float32(0.0), np.float32(0.0), np.float32(0.05), np.float32(0.35), np.float32(1.06), np.float32(1.40),
           np.float32(1.26), np.float32(0.97), np.float32(0.07), np.float32(.022),
           1.e-3,
           ]
#  VIBRATION V1 (RESONANCE ONLY) SCALED BY 1/E**3 ABOVE 50EV

XVBV1G1 = [np.float32(0.1126), np.float32(4.00), np.float32(5.00), np.float32(6.00), np.float32(7.00), np.float32(8.00),
           np.float32(9.00), np.float32(10.0), np.float32(15.0), np.float32(20.0),
           np.float32(50.0),
           ]
YVBV1G1 = [np.float32(0.0), np.float32(0.0), np.float32(.016), np.float32(.118), np.float32(0.36), np.float32(0.47),
           np.float32(0.42), np.float32(0.33), np.float32(.023), np.float32(.007),
           3.e-4,
           ]
#  VIBRATION V3 (RESONANCE ONLY) SCALED BY 1/E**3 ABOVE 50EV

XVBV3G1 = [np.float32(0.1588), np.float32(4.00), np.float32(5.00), np.float32(6.00), np.float32(7.00), np.float32(8.00),
           np.float32(9.00), np.float32(10.0), np.float32(15.0), np.float32(20.0),
           np.float32(50.0),
           ]
YVBV3G1 = [np.float32(0.0), np.float32(0.0), np.float32(0.15), np.float32(1.05), np.float32(3.19), np.float32(4.20),
           np.float32(3.78), np.float32(2.90), np.float32(0.20), np.float32(.067),
           3.e-3,
           ]
#  VIBRATION HARMONIC 2(V3) SCALED BY 1/E ABOVE 50EV

XVIB5G1 = [np.float32(0.3176), np.float32(1.00), np.float32(4.00), np.float32(5.00), np.float32(6.00), np.float32(7.00),
           np.float32(8.00), np.float32(9.00), np.float32(10.0), np.float32(15.0),
           np.float32(20.0), np.float32(50.0),
           ]
YVIB5G1 = [np.float32(0.0), np.float32(.001), np.float32(0.01), np.float32(.031), np.float32(0.23), np.float32(0.67),
           np.float32(0.87), np.float32(0.79), np.float32(0.60), np.float32(.042),
           np.float32(.014), np.float32(.0006),
           ]
# VIBRATION HARMONIC (3(V3) + ALL OTHER HARMONICS)

#  SCALED BY 1/E ABOVE 50 EV

XVIB6G1 = [np.float32(0.4764), np.float32(1.00), np.float32(4.00), np.float32(5.00), np.float32(6.00), np.float32(7.00),
           np.float32(8.00), np.float32(9.00), np.float32(10.0), np.float32(15.0),
           np.float32(20.0), np.float32(50.0),
           ]
YVIB6G1 = [np.float32(0.0), np.float32(.0009), np.float32(.045), np.float32(.117), np.float32(.774), np.float32(2.32),
           np.float32(3.06), np.float32(2.75), np.float32(2.12), np.float32(.138),
           np.float32(.037), np.float32(.0018),
           ]
#

#  DISSOCATIVE IONISATION :

#  WEIGHTED AVERAGE OF SIEGLAFF AND NISHIMURA FOR SINGLE IONISATION AND

#  DOUBLE IONISATION.

#  FOR DOUBLE IONISATION WITH BREAKUP :  BRUCE ET AL CPL 190(1992)285

#  NB.  (USED NISHIMURA ONLY BELOW 30EV)

#

# CF3 +

XCF3G1 = [np.float32(15.7), np.float32(16.0), np.float32(17.0), np.float32(18.0), np.float32(19.0), np.float32(20.0),
          np.float32(22.0), np.float32(24.0), np.float32(26.0), np.float32(28.0),
          np.float32(30.0), np.float32(35.0), np.float32(40.0), np.float32(45.0), np.float32(50.0), np.float32(60.0),
          np.float32(70.0), np.float32(80.0), np.float32(90.0), np.float32(100.),
          np.float32(120.), np.float32(140.), np.float32(160.), np.float32(200.), np.float32(250.), np.float32(300.),
          np.float32(400.), np.float32(500.), np.float32(600.), np.float32(800.),
          np.float32(1000.), np.float32(1250.), np.float32(1500.), np.float32(1750.), np.float32(2000.),
          np.float32(2500.), np.float32(3000.),
          ]
YCF3G1 = [np.float32(0.0), np.float32(.032), np.float32(.075), np.float32(.128), np.float32(.191), np.float32(.276),
          np.float32(.448), np.float32(.610), np.float32(.866), np.float32(1.08),
          np.float32(1.26), np.float32(1.72), np.float32(2.05), np.float32(2.35), np.float32(2.62), np.float32(2.94),
          np.float32(3.13), np.float32(3.24), np.float32(3.32), np.float32(3.35),
          np.float32(3.38), np.float32(3.34), np.float32(3.27), np.float32(3.17), np.float32(3.00), np.float32(2.81),
          np.float32(2.54), np.float32(2.28), np.float32(2.09), np.float32(1.77),
          np.float32(1.56), np.float32(1.32), np.float32(1.15), np.float32(1.05), np.float32(.937), np.float32(.804),
          np.float32(.692),
          ]
# CF2+

XCF2G1 = [np.float32(21.47), np.float32(24.0), np.float32(26.0), np.float32(28.0),
          np.float32(30.0), np.float32(35.0), np.float32(40.0), np.float32(45.0), np.float32(50.0), np.float32(60.0),
          np.float32(70.0), np.float32(80.0), np.float32(90.0), np.float32(100.),
          np.float32(120.), np.float32(140.), np.float32(160.), np.float32(200.), np.float32(250.), np.float32(300.),
          np.float32(400.), np.float32(500.), np.float32(600.), np.float32(800.),
          np.float32(1000.), np.float32(1250.), np.float32(1500.), np.float32(1750.), np.float32(2000.),
          np.float32(2500.), np.float32(3000.),
          ]
YCF2G1 = [np.float32(0.00), np.float32(.003), np.float32(.010), np.float32(.032),
          np.float32(.060), np.float32(.131), np.float32(.148), np.float32(.162), np.float32(.192), np.float32(.221),
          np.float32(.234), np.float32(.243), np.float32(.256), np.float32(.263),
          np.float32(.266), np.float32(.260), np.float32(.257), np.float32(.240), np.float32(.233), np.float32(.212),
          np.float32(.186), np.float32(.169), np.float32(.152), np.float32(.131),
          np.float32(.113), np.float32(.0961), np.float32(.0834), np.float32(.0763), np.float32(.0681),
          np.float32(.0585), np.float32(.0503),
          ]
# CF+

XCF1G1 = [np.float32(29.14),
          np.float32(30.0), np.float32(35.0), np.float32(40.0), np.float32(45.0), np.float32(50.0), np.float32(60.0),
          np.float32(70.0), np.float32(80.0), np.float32(90.0), np.float32(100.),
          np.float32(120.), np.float32(140.), np.float32(160.), np.float32(200.), np.float32(250.), np.float32(300.),
          np.float32(400.), np.float32(500.), np.float32(600.), np.float32(800.),
          np.float32(1000.), np.float32(1250.), np.float32(1500.), np.float32(1750.), np.float32(2000.),
          np.float32(2500.), np.float32(3000.),
          ]
YCF1G1 = [np.float32(0.00),
          np.float32(.0024), np.float32(.0145), np.float32(.0583), np.float32(.107), np.float32(.156), np.float32(.185),
          np.float32(.226), np.float32(.239), np.float32(.238), np.float32(.266),
          np.float32(.274), np.float32(.259), np.float32(.261), np.float32(.234), np.float32(.227), np.float32(.186),
          np.float32(.146), np.float32(.122), np.float32(.113), np.float32(.0909),
          np.float32(.0820), np.float32(.0695), np.float32(.0603), np.float32(.0552), np.float32(.0493),
          np.float32(.0423), np.float32(.0364),
          ]
# DATA CF3 2+

XCF32G1 = [np.float32(41.0), np.float32(45.0), np.float32(50.0), np.float32(60.0), np.float32(70.0), np.float32(80.0),
           np.float32(90.0), np.float32(100.), np.float32(120.), np.float32(140.),
           np.float32(160.), np.float32(200.), np.float32(250.), np.float32(300.), np.float32(400.), np.float32(500.),
           np.float32(600.), np.float32(800.), np.float32(1000.), np.float32(1250.),
           np.float32(1500.), np.float32(1750.), np.float32(2000.), np.float32(2500.), np.float32(3000.),
           ]
YCF32G1 = [np.float32(0.00), np.float32(.0053), np.float32(.0083), np.float32(.0104), np.float32(.0135),
           np.float32(.0154), np.float32(.0164), np.float32(.0187), np.float32(.0208),
           np.float32(.0198),
           np.float32(.0208), np.float32(.0198), np.float32(.0187), np.float32(.0167), np.float32(.0135),
           np.float32(.0114), np.float32(.0101), np.float32(.0079), np.float32(.0065), np.float32(.0055),
           np.float32(.0048), np.float32(.0044), np.float32(.0039), np.float32(.0033), np.float32(.0029),
           ]
# C+

XCF0G1 = [np.float32(34.77), np.float32(35.0), np.float32(40.0), np.float32(45.0), np.float32(50.0), np.float32(60.0),
          np.float32(70.0), np.float32(80.0), np.float32(90.0), np.float32(100.),
          np.float32(120.), np.float32(140.), np.float32(160.), np.float32(200.), np.float32(250.), np.float32(300.),
          np.float32(400.), np.float32(500.), np.float32(600.), np.float32(800.),
          np.float32(1000.), np.float32(1250.), np.float32(1500.), np.float32(1750.), np.float32(2000.),
          np.float32(2500.), np.float32(3000.),
          ]
YCF0G1 = [np.float32(0.0), np.float32(.0005), np.float32(.0093), np.float32(.0426), np.float32(.0884), np.float32(.134),
          np.float32(.172), np.float32(.193), np.float32(.207), np.float32(.228),
          np.float32(.245), np.float32(.246), np.float32(.249), np.float32(.236), np.float32(.222), np.float32(.191),
          np.float32(.166), np.float32(.144), np.float32(.134), np.float32(.104),
          np.float32(.0895), np.float32(.0759), np.float32(.0658), np.float32(.0602), np.float32(.0538),
          np.float32(.0462), np.float32(.0397),
          ]
# F+

XC0FG1 = [np.float32(34.5), np.float32(35.0), np.float32(40.0), np.float32(45.0), np.float32(50.0), np.float32(60.0),
          np.float32(70.0), np.float32(80.0), np.float32(90.0), np.float32(100.),
          np.float32(120.), np.float32(140.), np.float32(160.), np.float32(200.), np.float32(250.), np.float32(300.),
          np.float32(400.), np.float32(500.), np.float32(600.), np.float32(800.),
          np.float32(1000.), np.float32(1250.), np.float32(1500.), np.float32(1750.), np.float32(2000.),
          np.float32(2500.), np.float32(3000.),
          ]
YC0FG1 = [np.float32(0.0), np.float32(.0019), np.float32(.0085), np.float32(.0271), np.float32(.0561),
          np.float32(.1051), np.float32(.154), np.float32(.1937), np.float32(.212), np.float32(.289),
          np.float32(.363), np.float32(.408), np.float32(.439), np.float32(.461), np.float32(.440), np.float32(.378),
          np.float32(.316), np.float32(.264), np.float32(.227), np.float32(.174),
          np.float32(.170), np.float32(.144), np.float32(.125), np.float32(.114), np.float32(.102), np.float32(.0874),
          np.float32(.0753),
          ]
# CF2 2+

XCF22G1 = [np.float32(42.0), np.float32(45.0), np.float32(50.0), np.float32(60.0), np.float32(70.0), np.float32(80.0),
           np.float32(90.0), np.float32(100.), np.float32(120.), np.float32(140.),
           np.float32(160.), np.float32(200.), np.float32(250.), np.float32(300.), np.float32(400.), np.float32(500.),
           np.float32(600.), np.float32(800.), np.float32(1000.), np.float32(1250.),
           np.float32(1500.), np.float32(1750.), np.float32(2000.), np.float32(2500.), np.float32(3000.),
           ]
YCF22G1 = [np.float32(0.0), np.float32(.0002), np.float32(.0033), np.float32(.0095), np.float32(.0194),
           np.float32(.0287), np.float32(.0348), np.float32(.0409), np.float32(.0483),
           np.float32(.0521),
           np.float32(.0522), np.float32(.0517), np.float32(.0467), np.float32(.0458), np.float32(.0367),
           np.float32(.0303), np.float32(.0280), np.float32(.0218), np.float32(.0164), np.float32(.0139),
           np.float32(.0120), np.float32(.0110), np.float32(.0098), np.float32(.0084), np.float32(.0073),
           ]
# ION PAIRS:

#   (C+ , F+)

XCFG1 = [np.float32(63.0), np.float32(70.0), np.float32(80.0), np.float32(90.0), np.float32(100.), np.float32(120.),
         np.float32(140.), np.float32(160.), np.float32(200.), np.float32(250.),
         np.float32(300.), np.float32(400.), np.float32(500.), np.float32(600.), np.float32(800.), np.float32(1000.),
         np.float32(1250.), np.float32(1500.), np.float32(1750.), np.float32(2000.),
         np.float32(2500.), np.float32(3000.),
         ]
YCFG1 = [np.float32(0.0), np.float32(.002), np.float32(.009), np.float32(.020), np.float32(.025), np.float32(.038),
         np.float32(.048), np.float32(.056), np.float32(.062), np.float32(.059),
         np.float32(.068), np.float32(.049), np.float32(.043), np.float32(.036), np.float32(.025), np.float32(.019),
         np.float32(.016), np.float32(.014), np.float32(.012), np.float32(.011),
         np.float32(.0096), np.float32(.0082),
         ]
#   (CF+ , F+)

XCFFG1 = [np.float32(43.0), np.float32(50.0), np.float32(60.0), np.float32(70.0), np.float32(80.0), np.float32(90.0),
          np.float32(100.), np.float32(120.), np.float32(140.), np.float32(160.),
          np.float32(200.), np.float32(250.), np.float32(300.), np.float32(400.), np.float32(500.), np.float32(600.),
          np.float32(800.), np.float32(1000.), np.float32(1250.), np.float32(1500.),
          np.float32(1750.), np.float32(2000.), np.float32(2500.), np.float32(3000.),
          ]
YCFFG1 = [np.float32(0.0), np.float32(.001), np.float32(.009), np.float32(.028), np.float32(.049), np.float32(.077),
          np.float32(.084), np.float32(.111), np.float32(.125), np.float32(.136),
          np.float32(.139), np.float32(.126), np.float32(.133), np.float32(.109), np.float32(.095), np.float32(.078),
          np.float32(.059), np.float32(.040), np.float32(.034), np.float32(.030),
          np.float32(.027), np.float32(.024), np.float32(.021), np.float32(.018),
          ]
#   (CF2 + , F+)

XCF2FG1 = [np.float32(40.0), np.float32(45.0), np.float32(50.0), np.float32(60.0), np.float32(70.0), np.float32(80.0),
           np.float32(90.0), np.float32(100.), np.float32(120.), np.float32(140.),
           np.float32(160.), np.float32(200.), np.float32(250.), np.float32(300.), np.float32(400.), np.float32(500.),
           np.float32(600.), np.float32(800.), np.float32(1000.), np.float32(1250.),
           np.float32(1500.), np.float32(1750.), np.float32(2000.), np.float32(2500.), np.float32(3000.),
           ]
YCF2FG1 = [np.float32(0.0), np.float32(.001), np.float32(.004), np.float32(.013), np.float32(.024), np.float32(.034),
           np.float32(.043), np.float32(.046), np.float32(.053), np.float32(.054),
           np.float32(.057), np.float32(.056), np.float32(.049), np.float32(.050), np.float32(.042), np.float32(.036),
           np.float32(.030), np.float32(.023), np.float32(.015), np.float32(.013),
           np.float32(.011), np.float32(.0104), np.float32(.0093), np.float32(.0080), np.float32(.0069),
           ]
#   (CF3 + , F+)

XCF3FG1 = [np.float32(36.0), np.float32(40.0), np.float32(45.0), np.float32(50.0), np.float32(60.0), np.float32(70.0),
           np.float32(80.0), np.float32(90.0), np.float32(100.), np.float32(120.),
           np.float32(140.), np.float32(160.), np.float32(200.), np.float32(250.), np.float32(300.), np.float32(400.),
           np.float32(500.), np.float32(600.), np.float32(800.), np.float32(1000.),
           np.float32(1250.), np.float32(1500.), np.float32(1750.), np.float32(2000.), np.float32(2500.),
           np.float32(3000.),
           ]
YCF3FG1 = [np.float32(0.0), np.float32(.001), np.float32(.003), np.float32(.006), np.float32(.014), np.float32(.023),
           np.float32(.030), np.float32(.037), np.float32(.038), np.float32(.042),
           np.float32(.041), np.float32(.044), np.float32(.045), np.float32(.040), np.float32(.038), np.float32(.033),
           np.float32(.028), np.float32(.023), np.float32(.018), np.float32(.012),
           np.float32(.0105), np.float32(.0091), np.float32(.0083), np.float32(.0074), np.float32(.0064),
           np.float32(.0055),
           ]
# CARBON K-SHELL IONISATION X-SECTION

XKSHCG1 = [np.float32(285.), np.float32(298.), np.float32(307.), np.float32(316.), np.float32(325.), np.float32(335.),
           np.float32(345.), np.float32(365.), np.float32(398.), np.float32(422.),
           np.float32(447.), np.float32(473.), np.float32(501.), np.float32(531.), np.float32(613.), np.float32(668.),
           np.float32(708.), np.float32(750.), np.float32(817.), np.float32(917.),
           np.float32(1000.), np.float32(1122.), np.float32(1296.), np.float32(1496.), np.float32(1679.),
           np.float32(1884.), np.float32(2054.), np.float32(2238.), np.float32(2512.), np.float32(2985.),
           np.float32(3981.), np.float32(5012.), np.float32(7079.), 1.0e4, 1.50e4, 2.05e4, 2.51e4, 3.07e4, 4.10e4,
           5.01e4,
           6.13e4, 7.08e4, 8.18e4, 1.0e5, 1.54e5, 2.05e5, 2.99e5, 4.10e5, 5.01e5,
           6.13e5,
           7.08e5, 8.18e5, 1.0e6, 1.25e6, 1.5e6, 2.05e6, 3.07e6, 4.10e6, 5.01e6,
           6.13e6,
           7.08e6, 8.18e6, 1.0e7, 1.5e7, 2.05e7, 3.07e7, 4.10e7, 5.01e7, 6.13e7,
           7.08e7,
           8.18e7, 1.0e8, 1.5e8, 2.05e8, 3.07e8, 4.10e8, 5.01e8, 6.13e8, 7.08e8,
           8.18e8,
           1.0e9,
           ]
YKSHCG1 = [np.float32(0.00), 1.66e-4, 3.48e-4, 5.25e-4, 6.96e-4, 8.63e-4, 1.02e-3,
           1.33e-3, 1.75e-3, 2.01e-3,
           2.24e-3, 2.46e-3, 2.66e-3, 2.84e-3, 3.21e-3, 3.38e-3, 3.47e-3, 3.55e-3,
           3.65e-3, 3.72e-3,
           3.75e-3, 3.74e-3, 3.68e-3, 3.57e-3, 3.45e-3, 3.31e-3, 3.19e-3, 3.07e-3,
           2.91e-3, 2.66e-3,
           2.25e-3, 1.95e-3, 1.55e-3, 1.21e-3, 8.97e-4, 7.07e-4, 6.07e-4, 5.21e-4,
           4.21e-4, 3.63e-4,
           3.14e-4, 2.84e-4, 2.57e-4, 2.25e-4, 1.74e-4, 1.50e-4, 1.28e-4, 1.15e-4,
           1.09e-4, 1.05e-4,
           1.03e-4, 1.02e-4, 1.01e-4, 1.005e-4, 1.01e-4, 1.03e-4, 1.07e-4, 1.11e-4,
           1.14e-4, 1.17e-4,
           1.20e-4, 1.22e-4, 1.25e-4, 1.32e-4, 1.38e-4, 1.45e-4, 1.50e-4, 1.54e-4,
           1.58e-4, 1.60e-4,
           1.63e-4, 1.67e-4, 1.74e-4, 1.80e-4, 1.87e-4, 1.92e-4, 1.96e-4, 2.00e-4,
           2.02e-4, 2.05e-4,
           2.09e-4,
           ]
# FLUORINE K-SHELL IONISATION X-SECTION

XKSHFG1 = [np.float32(685.4), np.float32(705.), np.float32(726.), np.float32(747.), np.float32(770.), np.float32(792.),
           np.float32(816.), np.float32(840.), np.float32(865.), np.float32(890.),
           np.float32(916.), np.float32(944.), np.float32(1000.), np.float32(1090.), np.float32(1188.),
           np.float32(1296.), np.float32(1496.), np.float32(1679.), np.float32(1884.), np.float32(2054.),
           np.float32(2238.), np.float32(2512.), np.float32(2985.), np.float32(3758.), np.float32(4467.),
           np.float32(5158.), np.float32(5957.), np.float32(7079.), 1.0e4, 1.26e4,
           1.50e4, 2.05e4, 2.51e4, 3.07e4, 4.10e4, 5.01e4, 6.13e4, 7.08e4, 8.18e4,
           1.0e5,
           1.50e5, 2.05e5, 2.99e5, 4.10e5, 5.01e5, 6.13e5, 7.08e5, 8.18e5, 1.00e6,
           1.26e6,
           1.50e6, 2.05e6, 3.07e6, 4.10e6, 5.01e6, 6.13e6, 7.08e6, 8.18e6, 1.00e7,
           1.26e7,
           1.50e7, 2.05e7, 3.07e7, 4.10e7, 5.01e7, 6.13e7, 7.08e7, 8.18e7, 1.00e8,
           1.26e8,
           1.50e8, 2.05e8, 3.07e8, 4.10e8, 5.01e8, 6.13e8, 7.08e8, 8.18e8, 1.00e9,
           ]
YKSHFG1 = [np.float32(0.00), 3.39e-5, 6.77e-5, 1.00e-4, 1.32e-4, 1.63e-4, 1.92e-4,
           2.21e-4, 2.48e-4, 2.75e-4,
           3.00e-4, 3.25e-4, 3.71e-4, 4.33e-4, 4.87e-4, 5.34e-4, 5.96e-4, 6.32e-4,
           6.57e-4, 6.69e-4,
           6.77e-4, 6.79e-4, 6.68e-4, 6.33e-4, 5.97e-4, 5.62e-4, 5.25e-4, 4.80e-4,
           3.93e-4, 3.41e-4,
           3.04e-4, 2.45e-4, 2.13e-4, 1.85e-4, 1.51e-4, 1.31e-4, 1.14e-4, 1.04e-4,
           9.46e-5, 8.32e-5,
           6.58e-5, 5.60e-5, 4.80e-5, 4.35e-5, 4.15e-5, 4.00e-5, 3.93e-5, 3.89e-5,
           3.85e-5, 3.86e-5,
           3.89e-5, 3.98e-5, 4.17e-5, 4.33e-5, 4.45e-5, 4.58e-5, 4.68e-5, 4.78e-5,
           4.92e-5, 5.09e-5,
           5.21e-5, 5.45e-5, 5.75e-5, 5.96e-5, 6.12e-5, 6.27e-5, 6.38e-5, 6.49e-5,
           6.64e-5, 6.82e-5,
           6.95e-5, 7.19e-5, 7.50e-5, 7.72e-5, 7.88e-5, 8.03e-5, 8.14e-5, 8.25e-5,
           8.40e-5,
           ]
# ATTACHMENT

XATTG1 = [np.float32(4.00), np.float32(4.10), np.float32(5.00), np.float32(6.00), np.float32(7.00), np.float32(8.00),
          np.float32(9.00), np.float32(10.0), np.float32(11.0),
          np.float32(12.0), np.float32(100.),
          ]
YATTG1 = [np.float32(.0), np.float32(.00001), np.float32(.00087), np.float32(.0062), np.float32(.0125),
          np.float32(.0134), np.float32(.0047), np.float32(.0009), np.float32(.0004),
          np.float32(.00001), np.float32(.0000001),
          ]
#

#  NEUTRAL DISSOCIATION

#      DIPOLE NEUTRAL DISSOCIATION GIVEN ANALYTICALLY

#      NON-DIPOLE  NEUTRAL DISSOCIATION :

XTR1G1 = [np.float32(11.5), np.float32(12.5), np.float32(14.0), np.float32(15.0), np.float32(16.0), np.float32(17.0),
          np.float32(19.0), np.float32(21.0), np.float32(24.0), np.float32(27.0),
          np.float32(31.0), np.float32(34.0),
          ]
YTR1G1 = [np.float32(0.00), np.float32(.005), np.float32(.017), np.float32(.026), np.float32(.029), np.float32(.031),
          np.float32(.035), np.float32(.035), np.float32(.031), np.float32(.026),
          np.float32(.019), np.float32(.015),
          ]
XTR2G1 = [np.float32(12.5), np.float32(14.0), np.float32(15.0), np.float32(16.0), np.float32(17.0), np.float32(19.0),
          np.float32(21.0), np.float32(24.0), np.float32(27.0), np.float32(31.0),
          np.float32(34.0),
          ]
YTR2G1 = [np.float32(0.00), np.float32(.030), np.float32(.056), np.float32(.064), np.float32(.068), np.float32(.075),
          np.float32(.077), np.float32(.068), np.float32(.057), np.float32(.042),
          np.float32(.033),
          ]
XTR3G1 = [np.float32(14.0), np.float32(15.0), np.float32(16.0), np.float32(17.0), np.float32(19.0), np.float32(21.0),
          np.float32(24.0), np.float32(27.0), np.float32(31.0), np.float32(34.0),
          np.float32(39.0),
          ]
YTR3G1 = [np.float32(0.00), np.float32(.087), np.float32(.180), np.float32(.210), np.float32(.237), np.float32(.250),
          np.float32(.250), np.float32(.237), np.float32(.187), np.float32(.145),
          np.float32(.107),
          ]
# BREMSTRAHLUNG X-SECTION WITH CUT OFF

Z6TG1 = [np.float32(298.), np.float32(178.), np.float32(85.2), np.float32(47.5), np.float32(26.3), np.float32(12.2),
         np.float32(7.06), np.float32(4.45), np.float32(3.06), np.float32(2.82),
         np.float32(2.89), np.float32(2.99), np.float32(3.08), np.float32(3.13), np.float32(3.18), np.float32(3.25),
         np.float32(3.31), np.float32(3.39), np.float32(3.44), np.float32(3.49),
         np.float32(3.52), np.float32(3.54), np.float32(3.55), np.float32(3.57), np.float32(3.57),
         ]
Z9TG1 = [np.float32(573.), np.float32(358.), np.float32(179.), np.float32(101.6), np.float32(57.3), np.float32(26.5),
         np.float32(15.4), np.float32(9.63), np.float32(6.52), np.float32(5.92),
         np.float32(6.01), np.float32(6.18), np.float32(6.35), np.float32(6.43), np.float32(6.52), np.float32(6.65),
         np.float32(6.75), np.float32(6.87), np.float32(6.95), np.float32(7.02),
         np.float32(7.07), np.float32(7.10), np.float32(7.12), np.float32(7.13), np.float32(7.14),
         ]
EBRMG1 = [np.float32(1000.), np.float32(2000.), np.float32(5000.), np.float32(1.E4), np.float32(2.E4), np.float32(5.E4),
          np.float32(1.E5), np.float32(2.E5), np.float32(5.E5), np.float32(1.E6),
          np.float32(2.E6), np.float32(3.E6), np.float32(4.E6), np.float32(5.E6), np.float32(6.E6), np.float32(8.E6),
          np.float32(1.E7), np.float32(1.5E7), np.float32(2.E7), np.float32(3.E7),
          np.float32(4.E7), np.float32(5.E7), np.float32(6.E7), np.float32(8.E7), np.float32(1.E8),
          ]
gd['gas1/XEN'] = XENG1
gd['gas1/YELM'] = YELMG1
gd['gas1/YELT'] = YELTG1
gd['gas1/YEPS'] = YEPSG1
gd['gas1/XVBV4'] = XVBV4G1
gd['gas1/YVBV4'] = YVBV4G1
gd['gas1/XVBV1'] = XVBV1G1
gd['gas1/YVBV1'] = YVBV1G1
gd['gas1/XVBV3'] = XVBV3G1
gd['gas1/YVBV3'] = YVBV3G1
gd['gas1/XVIB5'] = XVIB5G1
gd['gas1/YVIB5'] = YVIB5G1
gd['gas1/XVIB6'] = XVIB6G1
gd['gas1/YVIB6'] = YVIB6G1
gd['gas1/XTR1'] = XTR1G1
gd['gas1/YTR1'] = YTR1G1
gd['gas1/XTR2'] = XTR2G1
gd['gas1/YTR2'] = YTR2G1
gd['gas1/XTR3'] = XTR3G1
gd['gas1/YTR3'] = YTR3G1
gd['gas1/XCF3'] = XCF3G1
gd['gas1/YCF3'] = YCF3G1
gd['gas1/XCF2'] = XCF2G1
gd['gas1/YCF2'] = YCF2G1
gd['gas1/XCF1'] = XCF1G1
gd['gas1/YCF1'] = YCF1G1
gd['gas1/XCF32'] = XCF32G1
gd['gas1/YCF32'] = YCF32G1
gd['gas1/XCF0'] = XCF0G1
gd['gas1/YCF0'] = YCF0G1
gd['gas1/XC0F'] = XC0FG1
gd['gas1/YC0F'] = YC0FG1
gd['gas1/XCF22'] = XCF22G1
gd['gas1/YCF22'] = YCF22G1
gd['gas1/XCF'] = XCFG1
gd['gas1/YCF'] = YCFG1
gd['gas1/XCFF'] = XCFFG1
gd['gas1/YCFF'] = YCFFG1
gd['gas1/XCF2F'] = XCF2FG1
gd['gas1/YCF2F'] = YCF2FG1
gd['gas1/XCF3F'] = XCF3FG1
gd['gas1/YCF3F'] = YCF3FG1
gd['gas1/XATT'] = XATTG1
gd['gas1/YATT'] = YATTG1
gd['gas1/XKSHC'] = XKSHCG1
gd['gas1/YKSHC'] = YKSHCG1
gd['gas1/XKSHF'] = XKSHFG1
gd['gas1/YKSHF'] = YKSHFG1
gd['gas1/Z6T'] = Z6TG1
gd['gas1/Z9T'] = Z9TG1
gd['gas1/EBRM'] = EBRMG1

EIN = [np.float32(-0.0539), np.float32(0.0539), np.float32(-0.0783), np.float32(0.0783), np.float32(-0.1126),
       np.float32(0.1126), np.float32(-0.1588), np.float32(0.1588), np.float32(0.3176), np.float32(0.4764),
       np.float32(11.5), np.float32(11.63), np.float32(11.88), np.float32(12.13), np.float32(12.38), np.float32(12.50),
       np.float32(12.63), np.float32(12.88), np.float32(13.13), np.float32(13.38), np.float32(13.63), np.float32(13.88),
       np.float32(14.00), np.float32(14.13), np.float32(14.38), np.float32(14.63), np.float32(14.88), np.float32(15.13),
       np.float32(15.38), np.float32(15.63), np.float32(15.88), np.float32(16.13), np.float32(16.38), np.float32(16.63),
       np.float32(16.88), np.float32(17.13), np.float32(17.38), np.float32(17.63), np.float32(17.88), np.float32(18.13),
       np.float32(18.38), np.float32(18.63), np.float32(18.88), np.float32(19.13), np.float32(19.38), np.float32(19.63),
       np.float32(0.0), np.float32(0.0)]
for i in range(0, 250 - 48):
    EIN = np.append(EIN, 0.0)

gd['gas1/EIN'] = EIN
#  ENERGY

XENG2 = [np.float32(1.00), np.float32(1.20), np.float32(1.50), np.float32(1.70), np.float32(2.00), np.float32(2.50),
         np.float32(3.00), np.float32(4.00), np.float32(5.00), np.float32(6.00),
         np.float32(7.00), np.float32(8.00), np.float32(9.00), np.float32(10.0), np.float32(11.0), np.float32(12.0),
         np.float32(13.0), np.float32(14.0), np.float32(15.0), np.float32(16.0),
         np.float32(18.0), np.float32(20.0), np.float32(25.0), np.float32(30.0), np.float32(40.0), np.float32(50.0),
         np.float32(60.0), np.float32(70.0), np.float32(80.0), np.float32(90.0),
         np.float32(100.), np.float32(125.), np.float32(150.), np.float32(200.), np.float32(250.), np.float32(300.),
         np.float32(350.), np.float32(400.), np.float32(500.), np.float32(600.),
         np.float32(700.), np.float32(800.), np.float32(1000.), np.float32(1500.), np.float32(2000.), np.float32(3000.),
         np.float32(4000.), np.float32(5000.), np.float32(6000.), np.float32(8000.),
         np.float32(10000.), np.float32(15000.), np.float32(20000.), np.float32(40000.), np.float32(60000.),
         np.float32(80000.), 1.e5, 1.25e5, 1.5e5,
         1.75e5,
         2.e5, 2.5e5, 3.e5, 3.5e5, 4.e5, 4.5e5, 5.0e5, 6.0e5, 7.0e5, 8.0e5,
         9.0e5, 1.0e6, 1.25e6, 1.5e6, 1.75e6, 2.0e6, 2.5e6, 3.0e6, 3.5e6, 4.0e6,
         4.5e6, 5.0e6, 6.0e6, 7.0e6, 8.0e6, 9.0e6, 1.0e7, 1.25e7, 1.5e7, 1.75e7,
         2.0e7, 2.5e7, 3.0e7, 3.5e7, 4.0e7, 4.5e7, 5.0e7, 6.0e7, 7.0e7, 8.0e7,
         9.0e7, 1.0e8, 1.25e8, 1.5e8, 1.75e8, 2.0e8, 2.5e8, 3.0e8, 3.5e8, 4.0e8,
         4.5e8, 5.0e8, 6.0e8, 7.0e8, 8.0e8, 9.0e8, 1.0e9,
         ]
# ELASTIC MOMENTUM TRANSFER

YSECG2 = [np.float32(1.3913), np.float32(1.66), np.float32(2.05), np.float32(2.33), np.float32(2.70), np.float32(3.43),
          np.float32(4.20), np.float32(5.70), np.float32(7.60), np.float32(9.60),
          np.float32(11.5), np.float32(13.1), np.float32(14.7), np.float32(16.2), np.float32(16.8), np.float32(16.6),
          np.float32(15.9), np.float32(15.1), np.float32(14.2), np.float32(13.3),
          np.float32(11.5), np.float32(10.0), np.float32(7.75), np.float32(6.25), np.float32(4.45), np.float32(3.50),
          np.float32(2.80), np.float32(2.25), np.float32(2.00), np.float32(1.70),
          np.float32(1.50), np.float32(1.22), np.float32(1.00), np.float32(0.78), np.float32(0.64), np.float32(0.55),
          np.float32(0.48), np.float32(0.43), np.float32(.355), np.float32(0.30),
          np.float32(0.26), np.float32(0.22), np.float32(0.16), np.float32(.095), np.float32(.063), np.float32(.033),
          np.float32(.021), np.float32(.0146), np.float32(.0108), np.float32(.00708),
          np.float32(.00484), np.float32(.00240), np.float32(.00145), 4.3e-4, 2.1e-4, 1.26e-4, 8.64e-5, 5.91e-5,
          4.35e-5, 3.36e-5,
          2.70e-5, 1.88e-5, 1.41e-5, 1.10e-5, 8.94e-6, 7.45e-6, 6.34e-6, 4.80e-6,
          3.80e-6, 3.10e-6,
          2.59e-6, 2.21e-6, 1.56e-6, 1.18e-6, 9.32e-7, 7.56e-7, 5.30e-7, 3.95e-7,
          3.07e-7, 2.46e-7,
          2.02e-7, 1.69e-7, 1.24e-7, 9.49e-8, 7.52e-8, 6.12e-8, 5.08e-8, 3.41e-8,
          2.46e-8, 1.86e-8,
          1.46e-8, 9.65e-9, 6.88e-9, 5.16e-9, 4.01e-9, 3.21e-9, 2.62e-9, 1.85e-9,
          1.37e-9, 1.06e-9,
          8.37e-10, 6.80e-10, 4.37e-10, 3.04e-10, 2.23e-10, 1.71e-10, 1.10e-10,
          7.61e-11, 5.59e-11, 4.28e-11,
          3.38e-11, 2.74e-11, 1.90e-11, 1.40e-11, 1.07e-11, 8.45e-12, 6.84e-12,
          ]
# ELASTIC

YELG2 = [np.float32(1.4945), np.float32(1.80), np.float32(2.25), np.float32(2.63), np.float32(3.20), np.float32(4.15),
         np.float32(5.10), np.float32(7.05), np.float32(8.90), np.float32(11.1),
         np.float32(13.4), np.float32(15.8), np.float32(18.1), np.float32(20.3), np.float32(21.9), np.float32(23.0),
         np.float32(23.4), np.float32(23.5), np.float32(23.2), np.float32(22.2),
         np.float32(19.4), np.float32(17.0), np.float32(13.3), np.float32(11.0), np.float32(8.44), np.float32(7.16),
         np.float32(6.28), np.float32(5.78), np.float32(5.25), np.float32(4.89),
         np.float32(4.50), np.float32(3.95), np.float32(3.51), np.float32(3.03), np.float32(2.70), np.float32(2.48),
         np.float32(2.30), np.float32(2.10), np.float32(1.90), np.float32(1.72),
         np.float32(1.58), np.float32(1.47), np.float32(1.27), np.float32(0.98), np.float32(.818), np.float32(.620),
         np.float32(.510), np.float32(.434), np.float32(.380), np.float32(.313),
         np.float32(.250), np.float32(.180), np.float32(.138), np.float32(.076), np.float32(.056), np.float32(.045),
         np.float32(.0378), np.float32(.0322), np.float32(.0284), np.float32(.0257),
         np.float32(.0237), np.float32(.0209), np.float32(.0190), np.float32(.0177), np.float32(.0168),
         np.float32(.0160), np.float32(.0155), np.float32(.0146), np.float32(.0140), np.float32(.0136),
         np.float32(.0132), np.float32(.0130), np.float32(.0126), np.float32(.0123), np.float32(.0121),
         np.float32(.0120), np.float32(.0119), np.float32(.0118), np.float32(.0117), np.float32(.0117),
         np.float32(.0116), np.float32(.0116), np.float32(.0116), np.float32(.0116), np.float32(.0116),
         np.float32(.0116), np.float32(.0115), np.float32(.0115), np.float32(.0115), np.float32(.0115),
         np.float32(.0115), np.float32(.0115), np.float32(.0115), np.float32(.0115), np.float32(.0115),
         np.float32(.0115), np.float32(.0115), np.float32(.0115), np.float32(.0115), np.float32(.0115),
         np.float32(.0115), np.float32(.0115), np.float32(.0115), np.float32(.0115), np.float32(.0115),
         np.float32(.0115), np.float32(.0115), np.float32(.0115), np.float32(.0115), np.float32(.0115),
         np.float32(.0115), np.float32(.0115), np.float32(.0115), np.float32(.0115), np.float32(.0115),
         np.float32(.0115), np.float32(.0115),
         ]
# EPSILON FOR ELASTIC ANGULAR DISTRIBUTION

XEPSG2 = [np.float32(.0), np.float32(.0001), np.float32(.0002), np.float32(.0003), np.float32(.0004), np.float32(.0006),
          np.float32(.0008), np.float32(.001), np.float32(.0012), np.float32(.0014),
          np.float32(.0017), np.float32(.002), np.float32(.0025), np.float32(.003), np.float32(.004), np.float32(.005),
          np.float32(.006), np.float32(.008), np.float32(.010), np.float32(.012),
          np.float32(.014), np.float32(.017), np.float32(.020), np.float32(.025), np.float32(.030), np.float32(.035),
          np.float32(.040), np.float32(.045), np.float32(.050), np.float32(.055),
          np.float32(.060), np.float32(.065), np.float32(.070), np.float32(.075), np.float32(.080), np.float32(.085),
          np.float32(.090), np.float32(.095), np.float32(.100), np.float32(.110),
          np.float32(0.12), np.float32(0.13), np.float32(0.14), np.float32(0.15), np.float32(0.16), np.float32(0.17),
          np.float32(0.18), np.float32(0.19), np.float32(0.20), np.float32(0.21),
          np.float32(0.22), np.float32(0.23), np.float32(0.24), np.float32(0.25), np.float32(0.26), np.float32(0.27),
          np.float32(0.28), np.float32(0.29), np.float32(0.30), np.float32(0.31),
          np.float32(0.32), np.float32(0.33), np.float32(0.34), np.float32(0.35), np.float32(0.36), np.float32(0.37),
          np.float32(0.38), np.float32(0.39), np.float32(0.40), np.float32(0.41),
          np.float32(0.42), np.float32(0.43), np.float32(0.44), np.float32(0.45), np.float32(0.46), np.float32(0.47),
          np.float32(0.48), np.float32(0.49), np.float32(0.50), np.float32(0.51),
          np.float32(0.52), np.float32(0.53), np.float32(0.54), np.float32(0.55), np.float32(0.56), np.float32(0.57),
          np.float32(0.58), np.float32(0.59), np.float32(0.60), np.float32(0.61),
          np.float32(0.62), np.float32(0.63), np.float32(0.65), np.float32(0.67), np.float32(0.70), np.float32(0.75),
          np.float32(0.80), np.float32(0.85), np.float32(0.90), np.float32(0.95),
          np.float32(1.00), np.float32(1.20), np.float32(1.50), np.float32(1.70), np.float32(2.00), np.float32(2.50),
          np.float32(3.00), np.float32(4.00), np.float32(5.00), np.float32(6.00),
          np.float32(7.00), np.float32(8.00), np.float32(9.00), np.float32(10.0), np.float32(11.0), np.float32(12.0),
          np.float32(13.0), np.float32(14.0), np.float32(15.0), np.float32(16.0),
          np.float32(18.0), np.float32(20.0), np.float32(25.0), np.float32(30.0), np.float32(40.0), np.float32(50.0),
          np.float32(60.0), np.float32(70.0), np.float32(80.0), np.float32(90.0),
          np.float32(100.), np.float32(125.), np.float32(150.), np.float32(200.), np.float32(250.), np.float32(300.),
          np.float32(350.), np.float32(400.), np.float32(500.), np.float32(600.),
          np.float32(700.), np.float32(800.), np.float32(1000.), np.float32(1500.), np.float32(2000.),
          np.float32(3000.), np.float32(4000.), np.float32(5000.), np.float32(6000.), np.float32(8000.),
          np.float32(10000.), np.float32(15000.), np.float32(20000.), np.float32(40000.), np.float32(60000.),
          np.float32(80000.), 1.e5, 1.25e5, 1.5e5,
          1.75e5,
          2.0e5, 2.5e5, 3.0e5, 3.5e5, 4.0e5, 4.5e5, 5.0e5, 6.0e5, 7.0e5, 8.0e5,
          9.0e5, 1.0e6, 1.25e6, 1.5e6, 1.75e6, 2.0e6, 2.5e6, 3.0e6, 3.5e6, 4.0e6,
          4.5e6, 5.0e6, 6.0e6, 7.0e6, 8.0e6, 9.0e6, 1.0e7, 1.25e7, 1.5e7, 1.75e7,
          2.0e7, 2.5e7, 3.0e7, 3.5e7, 4.0e7, 4.5e7, 5.0e7, 6.0e7, 7.0e7, 8.0e7,
          9.0e7, 1.0e8, 1.25e8, 1.5e8, 1.75e8, 2.0e8, 2.5e8, 3.0e8, 3.5e8, 4.0e8,
          4.5e8, 5.0e8, 6.0e8, 7.0e8, 8.0e8, 9.0e8, 1.0e9,
          ]
# EPSILON =1-YEPS

YEPSG2 = [np.float32(1.0), np.float32(.987), np.float32(.9814), np.float32(.977), np.float32(.9734), np.float32(.9673),
          np.float32(.9619), np.float32(.9572), np.float32(.9530), np.float32(.9492),
          np.float32(.9433), np.float32(.9384), np.float32(.9304), np.float32(.9234), np.float32(.9103),
          np.float32(.8988), np.float32(.8879), np.float32(.8681), np.float32(.8501), np.float32(.8332),
          np.float32(.8173), np.float32(.7947), np.float32(.7727), np.float32(.7395), np.float32(.7071),
          np.float32(.6770), np.float32(.6469), np.float32(.6187), np.float32(.5909), np.float32(.5642),
          np.float32(.5379), np.float32(.5119), np.float32(.4866), np.float32(.4623), np.float32(.4384),
          np.float32(.4154), np.float32(.3932), np.float32(.3716), np.float32(.3505), np.float32(.3108),
          np.float32(.2745), np.float32(.2414), np.float32(.2118), np.float32(.1859), np.float32(.1637),
          np.float32(.1452), np.float32(.1304), np.float32(.1195), np.float32(.1123), np.float32(.1089),
          np.float32(.1093), np.float32(.1140), np.float32(.1231), np.float32(.1369), np.float32(.1559),
          np.float32(.1802), np.float32(.2104), np.float32(.2465), np.float32(.2882), np.float32(.3353),
          np.float32(.3872), np.float32(.4434), np.float32(.5019), np.float32(.5620), np.float32(.6222),
          np.float32(.6818), np.float32(.7400), np.float32(.7957), np.float32(.8477), np.float32(.8970),
          np.float32(.9414), np.float32(.982), np.float32(1.019), np.float32(1.0521), np.float32(1.0812),
          np.float32(1.107), np.float32(1.1293), np.float32(1.1487), np.float32(1.1654), np.float32(1.1796),
          np.float32(1.191), np.float32(1.2014), np.float32(1.208), np.float32(1.2137), np.float32(1.2179),
          np.float32(1.2205), np.float32(1.222), np.float32(1.222), np.float32(1.2213), np.float32(1.2194),
          np.float32(1.2165), np.float32(1.213), np.float32(1.2035), np.float32(1.192), np.float32(1.171),
          np.float32(1.1296), np.float32(1.0836), np.float32(1.0358), np.float32(.9876), np.float32(.9411),
          np.float32(.8966), np.float32(.8836), np.float32(.8671), np.float32(.8299), np.float32(.7682),
          np.float32(.7432), np.float32(.7390), np.float32(.7174), np.float32(.7830), np.float32(.7989),
          np.float32(.7892), np.float32(.7470), np.float32(.7226), np.float32(.7025), np.float32(.6590),
          np.float32(.5967), np.float32(.5406), np.float32(.4932), np.float32(.4554), np.float32(.4396),
          np.float32(.4320), np.float32(.4266), np.float32(.4200), np.float32(.4030), np.float32(.3564),
          np.float32(.3152), np.float32(.3716), np.float32(.2186), np.float32(.2113), np.float32(.1829),
          np.float32(.1713), np.float32(.1522), np.float32(.1344), np.float32(.1152), np.float32(.1018),
          np.float32(.0922), np.float32(.0843), np.float32(.0820), np.float32(.0717), np.float32(.0649),
          np.float32(.0597), np.float32(.0522), np.float32(.0409), np.float32(.0286), np.float32(.0210),
          np.float32(.0129), np.float32(.0093), np.float32(.0072), np.float32(.0058), np.float32(.0044),
          np.float32(.0035), np.float32(.0023), np.float32(.00173), 8.3e-4, 5.1e-4, 3.73e-4, 2.919e-4, 2.274e-4,
          1.847e-4, 1.546e-4,
          1.322e-4, 1.012e-4, 8.095e-5, 6.673e-5, 5.621e-5, 4.823e-5, 4.197e-5,
          3.279e-5, 2.647e-5, 2.191e-5,
          1.848e-5, 1.582e-5, 1.123e-5, 8.449e-6, 7.602e-6, 5.315e-6, 3.660e-6,
          2.682e-6, 2.050e-6, 1.617e-6,
          1.310e-6, 1.083e-6, 7.762e-7, 5.840e-7, 4.551e-7, 3.648e-7, 2.990e-7,
          2.254e-7, 1.376e-7, 1.021e-7,
          7.88e-8, 5.08e-8, 3.55e-8, 2.61e-8, 2.00e-8, 1.58e-8, 1.28e-8, 8.79e-9,
          6.41e-9, 4.86e-9,
          3.81e-9, 3.06e-9, 1.92e-9, 1.31e-9, 9.50e-10, 7.2e-10, 4.5e-10, 3.1e-10,
          2.2e-10, 1.7e-10,
          1.31e-10, 1.05e-10, 7.2e-11, 5.2e-11, 3.9e-11, 3.1e-11, 2.5e-11,
          ]
# IONISATION ( VALUES ABOVE 20KEV GENERATED BY BORN BETHE IN SUB)

XENIG2 = [np.float32(15.75961), np.float32(16.0), np.float32(16.5), np.float32(17.0), np.float32(17.5),
          np.float32(18.0), np.float32(18.5), np.float32(19.0), np.float32(19.5), np.float32(20.0),
          np.float32(20.5), np.float32(21.0), np.float32(21.5), np.float32(22.0), np.float32(22.5), np.float32(23.0),
          np.float32(23.5), np.float32(24.0), np.float32(24.5), np.float32(25.0),
          np.float32(25.5), np.float32(26.0), np.float32(28.0), np.float32(30.0), np.float32(32.0), np.float32(34.0),
          np.float32(36.0), np.float32(38.0), np.float32(40.0), np.float32(45.0),
          np.float32(50.0), np.float32(55.0), np.float32(60.0), np.float32(65.0), np.float32(70.0), np.float32(75.0),
          np.float32(80.0), np.float32(85.0), np.float32(90.0), np.float32(95.0),
          np.float32(100.), np.float32(110.), np.float32(120.), np.float32(130.), np.float32(140.), np.float32(150.),
          np.float32(160.), np.float32(180.), np.float32(200.), np.float32(250.),
          np.float32(300.), np.float32(350.), np.float32(400.), np.float32(450.), np.float32(500.), np.float32(600.),
          np.float32(700.), np.float32(800.), np.float32(900.), np.float32(1000.),
          np.float32(1200.), np.float32(1400.), np.float32(1600.), np.float32(1800.), np.float32(2000.),
          np.float32(2500.), np.float32(3000.), np.float32(3500.), np.float32(4000.), np.float32(5000.),
          np.float32(6000.), np.float32(8000.), np.float32(10000.), np.float32(14000.), np.float32(20000.),
          ]
# GROSS IONISATION

YENIG2 = [np.float32(0.00), np.float32(.031), np.float32(.094), np.float32(.163), np.float32(.235), np.float32(.310),
          np.float32(.386), np.float32(.465), np.float32(.546), np.float32(.627),
          np.float32(.713), np.float32(.787), np.float32(.858), np.float32(.933), np.float32(.994), np.float32(1.06),
          np.float32(1.12), np.float32(1.18), np.float32(1.24), np.float32(1.30),
          np.float32(1.35), np.float32(1.41), np.float32(1.60), np.float32(1.80), np.float32(1.96), np.float32(2.11),
          np.float32(2.24), np.float32(2.33), np.float32(2.39), np.float32(2.49),
          np.float32(2.53), np.float32(2.60), np.float32(2.66), np.float32(2.73), np.float32(2.77), np.float32(2.82),
          np.float32(2.84), np.float32(2.85), np.float32(2.86), np.float32(2.86),
          np.float32(2.85), np.float32(2.83), np.float32(2.81), np.float32(2.76), np.float32(2.73), np.float32(2.68),
          np.float32(2.62), np.float32(2.52), np.float32(2.39), np.float32(2.17),
          np.float32(1.97), np.float32(1.80), np.float32(1.67), np.float32(1.54), np.float32(1.44), np.float32(1.28),
          np.float32(1.15), np.float32(1.04), np.float32(.971), np.float32(.898),
          np.float32(.768), np.float32(.688), np.float32(.638), np.float32(.576), np.float32(.526), np.float32(.446),
          np.float32(.384), np.float32(.340), np.float32(.302), np.float32(.255),
          np.float32(.220), np.float32(.172), np.float32(.144), np.float32(.110), np.float32(.0825),
          ]
# COUNTING IONISATION

YENCG2 = [np.float32(0.00), np.float32(.031), np.float32(.094), np.float32(.163), np.float32(.235), np.float32(.310),
          np.float32(.386), np.float32(.465), np.float32(.546), np.float32(.627),
          np.float32(.713), np.float32(.787), np.float32(.858), np.float32(.933), np.float32(.994), np.float32(1.06),
          np.float32(1.12), np.float32(1.18), np.float32(1.24), np.float32(1.30),
          np.float32(1.35), np.float32(1.41), np.float32(1.60), np.float32(1.80), np.float32(1.96), np.float32(2.11),
          np.float32(2.24), np.float32(2.33), np.float32(2.39), np.float32(2.49),
          np.float32(2.52), np.float32(2.56), np.float32(2.58), np.float32(2.62), np.float32(2.63), np.float32(2.67),
          np.float32(2.68), np.float32(2.68), np.float32(2.69), np.float32(2.69),
          np.float32(2.68), np.float32(2.66), np.float32(2.64), np.float32(2.59), np.float32(2.56), np.float32(2.52),
          np.float32(2.46), np.float32(2.37), np.float32(2.24), np.float32(2.04),
          np.float32(1.85), np.float32(1.69), np.float32(1.57), np.float32(1.45), np.float32(1.35), np.float32(1.21),
          np.float32(1.08), np.float32(.981), np.float32(.912), np.float32(.843),
          np.float32(.721), np.float32(.646), np.float32(.599), np.float32(.540), np.float32(.494), np.float32(.419),
          np.float32(.361), np.float32(.319), np.float32(.283), np.float32(.239),
          np.float32(.206), np.float32(.162), np.float32(.136), np.float32(.104), np.float32(.0775),
          ]
# IONISATION FOR CHARGE STATE = 1

YEN1G2 = [np.float32(0.00), np.float32(.031), np.float32(.094), np.float32(.163), np.float32(.235), np.float32(.310),
          np.float32(.386), np.float32(.465), np.float32(.546), np.float32(.627),
          np.float32(.713), np.float32(.787), np.float32(.858), np.float32(.933), np.float32(.994), np.float32(1.06),
          np.float32(1.12), np.float32(1.18), np.float32(1.24), np.float32(1.30),
          np.float32(1.35), np.float32(1.41), np.float32(1.60), np.float32(1.80), np.float32(1.96), np.float32(2.11),
          np.float32(2.24), np.float32(2.33), np.float32(2.39), np.float32(2.49),
          np.float32(2.51), np.float32(2.52), np.float32(2.50), np.float32(2.50), np.float32(2.50), np.float32(2.52),
          np.float32(2.52), np.float32(2.52), np.float32(2.52), np.float32(2.50),
          np.float32(2.49), np.float32(2.47), np.float32(2.45), np.float32(2.41), np.float32(2.38), np.float32(2.33),
          np.float32(2.29), np.float32(2.20), np.float32(2.10), np.float32(1.91),
          np.float32(1.74), np.float32(1.59), np.float32(1.48), np.float32(1.37), np.float32(1.28), np.float32(1.14),
          np.float32(1.02), np.float32(.925), np.float32(.863), np.float32(.798),
          np.float32(.682), np.float32(.612), np.float32(.567), np.float32(.511), np.float32(.468), np.float32(.397),
          np.float32(.342), np.float32(.302), np.float32(.268), np.float32(.226),
          np.float32(.195), np.float32(.153), np.float32(.129), np.float32(.0984), np.float32(.0734),
          ]
# IONISATION FOR CHARGE STATE = 2

XEN2G2 = [np.float32(43.38928), np.float32(45.0), np.float32(50.0), np.float32(55.0), np.float32(60.0),
          np.float32(65.0), np.float32(70.0), np.float32(75.0), np.float32(80.0), np.float32(85.0),
          np.float32(90.0), np.float32(95.0), np.float32(100.), np.float32(110.), np.float32(120.), np.float32(130.),
          np.float32(140.), np.float32(150.), np.float32(160.), np.float32(180.),
          np.float32(200.), np.float32(250.), np.float32(300.), np.float32(350.), np.float32(400.), np.float32(450.),
          np.float32(500.), np.float32(600.), np.float32(700.), np.float32(800.),
          np.float32(900.), np.float32(1000.), np.float32(1200.), np.float32(1400.), np.float32(1600.),
          np.float32(1800.), np.float32(2000.), np.float32(2500.), np.float32(3000.), np.float32(3500.),
          np.float32(4000.), np.float32(5000.), np.float32(6000.), np.float32(8000.), np.float32(10000.),
          np.float32(14000.), np.float32(20000.),
          ]
YEN2G2 = [np.float32(0.00), np.float32(.00045), np.float32(.012), np.float32(.0391), np.float32(.0803),
          np.float32(.114), np.float32(.136), np.float32(.148), np.float32(.159), np.float32(.165),
          np.float32(.172), np.float32(.175), np.float32(.179), np.float32(.180), np.float32(.180), np.float32(.176),
          np.float32(.172), np.float32(.167), np.float32(.161), np.float32(.153),
          np.float32(.138), np.float32(.121), np.float32(.106), np.float32(.093), np.float32(.085), np.float32(.076),
          np.float32(.0667), np.float32(.0568), np.float32(.0518), np.float32(.0453),
          np.float32(.0418), np.float32(.0375), np.float32(.0321), np.float32(.0287), np.float32(.0266),
          np.float32(.0240), np.float32(.0234), np.float32(.0186), np.float32(.0161), np.float32(.0142),
          np.float32(.0126), np.float32(.0106), np.float32(.00916), np.float32(.00681), np.float32(.00574),
          np.float32(.00438), np.float32(.00326),
          ]
# IONISATION FOR CHARGE STATE =3

XEN3G2 = [np.float32(84.124), np.float32(100.), np.float32(110.), np.float32(120.), np.float32(130.), np.float32(140.),
          np.float32(150.), np.float32(160.), np.float32(180.), np.float32(200.),
          np.float32(250.), np.float32(300.), np.float32(350.), np.float32(400.), np.float32(450.), np.float32(500.),
          np.float32(600.), np.float32(700.), np.float32(800.), np.float32(900.),
          np.float32(1000.), np.float32(1200.), np.float32(1400.), np.float32(1600.), np.float32(1800.),
          np.float32(2000.), np.float32(2500.), np.float32(3000.), np.float32(3500.), np.float32(4000.),
          np.float32(5000.), np.float32(6000.), np.float32(8000.), np.float32(10000.), np.float32(14000.),
          np.float32(20000.),
          ]
YEN3G2 = [np.float32(0.0), np.float32(.000972), np.float32(.00209), np.float32(.00311), np.float32(.00400),
          np.float32(.00481), np.float32(.00520), np.float32(.00541),
          np.float32(.00552), np.float32(.00532),
          np.float32(.00504), np.float32(.00489), np.float32(.00607), np.float32(.00673), np.float32(.00751),
          np.float32(.00823), np.float32(.00903), np.float32(.00890), np.float32(.00887),
          np.float32(.00825),
          np.float32(.00832), np.float32(.00711), np.float32(.00636), np.float32(.00590), np.float32(.00532),
          np.float32(.00486), np.float32(.00413), np.float32(.00355), np.float32(.00314),
          np.float32(.00278),
          np.float32(.00236), np.float32(.00203), np.float32(.00160), np.float32(.00134), np.float32(.001024),
          np.float32(.000764),
          ]
# K-SHELL IONISATION

XKSHG2 = [np.float32(3205.9), np.float32(3283.), np.float32(3378.), np.float32(3475.), np.float32(3576.),
          np.float32(3680.), np.float32(3786.), np.float32(3896.), np.float32(4009.),
          np.float32(4125.),
          np.float32(4368.), np.float32(4625.), np.float32(4898.), np.float32(5186.), np.float32(5492.),
          np.float32(5816.), np.float32(6159.), np.float32(6522.), np.float32(6907.), np.float32(7314.),
          np.float32(7971.), np.float32(8688.), np.float32(9468.), 1.03e4, 1.09e4, 1.19e4, 1.30e4, 1.42e4, 1.54e4,
          1.68e4,
          1.89e4, 2.12e4, 2.37e4, 2.66e4, 2.99e4, 3.45e4, 3.98e4, 4.60e4, 5.31e4,
          6.13e4,
          7.29e4, 8.66e4, 1.00e5, 1.19e5, 1.41e5, 1.68e5, 2.00e5, 2.37e5, 2.82e5,
          3.35e5,
          4.10e5, 5.01e5, 6.13e5, 7.50e5, 8.91e5, 1.00e6, 1.22e6, 1.50e6, 1.83e6,
          2.30e6,
          2.90e6, 3.65e6, 4.60e6, 5.79e6, 7.50e6, 8.66e6, 1.00e7, 1.22e7, 1.50e7,
          1.83e7,
          2.24e7, 2.74e7, 3.55e7, 4.60e7, 5.79e7, 7.50e7, 8.66e7, 1.00e8, 1.22e8,
          1.50e8,
          1.83e8, 2.24e8, 2.74e8, 3.55e8, 4.60e7, 5.79e8, 7.50e8, 8.66e8, 1.00e9,
          ]
YKSHG2 = [np.float32(0.0), 1.59e-6, 3.44e-6, 5.20e-6, 6.89e-6, 8.51e-6, 1.01e-5,
          1.15e-5, 1.29e-5, 1.43e-5,
          1.68e-5, 1.91e-5, 2.11e-5, 2.30e-5, 2.46e-5, 2.61e-5, 2.74e-5, 2.85e-5,
          2.95e-5, 3.04e-5,
          3.14e-5, 3.21e-5, 3.25e-5, 3.27e-5, 3.27e-5, 3.26e-5, 3.23e-5, 3.18e-5,
          3.12e-5, 3.04e-5,
          2.93e-5, 2.81e-5, 2.68e-5, 2.54e-5, 2.40e-5, 2.23e-5, 2.07e-5, 1.92e-5,
          1.77e-5, 1.63e-5,
          1.48e-5, 1.39e-5, 1.24e-5, 1.13e-5, 1.04e-5, 9.53e-6, 8.82e-6, 8.22e-6,
          7.72e-6, 7.32e-6,
          6.94e-6, 6.67e-6, 6.48e-6, 6.37e-6, 6.33e-6, 6.33e-6, 6.36e-6, 6.45e-6,
          6.57e-6, 6.75e-6,
          6.97e-6, 7.21e-6, 7.47e-6, 7.75e-6, 8.08e-6, 8.27e-6, 8.46e-6, 8.73e-6,
          9.01e-6, 9.28e-6,
          9.56e-6, 9.85e-6, 1.02e-5, 1.06e-5, 1.09e-5, 1.13e-5, 1.15e-5, 1.17e-5,
          1.20e-5, 1.23e-5,
          1.25e-5, 1.28e-5, 1.31e-5, 1.35e-5, 1.39e-5, 1.42e-5, 1.46e-5, 1.48e-5,
          1.50e-5,
          ]
# L1 SHELL IONISATION

XL1SG2 = [np.float32(326.3), np.float32(329.0), np.float32(338.3), np.float32(347.8), np.float32(357.5),
          np.float32(367.6), np.float32(378.0), np.float32(388.6), np.float32(399.6),
          np.float32(410.9),
          np.float32(422.5), np.float32(447.), np.float32(473.), np.float32(500.), np.float32(529.), np.float32(559.),
          np.float32(592.), np.float32(626.), np.float32(662.), np.float32(701.),
          np.float32(742.), np.float32(807.), np.float32(879.), np.float32(957.), np.float32(1013.), np.float32(1103.),
          np.float32(1203.), np.float32(1313.), np.float32(1423.), np.float32(1553.),
          np.float32(1693.), np.float32(1893.), np.float32(2123.), np.float32(2383.), np.float32(2673.),
          np.float32(3003.), np.float32(3463.), np.float32(3993.), np.float32(4613.), np.float32(5323.),
          np.float32(6143.), np.float32(7303.), np.float32(8673.), 1.00e4, 1.19e4, 1.41e4, 1.68e4, 2.00e4, 2.37e4,
          2.82e4,
          3.35e4, 4.10e4, 5.01e4, 6.13e4, 7.50e4, 8.91e4, 1.00e5, 1.22e5, 1.50e5,
          1.83e5,
          2.30e5, 2.90e5, 3.65e5, 4.60e5, 5.79e5, 7.50e5, 8.66e5, 1.00e6, 1.22e6,
          1.50e6,
          1.83e6, 2.30e6, 2.90e6, 3.65e6, 4.60e6, 5.79e6, 7.50e6, 8.66e6, 1.00e7,
          1.22e7,
          1.50e7, 1.83e7, 2.30e7, 2.90e7, 3.65e7, 4.60e7, 5.79e7, 7.50e7, 8.66e7,
          1.00e8,
          1.22e8, 1.50e8, 1.83e8, 2.30e8, 2.90e8, 3.65e8, 4.60e8, 5.79e8, 7.50e8,
          8.66e8,
          1.00e9,
          ]
YL1SG2 = [np.float32(0.0), 5.83e-5, 2.39e-4, 4.07e-4, 5.63e-4, 7.08e-4, 8.43e-4,
          9.71e-4, 1.09e-3, 1.20e-3,
          1.31e-3, 1.50e-3, 1.68e-3, 1.84e-3, 1.98e-3, 2.11e-3, 2.22e-3, 2.32e-3,
          2.41e-3, 2.49e-3,
          2.55e-3, 2.63e-3, 2.68e-3, 2.72e-3, 2.73e-3, 2.72e-3, 2.71e-3, 2.67e-3,
          2.62e-3, 2.56e-3,
          2.49e-3, 2.38e-3, 2.27e-3, 2.14e-3, 2.02e-3, 1.89e-3, 1.74e-3, 1.59e-3,
          1.44e-3, 1.31e-3,
          1.19e-3, 1.05e-3, 9.22e-4, 8.28e-4, 7.26e-4, 6.36e-4, 5.57e-4, 4.87e-4,
          4.26e-4, 3.72e-4,
          3.26e-4, 2.79e-4, 2.40e-4, 2.07e-4, 1.79e-4, 1.59e-4, 1.48e-4, 1.30e-4,
          1.15e-4, 1.03e-4,
          9.19e-5, 8.32e-5, 7.66e-5, 7.16e-5, 6.81e-5, 6.55e-5, 6.45e-5, 6.40e-5,
          6.36e-5, 6.38e-5,
          6.44e-5, 6.54e-5, 6.67e-5, 6.84e-5, 7.02e-5, 7.22e-5, 7.45e-5, 7.59e-5,
          7.72e-5, 7.92e-5,
          8.12e-5, 8.32e-5, 8.55e-5, 8.79e-5, 9.03e-5, 9.26e-5, 9.50e-5, 9.77e-5,
          9.92e-5, 1.01e-4,
          1.03e-4, 1.05e-4, 1.07e-4, 1.09e-4, 1.12e-4, 1.14e-4, 1.17e-4, 1.19e-4,
          1.22e-4, 1.23e-4,
          1.25e-4,
          ]
# L2 SHELL IONISATION

XL2SG2 = [np.float32(250.6), np.float32(252.3), np.float32(260.3), np.float32(267.3), np.float32(275.3),
          np.float32(283.3), np.float32(291.3), np.float32(300.3), np.float32(308.3),
          np.float32(317.3),
          np.float32(326.3), np.float32(346.3), np.float32(366.3), np.float32(388.3), np.float32(411.3),
          np.float32(435.3), np.float32(461.3), np.float32(488.3), np.float32(517.3), np.float32(547.3),
          np.float32(580.3), np.float32(614.3), np.float32(650.3), np.float32(689.3), np.float32(751.3),
          np.float32(819.3), np.float32(892.3), np.float32(1001.), np.float32(1121.), np.float32(1261.),
          np.float32(1411.), np.float32(1581.), np.float32(1781.), np.float32(1941.), np.float32(2181.),
          np.float32(2441.), np.float32(2741.), np.float32(3071.), np.float32(3451.), np.float32(3871.),
          np.float32(4471.), np.float32(5161.), np.float32(5961.), np.float32(6881.), np.float32(7941.),
          np.float32(8911.), 1.00e4, 1.19e4, 1.41e4, 1.68e4,
          2.05e4, 2.44e4, 2.90e4, 3.45e4, 4.10e4, 4.87e4, 5.79e4, 6.88e4, 8.18e4,
          1.00e5,
          1.22e5, 1.50e5, 1.83e5, 2.24e5, 2.74e5, 3.35e5, 4.10e5, 5.01e5, 6.13e5,
          7.50e5,
          1.00e6, 1.22e6, 1.50e6, 1.83e6, 2.30e6, 2.90e6, 3.65e6, 4.60e6, 5.79e6,
          7.50e6,
          8.66e6, 1.00e7, 1.22e7, 1.50e7, 1.83e7, 2.30e7, 2.90e7, 3.65e7, 4.60e7,
          5.79e7,
          7.50e7, 8.66e7, 1.00e8, 1.22e8, 1.50e8, 1.83e8, 2.30e8, 2.90e8, 3.65e8,
          4.60e8,
          5.79e8, 7.50e8, 8.66e8, 1.00e9,
          ]
YL2SG2 = [np.float32(0.00), 9.77e-5, 4.86e-4, 8.50e-4, 1.19e-3, 1.51e-3, 1.81e-3,
          2.10e-3, 2.36e-3, 2.62e-3,
          2.85e-3, 3.29e-3, 3.67e-3, 4.01e-3, 4.32e-3, 4.59e-3, 4.83e-3, 5.04e-3,
          5.22e-3, 5.38e-3,
          5.52e-3, 5.63e-3, 5.72e-3, 5.79e-3, 5.86e-3, 5.89e-3, 5.88e-3, 5.82e-3,
          5.70e-3, 5.55e-3,
          5.36e-3, 5.14e-3, 4.90e-3, 4.72e-3, 4.46e-3, 4.21e-3, 3.95e-3, 3.70e-3,
          3.47e-3, 3.24e-3,
          2.96e-3, 2.70e-3, 2.46e-3, 2.23e-3, 2.01e-3, 1.86e-3, 1.71e-3, 1.51e-3,
          1.33e-3, 1.17e-3,
          1.01e-3, 8.83e-4, 7.77e-4, 6.83e-4, 6.02e-4, 5.31e-4, 4.69e-4, 4.16e-4,
          3.70e-4, 3.25e-4,
          2.87e-4, 2.56e-4, 2.30e-4, 2.09e-4, 1.92e-4, 1.78e-4, 1.68e-4, 1.60e-4,
          1.54e-4, 1.50e-4,
          1.48e-4, 1.48e-4, 1.49e-4, 1.51e-4, 1.54e-4, 1.58e-4, 1.63e-4, 1.68e-4,
          1.73e-4, 1.80e-4,
          1.83e-4, 1.87e-4, 1.93e-4, 1.98e-4, 2.04e-4, 2.10e-4, 2.16e-4, 2.23e-4,
          2.29e-4, 2.36e-4,
          2.43e-4, 2.47e-4, 2.52e-4, 2.57e-4, 2.63e-4, 2.69e-4, 2.75e-4, 2.82e-4,
          2.89e-4, 2.95e-4,
          3.02e-4, 3.09e-4, 3.13e-4, 3.17e-4,
          ]
# L3 SHELL IONISATION

XL3SG2 = [np.float32(248.4), np.float32(252.5), np.float32(260.5), np.float32(267.5), np.float32(275.5),
          np.float32(283.5), np.float32(291.5), np.float32(300.5), np.float32(308.5),
          np.float32(317.5),
          np.float32(326.5), np.float32(346.5), np.float32(366.5), np.float32(388.5), np.float32(411.5),
          np.float32(435.5), np.float32(461.5), np.float32(488.5), np.float32(517.5), np.float32(547.5),
          np.float32(580.5), np.float32(614.5), np.float32(650.5), np.float32(689.5), np.float32(751.5),
          np.float32(819.5), np.float32(892.5), np.float32(1001.), np.float32(1121.), np.float32(1261.),
          np.float32(1411.), np.float32(1581.), np.float32(1781.), np.float32(1941.), np.float32(2181.),
          np.float32(2441.), np.float32(2741.), np.float32(3071.), np.float32(3451.), np.float32(3871.),
          np.float32(4471.), np.float32(5161.), np.float32(5961.), np.float32(6881.), np.float32(7941.),
          np.float32(8911.), 1.00e4, 1.19e4, 1.41e4, 1.68e4,
          2.05e4, 2.44e4, 2.90e4, 3.45e4, 4.10e4, 4.87e4, 5.79e4, 6.88e4, 8.18e4,
          1.00e5,
          1.22e5, 1.50e5, 1.83e5, 2.24e5, 2.74e5, 3.35e5, 4.10e5, 5.01e5, 6.13e5,
          7.50e5,
          1.00e6, 1.22e6, 1.50e6, 1.83e6, 2.30e6, 2.90e6, 3.65e6, 4.60e6, 5.79e6,
          7.50e6,
          8.66e6, 1.00e7, 1.22e7, 1.50e7, 1.83e7, 2.30e7, 2.90e7, 3.65e7, 4.60e7,
          5.79e7,
          7.50e7, 8.66e7, 1.00e8, 1.22e8, 1.50e8, 1.83e8, 2.30e8, 2.90e8, 3.65e8,
          4.60e8,
          5.79e8, 7.50e8, 8.66e8, 1.00e9,
          ]
YL3SG2 = [np.float32(0.0), 4.71e-4, 1.25e-3, 1.98e-3, 2.67e-3, 3.31e-3, 3.92e-3,
          4.48e-3, 5.02e-3, 5.52e-3,
          6.00e-3, 6.86e-3, 7.63e-3, 8.32e-3, 8.93e-3, 9.47e-3, 9.95e-3, 1.04e-2,
          1.07e-2, 1.10e-2,
          1.13e-2, 1.15e-2, 1.17e-2, 1.18e-2, 1.20e-2, 1.20e-2, 1.20e-2, 1.19e-2,
          1.16e-2, 1.13e-2,
          1.09e-2, 1.05e-2, 9.97e-3, 9.59e-3, 9.07e-3, 8.55e-3, 8.03e-3, 7.53e-3,
          7.04e-3, 6.58e-3,
          6.02e-3, 5.49e-3, 4.99e-3, 4.52e-3, 4.09e-3, 3.77e-3, 3.47e-3, 3.06e-3,
          2.69e-3, 2.37e-3,
          2.04e-3, 1.79e-3, 1.58e-3, 1.39e-3, 1.22e-3, 1.08e-3, 9.52e-4, 8.44e-4,
          7.51e-4, 6.59e-4,
          5.82e-4, 5.19e-4, 4.66e-4, 4.23e-4, 3.89e-4, 3.61e-4, 3.40e-4, 3.24e-4,
          3.12e-4, 3.05e-4,
          3.00e-4, 3.00e-4, 3.02e-4, 3.06e-4, 3.12e-4, 3.20e-4, 3.30e-4, 3.40e-4,
          3.51e-4, 3.64e-4,
          3.72e-4, 3.79e-4, 3.90e-4, 4.01e-4, 4.13e-4, 4.25e-4, 4.39e-4, 4.52e-4,
          4.65e-4, 4.78e-4,
          4.93e-4, 5.01e-4, 5.10e-4, 5.21e-4, 5.33e-4, 5.45e-4, 5.58e-4, 5.71e-4,
          5.85e-4, 5.98e-4,
          6.11e-4, 6.26e-4, 6.35e-4, 6.43e-4,
          ]
# 1S5 METASTABLE SCALE BY 1/E**3 ABOVE 100 EV

X1S5G2 = [np.float32(11.548), np.float32(11.60), np.float32(11.63), np.float32(11.64), np.float32(11.66),
          np.float32(11.70), np.float32(11.75), np.float32(11.80), np.float32(11.82),
          np.float32(11.83),
          np.float32(11.84), np.float32(11.86), np.float32(11.88), np.float32(11.90), np.float32(11.93),
          np.float32(12.00), np.float32(12.10), np.float32(12.20), np.float32(12.30), np.float32(12.40),
          np.float32(12.50), np.float32(12.60), np.float32(12.70), np.float32(12.80), np.float32(12.83),
          np.float32(12.86), np.float32(12.90), np.float32(12.91), np.float32(12.93), np.float32(12.96),
          np.float32(13.00), np.float32(13.03), np.float32(13.05), np.float32(13.08), np.float32(13.10),
          np.float32(13.12), np.float32(13.15), np.float32(13.18), np.float32(13.20), np.float32(13.26),
          np.float32(13.28), np.float32(13.29), np.float32(13.35), np.float32(13.40), np.float32(13.45),
          np.float32(13.47), np.float32(13.50), np.float32(13.60), np.float32(13.70), np.float32(13.80),
          np.float32(14.0), np.float32(14.5), np.float32(15.0), np.float32(16.0), np.float32(17.0), np.float32(18.0),
          np.float32(20.0), np.float32(22.0), np.float32(24.0), np.float32(26.0),
          np.float32(28.0), np.float32(30.0), np.float32(35.0), np.float32(40.0), np.float32(45.0), np.float32(50.0),
          np.float32(60.0), np.float32(70.0), np.float32(80.0), np.float32(90.0),
          np.float32(100.),
          ]
# UNITS 10-18 CM**2

Y1S5G2 = [np.float32(0.00), np.float32(0.70), np.float32(1.22), np.float32(1.22), np.float32(1.01), np.float32(0.88),
          np.float32(0.83), np.float32(0.90), np.float32(1.13), np.float32(1.69),
          np.float32(2.27), np.float32(1.64), np.float32(1.13), np.float32(1.04), np.float32(0.99), np.float32(1.10),
          np.float32(1.31), np.float32(1.64), np.float32(2.05), np.float32(2.47),
          np.float32(2.86), np.float32(3.20), np.float32(3.40), np.float32(3.40), np.float32(3.33), np.float32(3.19),
          np.float32(2.77), np.float32(3.28), np.float32(2.56), np.float32(2.27),
          np.float32(2.27), np.float32(3.89), np.float32(5.20), np.float32(3.89), np.float32(2.72), np.float32(2.14),
          np.float32(1.75), np.float32(1.96), np.float32(1.69), np.float32(1.53),
          np.float32(2.03), np.float32(1.76), np.float32(1.94), np.float32(2.09), np.float32(2.18), np.float32(2.52),
          np.float32(2.36), np.float32(2.56), np.float32(2.80), np.float32(3.10),
          np.float32(3.85), np.float32(4.40), np.float32(4.94), np.float32(5.58), np.float32(6.16), np.float32(6.44),
          np.float32(6.20), np.float32(4.90), np.float32(3.80), np.float32(3.20),
          np.float32(2.50), np.float32(2.00), np.float32(1.15), np.float32(0.80), np.float32(0.52), np.float32(0.37),
          np.float32(0.24), np.float32(.135), np.float32(.088), np.float32(.060),
          np.float32(.042),
          ]
YEPS1G2 = [np.float32(0.0), np.float32(0.0), np.float32(0.0), np.float32(0.0), np.float32(0.0), np.float32(0.0),
           np.float32(0.0), np.float32(0.0), np.float32(0.0), np.float32(0.0), np.float32(0.0), np.float32(0.0),
           np.float32(0.0), np.float32(0.0), np.float32(0.0), np.float32(0.0), np.float32(0.0), np.float32(0.0),
           np.float32(0.0), np.float32(0.0), np.float32(0.0), np.float32(0.0), np.float32(0.0), np.float32(0.0),
           np.float32(0.0), np.float32(0.0), np.float32(0.0), np.float32(0.0), np.float32(0.0), np.float32(0.0),
           np.float32(0.0), np.float32(0.0), np.float32(0.0), np.float32(0.0), np.float32(0.0), np.float32(0.0),
           np.float32(0.0), np.float32(0.0), np.float32(0.0), np.float32(0.0), np.float32(0.0), np.float32(0.0),
           np.float32(0.0), np.float32(0.0), np.float32(0.0), np.float32(0.0), np.float32(0.0), np.float32(0.0),
           np.float32(0.0), np.float32(0.0), np.float32(0.0), np.float32(0.0), np.float32(0.0), np.float32(0.0),
           np.float32(0.0), np.float32(0.0), np.float32(0.0), np.float32(0.0), np.float32(0.0), np.float32(0.0),
           np.float32(0.0), np.float32(0.0), np.float32(0.0), np.float32(0.0), np.float32(0.0), np.float32(0.0),
           np.float32(0.0), np.float32(0.0), np.float32(0.0), np.float32(0.0), np.float32(0.0),
           ]
# 1S4 RESONANCE RADIATION 106.66 NM WAVELENGTH

# USE BEF SCALING ABOVE 1000EV  F=0.058

X1S4G2 = [np.float32(11.624), np.float32(11.65), np.float32(11.66), np.float32(11.67), np.float32(11.68),
          np.float32(11.69), np.float32(11.70), np.float32(11.74), np.float32(11.75),
          np.float32(11.77),
          np.float32(11.79), np.float32(11.82), np.float32(11.84), np.float32(11.87), np.float32(11.88),
          np.float32(11.90), np.float32(11.95), np.float32(12.00), np.float32(12.05), np.float32(12.10),
          np.float32(12.20), np.float32(12.30), np.float32(12.40), np.float32(12.50), np.float32(12.60),
          np.float32(12.70), np.float32(12.80), np.float32(12.85), np.float32(12.90), np.float32(12.905),
          np.float32(12.91), np.float32(12.93), np.float32(12.97), np.float32(13.00), np.float32(13.03),
          np.float32(13.05), np.float32(13.06), np.float32(13.07), np.float32(13.09), np.float32(13.10),
          np.float32(13.15), np.float32(13.18), np.float32(13.20), np.float32(13.21), np.float32(13.23),
          np.float32(13.26), np.float32(13.30), np.float32(13.35), np.float32(13.40), np.float32(13.45),
          np.float32(13.47), np.float32(13.49), np.float32(13.60), np.float32(13.70), np.float32(13.80),
          np.float32(14.0), np.float32(15.0), np.float32(16.0), np.float32(17.0), np.float32(18.0),
          np.float32(19.0), np.float32(20.0), np.float32(24.0), np.float32(27.0), np.float32(30.0), np.float32(40.0),
          np.float32(50.0), np.float32(60.0), np.float32(80.0), np.float32(100.),
          np.float32(140.), np.float32(200.), np.float32(250.), np.float32(300.), np.float32(400.), np.float32(500.),
          np.float32(600.), np.float32(800.), np.float32(1000.),
          ]
# UNITS 10**-18 CM**2

Y1S4G2 = [np.float32(0.00), np.float32(0.90), np.float32(1.48), np.float32(1.57), np.float32(1.57), np.float32(1.55),
          np.float32(1.48), np.float32(1.10), np.float32(1.05), np.float32(1.14),
          np.float32(1.22), np.float32(1.30), np.float32(1.42), np.float32(0.90), np.float32(0.81), np.float32(.742),
          np.float32(.761), np.float32(.788), np.float32(0.86), np.float32(0.92),
          np.float32(1.12), np.float32(1.55), np.float32(1.64), np.float32(1.91), np.float32(2.16), np.float32(2.32),
          np.float32(2.38), np.float32(2.34), np.float32(2.12), np.float32(2.02),
          np.float32(2.29), np.float32(2.00), np.float32(1.87), np.float32(1.93), np.float32(2.38), np.float32(3.28),
          np.float32(3.49), np.float32(3.20), np.float32(2.21), np.float32(2.05),
          np.float32(1.76), np.float32(2.27), np.float32(2.11), np.float32(2.36), np.float32(2.11), np.float32(1.98),
          np.float32(1.89), np.float32(1.82), np.float32(1.87), np.float32(1.94),
          np.float32(2.16), np.float32(2.07), np.float32(2.23), np.float32(2.40), np.float32(2.55), np.float32(2.90),
          np.float32(5.02), np.float32(6.23), np.float32(6.86), np.float32(7.43),
          np.float32(8.00), np.float32(8.05), np.float32(8.05), np.float32(8.00), np.float32(7.80), np.float32(7.30),
          np.float32(6.80), np.float32(6.30), np.float32(5.60), np.float32(5.00),
          np.float32(4.30), np.float32(3.60), np.float32(3.30), np.float32(3.00), np.float32(2.50), np.float32(2.15),
          np.float32(1.92), np.float32(1.60), np.float32(1.41),
          ]
YEPS2G2 = [np.float32(0.0), np.float32(0.0), np.float32(0.0), np.float32(0.0), np.float32(0.0), np.float32(0.0),
           np.float32(0.0), np.float32(0.0), np.float32(0.0), np.float32(0.0), np.float32(0.0), np.float32(0.0),
           np.float32(0.0), np.float32(0.0), np.float32(0.0), np.float32(0.0), np.float32(0.0), np.float32(0.0),
           np.float32(0.0), np.float32(0.0), np.float32(0.0), np.float32(0.0), np.float32(0.0), np.float32(0.0),
           np.float32(0.0), np.float32(0.0), np.float32(0.0), np.float32(0.0), np.float32(0.0), np.float32(0.0),
           np.float32(0.0), np.float32(0.0), np.float32(0.0), np.float32(0.0), np.float32(0.0), np.float32(0.0),
           np.float32(0.0), np.float32(0.0), np.float32(0.0), np.float32(0.0), np.float32(0.0), np.float32(0.0),
           np.float32(0.0), np.float32(0.0), np.float32(0.0), np.float32(0.0), np.float32(0.0), np.float32(0.0),
           np.float32(0.0), np.float32(0.0), np.float32(0.0), np.float32(0.0), np.float32(0.0), np.float32(0.0),
           np.float32(0.0), np.float32(0.0), np.float32(0.0), np.float32(0.0), np.float32(0.0), np.float32(0.0),
           np.float32(0.0), np.float32(0.0), np.float32(0.0), np.float32(0.0), np.float32(0.0), np.float32(0.0),
           np.float32(0.0), np.float32(0.0), np.float32(0.0), np.float32(0.0), np.float32(0.0), np.float32(0.0),
           np.float32(0.0), np.float32(0.0), np.float32(0.0), np.float32(0.0), np.float32(0.0), np.float32(0.0),
           np.float32(0.0),
           ]
# 1S3 METASTABLE SCALE BY 1/E**3 ABOVE 100 EV

X1S3G2 = [np.float32(11.723), np.float32(11.75), np.float32(11.76), np.float32(11.78), np.float32(11.79),
          np.float32(11.80), np.float32(11.84), np.float32(11.86), np.float32(11.90),
          np.float32(11.95),
          np.float32(12.00), np.float32(12.10), np.float32(12.20), np.float32(12.30), np.float32(12.40),
          np.float32(12.50), np.float32(12.60), np.float32(12.70), np.float32(12.80), np.float32(12.85),
          np.float32(12.90), np.float32(12.91), np.float32(12.92), np.float32(12.94), np.float32(12.98),
          np.float32(12.99), np.float32(13.00), np.float32(13.01), np.float32(13.04), np.float32(13.05),
          np.float32(13.06), np.float32(13.08), np.float32(13.10), np.float32(13.15), np.float32(13.18),
          np.float32(13.20), np.float32(13.21), np.float32(13.23), np.float32(13.25), np.float32(13.27),
          np.float32(13.30), np.float32(13.35), np.float32(13.40), np.float32(13.45), np.float32(13.47),
          np.float32(13.49), np.float32(13.60), np.float32(13.70), np.float32(13.80), np.float32(14.0),
          np.float32(14.5), np.float32(15.0), np.float32(16.0), np.float32(17.0), np.float32(18.0), np.float32(20.0),
          np.float32(22.0), np.float32(24.0), np.float32(26.0), np.float32(28.0),
          np.float32(30.0), np.float32(35.0), np.float32(40.0), np.float32(45.0), np.float32(50.0), np.float32(60.0),
          np.float32(70.0), np.float32(80.0), np.float32(90.0), np.float32(100.),
          ]
# UNITS 10**-18 CM**2

Y1S3G2 = [np.float32(0.00), np.float32(.176), np.float32(0.38), np.float32(0.45), np.float32(0.45), np.float32(0.43),
          np.float32(0.23), np.float32(0.23), np.float32(.176), np.float32(.155),
          np.float32(.155), np.float32(.171), np.float32(.211), np.float32(.259), np.float32(.317), np.float32(.389),
          np.float32(.454), np.float32(.509), np.float32(.542), np.float32(.535),
          np.float32(.479), np.float32(.373), np.float32(.567), np.float32(.486), np.float32(.437), np.float32(.639),
          np.float32(.518), np.float32(.461), np.float32(.518), np.float32(.752),
          np.float32(.979), np.float32(.873), np.float32(.706), np.float32(.535), np.float32(.535), np.float32(.826),
          np.float32(1.12), np.float32(.891), np.float32(.720), np.float32(.616),
          np.float32(.461), np.float32(.236), np.float32(.243), np.float32(.252), np.float32(.445), np.float32(.356),
          np.float32(.405), np.float32(.454), np.float32(.486), np.float32(0.56),
          np.float32(0.80), np.float32(0.99), np.float32(1.12), np.float32(1.23), np.float32(1.29), np.float32(1.24),
          np.float32(0.98), np.float32(0.76), np.float32(0.64), np.float32(0.50),
          np.float32(0.40), np.float32(0.23), np.float32(0.16), np.float32(.104), np.float32(.074), np.float32(.048),
          np.float32(.027), np.float32(.0176), np.float32(.0120), np.float32(.0084),
          ]
YEPS3G2 = [np.float32(0.0), np.float32(0.0), np.float32(0.0), np.float32(0.0), np.float32(0.0), np.float32(0.0),
           np.float32(0.0), np.float32(0.0), np.float32(0.0), np.float32(0.0), np.float32(0.0), np.float32(0.0),
           np.float32(0.0), np.float32(0.0), np.float32(0.0), np.float32(0.0), np.float32(0.0), np.float32(0.0),
           np.float32(0.0), np.float32(0.0), np.float32(0.0), np.float32(0.0), np.float32(0.0), np.float32(0.0),
           np.float32(0.0), np.float32(0.0), np.float32(0.0), np.float32(0.0), np.float32(0.0), np.float32(0.0),
           np.float32(0.0), np.float32(0.0), np.float32(0.0), np.float32(0.0), np.float32(0.0), np.float32(0.0),
           np.float32(0.0), np.float32(0.0), np.float32(0.0), np.float32(0.0), np.float32(0.0), np.float32(0.0),
           np.float32(0.0), np.float32(0.0), np.float32(0.0), np.float32(0.0), np.float32(0.0), np.float32(0.0),
           np.float32(0.0), np.float32(0.0), np.float32(0.0), np.float32(0.0), np.float32(0.0), np.float32(0.0),
           np.float32(0.0), np.float32(0.0), np.float32(0.0), np.float32(0.0), np.float32(0.0), np.float32(0.0),
           np.float32(0.0), np.float32(0.0), np.float32(0.0), np.float32(0.0), np.float32(0.0), np.float32(0.0),
           np.float32(0.0), np.float32(0.0), np.float32(0.0), np.float32(0.0),
           ]
# 1S2 RESONANCE RADIATION 104.82 NM WAVELENGTH

# USE BEF SCALING ABOVE 400 EV F=0.2214

X1S2G2 = [np.float32(11.828), np.float32(11.85), np.float32(11.86), np.float32(11.88), np.float32(11.90),
          np.float32(11.93), np.float32(11.96), np.float32(12.00), np.float32(12.05),
          np.float32(12.10),
          np.float32(12.20), np.float32(12.30), np.float32(12.40), np.float32(12.50), np.float32(12.60),
          np.float32(12.70), np.float32(12.80), np.float32(12.85), np.float32(12.90), np.float32(12.91),
          np.float32(12.93), np.float32(12.95), np.float32(13.00), np.float32(13.02), np.float32(13.06),
          np.float32(13.10), np.float32(13.13), np.float32(13.15), np.float32(13.17), np.float32(13.20),
          np.float32(13.21), np.float32(13.23), np.float32(13.25), np.float32(13.27), np.float32(13.30),
          np.float32(13.35), np.float32(13.40), np.float32(13.45), np.float32(13.46), np.float32(13.48),
          np.float32(13.50), np.float32(13.60), np.float32(13.70), np.float32(13.80), np.float32(14.0),
          np.float32(15.0), np.float32(16.0), np.float32(17.0), np.float32(18.0), np.float32(19.0),
          np.float32(20.0), np.float32(22.0), np.float32(24.0), np.float32(26.0), np.float32(28.0), np.float32(30.0),
          np.float32(35.0), np.float32(40.0), np.float32(50.0), np.float32(60.0),
          np.float32(80.0), np.float32(100.), np.float32(120.), np.float32(140.), np.float32(170.), np.float32(200.),
          np.float32(250.), np.float32(300.), np.float32(350.), np.float32(400.),
          ]
# UNITS 10**-18 CM**2

Y1S2G2 = [np.float32(0.00), np.float32(1.55), np.float32(1.94), np.float32(1.76), np.float32(1.58), np.float32(1.37),
          np.float32(1.24), np.float32(1.19), np.float32(1.19), np.float32(1.21),
          np.float32(1.30), np.float32(1.44), np.float32(1.64), np.float32(1.91), np.float32(2.25), np.float32(2.52),
          np.float32(2.75), np.float32(2.83), np.float32(2.86), np.float32(3.46),
          np.float32(3.04), np.float32(2.95), np.float32(2.93), np.float32(3.08), np.float32(4.18), np.float32(3.29),
          np.float32(3.17), np.float32(3.02), np.float32(2.99), np.float32(3.60),
          np.float32(4.21), np.float32(3.78), np.float32(3.53), np.float32(3.17), np.float32(3.02), np.float32(2.74),
          np.float32(2.92), np.float32(3.29), np.float32(3.40), np.float32(3.24),
          np.float32(3.33), np.float32(3.71), np.float32(3.94), np.float32(4.20), np.float32(4.80), np.float32(7.20),
          np.float32(9.43), np.float32(11.7), np.float32(14.0), np.float32(16.0),
          np.float32(17.2), np.float32(18.8), np.float32(19.8), np.float32(20.6), np.float32(21.3), np.float32(22.0),
          np.float32(23.6), np.float32(24.7), np.float32(25.5), np.float32(25.3),
          np.float32(24.0), np.float32(22.3), np.float32(20.7), np.float32(19.3), np.float32(17.5), np.float32(16.0),
          np.float32(14.0), np.float32(12.5), np.float32(11.3), np.float32(10.3),
          ]
YEPS4G2 = [np.float32(0.0), np.float32(0.0), np.float32(0.0), np.float32(0.0), np.float32(0.0), np.float32(0.0),
           np.float32(0.0), np.float32(0.0), np.float32(0.0), np.float32(0.0), np.float32(0.0), np.float32(0.0),
           np.float32(0.0), np.float32(0.0), np.float32(0.0), np.float32(0.0), np.float32(0.0), np.float32(0.0),
           np.float32(0.0), np.float32(0.0), np.float32(0.0), np.float32(0.0), np.float32(0.0), np.float32(0.0),
           np.float32(0.0), np.float32(0.0), np.float32(0.0), np.float32(0.0), np.float32(0.0), np.float32(0.0),
           np.float32(0.0), np.float32(0.0), np.float32(0.0), np.float32(0.0), np.float32(0.0), np.float32(0.0),
           np.float32(0.0), np.float32(0.0), np.float32(0.0), np.float32(0.0), np.float32(0.0), np.float32(0.0),
           np.float32(0.0), np.float32(0.0), np.float32(0.0), np.float32(0.0), np.float32(0.0), np.float32(0.0),
           np.float32(0.0), np.float32(0.0), np.float32(0.0), np.float32(0.0), np.float32(0.0), np.float32(0.0),
           np.float32(0.0), np.float32(0.0), np.float32(0.0), np.float32(0.0), np.float32(0.0), np.float32(0.0),
           np.float32(0.0), np.float32(0.0), np.float32(0.0), np.float32(0.0), np.float32(0.0), np.float32(0.0),
           np.float32(0.0), np.float32(0.0), np.float32(0.0), np.float32(0.0),
           ]
# 2P10 J=1  SCALED BY 1/E**2 ABOVE 100 EV

X2P10G2 = [np.float32(12.907), np.float32(12.912), np.float32(12.922), np.float32(12.934), np.float32(12.949),
           np.float32(12.966), np.float32(13.00), np.float32(13.012),
           np.float32(13.035), np.float32(13.042),
           np.float32(13.053), np.float32(13.064), np.float32(13.068), np.float32(13.075), np.float32(13.089),
           np.float32(13.107), np.float32(13.141), np.float32(13.154), np.float32(13.162),
           np.float32(13.170),
           np.float32(13.180), np.float32(13.190), np.float32(13.202), np.float32(13.214), np.float32(13.220),
           np.float32(13.234), np.float32(13.239), np.float32(13.265), np.float32(13.271),
           np.float32(13.276),
           np.float32(13.300), np.float32(13.400), np.float32(13.445), np.float32(13.458), np.float32(13.467),
           np.float32(13.480), np.float32(13.50), np.float32(13.60), np.float32(14.0), np.float32(15.0),
           np.float32(16.0), np.float32(18.0), np.float32(19.0), np.float32(20.0), np.float32(21.0), np.float32(22.0),
           np.float32(25.0), np.float32(30.0), np.float32(35.0), np.float32(40.0),
           np.float32(50.0), np.float32(60.0), np.float32(80.0), np.float32(100.),
           ]
Y2P10G2 = [np.float32(0.00), np.float32(0.76), np.float32(0.40), np.float32(0.57), np.float32(0.53), np.float32(0.61),
           np.float32(0.95), np.float32(1.40), np.float32(1.78), np.float32(1.88),
           np.float32(1.74), np.float32(1.18), np.float32(0.70), np.float32(0.34), np.float32(0.13), np.float32(0.21),
           np.float32(0.39), np.float32(0.70), np.float32(1.01), np.float32(1.07),
           np.float32(1.33), np.float32(1.17), np.float32(1.43), np.float32(0.70), np.float32(0.36), np.float32(0.14),
           np.float32(0.11), np.float32(0.11), np.float32(0.25), np.float32(0.18),
           np.float32(0.19), np.float32(0.21), np.float32(0.22), np.float32(0.34), np.float32(0.51), np.float32(0.34),
           np.float32(0.32), np.float32(0.31), np.float32(0.39), np.float32(0.77),
           np.float32(1.13), np.float32(1.82), np.float32(2.03), np.float32(2.16), np.float32(2.20), np.float32(2.17),
           np.float32(1.89), np.float32(1.20), np.float32(0.81), np.float32(0.58),
           np.float32(0.33), np.float32(0.21), np.float32(0.11), np.float32(.065),
           ]
YEP2P10G2 = [np.float32(0.0), np.float32(0.0), np.float32(0.0), np.float32(0.0), np.float32(0.0), np.float32(0.0),
             np.float32(0.0), np.float32(0.0), np.float32(0.0), np.float32(0.0), np.float32(0.0), np.float32(0.0),
             np.float32(0.0), np.float32(0.0), np.float32(0.0), np.float32(0.0), np.float32(0.0), np.float32(0.0),
             np.float32(0.0), np.float32(0.0), np.float32(0.0), np.float32(0.0), np.float32(0.0), np.float32(0.0),
             np.float32(0.0), np.float32(0.0), np.float32(0.0), np.float32(0.0), np.float32(0.0), np.float32(0.0),
             np.float32(0.0), np.float32(0.0), np.float32(0.0), np.float32(0.0), np.float32(0.0), np.float32(0.0),
             np.float32(0.0), np.float32(0.0), np.float32(0.0), np.float32(0.0), np.float32(0.0), np.float32(0.0),
             np.float32(0.0), np.float32(0.0), np.float32(0.0), np.float32(0.0), np.float32(0.0), np.float32(0.0),
             np.float32(0.0), np.float32(0.0), np.float32(0.0), np.float32(0.0), np.float32(0.0), np.float32(0.0),
             ]
# 2P9 J=3  SCALED BY 1/E**2 ABOVE 100 EV

X2P9G2 = [np.float32(13.076), np.float32(14.0), np.float32(15.0), np.float32(16.0), np.float32(18.0), np.float32(19.0),
          np.float32(20.0), np.float32(21.0), np.float32(22.0), np.float32(25.0),
          np.float32(30.0), np.float32(35.0), np.float32(40.0), np.float32(50.0), np.float32(60.0), np.float32(80.0),
          np.float32(100.),
          ]
Y2P9G2 = [np.float32(0.00), np.float32(0.55), np.float32(1.23), np.float32(1.90), np.float32(2.75), np.float32(2.94),
          np.float32(3.00), np.float32(2.98), np.float32(2.92), np.float32(2.55),
          np.float32(1.73), np.float32(1.19), np.float32(0.85), np.float32(0.50), np.float32(0.32), np.float32(0.17),
          np.float32(0.11),
          ]
YEP2P9G2 = [np.float32(0.0), np.float32(0.0), np.float32(0.0), np.float32(0.0), np.float32(0.0), np.float32(0.0),
            np.float32(0.0), np.float32(0.0), np.float32(0.0), np.float32(0.0), np.float32(0.0), np.float32(0.0),
            np.float32(0.0), np.float32(0.0), np.float32(0.0), np.float32(0.0), np.float32(0.0),
            ]
# 2P8 J=2  SCALED BY 1/E ABOVE 100 EV

X2P8G2 = [np.float32(13.095), np.float32(14.0), np.float32(15.0), np.float32(16.0), np.float32(18.0), np.float32(20.0),
          np.float32(22.0), np.float32(25.0), np.float32(30.0), np.float32(35.0),
          np.float32(40.0), np.float32(50.0), np.float32(60.0), np.float32(80.0), np.float32(100.),
          ]
Y2P8G2 = [np.float32(0.00), np.float32(0.38), np.float32(0.85), np.float32(1.25), np.float32(1.85), np.float32(2.10),
          np.float32(2.30), np.float32(2.35), np.float32(2.40), np.float32(2.36),
          np.float32(2.20), np.float32(1.80), np.float32(1.50), np.float32(1.13), np.float32(0.90),
          ]
YEP2P8G2 = [np.float32(0.0), np.float32(0.0), np.float32(0.0), np.float32(0.0), np.float32(0.0), np.float32(0.0),
            np.float32(0.0), np.float32(0.0), np.float32(0.0), np.float32(0.0), np.float32(0.0), np.float32(0.0),
            np.float32(0.0), np.float32(0.0), np.float32(0.0),
            ]
# 2P7 J=1  SCALED BY 1/E**2 ABOVE 100 EV

X2P7G2 = [np.float32(13.153), np.float32(14.0), np.float32(15.0), np.float32(16.0), np.float32(18.0), np.float32(19.0),
          np.float32(20.0), np.float32(21.0), np.float32(22.0), np.float32(25.0),
          np.float32(30.0), np.float32(35.0), np.float32(40.0), np.float32(50.0), np.float32(60.0), np.float32(80.0),
          np.float32(100.),
          ]
Y2P7G2 = [np.float32(0.00), np.float32(0.20), np.float32(0.56), np.float32(0.92), np.float32(1.56), np.float32(1.74),
          np.float32(1.81), np.float32(1.81), np.float32(1.76), np.float32(1.60),
          np.float32(1.25), np.float32(1.00), np.float32(0.84), np.float32(0.61), np.float32(0.44), np.float32(0.27),
          np.float32(0.19),
          ]
YEP2P7G2 = [np.float32(0.0), np.float32(0.0), np.float32(0.0), np.float32(0.0), np.float32(0.0), np.float32(0.0),
            np.float32(0.0), np.float32(0.0), np.float32(0.0), np.float32(0.0), np.float32(0.0), np.float32(0.0),
            np.float32(0.0), np.float32(0.0), np.float32(0.0), np.float32(0.0), np.float32(0.0),
            ]
# 2P6 J=2  SCALED BY 1/E ABOVE 100 EV

X2P6G2 = [np.float32(13.172), np.float32(14.0), np.float32(15.0), np.float32(16.0), np.float32(18.0), np.float32(19.0),
          np.float32(20.0), np.float32(22.0), np.float32(25.0), np.float32(30.0),
          np.float32(35.0), np.float32(40.0), np.float32(50.0), np.float32(60.0), np.float32(80.0), np.float32(100.),
          ]
Y2P6G2 = [np.float32(0.00), np.float32(0.36), np.float32(0.81), np.float32(1.24), np.float32(1.84), np.float32(2.04),
          np.float32(2.10), np.float32(2.20), np.float32(2.18), np.float32(1.95),
          np.float32(1.80), np.float32(1.65), np.float32(1.42), np.float32(1.27), np.float32(1.04), np.float32(0.87),
          ]
YEP2P6G2 = [np.float32(0.0), np.float32(0.0), np.float32(0.0), np.float32(0.0), np.float32(0.0), np.float32(0.0),
            np.float32(0.0), np.float32(0.0), np.float32(0.0), np.float32(0.0), np.float32(0.0), np.float32(0.0),
            np.float32(0.0), np.float32(0.0), np.float32(0.0), np.float32(0.0),
            ]
# 2P5 J=0  SCALED BY 1/E ABOVE 100 EV

X2P5G2 = [np.float32(13.273), np.float32(14.0), np.float32(15.0), np.float32(16.0), np.float32(18.0), np.float32(19.0),
          np.float32(20.0), np.float32(21.0), np.float32(22.0), np.float32(25.0),
          np.float32(30.0), np.float32(35.0), np.float32(40.0), np.float32(50.0), np.float32(60.0), np.float32(80.0),
          np.float32(100.),
          ]
Y2P5G2 = [np.float32(0.00), np.float32(0.09), np.float32(0.28), np.float32(0.47), np.float32(0.83), np.float32(0.97),
          np.float32(1.08), np.float32(1.16), np.float32(1.20), np.float32(1.26),
          np.float32(1.25), np.float32(1.23), np.float32(1.20), np.float32(1.08), np.float32(0.96), np.float32(0.75),
          np.float32(0.60),
          ]
YEP2P5G2 = [np.float32(0.0), np.float32(0.0), np.float32(0.0), np.float32(0.0), np.float32(0.0), np.float32(0.0),
            np.float32(0.0), np.float32(0.0), np.float32(0.0), np.float32(0.0), np.float32(0.0), np.float32(0.0),
            np.float32(0.0), np.float32(0.0), np.float32(0.0), np.float32(0.0), np.float32(0.0),
            ]
# 2P4 J=1  SCALED BY 1/E**2 ABOVE 100 EV

X2P4G2 = [np.float32(13.283), np.float32(14.0), np.float32(15.0), np.float32(16.0), np.float32(18.0), np.float32(19.0),
          np.float32(20.0), np.float32(21.0), np.float32(22.0), np.float32(25.0),
          np.float32(30.0), np.float32(35.0), np.float32(40.0), np.float32(50.0), np.float32(60.0), np.float32(80.0),
          np.float32(100.),
          ]
Y2P4G2 = [np.float32(0.00), np.float32(0.18), np.float32(0.55), np.float32(0.90), np.float32(1.53), np.float32(1.71),
          np.float32(1.77), np.float32(1.77), np.float32(1.72), np.float32(1.57),
          np.float32(1.23), np.float32(0.98), np.float32(0.82), np.float32(0.60), np.float32(0.43), np.float32(0.26),
          np.float32(0.18),
          ]
YEP2P4G2 = [np.float32(0.0), np.float32(0.0), np.float32(0.0), np.float32(0.0), np.float32(0.0), np.float32(0.0),
            np.float32(0.0), np.float32(0.0), np.float32(0.0), np.float32(0.0), np.float32(0.0), np.float32(0.0),
            np.float32(0.0), np.float32(0.0), np.float32(0.0), np.float32(0.0), np.float32(0.0),
            ]
# 2P3 J=2  SCALED BY 1/E ABOVE 100 EV

X2P3G2 = [np.float32(13.302), np.float32(14.0), np.float32(15.0), np.float32(16.0), np.float32(18.0), np.float32(19.0),
          np.float32(20.0), np.float32(21.0), np.float32(22.0), np.float32(25.0),
          np.float32(30.0), np.float32(35.0), np.float32(40.0), np.float32(50.0), np.float32(60.0), np.float32(80.0),
          np.float32(100.),
          ]
Y2P3G2 = [np.float32(0.00), np.float32(.155), np.float32(0.39), np.float32(0.62), np.float32(1.11), np.float32(1.34),
          np.float32(1.51), np.float32(1.62), np.float32(1.70), np.float32(1.82),
          np.float32(1.85), np.float32(1.76), np.float32(1.62), np.float32(1.33), np.float32(1.10), np.float32(0.82),
          np.float32(0.66),
          ]
YEP2P3G2 = [np.float32(0.0), np.float32(0.0), np.float32(0.0), np.float32(0.0), np.float32(0.0), np.float32(0.0),
            np.float32(0.0), np.float32(0.0), np.float32(0.0), np.float32(0.0), np.float32(0.0), np.float32(0.0),
            np.float32(0.0), np.float32(0.0), np.float32(0.0), np.float32(0.0), np.float32(0.0),
            ]
# 2P2 J=1  SCALED BY 1/E**2 ABOVE 100 EV

X2P2G2 = [np.float32(13.328), np.float32(14.0), np.float32(15.0), np.float32(16.0), np.float32(18.0), np.float32(19.0),
          np.float32(20.0), np.float32(22.0), np.float32(25.0), np.float32(30.0),
          np.float32(35.0), np.float32(40.0), np.float32(50.0), np.float32(60.0), np.float32(80.0), np.float32(100.),
          ]
Y2P2G2 = [np.float32(0.00), np.float32(0.20), np.float32(0.46), np.float32(0.60), np.float32(0.74), np.float32(0.77),
          np.float32(.785), np.float32(0.78), np.float32(0.73), np.float32(0.62),
          np.float32(0.53), np.float32(0.44), np.float32(0.33), np.float32(0.25), np.float32(0.15), np.float32(0.10),
          ]
YEP2P2G2 = [np.float32(0.0), np.float32(0.0), np.float32(0.0), np.float32(0.0), np.float32(0.0), np.float32(0.0),
            np.float32(0.0), np.float32(0.0), np.float32(0.0), np.float32(0.0), np.float32(0.0), np.float32(0.0),
            np.float32(0.0), np.float32(0.0), np.float32(0.0), np.float32(0.0),
            ]
# 2P1 J=0  SCALED BY 1/E ABOVE 100 EV

X2P1G2 = [np.float32(13.480), np.float32(14.0), np.float32(15.0), np.float32(16.0), np.float32(18.0), np.float32(19.0),
          np.float32(20.0), np.float32(21.0), np.float32(22.0), np.float32(25.0),
          np.float32(30.0), np.float32(35.0), np.float32(40.0), np.float32(50.0), np.float32(60.0), np.float32(80.0),
          np.float32(100.),
          ]
Y2P1G2 = [np.float32(0.00), np.float32(0.29), np.float32(0.94), np.float32(1.58), np.float32(2.75), np.float32(3.22),
          np.float32(3.60), np.float32(3.85), np.float32(4.00), np.float32(4.20),
          np.float32(4.15), np.float32(4.10), np.float32(4.00), np.float32(3.60), np.float32(3.20), np.float32(2.50),
          np.float32(2.00),
          ]
YEP2P1G2 = [np.float32(0.0), np.float32(0.0), np.float32(0.0), np.float32(0.0), np.float32(0.0), np.float32(0.0),
            np.float32(0.0), np.float32(0.0), np.float32(0.0), np.float32(0.0), np.float32(0.0), np.float32(0.0),
            np.float32(0.0), np.float32(0.0), np.float32(0.0), np.float32(0.0), np.float32(0.0),
            ]
# 3D6 J=0 SCALED BY 1/E**3 ABOVE 100 EV

X3D6G2 = [np.float32(13.845), np.float32(14.0), np.float32(15.0), np.float32(16.0), np.float32(17.0), np.float32(18.0),
          np.float32(19.0), np.float32(20.0), np.float32(22.0), np.float32(25.0),
          np.float32(30.0), np.float32(35.0), np.float32(40.0), np.float32(45.0), np.float32(50.0), np.float32(60.0),
          np.float32(70.0), np.float32(80.0), np.float32(100.),
          ]
Y3D6G2 = [np.float32(0.00), np.float32(0.11), np.float32(0.64), np.float32(0.92), np.float32(1.05), np.float32(1.10),
          np.float32(1.10), np.float32(1.07), np.float32(0.97), np.float32(0.79),
          np.float32(0.56), np.float32(0.39), np.float32(0.28), np.float32(0.21), np.float32(0.16), np.float32(.099),
          np.float32(.065), np.float32(.045), np.float32(.024),
          ]
YEP3D6G2 = [np.float32(0.0), np.float32(0.0), np.float32(0.0), np.float32(0.0), np.float32(0.0), np.float32(0.0),
            np.float32(0.0), np.float32(0.0), np.float32(0.0), np.float32(0.0), np.float32(0.0), np.float32(0.0),
            np.float32(0.0), np.float32(0.0), np.float32(0.0), np.float32(0.0), np.float32(0.0), np.float32(0.0),
            np.float32(0.0),
            ]
# 3D5 J=1 DIPOLE ALLOWED BEF SCALING USE BEF ABOVE 400EV F=0.0010

X3D5G2 = [np.float32(13.864), np.float32(14.0), np.float32(15.0), np.float32(16.0), np.float32(17.0), np.float32(18.0),
          np.float32(19.0), np.float32(20.0), np.float32(22.0), np.float32(25.0),
          np.float32(30.0), np.float32(35.0), np.float32(40.0), np.float32(45.0), np.float32(50.0), np.float32(60.0),
          np.float32(70.0), np.float32(80.0), np.float32(100.), np.float32(120.),
          np.float32(140.), np.float32(170.), np.float32(200.), np.float32(250.), np.float32(300.), np.float32(400.),
          ]
#     DATA Y3D5/0.00,0.40,3.00,4.50,5.25,5.50,5.50,5.35,4.90,4.00,

#    /2.80,2.05,1.50,1.15,0.98,0.65,0.46,0.35,0.19,0.14,

#    /.115,.095,.077,.065,.054,.037/

Y3D5G2 = [np.float32(0.00), np.float32(0.32), np.float32(2.40), np.float32(3.60), np.float32(4.20), np.float32(4.40),
          np.float32(4.40), np.float32(4.28), np.float32(3.92), np.float32(3.20),
          np.float32(2.24), np.float32(1.64), np.float32(1.20), np.float32(0.92), np.float32(0.78), np.float32(0.52),
          np.float32(0.37), np.float32(0.28), np.float32(0.15), np.float32(.112),
          np.float32(.092), np.float32(.076), np.float32(.062), np.float32(.052), np.float32(.045), np.float32(.037),
          ]
YEP3D5G2 = [np.float32(0.0), np.float32(0.0), np.float32(0.0), np.float32(0.0), np.float32(0.0), np.float32(0.0),
            np.float32(0.0), np.float32(0.0), np.float32(0.0), np.float32(0.0), np.float32(0.0), np.float32(0.0),
            np.float32(0.0), np.float32(0.0), np.float32(0.0), np.float32(0.0), np.float32(0.0), np.float32(0.0),
            np.float32(0.0), np.float32(0.0), np.float32(0.0), np.float32(0.0), np.float32(0.0), np.float32(0.0),
            np.float32(0.0), np.float32(0.0),
            ]
# 3D4' J=4 SCALED BY 1/E**3 ABOVE 100 EV

X3D4PG2 = [np.float32(13.979), np.float32(15.0), np.float32(16.0), np.float32(17.0), np.float32(18.0), np.float32(19.0),
           np.float32(20.0), np.float32(22.0), np.float32(25.0), np.float32(30.0),
           np.float32(35.0), np.float32(40.0), np.float32(45.0), np.float32(50.0), np.float32(55.0), np.float32(60.0),
           np.float32(70.0), np.float32(80.0), np.float32(90.0), np.float32(100.),
           ]
Y3D4PG2 = [np.float32(0.00), np.float32(2.16), np.float32(3.31), np.float32(3.88), np.float32(4.11), np.float32(4.14),
           np.float32(4.04), np.float32(3.68), np.float32(3.03), np.float32(2.12),
           np.float32(1.50), np.float32(1.09), np.float32(.813), np.float32(.619), np.float32(.482), np.float32(.381),
           np.float32(.251), np.float32(.173), np.float32(.125), np.float32(.092),
           ]
YEP3D4PG2 = [np.float32(0.0), np.float32(0.0), np.float32(0.0), np.float32(0.0), np.float32(0.0), np.float32(0.0),
             np.float32(0.0), np.float32(0.0), np.float32(0.0), np.float32(0.0), np.float32(0.0), np.float32(0.0),
             np.float32(0.0), np.float32(0.0), np.float32(0.0), np.float32(0.0), np.float32(0.0), np.float32(0.0),
             np.float32(0.0), np.float32(0.0),
             ]
# 3D4  J=3  SCALED BY 1/E**2 ABOVE 100 EV

X3D4G2 = [np.float32(14.013), np.float32(15.0), np.float32(16.0), np.float32(17.0), np.float32(18.0), np.float32(19.0),
          np.float32(20.0), np.float32(21.0), np.float32(22.0), np.float32(25.0),
          np.float32(30.0), np.float32(35.0), np.float32(40.0), np.float32(45.0), np.float32(50.0), np.float32(55.0),
          np.float32(60.0), np.float32(65.0), np.float32(70.0), np.float32(75.0),
          np.float32(80.0), np.float32(90.0), np.float32(100.),
          ]
Y3D4G2 = [np.float32(0.00), np.float32(0.63), np.float32(1.05), np.float32(1.31), np.float32(1.48), np.float32(1.57),
          np.float32(1.62), np.float32(1.63), np.float32(1.62), np.float32(1.52),
          np.float32(1.28), np.float32(1.06), np.float32(0.88), np.float32(0.73), np.float32(0.62), np.float32(0.53),
          np.float32(0.46), np.float32(0.40), np.float32(0.35), np.float32(0.31),
          np.float32(0.28), np.float32(.225), np.float32(.186),
          ]
YEP3D4G2 = [np.float32(0.0), np.float32(0.0), np.float32(0.0), np.float32(0.0), np.float32(0.0), np.float32(0.0),
            np.float32(0.0), np.float32(0.0), np.float32(0.0), np.float32(0.0), np.float32(0.0), np.float32(0.0),
            np.float32(0.0), np.float32(0.0), np.float32(0.0), np.float32(0.0), np.float32(0.0), np.float32(0.0),
            np.float32(0.0), np.float32(0.0), np.float32(0.0), np.float32(0.0), np.float32(0.0),
            ]
# 3D3 J=2 SCALE BY 1/E**3 ABOVE 100 EV

X3D3G2 = [np.float32(13.903), np.float32(14.0), np.float32(15.0), np.float32(16.0), np.float32(17.0), np.float32(18.0),
          np.float32(19.0), np.float32(20.0), np.float32(22.0), np.float32(25.0),
          np.float32(30.0), np.float32(35.0), np.float32(40.0), np.float32(45.0), np.float32(50.0), np.float32(60.0),
          np.float32(70.0), np.float32(80.0), np.float32(90.0), np.float32(100.),
          ]
Y3D3G2 = [np.float32(0.00), np.float32(0.15), np.float32(1.60), np.float32(3.00), np.float32(3.70), np.float32(4.30),
          np.float32(4.50), np.float32(4.40), np.float32(4.20), np.float32(3.60),
          np.float32(2.63), np.float32(1.86), np.float32(1.35), np.float32(1.00), np.float32(0.76), np.float32(0.47),
          np.float32(0.31), np.float32(0.21), np.float32(0.15), np.float32(.114),
          ]
YEP3D3G2 = [np.float32(0.0), np.float32(0.0), np.float32(0.0), np.float32(0.0), np.float32(0.0), np.float32(0.0),
            np.float32(0.0), np.float32(0.0), np.float32(0.0), np.float32(0.0), np.float32(0.0), np.float32(0.0),
            np.float32(0.0), np.float32(0.0), np.float32(0.0), np.float32(0.0), np.float32(0.0), np.float32(0.0),
            np.float32(0.0), np.float32(0.0),
            ]
# 3D1'' J=2 (ALSO 2S5 J=1 ) SCALE BY 1/E**2 ABOVE 100 EV

X3D1PPG2 = [np.float32(14.063), np.float32(15.0), np.float32(16.0), np.float32(17.0), np.float32(18.0),
            np.float32(19.0), np.float32(20.0), np.float32(22.0), np.float32(25.0), np.float32(30.0),
            np.float32(35.0), np.float32(40.0), np.float32(45.0), np.float32(50.0), np.float32(60.0), np.float32(70.0),
            np.float32(80.0), np.float32(90.0), np.float32(100.),
            ]
Y3D1PPG2 = [np.float32(0.00), np.float32(0.60), np.float32(1.10), np.float32(1.50), np.float32(1.70), np.float32(1.80),
            np.float32(1.85), np.float32(1.85), np.float32(1.65), np.float32(1.35),
            np.float32(1.00), np.float32(0.73), np.float32(0.57), np.float32(0.45), np.float32(0.32), np.float32(0.23),
            np.float32(0.18), np.float32(.145), np.float32(.120),
            ]
YEP3D1PPG2 = [np.float32(0.0), np.float32(0.0), np.float32(0.0), np.float32(0.0), np.float32(0.0), np.float32(0.0),
              np.float32(0.0), np.float32(0.0), np.float32(0.0), np.float32(0.0), np.float32(0.0), np.float32(0.0),
              np.float32(0.0), np.float32(0.0), np.float32(0.0), np.float32(0.0), np.float32(0.0), np.float32(0.0),
              np.float32(0.0),
              ]
# 3D1'  J=3 SCALE BY 1/E ABOVE 100 EV

X3D1PG2 = [np.float32(14.099), np.float32(15.0), np.float32(16.0), np.float32(18.0), np.float32(19.0), np.float32(20.0),
           np.float32(21.0), np.float32(22.0), np.float32(25.0), np.float32(30.0),
           np.float32(35.0), np.float32(40.0), np.float32(50.0), np.float32(60.0), np.float32(80.0), np.float32(100.),
           ]
Y3D1PG2 = [np.float32(0.00), np.float32(0.08), np.float32(0.18), np.float32(0.33), np.float32(0.40), np.float32(0.45),
           np.float32(0.48), np.float32(0.50), np.float32(0.54), np.float32(0.55),
           np.float32(0.52), np.float32(0.48), np.float32(0.40), np.float32(0.33), np.float32(0.24), np.float32(0.20),
           ]
YEP3D1PG2 = [np.float32(0.0), np.float32(0.0), np.float32(0.0), np.float32(0.0), np.float32(0.0), np.float32(0.0),
             np.float32(0.0), np.float32(0.0), np.float32(0.0), np.float32(0.0), np.float32(0.0), np.float32(0.0),
             np.float32(0.0), np.float32(0.0), np.float32(0.0), np.float32(0.0),
             ]
# 3S1''''  J=2  SCALE BY 1/E**3 ABOVE 100 EV

X3S1PPPPG2 = [np.float32(14.214), np.float32(15.0), np.float32(16.0), np.float32(17.0), np.float32(18.0),
              np.float32(19.0), np.float32(20.0), np.float32(22.0), np.float32(24.0), np.float32(27.0),
              np.float32(30.0), np.float32(35.0), np.float32(40.0), np.float32(45.0), np.float32(50.0),
              np.float32(55.0), np.float32(60.0), np.float32(70.0), np.float32(80.0), np.float32(90.0),
              np.float32(100.),
              ]
Y3S1PPPPG2 = [np.float32(0.00), np.float32(0.80), np.float32(1.65), np.float32(2.10), np.float32(2.30),
              np.float32(2.35), np.float32(2.32), np.float32(2.15), np.float32(1.89), np.float32(1.54),
              np.float32(1.25), np.float32(0.89), np.float32(0.65), np.float32(0.48), np.float32(0.37),
              np.float32(0.29), np.float32(0.23), np.float32(0.15), np.float32(.103), np.float32(.074),
              np.float32(.055),
              ]
YEP3S1PPPPG2 = [np.float32(0.0), np.float32(0.0), np.float32(0.0), np.float32(0.0), np.float32(0.0), np.float32(0.0),
                np.float32(0.0), np.float32(0.0), np.float32(0.0), np.float32(0.0), np.float32(0.0), np.float32(0.0),
                np.float32(0.0), np.float32(0.0), np.float32(0.0), np.float32(0.0), np.float32(0.0), np.float32(0.0),
                np.float32(0.0), np.float32(0.0), np.float32(0.0),
                ]
# 3S1'''  J=3  SCALE BY 1/E ABOVE 100 EV

X3S1PPPG2 = [np.float32(14.236), np.float32(15.0), np.float32(16.0), np.float32(18.0), np.float32(19.0),
             np.float32(20.0), np.float32(21.0), np.float32(22.0), np.float32(25.0), np.float32(30.0),
             np.float32(35.0), np.float32(40.0), np.float32(50.0), np.float32(60.0), np.float32(80.0), np.float32(100.),
             ]
Y3S1PPPG2 = [np.float32(0.00), np.float32(0.12), np.float32(0.27), np.float32(0.50), np.float32(0.60), np.float32(0.68),
             np.float32(0.72), np.float32(0.75), np.float32(0.81), np.float32(0.82),
             np.float32(0.78), np.float32(0.72), np.float32(0.60), np.float32(0.52), np.float32(0.36), np.float32(0.30),
             ]
YEP3S1PPPG2 = [np.float32(0.0), np.float32(0.0), np.float32(0.0), np.float32(0.0), np.float32(0.0), np.float32(0.0),
               np.float32(0.0), np.float32(0.0), np.float32(0.0), np.float32(0.0), np.float32(0.0), np.float32(0.0),
               np.float32(0.0), np.float32(0.0), np.float32(0.0), np.float32(0.0),
               ]
# 3S1''  J=2  SCALE BY 1/E**3 ABOVE 100 EV

X3S1PPG2 = [np.float32(14.234), np.float32(15.0), np.float32(16.0), np.float32(17.0), np.float32(18.0),
            np.float32(19.0), np.float32(20.0), np.float32(21.0), np.float32(22.0), np.float32(25.0),
            np.float32(30.0), np.float32(35.0), np.float32(40.0), np.float32(45.0), np.float32(50.0), np.float32(55.0),
            np.float32(60.0), np.float32(70.0), np.float32(80.0), np.float32(90.0),
            np.float32(100.),
            ]
Y3S1PPG2 = [np.float32(0.00), np.float32(0.55), np.float32(1.06), np.float32(1.31), np.float32(1.42), np.float32(1.44),
            np.float32(1.42), np.float32(1.37), np.float32(1.31), np.float32(1.09),
            np.float32(0.77), np.float32(0.55), np.float32(0.40), np.float32(0.30), np.float32(0.23), np.float32(0.18),
            np.float32(0.14), np.float32(.0918), np.float32(.0635), np.float32(.0456),
            np.float32(.0339),
            ]
YEP3S1PPG2 = [np.float32(0.0), np.float32(0.0), np.float32(0.0), np.float32(0.0), np.float32(0.0), np.float32(0.0),
              np.float32(0.0), np.float32(0.0), np.float32(0.0), np.float32(0.0), np.float32(0.0), np.float32(0.0),
              np.float32(0.0), np.float32(0.0), np.float32(0.0), np.float32(0.0), np.float32(0.0), np.float32(0.0),
              np.float32(0.0), np.float32(0.0), np.float32(0.0),
              ]
# 2S5  J=2  SCALE BY 1/E**2  ABOVE 100 EV

X2S5G2 = [np.float32(14.068), np.float32(15.0), np.float32(16.0), np.float32(17.0), np.float32(18.0), np.float32(19.0),
          np.float32(20.0), np.float32(22.0), np.float32(25.0), np.float32(30.0),
          np.float32(35.0), np.float32(40.0), np.float32(45.0), np.float32(50.0), np.float32(60.0), np.float32(70.0),
          np.float32(80.0), np.float32(90.0), np.float32(100.),
          ]
Y2S5G2 = [np.float32(0.00), np.float32(0.60), np.float32(1.10), np.float32(1.50), np.float32(1.70), np.float32(1.80),
          np.float32(1.85), np.float32(1.85), np.float32(1.65), np.float32(1.35),
          np.float32(1.00), np.float32(0.73), np.float32(0.57), np.float32(0.45), np.float32(0.32), np.float32(0.23),
          np.float32(0.18), np.float32(.145), np.float32(.120),
          ]
YEP2S5G2 = [np.float32(0.0), np.float32(0.0), np.float32(0.0), np.float32(0.0), np.float32(0.0), np.float32(0.0),
            np.float32(0.0), np.float32(0.0), np.float32(0.0), np.float32(0.0), np.float32(0.0), np.float32(0.0),
            np.float32(0.0), np.float32(0.0), np.float32(0.0), np.float32(0.0), np.float32(0.0), np.float32(0.0),
            np.float32(0.0),
            ]
# 2S3  J=0  SCALE BY 1/E**2  ABOVE 100 EV

X2S3G2 = [np.float32(14.241), np.float32(15.0), np.float32(16.0), np.float32(17.0), np.float32(18.0), np.float32(19.0),
          np.float32(20.0), np.float32(22.0), np.float32(25.0), np.float32(30.0),
          np.float32(35.0), np.float32(40.0), np.float32(45.0), np.float32(50.0), np.float32(60.0), np.float32(70.0),
          np.float32(80.0), np.float32(90.0), np.float32(100.),
          ]
Y2S3G2 = [np.float32(0.00), np.float32(0.12), np.float32(0.22), np.float32(0.30), np.float32(0.34), np.float32(0.36),
          np.float32(0.37), np.float32(0.37), np.float32(0.33), np.float32(0.27),
          np.float32(0.20), np.float32(.146), np.float32(.114), np.float32(.090), np.float32(.064), np.float32(.046),
          np.float32(.036), np.float32(.029), np.float32(.024),
          ]
YEP2S3G2 = [np.float32(0.0), np.float32(0.0), np.float32(0.0), np.float32(0.0), np.float32(0.0), np.float32(0.0),
            np.float32(0.0), np.float32(0.0), np.float32(0.0), np.float32(0.0), np.float32(0.0), np.float32(0.0),
            np.float32(0.0), np.float32(0.0), np.float32(0.0), np.float32(0.0), np.float32(0.0), np.float32(0.0),
            np.float32(0.0),
            ]
# BREMSSTRAHLUNG X-SECTION WITH CUT OFF

# UNITS 10**-24 CM**2

Z18TG2 = [np.float32(1518.), np.float32(1035.), np.float32(582.), np.float32(355.), np.float32(207.), np.float32(99.5),
          np.float32(58.9), np.float32(37.1), np.float32(24.7), np.float32(21.9),
          np.float32(21.9), np.float32(22.3), np.float32(22.6), np.float32(22.9), np.float32(23.1), np.float32(23.4),
          np.float32(23.7), np.float32(24.0), np.float32(24.2), np.float32(24.4),
          np.float32(24.6), np.float32(24.7), np.float32(24.7), np.float32(24.8), np.float32(24.9),
          ]
EBRMG2 = [np.float32(1000.), np.float32(2000.), np.float32(5000.), np.float32(1.E4), np.float32(2.E4), np.float32(5.E4),
          np.float32(1.E5), np.float32(2.E5), np.float32(5.E5), np.float32(1.E6),
          np.float32(2.E6), np.float32(3.E6), np.float32(4.E6), np.float32(5.E6), np.float32(6.E6), np.float32(8.E6),
          np.float32(1.E7), np.float32(1.5E7), np.float32(2.E7), np.float32(3.E7),
          np.float32(4.E7), np.float32(5.E7), np.float32(6.E7), np.float32(8.E7), np.float32(1.E8),
          ]
EING2 = [np.float32(11.548), np.float32(11.624), np.float32(11.723), np.float32(11.828), np.float32(12.907),
         np.float32(13.076), np.float32(13.095), np.float32(13.153), np.float32(13.172), np.float32(13.273),
         np.float32(13.283), np.float32(13.302), np.float32(13.328), np.float32(13.480), np.float32(13.845),
         np.float32(13.864), np.float32(13.903), np.float32(13.979), np.float32(14.013), np.float32(14.063),
         np.float32(14.068), np.float32(14.090), np.float32(14.099), np.float32(14.153), np.float32(14.214),
         np.float32(14.234), np.float32(14.236), np.float32(14.241), np.float32(14.255), np.float32(14.304),
         np.float32(14.711), np.float32(14.848), np.float32(14.859), np.float32(15.004), np.float32(15.022),
         np.float32(15.118), np.float32(15.186), np.float32(15.190), np.float32(15.308), np.float32(15.351),
         np.float32(15.360), np.float32(15.366), np.float32(15.374), np.float32(15.660), np.float32(0.0)]
for i in range(0, 250 - 45):
    EING2.append(0.0)
gd['gas2/EIN'] = EING2
gd['gas2/XEN'] = XENG2
gd['gas2/YSEC'] = YSECG2
gd['gas2/YEL'] = YELG2
gd['gas2/XEPS'] = XEPSG2
gd['gas2/YEPS'] = YEPSG2
gd['gas2/XENI'] = XENIG2
gd['gas2/YENI'] = YENIG2
gd['gas2/YENC'] = YENCG2
gd['gas2/YEN1'] = YEN1G2
gd['gas2/XEN2'] = XEN2G2
gd['gas2/YEN2'] = YEN2G2
gd['gas2/XEN3'] = XEN3G2
gd['gas2/YEN3'] = YEN3G2
gd['gas2/XKSH'] = XKSHG2
gd['gas2/YKSH'] = YKSHG2
gd['gas2/XL1S'] = XL1SG2
gd['gas2/YL1S'] = YL1SG2
gd['gas2/XL2S'] = XL2SG2
gd['gas2/YL2S'] = YL2SG2
gd['gas2/XL3S'] = XL3SG2
gd['gas2/YL3S'] = YL3SG2
gd['gas2/X1S5'] = X1S5G2
gd['gas2/Y1S5'] = Y1S5G2
gd['gas2/YEPS1'] = YEPS1G2
gd['gas2/X1S4'] = X1S4G2
gd['gas2/Y1S4'] = Y1S4G2
gd['gas2/YEPS2'] = YEPS2G2
gd['gas2/X1S3'] = X1S3G2
gd['gas2/Y1S3'] = Y1S3G2
gd['gas2/YEPS3'] = YEPS3G2
gd['gas2/X1S2'] = X1S2G2
gd['gas2/Y1S2'] = Y1S2G2
gd['gas2/YEPS4'] = YEPS4G2
gd['gas2/X2P10'] = X2P10G2
gd['gas2/Y2P10'] = Y2P10G2
gd['gas2/YEP2P10'] = YEP2P10G2
gd['gas2/X2P9'] = X2P9G2
gd['gas2/Y2P9'] = Y2P9G2
gd['gas2/YEP2P9'] = YEP2P9G2
gd['gas2/X2P8'] = X2P8G2
gd['gas2/Y2P8'] = Y2P8G2
gd['gas2/YEP2P8'] = YEP2P8G2
gd['gas2/X2P7'] = X2P7G2
gd['gas2/Y2P7'] = Y2P7G2
gd['gas2/YEP2P7'] = YEP2P7G2
gd['gas2/X2P6'] = X2P6G2
gd['gas2/Y2P6'] = Y2P6G2
gd['gas2/YEP2P6'] = YEP2P6G2
gd['gas2/X2P5'] = X2P5G2
gd['gas2/Y2P5'] = Y2P5G2
gd['gas2/YEP2P5'] = YEP2P5G2
gd['gas2/X2P4'] = X2P4G2
gd['gas2/Y2P4'] = Y2P4G2
gd['gas2/YEP2P4'] = YEP2P4G2
gd['gas2/X2P3'] = X2P3G2
gd['gas2/Y2P3'] = Y2P3G2
gd['gas2/YEP2P3'] = YEP2P3G2
gd['gas2/X2P2'] = X2P2G2
gd['gas2/Y2P2'] = Y2P2G2
gd['gas2/YEP2P2'] = YEP2P2G2
gd['gas2/X2P1'] = X2P1G2
gd['gas2/Y2P1'] = Y2P1G2
gd['gas2/YEP2P1'] = YEP2P1G2
gd['gas2/X3D6'] = X3D6G2
gd['gas2/Y3D6'] = Y3D6G2
gd['gas2/YEP3D6'] = YEP3D6G2
gd['gas2/X3D5'] = X3D5G2
gd['gas2/Y3D5'] = Y3D5G2
gd['gas2/YEP3D5'] = YEP3D5G2
gd['gas2/X3D4P'] = X3D4PG2
gd['gas2/Y3D4P'] = Y3D4PG2
gd['gas2/YEP3D4P'] = YEP3D4PG2
gd['gas2/X3D4'] = X3D4G2
gd['gas2/Y3D4'] = Y3D4G2
gd['gas2/YEP3D4'] = YEP3D4G2
gd['gas2/X3D3'] = X3D3G2
gd['gas2/Y3D3'] = Y3D3G2
gd['gas2/YEP3D3'] = YEP3D3G2
gd['gas2/X3D1PP'] = X3D1PPG2
gd['gas2/Y3D1PP'] = Y3D1PPG2
gd['gas2/YEP3D1PP'] = YEP3D1PPG2
gd['gas2/X3D1P'] = X3D1PG2
gd['gas2/Y3D1P'] = Y3D1PG2
gd['gas2/YEP3D1P'] = YEP3D1PG2
gd['gas2/X3S1PPPP'] = X3S1PPPPG2
gd['gas2/Y3S1PPPP'] = Y3S1PPPPG2
gd['gas2/YEP3S1PPPP'] = YEP3S1PPPPG2
gd['gas2/X3S1PPP'] = X3S1PPPG2
gd['gas2/Y3S1PPP'] = Y3S1PPPG2
gd['gas2/YEP3S1PPP'] = YEP3S1PPPG2
gd['gas2/X3S1PP'] = X3S1PPG2
gd['gas2/Y3S1PP'] = Y3S1PPG2
gd['gas2/YEP3S1PP'] = YEP3S1PPG2
gd['gas2/X2S5'] = X2S5G2
gd['gas2/Y2S5'] = Y2S5G2
gd['gas2/YEP2S5'] = YEP2S5G2
gd['gas2/X2S3'] = X2S3G2
gd['gas2/Y2S3'] = Y2S3G2
gd['gas2/YEP2S3'] = YEP2S3G2
gd['gas2/Z18T'] = Z18TG2
gd['gas2/EBRM'] = EBRMG2

# ELASTIC

XENG3 = [np.float32(0.00), np.float32(.008), np.float32(.009), np.float32(0.01), np.float32(.013), np.float32(.017),
         np.float32(.020), np.float32(.025), np.float32(0.03), np.float32(0.04),
         np.float32(0.05), np.float32(0.06), np.float32(0.07), np.float32(0.08), np.float32(0.09), np.float32(0.10),
         np.float32(0.12), np.float32(0.15), np.float32(0.18), np.float32(0.20),
         np.float32(0.25), np.float32(0.30), np.float32(0.40), np.float32(0.50), np.float32(0.60), np.float32(0.70),
         np.float32(0.80), np.float32(0.90), np.float32(1.00), np.float32(1.20),
         np.float32(1.50), np.float32(1.80), np.float32(2.00), np.float32(2.50), np.float32(3.00), np.float32(4.00),
         np.float32(5.00), np.float32(6.00), np.float32(7.00), np.float32(8.00),
         np.float32(9.00), np.float32(10.0), np.float32(11.0), np.float32(12.0), np.float32(14.0), np.float32(16.0),
         np.float32(18.0), np.float32(20.0), np.float32(25.0), np.float32(30.0),
         np.float32(35.0), np.float32(40.0), np.float32(50.0), np.float32(60.0), np.float32(70.0), np.float32(80.0),
         np.float32(90.0), np.float32(100.), np.float32(125.), np.float32(150.),
         np.float32(200.), np.float32(250.), np.float32(300.), np.float32(400.), np.float32(500.), np.float32(600.),
         np.float32(800.), np.float32(1000.), np.float32(1500.), np.float32(2000.),
         np.float32(3000.), np.float32(4000.), np.float32(6000.), np.float32(8000.), np.float32(10000.), 1.25e4, 1.5e4,
         2.0e4, 2.5e4, 3.0e4,
         4.0e4, 6.0e4, 8.0e4, 1.0e5, 1.25e5, 1.5e5, 1.75e5, 2.0e5, 2.5e5, 3.0e5,
         3.5e5, 4.0e5, 4.5e5, 5.0e5, 6.0e5, 7.0e5, 8.0e5, 9.0e5, 1.0e6, 1.25e6,
         1.5e6, 1.75e6, 2.0e6, 2.5e6, 3.0e6, 3.5e6, 4.0e6, 4.5e6, 5.0e6, 6.0e6,
         7.0e6, 8.0e6, 9.0e6, 1.0e7, 1.25e7, 1.5e7, 1.75e7, 2.0e7, 2.5e7, 3.0e7,
         3.5e7, 4.0e7, 4.5e7, 5.0e7, 6.0e7, 7.0e7, 8.0e7, 9.0e7, 1.0e8, 1.25e8,
         1.5e8, 1.75e8, 2.0e8, 2.5e8, 3.0e8, 3.5e8, 4.0e8, 4.5e8, 5.0e8, 6.0e8,
         7.0e8, 8.0e8, 9.0e8, 1.0e9,
         ]
# ELASTIC MOMENTUM TRANSFER

YEMG3 = [np.float32(4.89), np.float32(5.18), np.float32(5.19), np.float32(5.21), np.float32(5.26), np.float32(5.31),
         np.float32(5.35), np.float32(5.41), np.float32(5.46), np.float32(5.54),
         np.float32(5.62), np.float32(5.68), np.float32(5.74), np.float32(5.79), np.float32(5.83), np.float32(5.86),
         np.float32(5.94), np.float32(6.04), np.float32(6.12), np.float32(6.16),
         np.float32(6.27), np.float32(6.35), np.float32(6.49), np.float32(6.59), np.float32(6.66), np.float32(6.73),
         np.float32(6.77), np.float32(6.82), np.float32(6.85), np.float32(6.91),
         np.float32(6.96), np.float32(6.98), np.float32(6.99), np.float32(6.96), np.float32(6.89), np.float32(6.62),
         np.float32(6.31), np.float32(6.00), np.float32(5.68), np.float32(5.35),
         np.float32(5.03), np.float32(4.72), np.float32(4.45), np.float32(4.20), np.float32(3.68), np.float32(3.28),
         np.float32(2.95), np.float32(2.64), np.float32(2.05), np.float32(1.63),
         np.float32(1.33), np.float32(1.09), np.float32(.785), np.float32(.590), np.float32(.465), np.float32(.375),
         np.float32(.309), np.float32(.262), np.float32(.179), np.float32(.132),
         np.float32(.0807), np.float32(.0549), np.float32(.0400), np.float32(.0242), np.float32(.0164),
         np.float32(.0119), np.float32(.00716), np.float32(.00482), np.float32(.00234), np.float32(.0014),
         np.float32(.000676), 4.03e-4, 1.93e-4, 1.15e-4, 7.65e-5, 5.10e-5, 3.66e-5, 2.17e-5,
         1.45e-5, 1.04e-5,
         6.18e-6, 2.99e-6, 1.71e-6, 1.21e-6, 8.26e-7, 6.05e-7, 4.66e-7, 3.73e-7,
         2.58e-7, 1.92e-7,
         1.50e-7, 1.22e-7, 1.01e-7, 8.59e-8, 6.48e-8, 5.11e-8, 4.17e-8, 3.48e-8,
         2.96e-8, 2.10e-8,
         1.58e-8, 1.24e-8, 1.01e-8, 7.05e-9, 5.24e-9, 4.07e-9, 3.25e-9, 2.67e-9,
         2.23e-9, 1.63e-9,
         1.25e-9, 9.89e-10, 8.04e-10, 6.67e-10, 4.47e-10, 3.22e-10, 2.43e-10,
         1.91e-10, 1.27e-10, 9.04e-11,
         6.79e-11, 5.29e-11, 4.24e-11, 3.48e-11, 2.46e-11, 1.84e-11, 1.42e-11,
         1.13e-11, 9.26e-12, 6.00e-12,
         4.20e-12, 3.10e-12, 2.38e-12, 1.53e-12, 1.06e-12, 7.82e-13, 5.99e-13,
         4.74e-13, 3.84e-13, 2.67e-13,
         1.96e-13, 1.50e-13, 1.19e-13, 9.62e-14,
         ]
# ELASTIC TOTAL

YELG3 = [np.float32(4.89), np.float32(5.19), np.float32(5.20), np.float32(5.21), np.float32(5.26), np.float32(5.29),
         np.float32(5.33), np.float32(5.37), np.float32(5.41), np.float32(5.47),
         np.float32(5.53), np.float32(5.58), np.float32(5.62), np.float32(5.66), np.float32(5.69), np.float32(5.70),
         np.float32(5.76), np.float32(5.83), np.float32(5.88), np.float32(5.90),
         np.float32(5.96), np.float32(6.01), np.float32(6.08), np.float32(6.12), np.float32(6.14), np.float32(6.16),
         np.float32(6.16), np.float32(6.17), np.float32(6.16), np.float32(6.16),
         np.float32(6.14), np.float32(6.11), np.float32(6.09), np.float32(6.01), np.float32(5.90), np.float32(5.60),
         np.float32(5.36), np.float32(5.10), np.float32(4.91), np.float32(4.70),
         np.float32(4.51), np.float32(4.32), np.float32(4.21), np.float32(4.10), np.float32(3.75), np.float32(3.49),
         np.float32(3.27), np.float32(3.03), np.float32(2.54), np.float32(2.14),
         np.float32(1.83), np.float32(1.61), np.float32(1.27), np.float32(1.06), np.float32(.884), np.float32(.746),
         np.float32(.652), np.float32(.580), np.float32(.460), np.float32(.355),
         np.float32(.244), np.float32(.194), np.float32(.150), np.float32(.117), np.float32(.087), np.float32(.071),
         np.float32(.052), np.float32(.041), np.float32(.028), np.float32(.022),
         np.float32(.014), np.float32(.0108), np.float32(.00722), np.float32(.00544), np.float32(.00437),
         np.float32(.00352), np.float32(.00295), np.float32(.00224), np.float32(.00182),
         np.float32(.00154),
         np.float32(.00118), np.float32(.000830), np.float32(.000654), np.float32(.000550), np.float32(.000466),
         np.float32(.000411), np.float32(.000371), np.float32(.000342),
         np.float32(.000301), np.float32(.000274),
         np.float32(.000255), np.float32(.000241), np.float32(.000230), np.float32(.000222), np.float32(.000209),
         np.float32(.000201), np.float32(.000195), np.float32(.000190),
         np.float32(.000186), np.float32(.000180),
         np.float32(.000177), np.float32(.000174), np.float32(.000172), np.float32(.000170), np.float32(.000169),
         np.float32(.000168), np.float32(.000167), np.float32(.000167),
         np.float32(.000167), np.float32(.000166),
         np.float32(.000166), np.float32(.000166), np.float32(.000166), np.float32(.000166), np.float32(.000165),
         np.float32(.000165), np.float32(.000165), np.float32(.000165), np.float32(.000165), np.float32(.000165),
         np.float32(.000165), np.float32(.000165), np.float32(.000165), np.float32(.000165), np.float32(.000165),
         np.float32(.000165), np.float32(.000165), np.float32(.000165), np.float32(.000165), np.float32(.000165),
         np.float32(.000165), np.float32(.000165), np.float32(.000165), np.float32(.000165), np.float32(.000165),
         np.float32(.000165), np.float32(.000165), np.float32(.000165), np.float32(.000165), np.float32(.000165),
         np.float32(.000165), np.float32(.000165), np.float32(.000165), np.float32(.000165),
         ]
# ANGULAR DISTRIBUTION PARAMETER EPSILON

# EPSILON = 1.0-YEPS

YEPSG3 = [np.float32(1.0), np.float32(.99711), np.float32(.99712), np.float32(1.0), np.float32(1.0),
          np.float32(1.00562), np.float32(1.00565), np.float32(1.01118),
          np.float32(1.01386), np.float32(1.01920),
          np.float32(1.02440), np.float32(1.02688), np.float32(1.03202), np.float32(1.03445), np.float32(1.03689),
          np.float32(1.04209), np.float32(1.04686), np.float32(1.05400),
          np.float32(1.06119), np.float32(1.06604),
          np.float32(1.07792), np.float32(1.08474), np.float32(1.10094), np.float32(1.11490), np.float32(1.12663),
          np.float32(1.13826), np.float32(1.14789), np.float32(1.15724),
          np.float32(1.16707), np.float32(1.18142),
          np.float32(1.19873), np.float32(1.21165), np.float32(1.21951), np.float32(1.23447), np.float32(1.24855),
          np.float32(1.26918), np.float32(1.26215), np.float32(1.26104),
          np.float32(1.23265), np.float32(1.20568),
          np.float32(1.17192), np.float32(1.13835), np.float32(1.08539), np.float32(1.03657), np.float32(.97200),
          np.float32(.90989), np.float32(.85384), np.float32(.80836),
          np.float32(.71541), np.float32(.65146),
          np.float32(.60355), np.float32(.53739), np.float32(.46277), np.float32(.38963), np.float32(.35522),
          np.float32(.32989), np.float32(.29979), np.float32(.27742),
          np.float32(.21850), np.float32(.20332),
          np.float32(.16921), np.float32(.13304), np.float32(.12155), np.float32(.08318), np.float32(.07263),
          np.float32(.06130), np.float32(.04637), np.float32(.03720),
          np.float32(.02338), np.float32(.016295),
          np.float32(.011386), np.float32(.008195), np.float32(.005394), np.float32(.004037), np.float32(.003205),
          np.float32(.002548), np.float32(.002113), np.float32(.001572),
          np.float32(.001246), np.float32(.001044),
          7.61e-4, 4.925e-4, 3.404e-4, 2.803e-4, 2.179e-4, 1.766e-4, 1.475e-4,
          1.258e-4, 9.60e-5, 7.65e-5,
          6.29e-5, 5.29e-5, 4.53e-5, 3.93e-5, 3.07e-5, 2.47e-5, 2.04e-5, 1.72e-5,
          1.47e-5, 1.05e-5,
          7.84e-6, 6.12e-6, 4.91e-6, 3.373e-6, 2.463e-6, 1.881e-6, 1.483e-6,
          1.200e-6, 9.91e-7, 7.09e-7,
          5.322e-7, 4.146e-7, 3.319e-7, 2.718e-7, 1.775e-7, 1.249e-7, 9.27e-8,
          7.15e-8, 4.62e-8, 3.23e-8,
          2.382e-8, 1.828e-8, 1.447e-8, 1.173e-8, 8.14e-9, 5.97e-9, 4.56e-9,
          3.59e-9, 2.90e-9, 1.83e-9,
          1.26e-9, 9.10e-10, 6.90e-10, 4.40e-10, 3.00e-10, 2.16e-10, 1.63e-10,
          1.27e-10, 1.02e-10, 7.0e-11,
          5.1e-11, 3.8e-11, 3.0e-11, 2.4e-11,
          ]
#  IONISATION (VALUES ABOVE 20KEV GENERATED BY BORN-BETHE IN SUB)

XIONG3 = [np.float32(24.58739), np.float32(25.0), np.float32(25.5), np.float32(26.0), np.float32(26.5),
          np.float32(27.0), np.float32(27.5), np.float32(28.0), np.float32(28.5), np.float32(29.0),
          np.float32(29.5), np.float32(30.0), np.float32(30.5), np.float32(31.0), np.float32(31.5), np.float32(32.0),
          np.float32(32.5), np.float32(33.0), np.float32(33.5), np.float32(34.0),
          np.float32(36.0), np.float32(38.0), np.float32(40.0), np.float32(45.0), np.float32(50.0), np.float32(55.0),
          np.float32(60.0), np.float32(65.0), np.float32(70.0), np.float32(75.0),
          np.float32(80.0), np.float32(85.0), np.float32(90.0), np.float32(95.0), np.float32(100.), np.float32(105.),
          np.float32(110.), np.float32(115.), np.float32(120.), np.float32(125.),
          np.float32(130.), np.float32(135.), np.float32(140.), np.float32(145.), np.float32(150.), np.float32(160.),
          np.float32(170.), np.float32(180.), np.float32(190.), np.float32(200.),
          np.float32(225.), np.float32(250.), np.float32(275.), np.float32(300.), np.float32(350.), np.float32(400.),
          np.float32(450.), np.float32(500.), np.float32(550.), np.float32(600.),
          np.float32(650.), np.float32(700.), np.float32(750.), np.float32(800.), np.float32(850.), np.float32(900.),
          np.float32(950.), np.float32(1000.), np.float32(1200.), np.float32(1400.),
          np.float32(1600.), np.float32(1800.), np.float32(2000.), np.float32(2500.), np.float32(3000.),
          np.float32(3500.), np.float32(4000.), np.float32(4500.), np.float32(5000.), np.float32(5500.),
          np.float32(6000.), np.float32(7000.), np.float32(8000.), np.float32(9000.), 1.0e4, 1.2e4, 1.4e4, 1.6e4, 1.8e4,
          2.0e4,
          ]
# GROSS IONISATION

YIONG3 = [np.float32(.0), np.float32(.0038), np.float32(.0094), np.float32(.0155), np.float32(.0218), np.float32(.0279),
          np.float32(.0336), np.float32(.0392), np.float32(.0446),
          np.float32(.0504),
          np.float32(.0561), np.float32(.0612), np.float32(.0667), np.float32(.0722), np.float32(.0773),
          np.float32(.0826), np.float32(.0878), np.float32(.0929), np.float32(.0981), np.float32(.103),
          np.float32(.121), np.float32(.138), np.float32(.154), np.float32(.188), np.float32(.219), np.float32(.242),
          np.float32(.262), np.float32(.276), np.float32(.290), np.float32(.301),
          np.float32(.311), np.float32(.319), np.float32(.326), np.float32(.333), np.float32(.336), np.float32(.338),
          np.float32(.340), np.float32(.341), np.float32(.342), np.float32(.342),
          np.float32(.343), np.float32(.342), np.float32(.341), np.float32(.340), np.float32(.338), np.float32(.335),
          np.float32(.332), np.float32(.326), np.float32(.322), np.float32(.316),
          np.float32(.302), np.float32(.290), np.float32(.279), np.float32(.268), np.float32(.246), np.float32(.231),
          np.float32(.216), np.float32(.203), np.float32(.191), np.float32(.180),
          np.float32(.171), np.float32(.163), np.float32(.155), np.float32(.148), np.float32(.142), np.float32(.136),
          np.float32(.130), np.float32(.125), np.float32(.109), np.float32(.097),
          np.float32(.0872), np.float32(.0795), np.float32(.0729), np.float32(.0608), np.float32(.0524),
          np.float32(.0458), np.float32(.0410), np.float32(.0368), np.float32(.0336), np.float32(.0311),
          np.float32(.0293), np.float32(.0255), np.float32(.0229), np.float32(.0206), np.float32(.0192),
          np.float32(.0164), np.float32(.0147), np.float32(.0130), np.float32(.0119), np.float32(.0108),
          ]
# COUNTING IONISATION

YINCG3 = [np.float32(.0), np.float32(.0038), np.float32(.0094), np.float32(.0155), np.float32(.0218), np.float32(.0279),
          np.float32(.0336), np.float32(.0392), np.float32(.0446),
          np.float32(.0504),
          np.float32(.0561), np.float32(.0612), np.float32(.0667), np.float32(.0722), np.float32(.0773),
          np.float32(.0826), np.float32(.0878), np.float32(.0929), np.float32(.0981), np.float32(.103),
          np.float32(.121), np.float32(.138), np.float32(.154), np.float32(.188), np.float32(.219), np.float32(.242),
          np.float32(.262), np.float32(.276), np.float32(.290), np.float32(.301),
          np.float32(.311), np.float32(.319), np.float32(.326), np.float32(.333), np.float32(.336), np.float32(.338),
          np.float32(.340), np.float32(.341), np.float32(.341), np.float32(.341),
          np.float32(.342), np.float32(.341), np.float32(.340), np.float32(.339), np.float32(.337), np.float32(.334),
          np.float32(.331), np.float32(.325), np.float32(.321), np.float32(.315),
          np.float32(.301), np.float32(.289), np.float32(.278), np.float32(.267), np.float32(.245), np.float32(.230),
          np.float32(.215), np.float32(.202), np.float32(.190), np.float32(.179),
          np.float32(.170), np.float32(.162), np.float32(.154), np.float32(.147), np.float32(.141), np.float32(.135),
          np.float32(.129), np.float32(.124), np.float32(.108), np.float32(.096),
          np.float32(.0867), np.float32(.0791), np.float32(.0725), np.float32(.0605), np.float32(.0522),
          np.float32(.0456), np.float32(.0408), np.float32(.0367), np.float32(.0335), np.float32(.0310),
          np.float32(.0292), np.float32(.0254), np.float32(.0228), np.float32(.0205), np.float32(.0191),
          np.float32(.0163), np.float32(.0146), np.float32(.0129), np.float32(.0118), np.float32(.0107),
          ]
#  ALL EXCITATIONS IN UNITS OF 10**-18

#  2 3S J=1 METASTABLE

X23SG3 = [np.float32(19.81961), np.float32(19.83), np.float32(19.85), np.float32(19.88), np.float32(19.9),
          np.float32(19.95), np.float32(20.0), np.float32(20.05), np.float32(20.1),
          np.float32(20.15),
          np.float32(20.2), np.float32(20.25), np.float32(20.3), np.float32(20.35), np.float32(20.4), np.float32(20.45),
          np.float32(20.50), np.float32(20.55), np.float32(20.6), np.float32(20.63),
          np.float32(20.66), np.float32(20.7), np.float32(20.75), np.float32(20.8), np.float32(20.85),
          np.float32(20.90), np.float32(20.94), np.float32(20.97), np.float32(21.0), np.float32(21.05),
          np.float32(21.1), np.float32(21.15), np.float32(21.2), np.float32(21.25), np.float32(21.3), np.float32(21.4),
          np.float32(21.5), np.float32(22.0), np.float32(22.2), np.float32(22.25),
          np.float32(22.3), np.float32(22.35), np.float32(22.4), np.float32(22.42), np.float32(22.44),
          np.float32(22.46), np.float32(22.48), np.float32(22.5), np.float32(22.52), np.float32(22.55),
          np.float32(22.6), np.float32(22.62), np.float32(22.64), np.float32(22.66), np.float32(22.68),
          np.float32(22.7), np.float32(22.71), np.float32(22.72), np.float32(22.75), np.float32(22.8),
          np.float32(22.85), np.float32(22.88), np.float32(22.9), np.float32(22.95), np.float32(22.97),
          np.float32(23.0), np.float32(23.05), np.float32(23.1), np.float32(23.3), np.float32(23.4),
          np.float32(23.5), np.float32(23.6), np.float32(23.8), np.float32(24.0), np.float32(24.5), np.float32(25.0),
          np.float32(26.0), np.float32(27.0), np.float32(28.0), np.float32(29.0),
          np.float32(30.0), np.float32(31.0), np.float32(32.0), np.float32(34.0), np.float32(36.0), np.float32(38.0),
          np.float32(40.0), np.float32(42.0), np.float32(44.0), np.float32(46.0),
          np.float32(48.0), np.float32(50.0), np.float32(55.0), np.float32(60.0), np.float32(65.0), np.float32(70.0),
          np.float32(75.0), np.float32(80.0), np.float32(85.0), np.float32(90.0),
          np.float32(100.), np.float32(110.), np.float32(120.), np.float32(130.), np.float32(140.), np.float32(150.),
          np.float32(160.), np.float32(180.), np.float32(200.), np.float32(220.),
          np.float32(240.), np.float32(260.), np.float32(280.), np.float32(300.), np.float32(340.), np.float32(380.),
          np.float32(420.), np.float32(460.), np.float32(500.), np.float32(550.),
          np.float32(600.), np.float32(650.), np.float32(700.), np.float32(750.), np.float32(800.), np.float32(850.),
          np.float32(900.), np.float32(950.), np.float32(1000.), np.float32(1100.),
          np.float32(1200.), np.float32(1300.), np.float32(1400.), np.float32(1500.), np.float32(1600.),
          np.float32(1700.), np.float32(1800.), np.float32(1900.), np.float32(2000.),
          ]
Y23SG3 = [np.float32(0.00), np.float32(.780), np.float32(1.16), np.float32(1.64), np.float32(1.98), np.float32(2.81),
          np.float32(3.53), np.float32(4.13), np.float32(4.61), np.float32(4.96),
          np.float32(5.20), np.float32(5.35), np.float32(5.41), np.float32(5.36), np.float32(5.21), np.float32(4.95),
          np.float32(4.63), np.float32(4.23), np.float32(3.66), np.float32(3.16),
          np.float32(3.04), np.float32(3.13), np.float32(3.41), np.float32(3.77), np.float32(4.14), np.float32(4.44),
          np.float32(4.54), np.float32(4.43), np.float32(4.27), np.float32(3.96),
          np.float32(3.69), np.float32(3.48), np.float32(3.32), np.float32(3.21), np.float32(3.15), np.float32(3.08),
          np.float32(3.06), np.float32(3.09), np.float32(3.08), np.float32(3.04),
          np.float32(2.97), np.float32(2.84), np.float32(2.25), np.float32(1.58), np.float32(1.83), np.float32(4.91),
          np.float32(4.45), np.float32(4.13), np.float32(3.95), np.float32(3.79),
          np.float32(3.60), np.float32(3.51), np.float32(3.07), np.float32(2.45), np.float32(2.61), np.float32(2.67),
          np.float32(2.36), np.float32(2.97), np.float32(3.01), np.float32(2.96),
          np.float32(2.87), np.float32(2.61), np.float32(3.04), np.float32(2.75), np.float32(3.16), np.float32(3.06),
          np.float32(2.90), np.float32(2.79), np.float32(2.81), np.float32(2.86),
          np.float32(2.75), np.float32(2.80), np.float32(2.71), np.float32(2.65), np.float32(2.58), np.float32(2.48),
          np.float32(2.39), np.float32(2.30), np.float32(2.19), np.float32(2.09),
          np.float32(1.98), np.float32(1.84), np.float32(1.73), np.float32(1.53), np.float32(1.36), np.float32(1.22),
          np.float32(1.09), np.float32(.985), np.float32(.892), np.float32(.812),
          np.float32(.742), np.float32(.680), np.float32(.555), np.float32(.461), np.float32(.389), np.float32(.332),
          np.float32(.287), np.float32(.250), np.float32(.220), np.float32(.194),
          np.float32(.154), np.float32(.125), np.float32(.103), np.float32(.0861), np.float32(.0726), np.float32(.0617),
          np.float32(.0529), np.float32(.0397), np.float32(.0305), np.float32(.0239),
          np.float32(.0191), np.float32(.0154), np.float32(.0126), np.float32(.0105), np.float32(.00740),
          np.float32(.00542), np.float32(.00407), np.float32(.00314), np.float32(.00247), np.float32(.00187),
          np.float32(.00145), np.float32(.00115), 9.23e-4, 7.53e-4, 6.22e-4, 5.20e-4, 4.39e-4, 3.74e-4,
          3.21e-4, 2.42e-4,
          1.86e-4, 1.47e-4, 1.18e-4, 9.57e-5, 7.89e-5, 6.58e-5, 5.54e-5, 4.71e-5,
          4.04e-5,
          ]
# 2 1S J=0 METASTABLE

X21SG3 = [np.float32(20.61577), np.float32(20.62), np.float32(20.63), np.float32(20.65), np.float32(20.67),
          np.float32(20.69), np.float32(20.72), np.float32(20.75),
          np.float32(20.80), np.float32(20.85),
          np.float32(20.90), np.float32(20.96), np.float32(20.98), np.float32(21.0), np.float32(21.05),
          np.float32(21.1), np.float32(21.15), np.float32(21.2), np.float32(21.22), np.float32(21.25),
          np.float32(21.3), np.float32(21.4), np.float32(21.5), np.float32(21.6), np.float32(21.7), np.float32(21.8),
          np.float32(21.9), np.float32(22.0), np.float32(22.1), np.float32(22.2),
          np.float32(22.25), np.float32(22.3), np.float32(22.35), np.float32(22.4), np.float32(22.42),
          np.float32(22.44), np.float32(22.46), np.float32(22.48), np.float32(22.5), np.float32(22.55),
          np.float32(22.59), np.float32(22.6), np.float32(22.61), np.float32(22.62), np.float32(22.63),
          np.float32(22.64), np.float32(22.65), np.float32(22.68), np.float32(22.7), np.float32(22.71),
          np.float32(22.72), np.float32(22.73), np.float32(22.75), np.float32(22.78), np.float32(22.8),
          np.float32(22.85), np.float32(22.87), np.float32(22.88), np.float32(22.89), np.float32(22.9),
          np.float32(22.91), np.float32(22.92), np.float32(22.93), np.float32(22.94), np.float32(22.95),
          np.float32(22.96), np.float32(22.97), np.float32(22.98), np.float32(22.99), np.float32(23.0),
          np.float32(23.01), np.float32(23.05), np.float32(23.1), np.float32(23.2), np.float32(23.3), np.float32(23.4),
          np.float32(23.5), np.float32(23.6), np.float32(23.8), np.float32(24.0),
          np.float32(24.2), np.float32(24.4), np.float32(24.7), np.float32(25.0), np.float32(26.0), np.float32(28.0),
          np.float32(30.0), np.float32(32.0), np.float32(35.0), np.float32(40.0),
          np.float32(45.0), np.float32(50.0), np.float32(55.0), np.float32(60.0), np.float32(65.0), np.float32(70.0),
          np.float32(80.0), np.float32(90.0), np.float32(100.), np.float32(110.),
          np.float32(120.), np.float32(140.), np.float32(170.), np.float32(200.), np.float32(240.), np.float32(280.),
          np.float32(320.), np.float32(360.), np.float32(400.), np.float32(450.),
          np.float32(500.), np.float32(550.), np.float32(600.), np.float32(650.), np.float32(700.), np.float32(800.),
          np.float32(900.), np.float32(1000.), np.float32(1100.), np.float32(1200.),
          np.float32(1400.), np.float32(1600.), np.float32(1800.), np.float32(2000.), np.float32(2200.),
          np.float32(2400.), np.float32(2700.), np.float32(3000.),
          ]
Y21SG3 = [np.float32(0.00), np.float32(.406), np.float32(.477), np.float32(.664), np.float32(.820), np.float32(.946),
          np.float32(1.10), np.float32(1.24), np.float32(1.47), np.float32(1.72),
          np.float32(2.03), np.float32(2.52), np.float32(2.40), np.float32(2.39), np.float32(2.39), np.float32(2.42),
          np.float32(2.46), np.float32(2.53), np.float32(2.55), np.float32(2.53),
          np.float32(2.52), np.float32(2.53), np.float32(2.57), np.float32(2.59), np.float32(2.62), np.float32(2.64),
          np.float32(2.65), np.float32(2.65), np.float32(2.65), np.float32(2.62),
          np.float32(2.59), np.float32(2.53), np.float32(2.42), np.float32(2.14), np.float32(1.86), np.float32(2.17),
          np.float32(3.35), np.float32(3.01), np.float32(2.79), np.float32(2.34),
          np.float32(1.80), np.float32(1.88), np.float32(2.53), np.float32(3.37), np.float32(3.64), np.float32(3.55),
          np.float32(3.42), np.float32(3.23), np.float32(2.95), np.float32(2.45),
          np.float32(1.84), np.float32(2.32), np.float32(2.49), np.float32(2.60), np.float32(2.62), np.float32(2.57),
          np.float32(2.40), np.float32(2.57), np.float32(2.59), np.float32(2.32),
          np.float32(1.73), np.float32(2.55), np.float32(2.36), np.float32(2.35), np.float32(2.32), np.float32(2.23),
          np.float32(2.50), np.float32(2.64), np.float32(2.61), np.float32(1.86),
          np.float32(2.28), np.float32(2.53), np.float32(2.35), np.float32(2.39), np.float32(2.44), np.float32(2.51),
          np.float32(2.48), np.float32(2.45), np.float32(2.44), np.float32(2.49),
          np.float32(2.57), np.float32(2.63), np.float32(2.56), np.float32(2.54), np.float32(2.53), np.float32(2.51),
          np.float32(2.45), np.float32(2.35), np.float32(2.21), np.float32(2.05),
          np.float32(1.88), np.float32(1.75), np.float32(1.65), np.float32(1.56), np.float32(1.48), np.float32(1.41),
          np.float32(1.30), np.float32(1.21), np.float32(1.14), np.float32(1.08),
          np.float32(1.03), np.float32(.948), np.float32(.850), np.float32(.771), np.float32(.686), np.float32(.617),
          np.float32(.560), np.float32(.512), np.float32(.471), np.float32(.428),
          np.float32(.392), np.float32(.361), np.float32(.335), np.float32(.312), np.float32(.292), np.float32(.259),
          np.float32(.233), np.float32(.211), np.float32(.193), np.float32(.178),
          np.float32(.154), np.float32(.136), np.float32(.121), np.float32(.109), np.float32(.0997), np.float32(.0916),
          np.float32(.0817), np.float32(.0737),
          ]
# 2 3P J=2,1,0

X23PG3 = [np.float32(20.96409), np.float32(20.97), np.float32(21.0), np.float32(21.05), np.float32(21.1),
          np.float32(21.15), np.float32(21.2), np.float32(21.25), np.float32(21.3),
          np.float32(21.35),
          np.float32(21.4), np.float32(21.5), np.float32(21.6), np.float32(21.7), np.float32(21.8), np.float32(21.9),
          np.float32(22.0), np.float32(22.1), np.float32(22.2), np.float32(22.3),
          np.float32(22.4), np.float32(22.45), np.float32(22.5), np.float32(22.55), np.float32(22.6), np.float32(22.61),
          np.float32(22.62), np.float32(22.63), np.float32(22.64), np.float32(22.65),
          np.float32(22.66), np.float32(22.67), np.float32(22.68), np.float32(22.69), np.float32(22.7),
          np.float32(22.71), np.float32(22.72), np.float32(22.73), np.float32(22.75), np.float32(22.77),
          np.float32(22.8), np.float32(22.85), np.float32(22.88), np.float32(22.9), np.float32(22.91),
          np.float32(22.92), np.float32(22.93), np.float32(22.96), np.float32(22.97), np.float32(22.99),
          np.float32(23.0), np.float32(23.04), np.float32(23.06), np.float32(23.07), np.float32(23.08),
          np.float32(23.1), np.float32(23.2), np.float32(23.3), np.float32(23.4), np.float32(23.5),
          np.float32(23.6), np.float32(23.7), np.float32(23.8), np.float32(23.9), np.float32(24.0), np.float32(24.2),
          np.float32(24.4), np.float32(24.6), np.float32(25.0), np.float32(26.0),
          np.float32(27.0), np.float32(28.0), np.float32(29.0), np.float32(30.0), np.float32(32.0), np.float32(34.0),
          np.float32(36.0), np.float32(38.0), np.float32(40.0), np.float32(42.0),
          np.float32(44.0), np.float32(46.0), np.float32(48.0), np.float32(50.0), np.float32(55.0), np.float32(60.0),
          np.float32(65.0), np.float32(70.0), np.float32(75.0), np.float32(80.0),
          np.float32(85.0), np.float32(90.0), np.float32(95.0), np.float32(100.), np.float32(110.), np.float32(120.),
          np.float32(130.), np.float32(140.), np.float32(150.), np.float32(160.),
          np.float32(170.), np.float32(180.), np.float32(190.), np.float32(200.), np.float32(220.), np.float32(240.),
          np.float32(260.), np.float32(280.), np.float32(300.), np.float32(340.),
          np.float32(380.), np.float32(420.), np.float32(460.), np.float32(500.), np.float32(550.), np.float32(600.),
          np.float32(700.), np.float32(800.), np.float32(900.), np.float32(1000.),
          np.float32(1200.), np.float32(1400.), np.float32(1600.), np.float32(1800.), np.float32(2000.),
          np.float32(2300.), np.float32(2600.), np.float32(3000.),
          ]
Y23PG3 = [np.float32(0.00), np.float32(.0936), np.float32(.241), np.float32(.442), np.float32(.611), np.float32(.761),
          np.float32(.912), np.float32(1.03), np.float32(1.10), np.float32(1.17),
          np.float32(1.23), np.float32(1.32), np.float32(1.40), np.float32(1.47), np.float32(1.54), np.float32(1.60),
          np.float32(1.66), np.float32(1.73), np.float32(1.80), np.float32(1.87),
          np.float32(1.94), np.float32(2.05), np.float32(2.07), np.float32(2.09), np.float32(2.22), np.float32(2.48),
          np.float32(2.68), np.float32(2.60), np.float32(2.27), np.float32(1.78),
          np.float32(1.45), np.float32(1.43), np.float32(1.52), np.float32(1.59), np.float32(1.60), np.float32(1.45),
          np.float32(1.47), np.float32(1.70), np.float32(1.83), np.float32(1.91),
          np.float32(1.95), np.float32(1.93), np.float32(2.32), np.float32(1.98), np.float32(1.72), np.float32(2.23),
          np.float32(2.09), np.float32(2.12), np.float32(2.07), np.float32(2.17),
          np.float32(1.82), np.float32(2.18), np.float32(1.80), np.float32(1.82), np.float32(1.94), np.float32(1.94),
          np.float32(1.90), np.float32(1.88), np.float32(1.89), np.float32(2.00),
          np.float32(2.16), np.float32(2.21), np.float32(2.14), np.float32(2.08), np.float32(2.09), np.float32(2.03),
          np.float32(2.16), np.float32(2.26), np.float32(2.29), np.float32(2.41),
          np.float32(2.47), np.float32(2.48), np.float32(2.47), np.float32(2.43), np.float32(2.30), np.float32(2.15),
          np.float32(2.00), np.float32(1.84), np.float32(1.69), np.float32(1.55),
          np.float32(1.43), np.float32(1.31), np.float32(1.21), np.float32(1.11), np.float32(.907), np.float32(.748),
          np.float32(.622), np.float32(.522), np.float32(.441), np.float32(.375),
          np.float32(.322), np.float32(.277), np.float32(.241), np.float32(.210), np.float32(.162), np.float32(.127),
          np.float32(.101), np.float32(.0812), np.float32(.0663), np.float32(.0547),
          np.float32(.0455), np.float32(.0382), np.float32(.0324), np.float32(.0277), np.float32(.0206),
          np.float32(.0156), np.float32(.0121), np.float32(.00961), np.float32(.00772), np.float32(.00518),
          np.float32(.00363), np.float32(.00264), np.float32(.00197), np.float32(.00151), np.float32(.00118), 8.48e-4,
          5.21e-4, 3.42e-4,
          2.37e-4, 1.70e-4,
          9.65e-5, 5.99e-5, 3.96e-5, 2.76e-5, 2.00e-5, 1.30e-5, 8.94e-6, 5.78e-6,
          ]
# 2 1P RESONANCE RADIATION J=1   58.434 NM       OSC STRENGTH F=0.27608

X21PG3 = [np.float32(21.21802), np.float32(21.23), np.float32(21.25), np.float32(21.3), np.float32(21.4),
          np.float32(21.5), np.float32(21.6), np.float32(21.7), np.float32(21.8), np.float32(21.9),
          np.float32(22.0), np.float32(22.1), np.float32(22.2), np.float32(22.3), np.float32(22.35), np.float32(22.4),
          np.float32(22.42), np.float32(22.44), np.float32(22.46), np.float32(22.48),
          np.float32(22.5), np.float32(22.55), np.float32(22.57), np.float32(22.59), np.float32(22.6),
          np.float32(22.61), np.float32(22.62), np.float32(22.63), np.float32(22.64), np.float32(22.65),
          np.float32(22.66), np.float32(22.68), np.float32(22.7), np.float32(22.71), np.float32(22.72),
          np.float32(22.73), np.float32(22.75), np.float32(22.8), np.float32(22.85), np.float32(22.87),
          np.float32(22.88), np.float32(22.9), np.float32(22.91), np.float32(22.94), np.float32(22.96),
          np.float32(22.97), np.float32(22.98), np.float32(22.99), np.float32(23.0), np.float32(23.01),
          np.float32(23.05), np.float32(23.1), np.float32(23.2), np.float32(23.3), np.float32(23.4), np.float32(23.5),
          np.float32(23.6), np.float32(23.7), np.float32(23.8), np.float32(23.9),
          np.float32(24.0), np.float32(24.2), np.float32(24.4), np.float32(24.6), np.float32(24.8), np.float32(25.0),
          np.float32(26.0), np.float32(27.0), np.float32(28.0), np.float32(29.0),
          np.float32(30.0), np.float32(31.0), np.float32(32.0), np.float32(33.0), np.float32(34.0), np.float32(35.0),
          np.float32(36.0), np.float32(37.0), np.float32(38.0), np.float32(39.0),
          np.float32(40.0), np.float32(42.0), np.float32(44.0), np.float32(46.0), np.float32(48.0), np.float32(50.0),
          np.float32(52.0), np.float32(54.0), np.float32(56.0), np.float32(58.0),
          np.float32(60.0), np.float32(64.0), np.float32(68.0), np.float32(72.0), np.float32(76.0), np.float32(80.0),
          np.float32(85.0), np.float32(90.0), np.float32(95.0), np.float32(100.),
          np.float32(110.), np.float32(120.), np.float32(130.), np.float32(140.), np.float32(160.), np.float32(180.),
          np.float32(200.), np.float32(240.), np.float32(280.), np.float32(320.),
          np.float32(360.), np.float32(400.), np.float32(450.), np.float32(500.), np.float32(550.), np.float32(600.),
          np.float32(650.), np.float32(700.), np.float32(800.), np.float32(900.),
          np.float32(1000.), np.float32(1100.), np.float32(1200.), np.float32(1300.), np.float32(1400.),
          ]
Y21PG3 = [np.float32(0.00), np.float32(.0519), np.float32(.0884), np.float32(.163), np.float32(.290), np.float32(.397),
          np.float32(.493), np.float32(.582), np.float32(.666), np.float32(.748),
          np.float32(.831), np.float32(.914), np.float32(.994), np.float32(1.06), np.float32(1.09), np.float32(1.10),
          np.float32(1.10), np.float32(1.36), np.float32(1.46), np.float32(1.35),
          np.float32(1.32), np.float32(1.30), np.float32(1.28), np.float32(1.19), np.float32(1.07), np.float32(.943),
          np.float32(.922), np.float32(.941), np.float32(.872), np.float32(.751),
          np.float32(.737), np.float32(.959), np.float32(1.13), np.float32(1.17), np.float32(.920), np.float32(1.03),
          np.float32(1.12), np.float32(1.23), np.float32(1.35), np.float32(1.27),
          np.float32(1.18), np.float32(1.22), np.float32(1.03), np.float32(1.14), np.float32(1.12), np.float32(1.38),
          np.float32(1.29), np.float32(1.25), np.float32(1.38), np.float32(1.24),
          np.float32(1.12), np.float32(1.13), np.float32(1.11), np.float32(1.12), np.float32(1.16), np.float32(1.30),
          np.float32(1.41), np.float32(1.44), np.float32(1.41), np.float32(1.37),
          np.float32(1.39), np.float32(1.42), np.float32(1.52), np.float32(1.70), np.float32(1.80), np.float32(1.89),
          np.float32(2.16), np.float32(2.42), np.float32(2.69), np.float32(2.96),
          np.float32(3.24), np.float32(3.53), np.float32(3.82), np.float32(4.12), np.float32(4.42), np.float32(4.71),
          np.float32(5.00), np.float32(5.29), np.float32(5.57), np.float32(5.85),
          np.float32(6.12), np.float32(6.63), np.float32(7.10), np.float32(7.53), np.float32(7.93), np.float32(8.28),
          np.float32(8.61), np.float32(8.90), np.float32(9.16), np.float32(9.39),
          np.float32(9.60), np.float32(9.95), np.float32(10.2), np.float32(10.4), np.float32(10.6), np.float32(10.7),
          np.float32(10.7), np.float32(10.8), np.float32(10.8), np.float32(10.7),
          np.float32(10.6), np.float32(10.4), np.float32(10.2), np.float32(10.0), np.float32(9.57), np.float32(9.13),
          np.float32(8.71), np.float32(7.96), np.float32(7.33), np.float32(6.79),
          np.float32(6.32), np.float32(5.92), np.float32(5.50), np.float32(5.13), np.float32(4.82), np.float32(4.54),
          np.float32(4.30), np.float32(4.08), np.float32(3.72), np.float32(3.41),
          np.float32(3.16), np.float32(2.95), np.float32(2.76), np.float32(2.60), np.float32(2.46),
          ]
# 3 3S J=1

X33SG3 = [np.float32(22.71847), np.float32(22.72), np.float32(22.73), np.float32(22.74), np.float32(22.75),
          np.float32(22.78), np.float32(22.8), np.float32(22.83), np.float32(22.85),
          np.float32(22.86),
          np.float32(22.87), np.float32(22.88), np.float32(22.89), np.float32(22.9), np.float32(22.91),
          np.float32(22.912), np.float32(22.914), np.float32(22.916), np.float32(22.92), np.float32(22.94),
          np.float32(22.96), np.float32(22.98), np.float32(23.0), np.float32(23.02), np.float32(23.05),
          np.float32(23.1), np.float32(23.2), np.float32(23.25), np.float32(23.3), np.float32(23.35),
          np.float32(23.4), np.float32(23.44), np.float32(23.48), np.float32(23.52), np.float32(23.57),
          np.float32(23.59), np.float32(23.62), np.float32(23.65), np.float32(23.7), np.float32(23.75),
          np.float32(23.82), np.float32(23.89), np.float32(23.93), np.float32(24.0), np.float32(24.4), np.float32(25.0),
          np.float32(26.0), np.float32(27.0), np.float32(28.0), np.float32(29.0),
          np.float32(30.0), np.float32(31.0), np.float32(32.0), np.float32(34.0), np.float32(36.0), np.float32(38.0),
          np.float32(40.0), np.float32(42.0), np.float32(44.0), np.float32(46.0),
          np.float32(48.0), np.float32(50.0), np.float32(54.0), np.float32(58.0), np.float32(62.0), np.float32(66.0),
          np.float32(70.0), np.float32(75.0), np.float32(80.0), np.float32(85.0),
          np.float32(90.0), np.float32(95.0), np.float32(100.), np.float32(110.), np.float32(120.), np.float32(130.),
          np.float32(140.), np.float32(150.), np.float32(160.), np.float32(170.),
          np.float32(180.), np.float32(200.), np.float32(220.), np.float32(240.), np.float32(260.), np.float32(280.),
          np.float32(300.), np.float32(340.), np.float32(380.), np.float32(420.),
          np.float32(460.), np.float32(500.), np.float32(550.), np.float32(600.), np.float32(650.), np.float32(700.),
          np.float32(750.), np.float32(800.), np.float32(850.), np.float32(900.),
          np.float32(950.), np.float32(1000.), np.float32(1100.), np.float32(1200.), np.float32(1300.),
          np.float32(1400.),
          ]
Y33SG3 = [np.float32(0.00), np.float32(.800), np.float32(1.15), np.float32(1.03), np.float32(.985), np.float32(.854),
          np.float32(.812), np.float32(.752), np.float32(.644), np.float32(.503),
          np.float32(.277), np.float32(1.79), np.float32(1.17), np.float32(1.06), np.float32(1.32), np.float32(1.51),
          np.float32(1.57), np.float32(1.37), np.float32(.896), np.float32(.848),
          np.float32(.907), np.float32(.816), np.float32(.838), np.float32(.656), np.float32(.872), np.float32(.859),
          np.float32(.890), np.float32(.900), np.float32(.860), np.float32(.750),
          np.float32(.620), np.float32(.810), np.float32(.770), np.float32(.960), np.float32(.870), np.float32(.870),
          np.float32(.730), np.float32(.710), np.float32(.710), np.float32(.730),
          np.float32(.770), np.float32(.690), np.float32(.760), np.float32(.742), np.float32(.725), np.float32(.694),
          np.float32(.665), np.float32(.635), np.float32(.605), np.float32(.577),
          np.float32(.550), np.float32(.524), np.float32(.499), np.float32(.452), np.float32(.409), np.float32(.370),
          np.float32(.336), np.float32(.305), np.float32(.278), np.float32(.253),
          np.float32(.231), np.float32(.212), np.float32(.178), np.float32(.151), np.float32(.130), np.float32(.112),
          np.float32(.0968), np.float32(.0817), np.float32(.0696), np.float32(.0597),
          np.float32(.0516), np.float32(.0449), np.float32(.0393), np.float32(.0306), np.float32(.0242),
          np.float32(.0195), np.float32(.0160), np.float32(.0132), np.float32(.0111), np.float32(.00938),
          np.float32(.00800), np.float32(.00596), np.float32(.00456), np.float32(.00356), np.float32(.00284),
          np.float32(.00230), np.float32(.00188), np.float32(.00131), 9.53e-4,
          7.13e-4,
          5.47e-4, 4.29e-4, 3.25e-4, 2.52e-4, 1.99e-4, 1.60e-4, 1.31e-4, 1.08e-4,
          9.02e-5, 7.62e-5,
          6.49e-5, 5.58e-5, 4.20e-5, 3.25e-5, 2.56e-5, 2.06e-5,
          ]
# 3 1S J=0

X31SG3 = [np.float32(22.92032), np.float32(22.96), np.float32(22.985), np.float32(23.02), np.float32(23.05),
          np.float32(23.07), np.float32(23.1), np.float32(23.15), np.float32(23.2),
          np.float32(23.25),
          np.float32(23.3), np.float32(23.33), np.float32(23.36), np.float32(23.39), np.float32(23.41),
          np.float32(23.45), np.float32(23.48), np.float32(23.51), np.float32(23.54), np.float32(23.56),
          np.float32(23.59), np.float32(23.62), np.float32(23.65), np.float32(23.68), np.float32(23.73),
          np.float32(23.82), np.float32(23.88), np.float32(23.94), np.float32(24.0), np.float32(25.0),
          np.float32(26.0), np.float32(28.0), np.float32(30.0), np.float32(32.0), np.float32(34.0), np.float32(36.0),
          np.float32(38.0), np.float32(40.0), np.float32(44.0), np.float32(48.0),
          np.float32(52.0), np.float32(56.0), np.float32(60.0), np.float32(65.0), np.float32(70.0), np.float32(75.0),
          np.float32(80.0), np.float32(90.0), np.float32(100.), np.float32(110.),
          np.float32(120.), np.float32(130.), np.float32(140.), np.float32(160.), np.float32(180.), np.float32(200.),
          np.float32(220.), np.float32(240.), np.float32(260.), np.float32(280.),
          np.float32(300.), np.float32(340.), np.float32(380.), np.float32(420.), np.float32(460.), np.float32(500.),
          np.float32(550.), np.float32(600.), np.float32(650.), np.float32(700.),
          np.float32(750.), np.float32(800.), np.float32(900.), np.float32(1000.), np.float32(1100.), np.float32(1200.),
          np.float32(1300.), np.float32(1400.), np.float32(1500.), np.float32(1600.),
          np.float32(1800.), np.float32(2000.), np.float32(2400.), np.float32(2800.), np.float32(3200.),
          np.float32(3600.), np.float32(4000.),
          ]
Y31SG3 = [np.float32(0.00), np.float32(.535), np.float32(.457), np.float32(.587), np.float32(.490), np.float32(.490),
          np.float32(.478), np.float32(.491), np.float32(.506), np.float32(.512),
          np.float32(.501), np.float32(.470), np.float32(.418), np.float32(.374), np.float32(.351), np.float32(.371),
          np.float32(.520), np.float32(.681), np.float32(.520), np.float32(.467),
          np.float32(.496), np.float32(.410), np.float32(.442), np.float32(.429), np.float32(.416), np.float32(.455),
          np.float32(.377), np.float32(.444), np.float32(.422), np.float32(.426),
          np.float32(.428), np.float32(.429), np.float32(.425), np.float32(.419), np.float32(.412), np.float32(.402),
          np.float32(.396), np.float32(.387), np.float32(.370), np.float32(.354),
          np.float32(.338), np.float32(.324), np.float32(.311), np.float32(.296), np.float32(.283), np.float32(.271),
          np.float32(.260), np.float32(.242), np.float32(.226), np.float32(.213),
          np.float32(.203), np.float32(.193), np.float32(.185), np.float32(.172), np.float32(.161), np.float32(.152),
          np.float32(.144), np.float32(.137), np.float32(.131), np.float32(.125),
          np.float32(.120), np.float32(.111), np.float32(.103), np.float32(.0957), np.float32(.0894), np.float32(.0839),
          np.float32(.0778), np.float32(.0725), np.float32(.0678), np.float32(.0636),
          np.float32(.0599), np.float32(.0566), np.float32(.0509), np.float32(.0462), np.float32(.0423),
          np.float32(.0389), np.float32(.0361), np.float32(.0336), np.float32(.0315), np.float32(.0296),
          np.float32(.0264), np.float32(.0238), np.float32(.0199), np.float32(.0171), np.float32(.0150),
          np.float32(.0133), np.float32(.0120),
          ]
# 3 3P J=2,1,0

X33PG3 = [np.float32(23.00707), np.float32(23.02), np.float32(23.03), np.float32(23.04), np.float32(23.05),
          np.float32(23.06), np.float32(23.07), np.float32(23.08), np.float32(23.1),
          np.float32(23.2),
          np.float32(23.3), np.float32(23.4), np.float32(23.5), np.float32(23.55), np.float32(23.6), np.float32(23.65),
          np.float32(23.7), np.float32(23.8), np.float32(23.9), np.float32(24.0),
          np.float32(24.1), np.float32(24.2), np.float32(24.3), np.float32(24.4), np.float32(24.6), np.float32(24.8),
          np.float32(25.0), np.float32(26.0), np.float32(27.0), np.float32(28.0),
          np.float32(30.0), np.float32(32.0), np.float32(34.0), np.float32(36.0), np.float32(38.0), np.float32(40.0),
          np.float32(44.0), np.float32(48.0), np.float32(52.0), np.float32(56.0),
          np.float32(60.0), np.float32(64.0), np.float32(68.0), np.float32(72.0), np.float32(76.0), np.float32(80.0),
          np.float32(85.0), np.float32(90.0), np.float32(95.0), np.float32(100.),
          np.float32(110.), np.float32(120.), np.float32(130.), np.float32(140.), np.float32(150.), np.float32(160.),
          np.float32(170.), np.float32(180.), np.float32(200.), np.float32(220.),
          np.float32(240.), np.float32(260.), np.float32(280.), np.float32(300.), np.float32(340.), np.float32(380.),
          np.float32(420.), np.float32(460.), np.float32(500.), np.float32(550.),
          np.float32(600.), np.float32(650.), np.float32(700.), np.float32(750.), np.float32(800.), np.float32(850.),
          np.float32(900.), np.float32(950.), np.float32(1000.), np.float32(1100.),
          np.float32(1200.), np.float32(1300.), np.float32(1400.), np.float32(1600.), np.float32(1800.),
          np.float32(2000.), np.float32(2200.), np.float32(2400.), np.float32(2600.), np.float32(2800.),
          np.float32(3000.),
          ]
Y33PG3 = [np.float32(0.00), np.float32(.387), np.float32(.410), np.float32(.179), np.float32(.148), np.float32(.335),
          np.float32(.381), np.float32(.282), np.float32(.280), np.float32(.309),
          np.float32(.332), np.float32(.359), np.float32(.411), np.float32(.416), np.float32(.405), np.float32(.448),
          np.float32(.438), np.float32(.467), np.float32(.485), np.float32(.493),
          np.float32(.500), np.float32(.515), np.float32(.517), np.float32(.513), np.float32(.503), np.float32(.508),
          np.float32(.512), np.float32(.516), np.float32(.515), np.float32(.524),
          np.float32(.544), np.float32(.539), np.float32(.523), np.float32(.500), np.float32(.474), np.float32(.446),
          np.float32(.392), np.float32(.342), np.float32(.297), np.float32(.259),
          np.float32(.226), np.float32(.197), np.float32(.173), np.float32(.152), np.float32(.134), np.float32(.118),
          np.float32(.102), np.float32(.0878), np.float32(.0762), np.float32(.0665),
          np.float32(.0512), np.float32(.0401), np.float32(.0318), np.float32(.0255), np.float32(.0208),
          np.float32(.0171), np.float32(.0142), np.float32(.0119), np.float32(.00854), np.float32(.00632),
          np.float32(.00479), np.float32(.00371), np.float32(.00292), np.float32(.00234), np.float32(.00157),
          np.float32(.00109), 7.93e-4, 5.92e-4, 4.53e-4,
          3.34e-4,
          2.53e-4, 1.96e-4, 1.55e-4, 1.24e-4, 1.01e-4, 8.37e-5, 6.99e-5, 5.89e-5,
          5.02e-5, 3.72e-5,
          2.83e-5, 2.21e-5, 1.75e-5, 1.16e-5, 8.05e-6, 5.82e-6, 4.34e-6, 3.32e-6,
          2.60e-6, 2.07e-6,
          1.68e-6,
          ]
# 3 3D J=3,2,1

X33DG3 = [np.float32(23.07365), np.float32(23.1), np.float32(23.15), np.float32(23.2), np.float32(23.25),
          np.float32(23.3), np.float32(23.35), np.float32(23.4), np.float32(23.45),
          np.float32(23.5),
          np.float32(23.55), np.float32(23.6), np.float32(23.66), np.float32(23.7), np.float32(23.75), np.float32(23.8),
          np.float32(23.85), np.float32(23.9), np.float32(23.95), np.float32(24.0),
          np.float32(24.05), np.float32(24.1), np.float32(24.15), np.float32(24.2), np.float32(24.25), np.float32(24.3),
          np.float32(24.35), np.float32(24.4), np.float32(24.45), np.float32(24.5),
          np.float32(24.55), np.float32(24.6), np.float32(24.65), np.float32(24.7), np.float32(24.8), np.float32(24.9),
          np.float32(25.0), np.float32(26.0), np.float32(27.0), np.float32(28.0),
          np.float32(29.0), np.float32(30.0), np.float32(32.0), np.float32(34.0), np.float32(36.0), np.float32(38.0),
          np.float32(40.0), np.float32(42.0), np.float32(44.0), np.float32(46.0),
          np.float32(48.0), np.float32(50.0), np.float32(52.0), np.float32(54.0), np.float32(56.0), np.float32(58.0),
          np.float32(60.0), np.float32(64.0), np.float32(68.0), np.float32(72.0),
          np.float32(76.0), np.float32(80.0), np.float32(85.0), np.float32(90.0), np.float32(95.0), np.float32(100.),
          np.float32(110.), np.float32(120.), np.float32(130.), np.float32(140.),
          np.float32(150.), np.float32(160.), np.float32(180.), np.float32(200.), np.float32(220.), np.float32(240.),
          np.float32(260.), np.float32(280.), np.float32(300.), np.float32(320.),
          np.float32(340.), np.float32(360.), np.float32(380.), np.float32(400.), np.float32(440.), np.float32(480.),
          np.float32(520.), np.float32(560.), np.float32(600.), np.float32(650.),
          np.float32(700.), np.float32(750.), np.float32(800.), np.float32(850.), np.float32(900.), np.float32(1000.),
          np.float32(1100.), np.float32(1200.), np.float32(1300.), np.float32(1400.),
          np.float32(1600.), np.float32(1800.), np.float32(2000.), np.float32(2200.), np.float32(2400.),
          np.float32(2600.), np.float32(2800.), np.float32(3000.),
          ]
Y33DG3 = [np.float32(0.00), np.float32(.00956), np.float32(.0236), np.float32(.0401), np.float32(.0602),
          np.float32(.0861), np.float32(.120), np.float32(.166), np.float32(.222), np.float32(.229),
          np.float32(.238), np.float32(.197), np.float32(.123), np.float32(.118), np.float32(.110), np.float32(.112),
          np.float32(.104), np.float32(.110), np.float32(.099), np.float32(.0985),
          np.float32(.113), np.float32(.107), np.float32(.109), np.float32(.114), np.float32(.118), np.float32(.119),
          np.float32(.118), np.float32(.116), np.float32(.113), np.float32(.105),
          np.float32(.112), np.float32(.116), np.float32(.118), np.float32(.119), np.float32(.120), np.float32(.120),
          np.float32(.119), np.float32(.115), np.float32(.118), np.float32(.121),
          np.float32(.121), np.float32(.120), np.float32(.113), np.float32(.105), np.float32(.0958), np.float32(.0867),
          np.float32(.0780), np.float32(.0701), np.float32(.0628), np.float32(.0563),
          np.float32(.0505), np.float32(.0453), np.float32(.0407), np.float32(.0366), np.float32(.0330),
          np.float32(.0298), np.float32(.0269), np.float32(.0221), np.float32(.0183), np.float32(.0152),
          np.float32(.0127), np.float32(.0107), np.float32(.00868), np.float32(.00712), np.float32(.00588),
          np.float32(.00490), np.float32(.00347), np.float32(.00252), np.float32(.00188),
          np.float32(.00142),
          np.float32(.00110), 8.64e-4, 5.56e-4, 3.76e-4, 2.64e-4, 1.92e-4, 1.44e-4, 1.10e-4,
          8.60e-5, 6.84e-5,
          5.53e-5, 4.53e-5, 3.76e-5, 3.15e-5, 2.28e-5, 1.70e-5, 1.30e-5, 1.02e-5,
          8.12e-6, 6.25e-6,
          4.92e-6, 3.94e-6, 3.21e-6, 2.64e-6, 2.21e-6, 1.58e-6, 1.17e-6, 8.95e-7,
          6.98e-7, 5.55e-7,
          3.67e-7, 2.56e-7, 1.85e-7, 1.38e-7, 1.06e-7, 8.32e-8, 6.64e-8, 5.38e-8,
          ]
# 3 1D J=2

X31DG3 = [np.float32(23.07407), np.float32(23.08), np.float32(23.1), np.float32(23.15), np.float32(23.2),
          np.float32(23.25), np.float32(23.3), np.float32(23.35), np.float32(23.4),
          np.float32(23.45),
          np.float32(23.5), np.float32(23.55), np.float32(23.6), np.float32(23.66), np.float32(23.7), np.float32(23.75),
          np.float32(23.8), np.float32(23.85), np.float32(23.9), np.float32(23.95),
          np.float32(24.0), np.float32(24.05), np.float32(24.1), np.float32(24.15), np.float32(24.2), np.float32(24.25),
          np.float32(24.3), np.float32(24.35), np.float32(24.4), np.float32(24.45),
          np.float32(24.5), np.float32(24.6), np.float32(24.7), np.float32(24.8), np.float32(25.0), np.float32(26.0),
          np.float32(28.0), np.float32(30.0), np.float32(32.0), np.float32(34.0),
          np.float32(36.0), np.float32(38.0), np.float32(40.0), np.float32(42.0), np.float32(44.0), np.float32(46.0),
          np.float32(48.0), np.float32(50.0), np.float32(54.0), np.float32(58.0),
          np.float32(62.0), np.float32(66.0), np.float32(70.0), np.float32(75.0), np.float32(80.0), np.float32(90.0),
          np.float32(100.), np.float32(110.), np.float32(120.), np.float32(140.),
          np.float32(160.), np.float32(180.), np.float32(200.), np.float32(220.), np.float32(240.), np.float32(260.),
          np.float32(280.), np.float32(300.), np.float32(320.), np.float32(340.),
          np.float32(370.), np.float32(400.), np.float32(440.), np.float32(480.), np.float32(520.), np.float32(560.),
          np.float32(600.), np.float32(650.), np.float32(700.), np.float32(800.),
          np.float32(900.), np.float32(1000.), np.float32(1100.), np.float32(1200.), np.float32(1300.),
          np.float32(1400.), np.float32(1600.), np.float32(1800.), np.float32(2000.), np.float32(2200.),
          np.float32(2400.), np.float32(2600.), np.float32(2800.), np.float32(3000.),
          ]
Y31DG3 = [np.float32(0.00), np.float32(.097), np.float32(.0973), np.float32(.110), np.float32(.126), np.float32(.148),
          np.float32(.175), np.float32(.200), np.float32(.221), np.float32(.237),
          np.float32(.235), np.float32(.198), np.float32(.185), np.float32(.192), np.float32(.168), np.float32(.181),
          np.float32(.189), np.float32(.172), np.float32(.193), np.float32(.184),
          np.float32(.190), np.float32(.209), np.float32(.206), np.float32(.211), np.float32(.214), np.float32(.215),
          np.float32(.212), np.float32(.206), np.float32(.199), np.float32(.191),
          np.float32(.174), np.float32(.177), np.float32(.179), np.float32(.180), np.float32(.181), np.float32(.180),
          np.float32(.180), np.float32(.188), np.float32(.198), np.float32(.209),
          np.float32(.217), np.float32(.224), np.float32(.229), np.float32(.232), np.float32(.234), np.float32(.235),
          np.float32(.234), np.float32(.233), np.float32(.228), np.float32(.222),
          np.float32(.215), np.float32(.207), np.float32(.199), np.float32(.190), np.float32(.180), np.float32(.163),
          np.float32(.148), np.float32(.135), np.float32(.124), np.float32(.105),
          np.float32(.0913), np.float32(.0803), np.float32(.0715), np.float32(.0643), np.float32(.0584),
          np.float32(.0534), np.float32(.0492), np.float32(.0456), np.float32(.0424), np.float32(.0397),
          np.float32(.0361), np.float32(.0332), np.float32(.0299), np.float32(.0272), np.float32(.0249),
          np.float32(.0230), np.float32(.0213), np.float32(.0196), np.float32(.0181), np.float32(.0156),
          np.float32(.0138), np.float32(.0124), np.float32(.0112), np.float32(.0102), np.float32(.00938),
          np.float32(.00868), np.float32(.00756), np.float32(.00669), np.float32(.00600), np.float32(.00544),
          np.float32(.00497), np.float32(.00458), np.float32(.00425), np.float32(.00396),
          ]
# 3 1P  RESONANCE RADIATION J=1  53.703 NM     OSC STRENGTH F=0.07342

X31PG3 = [np.float32(23.08702), np.float32(23.1), np.float32(23.15), np.float32(23.2), np.float32(23.25),
          np.float32(23.3), np.float32(23.35), np.float32(23.4), np.float32(23.45),
          np.float32(23.5),
          np.float32(23.54), np.float32(23.56), np.float32(23.60), np.float32(23.64), np.float32(23.68),
          np.float32(23.7), np.float32(23.75), np.float32(23.80), np.float32(23.88), np.float32(23.9),
          np.float32(23.95), np.float32(24.0), np.float32(24.05), np.float32(24.1), np.float32(24.15), np.float32(24.2),
          np.float32(24.3), np.float32(24.4), np.float32(24.5), np.float32(24.6),
          np.float32(24.7), np.float32(24.8), np.float32(25.0), np.float32(25.2), np.float32(25.4), np.float32(25.6),
          np.float32(26.0), np.float32(27.0), np.float32(28.0), np.float32(29.0),
          np.float32(30.0), np.float32(31.0), np.float32(32.0), np.float32(34.0), np.float32(36.0), np.float32(38.0),
          np.float32(40.0), np.float32(42.0), np.float32(44.0), np.float32(46.0),
          np.float32(48.0), np.float32(50.0), np.float32(52.0), np.float32(54.0), np.float32(56.0), np.float32(58.0),
          np.float32(60.0), np.float32(65.0), np.float32(70.0), np.float32(75.0),
          np.float32(80.0), np.float32(85.0), np.float32(90.0), np.float32(95.0), np.float32(100.), np.float32(110.),
          np.float32(120.), np.float32(130.), np.float32(140.), np.float32(160.),
          np.float32(180.), np.float32(200.), np.float32(220.), np.float32(240.), np.float32(260.), np.float32(280.),
          np.float32(300.), np.float32(340.), np.float32(380.), np.float32(420.),
          np.float32(460.), np.float32(500.), np.float32(550.), np.float32(600.), np.float32(650.), np.float32(700.),
          np.float32(750.), np.float32(800.), np.float32(900.), np.float32(1000.),
          np.float32(1100.), np.float32(1200.), np.float32(1300.), np.float32(1400.), np.float32(1600.),
          np.float32(1800.), np.float32(2000.), np.float32(2200.), np.float32(2400.), np.float32(2600.),
          np.float32(2800.), np.float32(3000.), np.float32(3400.), np.float32(3800.), np.float32(4200.),
          np.float32(4600.), np.float32(5000.), np.float32(5500.), np.float32(6000.), np.float32(6500.),
          np.float32(7000.), np.float32(8000.), np.float32(9000.), np.float32(10000.),
          ]
Y31PG3 = [np.float32(0.00), np.float32(.114), np.float32(.129), np.float32(.137), np.float32(.137), np.float32(.134),
          np.float32(.131), np.float32(.130), np.float32(.128), np.float32(.129),
          np.float32(.117), np.float32(.127), np.float32(.122), np.float32(.163), np.float32(.146), np.float32(.150),
          np.float32(.191), np.float32(.180), np.float32(.226), np.float32(.224),
          np.float32(.218), np.float32(.230), np.float32(.245), np.float32(.253), np.float32(.265), np.float32(.274),
          np.float32(.294), np.float32(.308), np.float32(.330), np.float32(.360),
          np.float32(.373), np.float32(.382), np.float32(.397), np.float32(.409), np.float32(.418), np.float32(.423),
          np.float32(.434), np.float32(.469), np.float32(.516), np.float32(.577),
          np.float32(.648), np.float32(.723), np.float32(.808), np.float32(.941), np.float32(1.07), np.float32(1.20),
          np.float32(1.32), np.float32(1.43), np.float32(1.54), np.float32(1.64),
          np.float32(1.74), np.float32(1.82), np.float32(1.90), np.float32(1.97), np.float32(2.04), np.float32(2.10),
          np.float32(2.15), np.float32(2.27), np.float32(2.35), np.float32(2.42),
          np.float32(2.47), np.float32(2.50), np.float32(2.52), np.float32(2.53), np.float32(2.53), np.float32(2.52),
          np.float32(2.50), np.float32(2.47), np.float32(2.42), np.float32(2.33),
          np.float32(2.24), np.float32(2.14), np.float32(2.06), np.float32(1.97), np.float32(1.90), np.float32(1.82),
          np.float32(1.76), np.float32(1.64), np.float32(1.53), np.float32(1.44),
          np.float32(1.36), np.float32(1.29), np.float32(1.21), np.float32(1.15), np.float32(1.08), np.float32(1.03),
          np.float32(.982), np.float32(.938), np.float32(.862), np.float32(.799),
          np.float32(.745), np.float32(.699), np.float32(.658), np.float32(.623), np.float32(.563), np.float32(.514),
          np.float32(.474), np.float32(.440), np.float32(.411), np.float32(.386),
          np.float32(.364), np.float32(.344), np.float32(.312), np.float32(.285), np.float32(.263), np.float32(.244),
          np.float32(.228), np.float32(.211), np.float32(.197), np.float32(.184),
          np.float32(.173), np.float32(.155), np.float32(.140), np.float32(.128),
          ]
# 4 3S J=1

X43SG3 = [np.float32(23.59396), np.float32(23.62), np.float32(23.65), np.float32(23.7), np.float32(23.8),
          np.float32(23.9), np.float32(24.0), np.float32(25.0), np.float32(26.0), np.float32(27.0),
          np.float32(28.0), np.float32(30.0), np.float32(32.0), np.float32(34.0), np.float32(36.0), np.float32(38.0),
          np.float32(40.0), np.float32(42.0), np.float32(44.0), np.float32(46.0),
          np.float32(48.0), np.float32(50.0), np.float32(52.0), np.float32(54.0), np.float32(56.0), np.float32(58.0),
          np.float32(60.0), np.float32(64.0), np.float32(68.0), np.float32(72.0),
          np.float32(76.0), np.float32(80.0), np.float32(85.0), np.float32(90.0), np.float32(95.0), np.float32(100.),
          np.float32(110.), np.float32(120.), np.float32(130.), np.float32(140.),
          np.float32(150.), np.float32(160.), np.float32(180.), np.float32(200.), np.float32(220.), np.float32(240.),
          np.float32(260.), np.float32(280.), np.float32(300.), np.float32(320.),
          np.float32(340.), np.float32(360.), np.float32(380.), np.float32(400.), np.float32(440.), np.float32(480.),
          np.float32(520.), np.float32(560.), np.float32(600.),
          ]
Y43SG3 = [np.float32(0.0), np.float32(.314), np.float32(.304), np.float32(.292), np.float32(.276), np.float32(.266),
          np.float32(.260), np.float32(.243), np.float32(.238), np.float32(.234),
          np.float32(.227), np.float32(.212), np.float32(.195), np.float32(.178), np.float32(.162), np.float32(.147),
          np.float32(.133), np.float32(.121), np.float32(.110), np.float32(.100),
          np.float32(.0911), np.float32(.0832), np.float32(.0761), np.float32(.0697), np.float32(.0640),
          np.float32(.0589), np.float32(.0543), np.float32(.0464), np.float32(.0399), np.float32(.0346),
          np.float32(.0301), np.float32(.0264), np.float32(.0225), np.float32(.0194), np.float32(.0168),
          np.float32(.0147), np.float32(.0113), np.float32(.00894), np.float32(.00718), np.float32(.00585),
          np.float32(.00483), np.float32(.00403), np.float32(.00289), np.float32(.00214), np.float32(.00164),
          np.float32(.00127), np.float32(.00101), 8.17e-4, 6.69e-4,
          5.55e-4,
          4.66e-4, 3.94e-4, 3.37e-4, 2.90e-4, 2.19e-4, 1.70e-4, 1.34e-4, 1.08e-4,
          8.81e-5,
          ]
# 4 1S J=0

X41SG3 = [np.float32(23.67357), np.float32(23.7), np.float32(23.8), np.float32(23.9), np.float32(24.0),
          np.float32(25.0), np.float32(26.0), np.float32(27.0), np.float32(28.0), np.float32(29.0),
          np.float32(30.0), np.float32(32.0), np.float32(34.0), np.float32(36.0), np.float32(38.0), np.float32(40.0),
          np.float32(44.0), np.float32(48.0), np.float32(52.0), np.float32(56.0),
          np.float32(60.0), np.float32(65.0), np.float32(70.0), np.float32(75.0), np.float32(80.0), np.float32(90.0),
          np.float32(100.), np.float32(110.), np.float32(120.), np.float32(130.),
          np.float32(140.), np.float32(160.), np.float32(180.), np.float32(200.), np.float32(250.), np.float32(300.),
          np.float32(350.), np.float32(400.), np.float32(450.), np.float32(500.),
          np.float32(600.), np.float32(700.), np.float32(800.), np.float32(900.), np.float32(1000.), np.float32(1200.),
          np.float32(1400.), np.float32(1600.), np.float32(1800.), np.float32(2000.),
          np.float32(2200.), np.float32(2400.), np.float32(2600.), np.float32(2800.), np.float32(3000.),
          ]
Y41SG3 = [np.float32(0.0), np.float32(.109), np.float32(.110), np.float32(.111), np.float32(.112), np.float32(.121),
          np.float32(.128), np.float32(.133), np.float32(.138), np.float32(.141),
          np.float32(.143), np.float32(.146), np.float32(.148), np.float32(.147), np.float32(.146), np.float32(.144),
          np.float32(.139), np.float32(.134), np.float32(.129), np.float32(.123),
          np.float32(.118), np.float32(.113), np.float32(.108), np.float32(.103), np.float32(.0990), np.float32(.0922),
          np.float32(.0868), np.float32(.0823), np.float32(.0786), np.float32(.0753),
          np.float32(.0725), np.float32(.0677), np.float32(.0636), np.float32(.0601), np.float32(.0527),
          np.float32(.0469), np.float32(.0422), np.float32(.0382), np.float32(.0349), np.float32(.0322),
          np.float32(.0277), np.float32(.0243), np.float32(.0216), np.float32(.0195), np.float32(.0177),
          np.float32(.0150), np.float32(.0130), np.float32(.0114), np.float32(.0102), np.float32(.00925),
          np.float32(.00845), np.float32(.00777), np.float32(.00719), np.float32(.00669), np.float32(.00626),
          ]
# 4 3P J=2,1,0

X43PG3 = [np.float32(23.70789), np.float32(23.75), np.float32(23.8), np.float32(24.0), np.float32(25.0),
          np.float32(26.0), np.float32(27.0), np.float32(28.0), np.float32(29.0), np.float32(30.0),
          np.float32(32.0), np.float32(34.0), np.float32(36.0), np.float32(38.0), np.float32(40.0), np.float32(42.0),
          np.float32(44.0), np.float32(46.0), np.float32(48.0), np.float32(50.0),
          np.float32(54.0), np.float32(58.0), np.float32(62.0), np.float32(66.0), np.float32(70.0), np.float32(75.0),
          np.float32(80.0), np.float32(85.0), np.float32(90.0), np.float32(95.0),
          np.float32(100.), np.float32(110.), np.float32(120.), np.float32(130.), np.float32(140.), np.float32(150.),
          np.float32(160.), np.float32(170.), np.float32(180.), np.float32(190.),
          np.float32(200.), np.float32(220.), np.float32(240.), np.float32(260.), np.float32(280.), np.float32(300.),
          np.float32(320.), np.float32(340.), np.float32(360.), np.float32(380.),
          np.float32(400.), np.float32(440.), np.float32(480.), np.float32(520.), np.float32(560.), np.float32(600.),
          np.float32(650.), np.float32(700.), np.float32(750.), np.float32(800.),
          np.float32(850.), np.float32(900.), np.float32(950.), np.float32(1000.), np.float32(1100.), np.float32(1200.),
          np.float32(1300.), np.float32(1400.), np.float32(1600.), np.float32(1800.),
          np.float32(2000.), np.float32(2200.), np.float32(2400.), np.float32(2600.), np.float32(2800.),
          np.float32(3000.),
          ]
Y43PG3 = [np.float32(0.0), np.float32(.085), np.float32(.110), np.float32(.118), np.float32(.152), np.float32(.177),
          np.float32(.194), np.float32(.205), np.float32(.211), np.float32(.215),
          np.float32(.215), np.float32(.209), np.float32(.200), np.float32(.189), np.float32(.178), np.float32(.167),
          np.float32(.156), np.float32(.146), np.float32(.136), np.float32(.127),
          np.float32(.110), np.float32(.0962), np.float32(.0840), np.float32(.0736), np.float32(.0647),
          np.float32(.0553), np.float32(.0475), np.float32(.0410), np.float32(.0356), np.float32(.0310),
          np.float32(.0271), np.float32(.0210), np.float32(.0165), np.float32(.0132), np.float32(.0106),
          np.float32(.00865), np.float32(.00713), np.float32(.00593), np.float32(.00498), np.float32(.00421),
          np.float32(.00359), np.float32(.00266), np.float32(.00202), np.float32(.00156), np.float32(.00123), 9.88e-4,
          8.03e-4, 6.60e-4,
          5.49e-4, 4.61e-4,
          3.90e-4, 2.87e-4, 2.17e-4, 1.67e-4, 1.32e-4, 1.06e-4, 8.18e-5, 6.46e-5,
          5.18e-5, 4.22e-5,
          3.48e-5, 2.90e-5, 2.45e-5, 2.08e-5, 1.54e-5, 1.17e-5, 9.13e-6, 7.25e-6,
          4.78e-6, 3.32e-6,
          2.39e-6, 1.78e-6, 1.36e-6, 1.07e-6, 8.50e-7, 6.88e-7,
          ]
# 4 3D J=3,2,1

X43DG3 = [np.float32(23.73609), np.float32(23.8), np.float32(23.9), np.float32(24.0), np.float32(25.0),
          np.float32(26.0), np.float32(27.0), np.float32(28.0), np.float32(29.0), np.float32(30.0),
          np.float32(32.0), np.float32(34.0), np.float32(36.0), np.float32(38.0), np.float32(40.0), np.float32(42.0),
          np.float32(44.0), np.float32(46.0), np.float32(48.0), np.float32(50.0),
          np.float32(54.0), np.float32(58.0), np.float32(62.0), np.float32(66.0), np.float32(70.0), np.float32(75.0),
          np.float32(80.0), np.float32(85.0), np.float32(90.0), np.float32(95.0),
          np.float32(100.), np.float32(110.), np.float32(120.), np.float32(130.), np.float32(140.), np.float32(150.),
          np.float32(160.), np.float32(180.), np.float32(200.), np.float32(220.),
          np.float32(240.), np.float32(260.), np.float32(280.), np.float32(300.), np.float32(340.), np.float32(380.),
          np.float32(420.), np.float32(460.), np.float32(500.), np.float32(550.),
          np.float32(600.), np.float32(650.), np.float32(700.), np.float32(750.), np.float32(800.), np.float32(850.),
          np.float32(900.), np.float32(950.), np.float32(1000.), np.float32(1100.),
          np.float32(1200.), np.float32(1300.), np.float32(1400.), np.float32(1500.), np.float32(1600.),
          ]
Y43DG3 = [np.float32(.0), np.float32(.0288), np.float32(.0363), np.float32(.0407), np.float32(.0575), np.float32(.0646),
          np.float32(.0681), np.float32(.0692), np.float32(.069), np.float32(.0675),
          np.float32(.0629), np.float32(.0573), np.float32(.0516), np.float32(.0461), np.float32(.0411),
          np.float32(.0365), np.float32(.0325), np.float32(.0290), np.float32(.0258), np.float32(.0231),
          np.float32(.0186), np.float32(.0151), np.float32(.0123), np.float32(.0102), np.float32(.00847),
          np.float32(.00681), np.float32(.00554), np.float32(.00455), np.float32(.00378), np.float32(.00316),
          np.float32(.00267), np.float32(.00194), np.float32(.00145), np.float32(.00111), 8.61e-4, 6.81e-4, 5.47e-4,
          3.66e-4,
          2.55e-4, 1.84e-4,
          1.37e-4, 1.04e-4, 8.08e-5, 6.39e-5, 4.18e-5, 2.87e-5, 2.05e-5, 1.51e-5,
          1.14e-5, 8.32e-6,
          6.24e-6, 4.79e-6, 3.75e-6, 3.00e-6, 2.43e-6, 1.99e-6, 1.65e-6, 1.39e-6,
          1.18e-6, 8.66e-7,
          6.55e-7, 5.08e-7, 4.01e-7, 3.22e-7, 2.63e-7,
          ]
# 4 1D J=2

X41DG3 = [np.float32(23.73633), np.float32(23.8), np.float32(24.0), np.float32(25.0), np.float32(26.0),
          np.float32(27.0), np.float32(28.0), np.float32(29.0), np.float32(30.0), np.float32(32.0),
          np.float32(34.0), np.float32(36.0), np.float32(38.0), np.float32(40.0), np.float32(44.0), np.float32(48.0),
          np.float32(52.0), np.float32(56.0), np.float32(60.0), np.float32(64.0),
          np.float32(68.0), np.float32(72.0), np.float32(76.0), np.float32(80.0), np.float32(85.0), np.float32(90.0),
          np.float32(95.0), np.float32(100.), np.float32(110.), np.float32(120.),
          np.float32(130.), np.float32(140.), np.float32(160.), np.float32(180.), np.float32(200.), np.float32(220.),
          np.float32(240.), np.float32(260.), np.float32(300.), np.float32(340.),
          np.float32(380.), np.float32(420.), np.float32(460.), np.float32(500.), np.float32(550.), np.float32(600.),
          np.float32(650.), np.float32(700.), np.float32(800.), np.float32(900.),
          np.float32(1000.), np.float32(1100.), np.float32(1200.),
          ]
Y41DG3 = [np.float32(0.0), np.float32(.0791), np.float32(.0799), np.float32(.0846), np.float32(.0902),
          np.float32(.0959), np.float32(.102), np.float32(.107), np.float32(.112), np.float32(.120),
          np.float32(.127), np.float32(.131), np.float32(.134), np.float32(.136), np.float32(.136), np.float32(.134),
          np.float32(.131), np.float32(.126), np.float32(.121), np.float32(.116),
          np.float32(.112), np.float32(.107), np.float32(.102), np.float32(.0978), np.float32(.0927), np.float32(.0880),
          np.float32(.0836), np.float32(.0796), np.float32(.0724), np.float32(.0663),
          np.float32(.0610), np.float32(.0564), np.float32(.0489), np.float32(.0430), np.float32(.0384),
          np.float32(.0346), np.float32(.0314), np.float32(.0288), np.float32(.0246), np.float32(.0215),
          np.float32(.0190), np.float32(.0171), np.float32(.0155), np.float32(.0142), np.float32(.0128),
          np.float32(.0117), np.float32(.0107), np.float32(.00990), np.float32(.00860), np.float32(.00760),
          np.float32(.00681), np.float32(.00616), np.float32(.00563),
          ]
# 4 3F J=3,4,2

X43FG3 = [np.float32(23.73701), np.float32(23.8), np.float32(23.9), np.float32(24.0), np.float32(25.0),
          np.float32(26.0), np.float32(27.0), np.float32(28.0), np.float32(29.0), np.float32(30.0),
          np.float32(31.0), np.float32(32.0), np.float32(33.0), np.float32(34.0), np.float32(35.0), np.float32(36.0),
          np.float32(37.0), np.float32(38.0), np.float32(39.0), np.float32(40.0),
          np.float32(42.0), np.float32(44.0), np.float32(46.0), np.float32(48.0), np.float32(50.0), np.float32(54.0),
          np.float32(58.0), np.float32(62.0), np.float32(66.0), np.float32(70.0),
          np.float32(75.0), np.float32(80.0), np.float32(85.0), np.float32(90.0), np.float32(95.0), np.float32(100.),
          np.float32(110.), np.float32(120.), np.float32(130.), np.float32(140.),
          ]
Y43FG3 = [np.float32(0.0), np.float32(.0357), np.float32(.0318), np.float32(.0289), np.float32(.0161),
          np.float32(.0117), np.float32(.00922), np.float32(.00760), np.float32(.00642),
          np.float32(.00550),
          np.float32(.00478), np.float32(.00418), np.float32(.00369), np.float32(.00327), np.float32(.00291),
          np.float32(.00261), np.float32(.00234), np.float32(.00211), np.float32(.00191),
          np.float32(.00173),
          np.float32(.00144), np.float32(.00121), np.float32(.00102), 8.68e-4, 7.44e-4, 5.57e-4, 4.25e-4, 3.30e-4,
          2.61e-4, 2.09e-4,
          1.61e-4, 1.26e-4, 9.98e-5, 8.03e-5, 6.53e-5, 5.36e-5, 3.72e-5, 2.66e-5,
          1.96e-5, 1.47e-5,
          ]
# 4 1F J=3

X41FG3 = [np.float32(23.73701), np.float32(23.8), np.float32(24.0), np.float32(25.0), np.float32(26.0),
          np.float32(27.0), np.float32(28.0), np.float32(29.0), np.float32(30.0), np.float32(31.0),
          np.float32(32.0), np.float32(34.0), np.float32(36.0), np.float32(38.0), np.float32(40.0), np.float32(42.0),
          np.float32(44.0), np.float32(46.0), np.float32(48.0), np.float32(50.0),
          np.float32(54.0), np.float32(58.0), np.float32(62.0), np.float32(66.0), np.float32(70.0), np.float32(75.0),
          np.float32(80.0), np.float32(85.0), np.float32(90.0), np.float32(95.0),
          np.float32(100.), np.float32(110.), np.float32(120.), np.float32(130.), np.float32(140.), np.float32(150.),
          np.float32(160.), np.float32(180.), np.float32(200.), np.float32(220.),
          np.float32(240.), np.float32(260.), np.float32(280.), np.float32(300.), np.float32(340.), np.float32(380.),
          np.float32(420.), np.float32(460.), np.float32(500.), np.float32(550.),
          np.float32(600.), np.float32(650.), np.float32(700.), np.float32(750.), np.float32(800.), np.float32(900.),
          np.float32(1000.),
          ]
Y41FG3 = [np.float32(0.0), np.float32(.0175), np.float32(.0172), np.float32(.0160), np.float32(.0149),
          np.float32(.0139), np.float32(.0130), np.float32(.0122), np.float32(.0114),
          np.float32(.0108),
          np.float32(.0102), np.float32(.00909), np.float32(.00819), np.float32(.00742), np.float32(.00677),
          np.float32(.00619), np.float32(.00569), np.float32(.00525), np.float32(.00487),
          np.float32(.00452),
          np.float32(.00393), np.float32(.00346), np.float32(.00307), np.float32(.00274), np.float32(.00246),
          np.float32(.00217), np.float32(.00193), np.float32(.00173), np.float32(.00156),
          np.float32(.00142),
          np.float32(.00129), np.float32(.00108), 9.24e-4, 7.99e-4, 6.99e-4, 6.17e-4, 5.50e-4, 4.47e-4,
          3.73e-4, 3.19e-4,
          2.77e-4, 2.45e-4, 2.19e-4, 1.99e-4, 1.67e-4, 1.45e-4, 1.28e-4, 1.15e-4,
          1.04e-4, 9.39e-5,
          8.55e-5, 7.86e-5, 7.27e-5, 6.78e-5, 6.35e-5, 5.63e-5, 5.07e-5,
          ]
# 4 1P RESONANCE RADIATION J=1   52.222 NM    OSC STRENGTH F=0.02986

X41PG3 = [np.float32(23.74207), np.float32(23.8), np.float32(23.9), np.float32(24.0), np.float32(25.0),
          np.float32(26.0), np.float32(27.0), np.float32(28.0), np.float32(29.0), np.float32(30.0),
          np.float32(31.0), np.float32(32.0), np.float32(33.0), np.float32(34.0), np.float32(35.0), np.float32(36.0),
          np.float32(37.0), np.float32(38.0), np.float32(39.0), np.float32(40.0),
          np.float32(42.0), np.float32(44.0), np.float32(46.0), np.float32(48.0), np.float32(50.0), np.float32(52.0),
          np.float32(54.0), np.float32(56.0), np.float32(58.0), np.float32(60.0),
          np.float32(64.0), np.float32(68.0), np.float32(72.0), np.float32(76.0), np.float32(80.0), np.float32(85.0),
          np.float32(90.0), np.float32(95.0), np.float32(100.), np.float32(110.),
          np.float32(120.), np.float32(130.), np.float32(140.), np.float32(150.), np.float32(160.), np.float32(180.),
          np.float32(200.), np.float32(220.), np.float32(240.), np.float32(260.),
          np.float32(280.), np.float32(300.), np.float32(320.), np.float32(340.), np.float32(360.), np.float32(380.),
          np.float32(400.), np.float32(440.), np.float32(480.), np.float32(520.),
          np.float32(560.), np.float32(600.), np.float32(640.), np.float32(680.), np.float32(720.), np.float32(760.),
          np.float32(800.), np.float32(850.), np.float32(900.), np.float32(950.),
          np.float32(1000.), np.float32(1100.), np.float32(1200.), np.float32(1300.), np.float32(1400.),
          np.float32(1600.), np.float32(1800.), np.float32(2000.), np.float32(2200.), np.float32(2400.),
          np.float32(2600.), np.float32(2800.), np.float32(3000.), np.float32(3400.), np.float32(3800.),
          np.float32(4200.), np.float32(4600.), np.float32(5000.), np.float32(5500.), np.float32(6000.),
          np.float32(6500.), np.float32(7000.), np.float32(7500.), np.float32(8000.), np.float32(9000.),
          np.float32(10000.),
          ]
Y41PG3 = [np.float32(0.00), np.float32(.0147), np.float32(.0242), np.float32(.0334), np.float32(.107), np.float32(.158),
          np.float32(.196), np.float32(.227), np.float32(.255), np.float32(.281),
          np.float32(.307), np.float32(.333), np.float32(.360), np.float32(.387), np.float32(.414), np.float32(.442),
          np.float32(.470), np.float32(.498), np.float32(.526), np.float32(.553),
          np.float32(.606), np.float32(.657), np.float32(.704), np.float32(.748), np.float32(.789), np.float32(.826),
          np.float32(.860), np.float32(.891), np.float32(.919), np.float32(.944),
          np.float32(.986), np.float32(1.02), np.float32(1.05), np.float32(1.06), np.float32(1.08), np.float32(1.09),
          np.float32(1.10), np.float32(1.10), np.float32(1.10), np.float32(1.09),
          np.float32(1.07), np.float32(1.05), np.float32(1.03), np.float32(1.01), np.float32(.985), np.float32(.939),
          np.float32(.896), np.float32(.855), np.float32(.817), np.float32(.783),
          np.float32(.751), np.float32(.722), np.float32(.695), np.float32(.670), np.float32(.646), np.float32(.625),
          np.float32(.605), np.float32(.569), np.float32(.537), np.float32(.509),
          np.float32(.484), np.float32(.461), np.float32(.441), np.float32(.423), np.float32(.406), np.float32(.390),
          np.float32(.376), np.float32(.360), np.float32(.345), np.float32(.332),
          np.float32(.320), np.float32(.298), np.float32(.279), np.float32(.263), np.float32(.248), np.float32(.224),
          np.float32(.205), np.float32(.189), np.float32(.175), np.float32(.163),
          np.float32(.153), np.float32(.145), np.float32(.137), np.float32(.124), np.float32(.113), np.float32(.104),
          np.float32(.0969), np.float32(.0905), np.float32(.0837), np.float32(.0779),
          np.float32(.0729), np.float32(.0686), np.float32(.0648), np.float32(.0614), np.float32(.0556),
          np.float32(.0510),
          ]
# 5 1P RESONANCE  RADIATION J=1  51.562 NM      F=0.01504

# 6 1P RESONANCE  RADIATION J=1  51.210 NM      F=0.00863

# 7 1P RESONANCE  RADIATION J=1  51.000 NM      F=0.00540

# 8 1P RESONANCE  RADIATION J=1  50.865 NM      F=0.00362

# 9 1P RESONANCE  RADIATION J=1  50.772 NM      F=0.00253

# 10 1P RESONANCE RADIATION J=1  50.706 NM      F=0.00184

# 11 1P RESONANCE RADIATION J=1  50.657 NM      F=0.00138

# 12 1P RESONANCE RADIATION J=1  50.620 NM      F=0.00106

# SUM HIGHER 1P LEVELS RESONANCE RADIATION J=1  F=0.00440

# TOTAL SUM OSCILLATOR STRENGTH = 0.42326

#

# BREMSSTRAHLUNG X-SECTION WITH CUT OFF

Z2TG3 = [np.float32(42.1), np.float32(23.5), np.float32(10.7), np.float32(5.88), np.float32(3.25), np.float32(1.50),
         np.float32(.886), np.float32(.582), np.float32(.437), np.float32(.429),
         np.float32(.460), np.float32(.484), np.float32(.502), np.float32(.515), np.float32(.525), np.float32(.540),
         np.float32(.550), np.float32(.566), np.float32(.575), np.float32(.585),
         np.float32(.592), np.float32(.596), np.float32(.597), np.float32(.598), np.float32(.598),
         ]
# UNITS 10**-24

EBRMG3 = [np.float32(1000.), np.float32(2000.), np.float32(5000.), np.float32(1.E4), np.float32(2.E4), np.float32(5.E4),
          np.float32(1.E5), np.float32(2.E5), np.float32(5.E5), np.float32(1.E6),
          np.float32(2.E6), np.float32(3.E6), np.float32(4.E6), np.float32(5.E6), np.float32(6.E6), np.float32(8.E6),
          np.float32(1.E7), np.float32(1.5E7), np.float32(2.E7), np.float32(3.E7),
          np.float32(4.E7), np.float32(5.E7), np.float32(6.E7), np.float32(8.E7), np.float32(1.E8),
          ]

gd['gas3/XEN'] = XENG3
gd['gas3/YEM'] = YEMG3
gd['gas3/YEL'] = YELG3
gd['gas3/YEPS'] = YEPSG3
gd['gas3/XION'] = XIONG3
gd['gas3/YION'] = YIONG3
gd['gas3/YINC'] = YINCG3
gd['gas3/X23S'] = X23SG3
gd['gas3/Y23S'] = Y23SG3
gd['gas3/X21S'] = X21SG3
gd['gas3/Y21S'] = Y21SG3
gd['gas3/X23P'] = X23PG3
gd['gas3/Y23P'] = Y23PG3
gd['gas3/X21P'] = X21PG3
gd['gas3/Y21P'] = Y21PG3
gd['gas3/X33S'] = X33SG3
gd['gas3/Y33S'] = Y33SG3
gd['gas3/X31S'] = X31SG3
gd['gas3/Y31S'] = Y31SG3
gd['gas3/X33P'] = X33PG3
gd['gas3/Y33P'] = Y33PG3
gd['gas3/X33D'] = X33DG3
gd['gas3/Y33D'] = Y33DG3
gd['gas3/X31D'] = X31DG3
gd['gas3/Y31D'] = Y31DG3
gd['gas3/X31P'] = X31PG3
gd['gas3/Y31P'] = Y31PG3
gd['gas3/X43S'] = X43SG3
gd['gas3/Y43S'] = Y43SG3
gd['gas3/X41S'] = X41SG3
gd['gas3/Y41S'] = Y41SG3
gd['gas3/X43P'] = X43PG3
gd['gas3/Y43P'] = Y43PG3
gd['gas3/X43D'] = X43DG3
gd['gas3/Y43D'] = Y43DG3
gd['gas3/X41D'] = X41DG3
gd['gas3/Y41D'] = Y41DG3
gd['gas3/X43F'] = X43FG3
gd['gas3/Y43F'] = Y43FG3
gd['gas3/X41F'] = X41FG3
gd['gas3/Y41F'] = Y41FG3
gd['gas3/X41P'] = X41PG3
gd['gas3/Y41P'] = Y41PG3
gd['gas3/Z2T'] = Z2TG3
gd['gas3/EBRM'] = EBRMG3

# XENON gas7
# ELASTIC MOMENTUM TRANSFER
XENG7 = [0.00, .001, .005, .007, 0.01, .015, 0.02, .025, 0.03, 0.04, 0.05, 0.06, 0.07, 0.08, 0.10, 0.12, 0.14, 0.17,
         0.20, 0.25, 0.27, 0.30, 0.32, 0.35, 0.37, 0.40, 0.42, 0.44, 0.46, 0.48, 0.50, 0.51, 0.52, 0.53, 0.54, 0.55,
         0.56, 0.57, 0.58, 0.59, 0.60, 0.61, 0.62, 0.63, 0.64, 0.65, 0.66, 0.67, 0.68, 0.69, 0.70, .715, 0.73, 0.75,
         0.77, 0.80, 0.83, 0.85, 0.87, 0.90, 1.00, 1.08, 1.14, 1.20, 1.30, 1.40, 1.50, 1.70, 2.00, 2.50, 3.00, 3.50,
         4.00, 4.50, 5.00, 5.50, 6.00, 6.50, 7.00, 8.00, 9.00, 10.0, 12.0, 15.0, 18.0, 20.0, 25.0, 30.0, 40.0, 50.0,
         60.0, 70.0, 80.0, 90.0, 100., 125., 150., 200., 250., 300., 400., 500., 600., 700., 800., 1000., 1500., 2000.,
         3000., 4000., 5000., 6000., 8000., 1.0e4, 1.5e4, 2.0e4, 3.0e4, 4.0e4, 5.0e4, 6.0e4, 8.0e4, 1.0e5, 1.25e5,
         1.5e5, 1.75e5, 2.0e5, 2.5e5, 3.0e5, 3.5e5, 4.0e5, 4.5e5, 5.0e5, 6.0e5, 7.0e5, 8.0e5, 9.0e5, 1.0e6, 1.25e6,
         1.5e6, 1.75e6, 2.0e6, 2.5e6, 3.0e6, 3.5e6, 4.0e6, 4.5e6, 5.0e6, 6.0e6, 7.0e6, 8.0e6, 9.0e6, 1.0e7, 1.25e7,
         1.5e7, 1.75e7, 2.0e7, 2.5e7, 3.0e7, 3.5e7, 4.0e7, 4.5e7, 5.0e7, 6.0e7, 7.0e7, 8.0e7, 9.0e7, 1.0e8, 1.25e8,
         1.5e8, 1.75e8, 2.0e8, 2.5e8, 3.0e8, 3.5e8, 4.0e8, 4.5e8, 5.0e8, 6.0e8, 7.0e8, 8.0e8, 9.0e8, 1.0e9]

YMOMG7 = [131., 115., 97.0, 91.1, 83.9, 74.6, 67.3, 61.2, 56.1, 47.9, 41.4, 36.2, 31.8, 28.2, 22.5, 18.1, 14.8, 11.1,
          8.36, 5.33, 4.47, 3.43, 2.88, 2.22, 1.86, 1.43, 1.20, 1.01, .844, .708, .596, .548, .504, .465, .430, .399,
          .372, .348, .328, .310, .296, .285, .276, .270, .266, .265, .266, .270, .276, .287, .306, .341, .377, .427,
          .479, .562, .651, .713, .778, .880, 1.26, 1.62, 1.92, 2.25, 2.85, 3.51, 4.22, 5.73, 7.97, 11.8, 15.8, 20.4,
          24.4, 28.0, 30.7, 31.5, 32.3, 31.6, 31.0, 27.8, 23.5, 19.8, 15.0, 10.9, 8.40, 7.25, 5.65, 5.00, 4.50, 3.10,
          2.42, 2.17, 2.00, 1.89, 1.80, 1.73, 1.65, 1.50, 1.39, 1.26, 1.09, 0.94, 0.84, 0.75, 0.68, 0.56, 0.38, 0.26,
          .155, .105, .076, .059, .038, .027, .0148, .0094, .0050, .0031, .0022, .00163, .001024, .000714, .000498,
          .000372, .000291, .000236, .000166, .000125, 9.90e-5, 8.08e-5, 6.76e-5, 5.77e-5, 4.38e-5, 3.48e-5, 2.85e-5,
          2.39e-5, 2.04e-5, 1.43e-5, 1.08e-5, 8.52e-6, 6.91e-6, 4.85e-6, 3.62e-6, 2.81e-6, 2.25e-6, 1.85e-6, 1.55e-6,
          1.13e-6, 8.67e-7, 6.86e-7, 5.58e-7, 4.63e-7, 3.10e-7, 2.23e-7, 1.68e-7, 1.31e-7, 8.64e-8, 6.11e-8, 4.54e-8,
          3.51e-8, 2.78e-8, 2.26e-8, 1.57e-8, 1.15e-8, 8.79e-9, 6.93e-9, 5.60e-9, 3.57e-9, 2.47e-9, 1.81e-9, 1.38e-9,
          8.82e-10, 6.11e-10, 4.48e-10, 3.43e-10, 2.71e-10, 2.19e-10, 1.52e-10, 1.12e-10, 8.55e-11, 6.75e-11, 5.47e-11]

# ELASTIC TOTAL
XELG7 = [0.00, .001, .005, .007, 0.01, .015, 0.02, .025, 0.03, 0.04, 0.05, 0.06, 0.07, 0.08, 0.10, 0.12, 0.14, 0.17,
         0.20, 0.25, 0.27, 0.30, 0.32, 0.35, 0.37, 0.40, 0.42, 0.44, 0.46, 0.48, 0.50, 0.51, 0.52, 0.53, 0.54, 0.55,
         0.56, 0.57, 0.58, 0.59, 0.60, 0.61, 0.62, 0.63, 0.64, 0.65, 0.66, 0.67, 0.68, 0.69, 0.70, 0.75, 0.80, 0.85,
         0.90, 1.00, 1.20, 1.50, 1.75, 2.00, 2.50, 2.75, 3.00, 3.75, 4.00, 4.50, 5.00, 5.50, 6.00, 6.50, 7.00, 8.00,
         9.00, 10.0, 12.0, 15.0, 18.0, 20.0, 25.0, 30.0, 40.0, 50.0, 60.0, 70.0, 80.0, 90.0, 100., 125., 150., 200.,
         250., 300., 400., 500., 600., 700., 800., 1000., 1500., 2000., 3000., 4000., 5000., 6000., 8000., 1.0e4, 1.5e4,
         2.0e4, 3.0e4, 4.0e4, 5.0e4, 6.0e4, 8.0e4, 1.0e5, 1.25e5, 1.5e5, 1.75e5, 2.0e5, 2.5e5, 3.0e5, 3.5e5, 4.0e5,
         4.5e5, 5.0e5, 6.0e5, 7.0e5, 8.0e5, 9.0e5, 1.0e6, 1.25e6, 1.5e6, 1.75e6, 2.0e6, 2.5e6, 3.0e6, 3.5e6, 4.0e6,
         4.5e6, 5.0e6, 6.0e6, 7.0e6, 8.0e6, 9.0e6, 1.0e7, 1.25e7, 1.5e7, 1.75e7, 2.0e7, 2.5e7, 3.0e7, 3.5e7, 7.0e7,
         1.e9]
YELG7 = [131., 117., 101., 95.4, 88.8, 80.1, 73.3, 67.5, 62.6, 54.7, 48.4, 43.2, 38.8, 35.2, 29.4, 24.7, 21.2, 17.1,
         14.0, 10.3, 9.10, 7.75, 6.94, 5.95, 5.40, 4.50, 4.25, 3.95, 3.65, 3.45, 3.20, 3.11, 3.00, 2.90, 2.79, 2.69,
         2.59, 2.48, 2.37, 2.25, 2.14, 2.02, 1.92, 1.80, 1.69, 1.58, 1.48, 1.40, 1.32, 1.28, 1.26, 1.24, 1.30, 1.45,
         1.50, 1.87, 2.80, 4.76, 6.68, 8.85, 13.7, 16.3, 18.7, 24.5, 29.0, 32.7, 36.8, 39.3, 41.7, 41.7, 41.8, 41.8,
         41.0, 40.0, 37.4, 34.2, 32.4, 30.8, 21.9, 14.1, 8.58, 6.78, 5.97, 5.49, 5.29, 5.21, 5.10, 4.66, 4.58, 4.67,
         4.53, 4.35, 4.12, 3.77, 3.58, 3.30, 3.12, 2.80, 2.36, 2.07, 1.72, 1.52, 1.34, 1.13, .937, .817, .632, .523,
         .397, .326, .279, .246, .203, .175, .152, .136, .124, .116, .103, .0946, .0886, .0841, .0807, .0779, .0739,
         .0711, .0690, .0674, .0662, .0640, .0627, .0618, .0612, .0604, .0599, .0596, .0594, .0593, .0592, .0590, .0589,
         .0589, .0588, .0588, .0587, .0587, .0587, .0587, .0587, .05867, .05866, .05865, .05865]

# ELASTIC ANGULAR  DISTRIBUTION (EPSILON)
XEPSG7 = [0.00, .001, .005, .007, .010, .015, .020, .025, .030, .040, 0.05, 0.06, 0.07, 0.08, 0.10, 0.12, 0.14, 0.17,
          0.20, 0.25, 0.27, 0.30, 0.32, 0.35, 0.37, 0.40, 0.42, 0.44, 0.46, 0.48, 0.50, 0.51, 0.52, 0.53, 0.54, 0.55,
          0.56, 0.57, 0.58, 0.59, 0.60, 0.61, 0.62, 0.63, 0.64, 0.65, 0.66, 0.67, 0.68, 0.69, 0.70, 0.71, 0.72, 0.73,
          0.75, 0.77, 0.80, 0.83, 0.85, 0.87, 0.90, 1.00, 1.10, 1.20, 1.30, 1.40, 1.50, 1.70, 2.00, 2.50, 3.00, 3.50,
          4.00, 4.50, 5.00, 5.50, 6.00, 6.50, 7.00, 8.00, 9.00, 10.0, 12.0, 15.0, 18.0, 20.0, 25.0, 30.0, 40.0, 50.0,
          60.0, 70.0, 80.0, 90.0, 100., 125., 150., 200., 250., 300., 400., 500., 600., 700., 800., 1000., 1500., 2000.,
          3000., 4000., 5000., 6000., 8000., 10000., 15000., 2.0e4, 3.0e4, 4.0e4, 5.0e4, 6.0e4, 8.0e4, 1.0e5, 1.25e5,
          1.5e5, 1.75e5, 2.0e5, 2.5e5, 3.0e5, 3.5e5, 4.0e5, 4.5e5, 5.0e5, 6.0e5, 7.0e5, 8.0e5, 9.0e5, 1.0e6, 1.25e6,
          1.5e6, 1.75e6, 2.0e6, 2.5e6, 3.0e6, 3.5e6, 4.0e6, 4.5e6, 5.0e6, 6.0e6, 7.0e6, 8.0e6, 9.0e6, 1.0e7, 1.25e7,
          1.5e7, 1.75e7, 2.0e7, 2.5e7, 3.0e7, 3.5e7, 4.0e7, 4.5e7, 5.0e7, 6.0e7, 7.0e7, 8.0e7, 9.0e7, 1.0e8, 1.25e8,
          1.5e8, 1.75e8, 2.0e8, 2.5e8, 3.0e8, 3.5e8, 4.0e8, 4.5e8, 5.0e8, 6.0e8, 7.0e8, 8.0e8, 9.0e8, 1.0e9]
YEPSG7 = [1., .9744, .9406, .9325, .9173, .8972, .8776, .8606, .845, .8148, .7851, .7598, .7333, .7069, .6565, .6117,
          .5651, .5015, .4373, .3459, .3177, .2684, .2421, .2044, .1803, .1590, .1326, .1141, .0981, .0822, .0714,
          .0659, .0615, .0575, .0544, .0515, .0492, .0476, .0467, .0464, .0467, .0480, .0493, .0523, .0560, .0614,
          .0678, .0751, .0845, .0937, .1056, .1183, .1321, .1471, .1802, .2095, .2585, .2944, .3183, .3588, .4247,
          .5332, .6259, .7104, .7648, .8047, .8308, .8717, .8515, .7938, .7699, .7682, .7647, .7864, .7544, .7075,
          .6695, .6461, .6238, .5219, .4088, .3217, .2293, .1597, .1165, .1011, .1156, .1887, .3535, .2829, .2332,
          .2240, .2087, .1956, .1873, .2028, .1934, .1617, .1506, .1379, .1201, .1098, .1003, .0956, .0899, .0792,
          .0579, .0408, .0259, .0182, .0140, .0126, .0091, .0070, .0046, .00331, .00215, .00154, .00123, .00100,
          7.30e-4, 5.69e-4, 4.42e-4, 3.59e-4, 3.00e-4, 2.56e-4, 1.96e-4, 1.57e-4, 1.29e-4, 1.09e-4, 9.34e-5, 8.12e-5,
          6.34e-5, 5.12e-5, 4.23e-5, 3.563e-5, 3.048e-5, 2.134e-5, 1.607e-5, 1.255e-5, 1.009e-5, 6.944e-6, 5.077e-6,
          3.875e-6, 3.056e-6, 2.473e-6, 2.043e-6, 1.461e-6, 1.097e-6, 8.531e-7, 6.826e-7, 5.583e-7, 3.635e-7, 2.550e-7,
          1.885e-7, 1.447e-7, 9.266e-8, 6.407e-8, 4.674e-8, 3.548e-8, 2.775e-8, 2.224e-8, 1.512e-8, 1.089e-8, 8.19e-9,
          6.36e-9, 5.08e-9, 3.16e-8, 2.14e-9, 1.54e-9, 1.163e-9, 7.25e-10, 4.93e-10, 3.56e-10, 2.69e-10, 2.10e-10,
          1.68e-10, 1.15e-10, 8.3e-11, 6.3e-11, 4.9e-11, 3.9e-11]
# IONISATION (VALUES ABOVE 20KEV GENERATED BY BORN BETHE IN SUB)
XIONG7 = [12.129843, 12.5, 13.0, 13.5, 14.0, 14.5, 15.0, 15.5, 16.0, 16.5, 17.0, 18.0, 19.0, 20.0, 21.0, 22.0, 23.0,
          24.0, 26.0, 28.0, 30.0, 32.0, 34.0, 36.0, 40.0, 45.0, 50.0, 55.0, 60.0, 65.0, 70.0, 80.0, 90.0, 100., 110.,
          120., 130., 140., 150., 160., 180., 200., 250., 300., 350., 400., 450., 500., 550., 600., 700., 800., 900.,
          1000., 1200., 1400., 1600., 1800., 2000., 2500., 3000., 3500., 4000., 4500., 5000., 5500., 6000., 7000.,
          8000., 9000., 10000., 12000., 14000., 16000., 18000., 20000.]
# GROSS IONISATION
YIONG7 = [0.00, .137, .344, .549, .748, .939, 1.12, 1.29, 1.46, 1.62, 1.77, 2.04, 2.30, 2.52, 2.73, 2.93, 3.10, 3.27,
          3.56, 3.82, 4.06, 4.27, 4.42, 4.53, 4.73, 4.94, 5.11, 5.21, 5.31, 5.36, 5.40, 5.46, 5.56, 5.68, 5.75, 5.75,
          5.70, 5.58, 5.48, 5.35, 5.11, 4.83, 4.36, 4.02, 3.72, 3.46, 3.24, 3.06, 2.87, 2.72, 2.49, 2.26, 2.10, 1.94,
          1.68, 1.48, 1.35, 1.23, 1.13, .964, .836, .736, .663, .602, .555, .515, .480, .424, .382, .346, .319, .273,
          .242, .218, .200, .186]

# COUNTING IONISATION
YINCG7 = [0.00, .137, .344, .549, .748, .939, 1.12, 1.29, 1.46, 1.62, 1.77, 2.04, 2.30, 2.52, 2.73, 2.93, 3.10, 3.27,
          3.56, 3.82, 4.06, 4.27, 4.42, 4.53, 4.66, 4.77, 4.84, 4.89, 4.95, 4.99, 5.02, 5.04, 5.03, 5.02, 4.98, 4.90,
          4.80, 4.69, 4.60, 4.49, 4.27, 4.01, 3.58, 3.27, 3.00, 2.76, 2.57, 2.41, 2.25, 2.12, 1.93, 1.75, 1.62, 1.49,
          1.28, 1.12, 1.03, .923, .855, .731, .632, .557, .501, .455, .420, .389, .364, .320, .289, .262, .241, .206,
          .183, .165, .152, .141]

YIN1G7 = [0.00, .137, .344, .549, .748, .939, 1.12, 1.29, 1.46, 1.62, 1.77, 2.04, 2.30, 2.52, 2.73, 2.93, 3.10, 3.27,
          3.56, 3.82, 4.06, 4.27, 4.42, 4.51, 4.59, 4.60, 4.58, 4.60, 4.62, 4.64, 4.67, 4.64, 4.53, 4.44, 4.33, 4.21,
          4.08, 4.01, 3.93, 3.85, 3.65, 3.44, 3.06, 2.77, 2.48, 2.31, 2.15, 2.00, 1.87, 1.75, 1.58, 1.42, 1.32, 1.21,
          1.03, .903, .830, .744, .689, .589, .509, .449, .404, .367, .339, .314, .293, .258, .233, .211, .194, .166,
          .148, .133, .123, .114]

XIN2G7 = [33.105, 36.0, 40.0, 45.0, 50.0, 55.0, 60.0, 65.0, 70.0, 80.0, 90.0, 100., 110., 120., 130., 140., 150., 160.,
          180., 200., 250., 300., 350., 400., 450., 500., 550., 600., 700., 800., 900., 1000., 1200., 1400., 1600.,
          1800., 2000., 2500., 3000., 3500., 4000., 4500., 5000., 5500., 6000., 7000., 8000., 9000., 10000., 12000.,
          14000., 16000., 18000., 20000.]

YIN2G7 = [0.0, 0.02, .0688, .174, .257, .318, .363, .376, .386, .398, .461, .503, .534, .533, .521, .495, .470, .447,
          .405, .373, .325, .305, .294, .267, .253, .240, .230, .220, .204, .190, .175, .170, .145, .127, .117, .105,
          .0969, .0828, .0716, .0631, .0568, .0516, .0476, .0441, .0412, .0363, .0327, .0297, .0220, .0188, .0176,
          .0151, .0139, .0129]

XIN3G7 = [64.15, 70.0, 80.0, 90.0, 100., 110., 120., 130., 140., 150., 160., 180., 200., 250., 300., 350., 400., 450.,
          500., 550., 600., 700., 800., 900., 1000., 1200., 1400., 1600., 1800., 2000., 2500., 3000., 3500., 4000.,
          4500., 5000., 5500., 6000., 7000., 8000., 9000., 10000., 12000., 14000., 16000., 18000., 20000.]

YIN3G7 = [0.0, .001, .010, .0324, .0764, .122, .159, .184, .190, .189, .180, .169, .158, .142, .140, .137, .129, .123,
          .118, .112, .107, .102, .0921, .0844, .0825, .0703, .0616, .0566, .0507, .0470, .0402, .0347, .0306, .0275,
          .0250, .0231, .0214, .0200, .0176, .0159, .0144, .0132, .0113, .0101, .00907, .00835, .00775]

XIN4G7 = [106.35, 120., 130., 140., 150., 160., 180., 200., 250., 300., 350., 400., 450., 500., 550., 600., 700., 800.,
          900., 1000., 1200., 1400., 1600., 1800., 2000., 2500., 3000., 3500., 4000., 4500., 5000., 5500., 6000., 7000.,
          8000., 9000., 10000., 12000., 14000., 16000., 18000., 20000.]

YIN4G7 = [0.0, .0002, .00098, .0033, .0103, .0157, .0279, .0426, .0483, .0421, .0425, .0409, .0402, .0395, .0382, .0369,
          .0348, .0339, .0319, .0294, .0251, .0219, .0202, .0181, .0167, .0143, .0124, .0109, .00981, .00891, .00823,
          .00762, .00713, .00627, .00566, .00513, .00472, .00404, .00358, .00323, .00298, .00276]

XIN5G7 = [160.45, 180., 200., 250., 300., 350., 400., 450., 500., 550., 600., 700., 800., 900., 1000., 1200., 1400.,
          1600., 1800., 2000., 2500., 3000., 3500., 4000., 4500., 5000., 5500., 6000., 7000., 8000., 9000., 10000.,
          12000., 14000., 16000., 18000., 20000.]

YIN5G7 = [0.0, .00013, .0018, .0062, .0101, .0113, .0106, .0108, .0109, .0104, .0098, .0089, .0078, .0073, .0069, .059,
          .051, .0047, .0042, .0039, .0034, .0029, .0026, .0023, .0021, .00193, .00179, .00167, .00147, .00133, .00120,
          .00111, .00095, .00084, .00076, .00070, .00065]

XIN6G7 = [227.2, 250., 300., 350., 400., 450., 500., 550., 600., 700., 800., 900., 1000., 1200., 1400., 1600., 1800.,
          2000., 2500., 3000., 3500., 4000., 4500., 5000., 5500., 6000., 7000., 8000., 9000., 10000., 12000., 14000.,
          16000., 18000., 20000.]

YIN6G7 = [0.0, .00005, .00036, .00082, .00128, .00140, .00153, .00162, .00171, .00188, .00182, .00191, .00188, .00160,
          .00140, .00129, .00116, .00107, .00092, .00079, .00070, .00063, .00057, .00053, .00049, .00046, .00040,
          .00036, .00033, .00030, .00026, .00023, .00021, .00019, .00018]

XKSHG7 = [34561., 35490., 36526., 37592., 38690., 39819., 40982., 42178.,
          43410., 45981.,
          48706., 51591., 54648., 57885., 64947., 72871., 81761., 1.00e5, 1.22e5,
          1.50e5,
          1.83e5, 2.24e5, 2.82e5, 3.65e5, 4.87e5, 6.49e5, 8.66e5, 1.00e6, 1.22e6,
          1.50e6,
          1.83e6, 2.24e6, 2.82e6, 3.65e6, 4.87e6, 6.49e6, 8.66e6, 1.00e7, 1.22e7,
          1.50e7,
          2.05e7, 2.51e7, 3.07e7, 4.10e7, 5.16e7, 6.31e7, 7.50e7, 8.66e7, 1.00e8,
          1.22e8,
          1.50e8, 2.05e8, 2.51e8, 3.07e8, 4.10e8, 5.16e8, 6.31e8, 7.50e8, 8.66e8,
          1.00e9
          ]
YKSHG7 = [0.0, 1.74e-8, 3.56e-8, 5.30e-8, 6.98e-8, 8.58e-8, 1.01e-7,
          1.16e-7, 1.29e-7, 1.55e-7,
          1.78e-7, 1.99e-7, 2.17e-7, 2.34e-7, 2.62e-7, 2.84e-7, 3.00e-7, 3.20e-7,
          3.31e-7, 3.35e-7,
          3.34e-7, 3.31e-7, 3.26e-7, 3.21e-7, 3.20e-7, 3.23e-7, 3.29e-7, 3.34e-7,
          3.43e-7, 3.55e-7,
          3.68e-7, 3.83e-7, 4.01e-7, 4.23e-7, 4.50e-7, 4.77e-7, 5.05e-7, 5.20e-7,
          5.40e-7, 5.61e-7,
          5.93e-7, 6.14e-7, 6.35e-7, 6.65e-7, 6.89e-7, 7.10e-7, 7.28e-7, 7.43e-7,
          7.58e-7, 7.79e-7,
          7.99e-7, 8.32e-7, 8.53e-7, 8.74e-7, 9.03e-7, 9.27e-7, 9.47e-7, 9.65e-7,
          9.79e-7, 9.94e-7
          ]
XL1SG7 = [5453., 5499.2, 5658.7, 5823., 5992., 6166., 6345., 6529.,
          6719., 6914.,
          7321., 7753., 8210., 8695., 9208., 1.00e4, 1.09e4, 1.19e4, 1.30e4, 1.41e4,
          1.58e4, 1.78e4, 2.00e4, 2.24e4, 2.51e4, 2.90e4, 3.35e4, 3.87e4, 4.47e4,
          5.16e4,
          6.13e4, 7.29e4, 8.66e4, 1.00e5, 1.22e5, 1.54e5, 2.00e5, 2.59e5, 3.35e5,
          4.47e5,
          5.96e5, 8.66e5, 1.00e6, 1.22e6, 1.50e6, 1.83e6, 2.30e6, 2.90e6, 3.65e6,
          4.60e6,
          5.79e6, 7.50e6, 8.66e6, 1.00e7, 1.22e7, 1.50e7, 1.83e7, 2.30e7, 2.90e7,
          3.65e7,
          4.60e7, 5.79e7, 7.29e7, 8.66e7, 1.00e8, 1.22e8, 1.50e8, 1.83e8, 2.30e8,
          2.90e8,
          3.65e8, 4.60e8, 5.79e8, 7.29e8, 8.66e8, 1.00e9
          ]
YL1SG7 = [0.0, 2.21e-7, 9.39e-7, 1.62e-6, 2.26e-6, 2.86e-6, 3.43e-6,
          3.96e-6, 4.47e-6, 4.95e-6,
          5.82e-6, 6.59e-6, 7.26e-6, 7.86e-6, 8.37e-6, 9.02e-6, 9.52e-6, 9.89e-6,
          1.02e-5, 1.03e-5,
          1.04e-5, 1.04e-5, 1.02e-5, 9.98e-6, 9.68e-6, 9.23e-6, 8.73e-6, 8.20e-6,
          7.66e-6, 7.14e-6,
          6.53e-6, 5.97e-6, 5.46e-6, 5.06e-6, 4.57e-6, 4.08e-6, 3.64e-6, 3.30e-6,
          3.04e-6, 2.84e-6,
          2.71e-6, 2.64e-6, 2.64e-6, 2.66e-6, 2.69e-6, 2.74e-6, 2.82e-6, 2.90e-6,
          3.00e-6, 3.11e-6,
          3.23e-6, 3.36e-6, 3.44e-6, 3.52e-6, 3.63e-6, 3.74e-6, 3.85e-6, 3.98e-6,
          4.12e-6, 4.25e-6,
          4.38e-6, 4.51e-6, 4.65e-6, 4.75e-6, 4.83e-6, 4.95e-6, 5.06e-6, 5.18e-6,
          5.32e-6, 5.45e-6,
          5.58e-6, 5.72e-6, 5.85e-6, 5.99e-6, 6.09e-6, 6.17e-6
          ]
XL2SG7 = [5107., 5160.6, 5311.3, 5466., 5626., 5790., 5959., 6133.,
          6312., 6686.,
          7081., 7501., 7945., 8416., 9175., 1.00e4, 1.09e4, 1.19e4, 1.30e4, 1.41e4,
          1.58e4, 1.78e4, 2.00e4, 2.24e4, 2.51e4, 2.90e4, 3.35e4, 3.87e4, 4.47e4,
          5.16e4,
          6.13e4, 7.29e4, 8.66e4, 1.00e5, 1.22e5, 1.54e5, 2.00e5, 2.59e5, 3.35e5,
          4.47e5,
          5.96e5, 8.66e5, 1.00e6, 1.22e6, 1.50e6, 1.83e6, 2.30e6, 2.90e6, 3.65e6,
          4.60e6,
          5.79e6, 7.50e6, 8.66e6, 1.00e7, 1.22e7, 1.50e7, 2.05e7, 2.59e7, 3.16e7,
          4.10e7,
          5.16e7, 6.31e7, 7.50e7, 8.66e7, 1.00e8, 1.22e8, 1.50e8, 2.05e8, 2.59e8,
          3.16e8,
          4.10e8, 5.16e8, 6.31e8, 7.50e8, 8.66e8, 1.00e9
          ]
YL2SG7 = [0.0, 4.47e-7, 1.62e-6, 2.72e-6, 3.76e-6, 4.73e-6, 5.64e-6,
          6.49e-6, 7.28e-6, 8.71e-6,
          9.94e-6, 1.10e-5, 1.19e-5, 1.27e-5, 1.36e-5, 1.43e-5, 1.47e-5, 1.50e-5,
          1.52e-5, 1.52e-5,
          1.51e-5, 1.49e-5, 1.45e-5, 1.41e-5, 1.36e-5, 1.29e-5, 1.21e-5, 1.13e-5,
          1.06e-5, 9.81e-6,
          8.97e-6, 8.20e-6, 7.49e-6, 6.96e-6, 6.29e-6, 5.63e-6, 5.03e-6, 4.55e-6,
          4.19e-6, 3.92e-6,
          3.75e-6, 3.66e-6, 3.66e-6, 3.69e-6, 3.74e-6, 3.82e-6, 3.93e-6, 4.06e-6,
          4.20e-6, 4.36e-6,
          4.52e-6, 4.72e-6, 4.83e-6, 4.94e-6, 5.10e-6, 5.26e-6, 5.52e-6, 5.71e-6,
          5.88e-6, 6.09e-6,
          6.28e-6, 6.45e-6, 6.59e-6, 6.71e-6, 6.83e-6, 7.00e-6, 7.17e-6, 7.43e-6,
          7.63e-6, 7.79e-6,
          8.01e-6, 8.20e-6, 8.37e-6, 8.51e-6, 8.63e-6, 8.75e-6
          ]
XL3SG7 = [4786., 4881.6, 5023.7, 5170., 5321., 5476., 5635., 5800.,
          5968., 6321.,
          6695., 7091., 7511., 8187., 8924., 1.00e4, 1.09e4, 1.19e4, 1.30e4, 1.41e4,
          1.58e4, 1.78e4, 2.00e4, 2.24e4, 2.51e4, 2.90e4, 3.35e4, 3.87e4, 4.47e4,
          5.16e4,
          6.13e4, 7.29e4, 8.66e4, 1.00e5, 1.22e5, 1.54e5, 2.00e5, 2.59e5, 3.35e5,
          4.47e5,
          5.96e5, 8.66e5, 1.00e6, 1.22e6, 1.50e6, 1.83e6, 2.30e6, 2.90e6, 3.65e6,
          4.60e6,
          5.79e6, 7.50e6, 8.66e6, 1.00e7, 1.22e7, 1.50e7, 1.83e7, 2.30e7, 2.90e7,
          3.65e7,
          4.60e7, 5.79e7, 7.50e7, 8.66e7, 1.00e8, 1.22e8, 1.50e8, 1.83e8, 2.30e8,
          2.90e8,
          3.65e8, 4.60e8, 5.79e8, 7.50e8, 8.66e8, 1.00e9
          ]
YL3SG7 = [0.0, 1.94e-6, 4.64e-6, 7.17e-6, 9.54e-6, 1.18e-5, 1.38e-5,
          1.58e-5, 1.76e-5, 2.08e-5,
          2.36e-5, 2.60e-5, 2.80e-5, 3.05e-5, 3.23e-5, 3.40e-5, 3.48e-5, 3.52e-5,
          3.54e-5, 3.53e-5,
          3.48e-5, 3.41e-5, 3.31e-5, 3.19e-5, 3.06e-5, 2.86e-5, 2.70e-5, 2.52e-5,
          2.34e-5, 2.17e-5,
          1.98e-5, 1.81e-5, 1.65e-5, 1.53e-5, 1.38e-5, 1.23e-5, 1.09e-5, 9.89e-6,
          9.10e-6, 8.49e-6,
          8.10e-6, 7.90e-6, 7.89e-6, 7.93e-6, 8.04e-6, 8.19e-6, 8.41e-6, 8.67e-6,
          8.97e-6, 9.29e-6,
          9.63e-6, 1.00e-5, 1.03e-5, 1.05e-5, 1.08e-5, 1.12e-5, 1.15e-5, 1.19e-5,
          1.23e-5, 1.27e-5,
          1.31e-5, 1.35e-5, 1.39e-5, 1.42e-5, 1.45e-5, 1.48e-5, 1.52e-5, 1.55e-5,
          1.59e-5, 1.63e-5,
          1.67e-5, 1.71e-5, 1.75e-5, 1.80e-5, 1.82e-5, 1.85e-5
          ]
XM1SG7 = [1148.7, 1180.9, 1214.7, 1249.4, 1285.1, 1321.8, 1359.7, 1398.6,
          1438.7, 1479.9,
          1566., 1657., 1754., 1856., 1965., 2140., 2330., 2538., 2765., 3012.,
          3376., 3784., 4243., 4758., 5335., 6157., 7105., 8201., 1.00e4, 1.22e4,
          1.50e4, 1.88e4, 2.37e4, 3.00e4, 3.76e4, 4.87e4, 6.31e4, 8.41e4, 1.00e5,
          1.22e5,
          1.50e5, 1.88e5, 2.37e5, 3.00e5, 3.76e5, 4.87e5, 6.31e5, 8.41e5, 1.00e6,
          1.22e6,
          1.50e6, 1.88e6, 2.37e6, 3.00e6, 3.76e6, 4.87e6, 6.31e6, 8.41e6, 1.00e7,
          1.22e7,
          1.50e7, 1.88e7, 2.37e7, 2.99e7, 3.76e7, 4.87e7, 6.31e7, 8.41e7, 1.00e8,
          1.22e8,
          1.50e8, 1.88e8, 2.37e8, 2.99e8, 3.76e8, 4.87e8, 6.31e8, 8.41e8, 1.00e9
          ]
YM1SG7 = [0.0, 2.13e-5, 4.08e-5, 5.85e-5, 7.47e-5, 8.95e-5, 1.03e-4,
          1.16e-4, 1.27e-4, 1.37e-4,
          1.56e-4, 1.71e-4, 1.84e-4, 1.95e-4, 2.04e-4, 2.15e-4, 2.23e-4, 2.28e-4,
          2.30e-4, 2.31e-4,
          2.29e-4, 2.24e-4, 2.18e-4, 2.10e-4, 2.01e-4, 1.88e-4, 1.75e-4, 1.62e-4,
          1.44e-4, 1.27e-4,
          1.12e-4, 9.60e-5, 8.20e-5, 6.83e-5, 5.92e-5, 4.93e-5, 4.11e-5, 3.38e-5,
          3.03e-5, 2.67e-5,
          2.38e-5, 2.10e-5, 1.88e-5, 1.71e-5, 1.58e-5, 1.47e-5, 1.40e-5, 1.35e-5,
          1.34e-5, 1.33e-5,
          1.34e-5, 1.35e-5, 1.37e-5, 1.40e-5, 1.44e-5, 1.48e-5, 1.53e-5, 1.59e-5,
          1.62e-5, 1.66e-5,
          1.70e-5, 1.75e-5, 1.80e-5, 1.85e-5, 1.90e-5, 1.96e-5, 2.01e-5, 2.08e-5,
          2.11e-5, 2.16e-5,
          2.20e-5, 2.25e-5, 2.30e-5, 2.35e-5, 2.40e-5, 2.46e-5, 2.52e-5, 2.58e-5,
          2.62e-5
          ]
XM2SG7 = [1002.1, 1012.5, 1041.7, 1071.7, 1102.6, 1134.5, 1167.2, 1201.,
          1236., 1271.,
          1346., 1425., 1509., 1597., 1691., 1843., 2008., 2188., 2384., 2598.,
          2913., 3267., 3664., 4109., 4744., 5635., 6695., 7730., 8925., 1.00e4,
          1.22e4, 1.50e4, 1.88e4, 2.37e4, 3.00e4, 3.76e4, 4.87e4, 6.31e4, 8.41e4,
          1.00e5,
          1.22e5, 1.50e5, 1.88e5, 2.37e5, 3.00e5, 3.76e5, 4.87e5, 6.31e5, 8.41e5,
          1.00e6,
          1.22e6, 1.50e6, 1.88e6, 2.37e6, 3.00e6, 3.76e6, 4.87e6, 6.31e6, 8.41e6,
          1.00e7,
          1.22e7, 1.50e7, 1.88e7, 2.37e7, 2.99e7, 3.76e7, 4.87e7, 6.31e7, 8.41e7,
          1.00e8,
          1.22e8, 1.50e8, 1.88e8, 2.37e8, 2.99e8, 3.76e8, 4.87e8, 6.31e8, 8.41e8,
          1.00e9
          ]
YM2SG7 = [0.0, 1.17e-5, 4.18e-5, 6.88e-5, 9.29e-5, 1.15e-4, 1.34e-4,
          1.52e-4, 1.68e-4, 1.83e-4,
          2.08e-4, 2.30e-4, 2.49e-4, 2.64e-4, 2.78e-4, 2.95e-4, 3.09e-4, 3.19e-4,
          3.27e-4, 3.31e-4,
          3.34e-4, 3.32e-4, 3.27e-4, 3.19e-4, 3.06e-4, 2.86e-4, 2.64e-4, 2.45e-4,
          2.26e-4, 2.11e-4,
          1.86e-4, 1.63e-4, 1.39e-4, 1.19e-4, 1.01e-4, 8.55e-5, 7.12e-5, 5.94e-5,
          4.90e-5, 4.38e-5,
          3.87e-5, 3.45e-5, 3.05e-5, 2.74e-5, 2.50e-5, 2.31e-5, 2.16e-5, 2.06e-5,
          1.99e-5, 1.98e-5,
          1.97e-5, 1.98e-5, 2.01e-5, 2.05e-5, 2.10e-5, 2.16e-5, 2.23e-5, 2.31e-5,
          2.40e-5, 2.46e-5,
          2.52e-5, 2.59e-5, 2.67e-5, 2.75e-5, 2.83e-5, 2.91e-5, 3.00e-5, 3.09e-5,
          3.20e-5, 3.26e-5,
          3.33e-5, 3.40e-5, 3.48e-5, 3.56e-5, 3.65e-5, 3.73e-5, 3.82e-5, 3.91e-5,
          4.01e-5, 4.08e-5
          ]
XM3SG7 = [940.6, 958.1, 985.7, 1014.1, 1043.3, 1073.3, 1104.3, 1136.1,
          1168.9, 1202.6,
          1273., 1348., 1427., 1510., 1599., 1693., 1844., 2009., 2189., 2385.,
          2599., 2915., 3269., 3666., 4111., 4746., 5637., 6697., 7732., 8927.,
          1.00e4, 1.22e4, 1.50e4, 1.88e4, 2.37e4, 3.00e4, 3.76e4, 4.87e4, 6.31e4,
          8.41e4,
          1.00e5, 1.22e5, 1.50e5, 1.88e5, 2.37e5, 3.00e5, 3.76e5, 4.87e5, 6.31e5,
          8.41e5,
          1.00e6, 1.22e6, 1.88e6, 2.37e6, 3.00e6, 3.76e6, 4.87e6, 6.31e6, 8.41e6,
          1.00e7,
          1.22e7, 1.50e7, 1.88e7, 2.37e7, 2.99e7, 3.76e7, 4.87e7, 6.31e7, 8.41e7,
          1.00e8,
          1.22e8, 1.50e8, 1.88e8, 2.37e8, 2.99e8, 3.76e8, 4.87e8, 6.31e8, 8.41e8,
          1.00e9
          ]
YM3SG7 = [0.0, 5.19e-5, 1.24e-4, 1.88e-4, 2.44e-4, 2.95e-4, 3.40e-4,
          3.81e-4, 4.18e-4, 4.51e-4,
          5.10e-4, 5.59e-4, 6.01e-4, 6.37e-4, 6.68e-4, 6.96e-4, 7.29e-4, 7.56e-4,
          7.75e-4, 7.88e-4,
          7.96e-4, 7.96e-4, 7.88e-4, 7.72e-4, 7.50e-4, 7.15e-4, 6.66e-4, 6.12e-4,
          5.66e-4, 5.20e-4,
          4.85e-4, 4.27e-4, 3.74e-4, 3.19e-4, 2.72e-4, 2.31e-4, 1.96e-4, 1.63e-4,
          1.36e-4, 1.12e-4,
          1.00e-4, 8.86e-5, 7.89e-5, 6.99e-5, 6.27e-5, 5.71e-5, 5.29e-5, 4.94e-5,
          4.71e-5, 4.57e-5,
          4.53e-5, 4.52e-5, 4.61e-5, 4.71e-5, 4.82e-5, 4.96e-5, 5.13e-5, 5.31e-5,
          5.52e-5, 5.65e-5,
          5.81e-5, 5.97e-5, 6.15e-5, 6.34e-5, 6.53e-5, 6.71e-5, 6.93e-5, 7.14e-5,
          7.38e-5, 7.52e-5,
          7.69e-5, 7.86e-5, 8.05e-5, 8.24e-5, 8.43e-5, 8.62e-5, 8.84e-5, 9.05e-5,
          9.29e-5, 9.43e-5]
# M4-SHELL IONISATION

XM4SG7 = [689.0, 706.2, 726.8, 748.1, 770.0, 792.6, 815.7, 839.6, 864.2,
          889.5,
          942.3, 998.2, 1057., 1120., 1187., 1294., 1411., 1538., 1677., 1828.,
          2052., 2302., 2583., 2899., 3253., 3756., 4338., 5010., 5786., 6681.,
          7716., 8911., 1.00e4, 1.22e4, 1.50e4, 1.88e4, 2.37e4, 3.00e4, 3.76e4,
          4.87e4,
          6.31e4, 8.41e4, 1.00e5, 1.22e5, 1.50e5, 1.88e5, 2.37e5, 3.00e5, 3.76e5,
          4.87e5,
          6.31e5, 8.41e5, 1.00e6, 1.22e6, 1.88e6, 2.37e6, 3.00e6, 3.76e6, 4.87e6,
          6.31e6,
          8.41e6, 1.00e7, 1.22e7, 1.50e7, 1.88e7, 2.37e7, 2.99e7, 3.76e7, 4.87e7,
          6.31e7,
          8.41e7, 1.00e8, 1.22e8, 1.50e8, 1.88e8, 2.37e8, 2.99e8, 3.76e8, 4.87e8,
          6.31e8,
          8.41e8, 1.00e9
          ]
YM4SG7 = [0.0, 1.79e-4, 3.69e-4, 5.38e-4, 6.89e-4, 8.24e-4, 9.45e-4,
          1.05e-3, 1.15e-3, 1.24e-3,
          1.39e-3, 1.52e-3, 1.62e-3, 1.71e-3, 1.79e-3, 1.88e-3, 1.95e-3, 2.00e-3,
          2.03e-3, 2.05e-3,
          2.06e-3, 2.05e-3, 2.01e-3, 1.97e-3, 1.91e-3, 1.82e-3, 1.72e-3, 1.61e-3,
          1.50e-3, 1.39e-3,
          1.29e-3, 1.18e-3, 1.11e-3, 9.84e-4, 8.68e-4, 7.49e-4, 6.43e-4, 5.51e-4,
          4.71e-4, 3.96e-4,
          3.33e-4, 2.77e-4, 2.50e-4, 2.22e-4, 1.99e-4, 1.77e-4, 1.60e-4, 1.47e-4,
          1.37e-4, 1.29e-4,
          1.24e-4, 1.21e-4, 1.21e-4, 1.21e-4, 1.25e-4, 1.29e-4, 1.33e-4, 1.38e-4,
          1.43e-4, 1.49e-4,
          1.56e-4, 1.61e-4, 1.66e-4, 1.71e-4, 1.77e-4, 1.83e-4, 1.89e-4, 1.96e-4,
          2.03e-4, 2.10e-4,
          2.18e-4, 2.22e-4, 2.28e-4, 2.33e-4, 2.40e-4, 2.46e-4, 2.52e-4, 2.58e-4,
          2.65e-4, 2.73e-4,
          2.80e-4, 2.85e-4]
# M5-SHELL IONISATION

XM5SG7 = [676.4, 686.9, 707.0, 727.7, 748.9, 770.8, 793.4, 816.6, 840.4,
          865.0,
          916.3, 970.7, 1028., 1089., 1154., 1258., 1372., 1495., 1630., 1777.,
          1994., 2238., 2511., 2817., 3161., 3651., 4216., 4869., 5622., 6493.,
          7717., 8911., 1.00e4, 1.22e4, 1.50e4, 1.88e4, 2.37e4, 3.00e4, 3.76e4,
          4.87e4,
          6.31e4, 8.41e4, 1.00e5, 1.22e5, 1.50e5, 1.88e5, 2.37e5, 3.00e5, 3.76e5,
          4.87e5,
          6.31e5, 8.41e5, 1.00e6, 1.22e6, 1.50e6, 1.88e6, 2.37e6, 3.00e6, 3.76e6,
          4.87e6,
          6.31e6, 8.41e6, 1.00e7, 1.22e7, 1.50e7, 1.88e7, 2.37e7, 2.99e7, 3.76e7,
          4.87e7,
          6.31e7, 8.41e7, 1.00e8, 1.22e8, 1.50e8, 1.88e8, 2.37e8, 2.99e8, 3.76e8,
          4.87e8,
          6.31e8, 8.41e8, 1.00e9
          ]
YM5SG7 = [0.0, 1.84e-4, 4.98e-4, 7.77e-4, 1.02e-3, 1.25e-3, 1.44e-3,
          1.62e-3, 1.78e-3, 1.92e-3,
          2.16e-3, 2.37e-3, 2.53e-3, 2.67e-3, 2.79e-3, 2.93e-3, 3.04e-3, 3.12e-3,
          3.18e-3, 3.21e-3,
          3.23e-3, 3.21e-3, 3.16e-3, 3.09e-3, 2.99e-3, 2.86e-3, 2.70e-3, 2.53e-3,
          2.36e-3, 2.19e-3,
          1.99e-3, 1.83e-3, 1.71e-3, 1.52e-3, 1.34e-3, 1.16e-3, 9.92e-4, 8.50e-4,
          7.27e-4, 6.10e-4,
          5.14e-4, 4.28e-4, 3.85e-4, 3.42e-4, 3.06e-4, 2.73e-4, 2.47e-4, 2.26e-4,
          2.11e-4, 1.98e-4,
          1.91e-4, 1.86e-4, 1.86e-4, 1.87e-4, 1.89e-4, 1.93e-4, 1.98e-4, 2.04e-4,
          2.11e-4, 2.20e-4,
          2.29e-4, 2.40e-4, 2.47e-4, 2.55e-4, 2.63e-4, 2.72e-4, 2.81e-4, 2.91e-4,
          3.00e-4, 3.11e-4,
          3.22e-4, 3.34e-4, 3.41e-4, 3.50e-4, 3.58e-4, 3.68e-4, 3.77e-4, 3.87e-4,
          3.97e-4, 4.08e-4,
          4.18e-4, 4.31e-4, 4.38e-4
          ]
#
# EX#ITATION  UNITS OF 10**-18#M**2
#
# 1S5 METASTABLE E=8.3153155 EV  J=2
# SHAPE FUN#TION BELOW 11EV FROM BARTS#HAT AND ZATSARINNY
# ABOVE 100EV S#ALEe BY 1/E**3

X1S5G7 = [8.3153, 8.35, 8.40, 8.44, 8.48, 8.52, 8.56, 8.60, 8.65, 8.70,
          8.75, 8.80, 8.85, 8.90, 8.95, 9.00, 9.05, 9.10, 9.15, 9.20,
          9.25, 9.30, 9.35, 9.40, 9.45, 9.50, 9.516, 9.52, 9.525, 9.53,
          9.54, 9.545, 9.55, 9.555, 9.56, 9.57, 9.58, 9.59, 9.60, 9.61,
          9.615, 9.62, 9.625, 9.63, 9.64, 9.65, 9.66, 9.67, 9.68, 9.70,
          9.75, 10.0, 10.5, 11.0, 11.5, 12.0, 12.5, 13.0, 14.0, 15.0,
          16.0, 18.0, 20.0, 25.0, 30.0, 40.0, 50.0, 60.0, 80.0, 100.
          ]
Y1S5G7 = [0.00, 2.38, 4.93, 6.41, 3.42, 2.84, 3.00, 3.33, 3.89, 4.59,
          5.45, 6.48, 7.72, 9.05, 10.4, 11.5, 12.3, 12.2, 10.8, 9.45,
          8.84, 9.04, 9.18, 9.18, 9.11, 9.32, 23.6, 15.7, 12.1, 10.7,
          9.79, 11.4, 15.8, 18.0, 15.9, 13.1, 13.6, 12.6, 10.4, 12.1,
          14.9, 20.5, 21.5, 18.5, 17.2, 16.9, 15.9, 13.8, 12.4, 11.1,
          10.1, 10.0, 9.90, 9.80, 9.70, 9.60, 9.30, 8.80, 8.10, 7.45,
          6.80, 5.50, 4.40, 2.20, 1.10, .500, .230, .150, .065, .034
          ]
YP1S5G7 = np.zeros(70)
# 1S4 E=8.4365236 EV J=1  RESONAN#E RAeIATION 146.96 NM       F=0.260
#    USEe BEF S#ALING ABOVE 11.0EV
# SHAPE FUN#TION BELOW 11EV FROM BARTS#HAT AND ZATSARINNY

X1S4G7 = [8.4365, 8.45, 8.46, 8.47, 8.48, 8.49, 8.50, 8.52, 8.54, 8.56,
          8.60, 8.65, 8.70, 8.75, 8.80, 8.85, 8.90, 8.95, 9.00, 9.05,
          9.10, 9.15, 9.20, 9.25, 9.30, 9.35, 9.40, 9.45, 9.50, 9.55,
          9.60, 9.62, 9.65, 9.70, 9.75, 9.80, 10.0, 11.0
          ]
Y1S4G7 = [0.00, 2.60, 5.60, 6.09, 5.50, 4.72, 4.27, 3.70, 3.42, 3.24,
          3.10, 3.02, 3.34, 3.70, 4.25, 5.03, 6.00, 7.23, 8.70, 9.67,
          10.3, 10.1, 9.37, 9.00, 8.70, 8.55, 8.62, 8.77, 9.00, 10.1,
          10.5, 10.7, 10.2, 9.22, 9.40, 9.60, 10.8, 16.87
          ]
YP1S4G7 = np.zeros(38)
# 1S3  METASTABLE   E=9.4471945 EV J=0
# SHAPE FUN#TION BELOW 11EV FROM BARTS#AT AND ZATSARINNY
# ABOVE 100EV SCALED BY 1/E**3

X1S3G7 = [9.4472, 9.45, 9.47, 9.48, 9.49, 9.50, 9.506, 9.51, 9.52, 9.525,
          9.53, 9.54, 9.55, 9.555, 9.56, 9.57, 9.58, 9.60, 9.62, 9.64,
          9.67, 9.68, 9.69, 9.70, 9.71, 9.72, 9.73, 9.74, 9.75, 9.80,
          10.0, 11.0, 12.0, 13.0, 14.0, 15.0, 16.0, 18.0, 20.0, 24.0,
          30.0, 40.0, 50.0, 60.0, 80.0, 100.
          ]
Y1S3G7 = [0.00, .313, .324, .230, .360, 1.67, 3.78, 2.57, 1.26, 1.71,
          1.80, 1.78, 2.23, 2.70, 2.43, .635, 1.14, 1.04, 1.49, 1.59,
          1.62, 2.77, 3.89, 6.21, 9.38, 8.28, 6.75, 4.29, 3.97, .556,
          0.77, 3.30, 4.30, 4.50, 4.30, 3.70, 3.30, 2.65, 2.25, 1.50,
          0.80, 0.32, 0.17, 0.10, .040, .021
          ]
YP1S3G7 = np.zeros(46)
# 1S2 E=9.5697248 EV J=1 RESONAN#E RAeIATION 129.56 NM        F=0.183
#   USEe BEF S#ALING ABOVE 11.0EV
# SHAPE FUN#TION BELOW 11EV FROM BARTS#HAT AND ZATSARINNY

X1S2G7 = [9.5697, 9.58, 9.59, 9.60, 9.61, 9.62, 9.63, 9.64, 9.65, 9.67,
          9.68, 9.69, 9.70, 9.75, 9.77, 9.80, 9.85, 9.90, 10.0, 11.0
          ]
Y1S2G7 = [0.00, 1.21, 1.32, 1.41, 1.41, 1.30, 1.88, 2.00, 2.02, 2.02,
          2.83, 2.11, 2.07, 1.78, 2.10, 1.96, 1.75, 1.87, 2.17, 5.305
          ]
YP1S2G7 = np.zeros(20)
# 2P10 E=9.5801524 EV  J=1
# ABOVE 100EV S#ALEe BY 1/E**3

X2P10G7 = [9.5802, 9.80, 10.0, 10.5, 11.0, 11.5, 12.0, 12.5, 13.0, 14.0,
           15.0, 16.0, 18.0, 20.0, 25.0, 30.0, 35.0, 40.0, 50.0, 60.0,
           80.0, 100.
           ]
Y2P10G7 = [0.00, 0.69, 1.23, 2.34, 3.15, 3.73, 4.14, 4.41, 4.59, 4.76,
           4.74, 4.63, 4.26, 3.84, 2.91, 2.23, 1.75, 1.40, 0.95, 0.69,
           .406, .267
           ]
YP2P10G7 = np.zeros(22)
# 2P9 E=9.6856199 EV  J=2
# ABOVE 100EV S#ALEe BY 1/E

X2P9G7 = [9.6856, 10.0, 10.5, 11.0, 11.5, 12.0, 12.5, 13.0, 14.0, 15.0,
          16.0, 18.0, 20.0, 25.0, 30.0, 35.0, 40.0, 50.0, 60.0, 80.0,
          100.
          ]
Y2P9G7 = [0.00, 1.50, 3.37, 4.49, 5.47, 6.04, 6.48, 6.91, 7.41, 7.49,
          7.41, 6.98, 6.26, 5.04, 4.17, 3.52, 3.09, 2.52, 2.08, 1.58,
          1.22
          ]
YP2P9G7 = np.zeros(21)
# 2P8 E=9.7207401 EV  J=3
# ABOVE 100EV S#ALEe BY 1/E**3

X2P8G7 = [9.7207, 10.0, 10.5, 11.0, 11.5, 12.0, 12.5, 13.0, 13.5, 14.0,
          15.0, 16.0, 18.0, 20.0, 25.0, 30.0, 35.0, 40.0, 50.0, 60.0,
          80.0, 100.
          ]
Y2P8G7 = [0.00, 1.16, 2.78, 3.88, 4.86, 5.44, 5.83, 6.02, 6.35, 6.41,
          6.48, 6.33, 4.89, 3.24, 1.51, 0.72, 0.43, 0.26, 0.11, .061,
          .021, .0093
          ]
YP2P8G7 = np.zeros(22)
# 2P7 E=9.7892996 EV  J=1
# ABOVE 100EV S#ALEe BY 1/E**2

X2P7G7 = [9.7893, 10.0, 10.5, 11.0, 11.5, 12.0, 12.5, 13.0, 13.5, 14.0,
          15.0, 16.0, 18.0, 20.0, 25.0, 30.0, 35.0, 40.0, 50.0, 60.0,
          80.0, 100.
          ]
Y2P7G7 = [0.00, 0.66, 1.68, 2.52, 3.12, 3.48, 3.72, 3.90, 4.02, 4.14,
          4.20, 4.20, 3.90, 3.48, 2.64, 1.80, 1.26, 0.96, 0.63, 0.42,
          0.24, 0.15
          ]
YP2P7G7 = np.zeros(22)
# 2P6 E=9.8210934 EV  J=2
# ABOVE 100EV S#ALEe BY 1/E

X2P6G7 = [9.8211, 10.0, 10.5, 11.0, 11.5, 12.0, 12.5, 13.0, 13.5, 14.0,
          15.0, 16.0, 18.0, 20.0, 25.0, 30.0, 35.0, 40.0, 50.0, 60.0,
          80.0, 100.
          ]
Y2P6G7 = [0.00, 0.26, 1.05, 1.47, 1.92, 2.19, 2.32, 2.43, 2.53, 2.62,
          2.64, 2.88, 3.06, 2.94, 2.70, 2.10, 1.68, 1.53, 1.26, 1.02,
          0.78, 0.60
          ]
YP2P6G7 = np.zeros(22)
# 3e6 E=9.8903760 EV  J=0
# ABOVE 100EV S#ALEe BY 1/E**1.5

X3D6G7 = [9.8904, 10.0, 10.5, 11.0, 11.5, 12.0, 12.5, 13.0, 13.5, 14.0,
          14.5, 15.0, 16.0, 17.0, 18.0, 20.0, 22.0, 25.0, 30.0, 40.0,
          50.0, 60.0, 80.0, 100.
          ]
Y3D6G7 = [0.00, 0.23, 0.83, 1.50, 2.17, 2.77, 3.22, 3.60, 3.90, 4.20,
          4.42, 4.65, 4.80, 5.02, 5.02, 4.80, 4.50, 3.90, 2.78, 1.87,
          1.35, 1.01, 0.66, 0.48
          ]
YP3D6G7 = np.zeros(24)
#
# 3e5 E=9.9170761 EV J=1 RESONA#E RAeIATION 125.02 NM         F=0.010
#
# 2P5 E=9.9334847 EV  J=0
# ABOVE 100EV S#ALEe BY 1/E

X2P5G7 = [9.9335, 13.0, 16.0, 17.5, 20.0, 24.0, 26.0, 28.0, 30.0, 35.0,
          40.0, 50.0, 60.0, 80.0, 100.
          ]
Y2P5G7 = [0.00, 1.60, 2.16, 2.70, 4.26, 7.32, 8.46, 8.88, 8.70, 8.40,
          7.50, 5.70, 4.80, 3.60, 3.00
          ]
YP2P5G7 = np.zeros(15)
# 3e4! E=9.9431141 EV  J=4
# ABOVE 100EV S#ALEe BY 1/E**1.5

X3D4PG7 = [9.9431, 10.0, 10.5, 11.0, 11.5, 12.0, 12.5, 13.0, 13.5, 14.0,
           14.5, 15.0, 16.0, 17.0, 18.0, 20.0, 22.0, 25.0, 30.0, 40.0,
           50.0, 60.0, 80.0, 100.
           ]
Y3D4PG7 = [0.00, 0.45, 1.65, 3.00, 4.35, 5.55, 6.45, 7.20, 7.80, 8.40,
           8.85, 9.30, 9.60, 10.1, 10.1, 9.60, 9.00, 7.80, 5.77, 3.75,
           2.70, 2.03, 1.32, 0.96
           ]
YP3D4PG7 = np.zeros(24)
# 3e3 E=9.9587506 EV  J=2
# ABOVE 100EV S#ALEe BY 1/E**1.5

X3D3G7 = [9.9588, 10.0, 10.5, 11.0, 11.5, 12.0, 12.5, 13.0, 13.5, 14.0,
          14.5, 15.0, 16.0, 17.0, 18.0, 20.0, 22.0, 25.0, 30.0, 40.0,
          50.0, 60.0, 80.0, 100.
          ]
Y3D3G7 = [0.00, 0.48, 1.76, 3.20, 4.64, 5.92, 6.88, 7.68, 8.32, 8.96,
          9.44, 9.92, 10.2, 10.7, 10.7, 10.2, 9.60, 8.32, 5.92, 4.00,
          2.88, 2.16, 1.41, 1.03
          ]
YP3D3G7 = np.zeros(24)
# 3e4 E=10.039054 EV  J=3
# ABOVE 100EV S#ALEe BY 1/E**2

X3D4G7 = [10.0391, 10.2, 10.5, 10.7, 11.0, 11.2, 11.5, 12.0, 12.5, 13.0,
          13.5, 14.0, 14.5, 15.0, 16.0, 18.0, 20.0, 22.0, 25.0, 30.0,
          35.0, 40.0, 50.0, 60.0, 80.0, 100.
          ]
Y3D4G7 = [0.00, 0.50, 1.50, 2.20, 3.30, 4.00, 5.00, 6.90, 8.70, 10.7,
          12.2, 13.3, 13.6, 13.6, 12.8, 10.2, 9.00, 7.30, 5.70, 3.40,
          2.90, 2.20, 1.45, 1.00, 0.56, 0.36
          ]
YP3D4G7 = np.zeros(26)
# 3e1!! E=10.157469 EV  J=2
# ABOVE 100EV S#ALEe BY 1/E**3

X3D1PPG7 = [10.1575, 10.5, 10.7, 11.0, 11.5, 12.0, 12.5, 13.0, 13.5, 14.0,
            14.5, 15.0, 16.0, 18.0, 20.0, 22.0, 25.0, 30.0, 40.0, 50.0,
            60.0, 80.0, 100.
            ]
Y3D1PPG7 = [0.00, 0.70, 1.30, 2.00, 3.20, 4.50, 5.70, 6.80, 7.80, 8.30,
            8.50, 8.50, 8.20, 6.70, 5.30, 3.80, 2.90, 1.55, 0.67, 0.35,
            0.20, .085, .044
            ]
YP3D1PPG7 = np.zeros(23)
# 3e1! E=10.220042  J=3
# ABOVE 100EV S#ALEe BY 1/E

X3D1PG7 = [10.2200, 10.7, 11.0, 11.5, 12.0, 12.5, 13.0, 13.5, 14.0, 14.5,
           15.0, 16.0, 18.0, 20.0, 22.0, 25.0, 30.0, 40.0, 50.0, 60.0,
           80.0, 100.
           ]
Y3D1PG7 = [0.00, 0.60, 1.04, 1.83, 2.39, 3.00, 3.39, 3.65, 3.83, 3.94,
           4.00, 4.00, 3.95, 3.85, 3.70, 3.45, 2.90, 2.15, 1.70, 1.45,
           1.08, .875
           ]
YP3D1PG7 = np.zeros(22)
#
# 3e2 E=10.401030  J=1 RESONAN#E RAeIATION  119.20 NM         F=0.379
#
# 2S5  E=10.562062 EV  J=2 NOT OBSERVEe  USE 1S5 S#ALEe BY 0.25
# ABOVE 100EV S#ALEe BY 1/E**3

X2S5G7 = [10.5621, 11.0, 11.5, 12.0, 12.5, 13.0, 14.0, 15.0, 16.0, 18.0,
          20.0, 25.0, 30.0, 40.0, 50.0, 60.0, 80.0, 100.
          ]
Y2S5G7 = [0.00, 0.10, 0.25, 0.50, 1.00, 1.50, 2.02, 1.75, 1.70, 1.37,
          1.10, .550, .275, .125, .057, .037, .016, .0085
          ]
YP2S5G7 = np.zeros(18)
#
# 2S4  E=10.593211 EV  J=1  RESONAN#E RAeIATION 117.04 NM     F=0.086
#
# 3P10+3P9+3P8+3P7+3P6+3P5  E=10.9016 EV S#ALEe SUM OF 2P10--2P5 BY 0.25
# ABOVE 100EV S#ALEe BY 1/E

X3P105G7 = [10.9016, 11.50, 12.0, 12.5, 13.0, 14.0, 15.0, 16.0, 18.0, 20.0,
            25.0, 30.0, 35.0, 40.0, 50.0, 60.0, 80.0, 100.
            ]
Y3P105G7 = [0.00, 1.00, 2.70, 3.42, 4.20, 5.10, 5.70, 5.94, 5.93, 5.52,
            5.31, 4.71, 4.09, 3.54, 2.68, 2.18, 1.59, 1.26
            ]
YP3P105G7 = np.zeros(18)
# 2P4 E=10.957614 J=1
# ABOVE 100EV S#ALEe BY 1/E**2

X2P4G7 = [10.9576, 13.0, 14.0, 15.0, 16.0, 18.0, 20.0, 25.0, 30.0, 40.0,
          50.0, 60.0, 80.0, 100.
          ]
Y2P4G7 = [0.00, 0.75, 1.10, 1.20, 1.10, 0.75, 0.60, 0.38, 0.25, .145,
          .095, .065, .037, .025
          ]
YP2P4G7 = np.zeros(14)
# 4e6+4e3+4e4!+4e4+4e1!!+4e1!  SUM 4e  E=10.9715
#       SHAPE FROM PETROV NORMALISEe TO HAYASHI TOTAL
# ABOVE 100EV S#ALEe BY 1/E**3

X4DSUMG7 = [10.9715, 12.0, 13.0, 14.0, 15.0, 16.0, 18.0, 20.0, 25.0, 30.0,
            35.0, 40.0, 50.0, 60.0, 80.0, 100.
            ]
Y4DSUMG7 = [0.00, 1.50, 4.35, 4.65, 4.50, 4.05, 3.00, 2.25, 0.96, 0.57,
            0.36, 0.21, .099, .060, .024, .011
            ]
YP4DSUMG7 = np.zeros(16)
#
# 4e5 E=10.978772 J=1 RESONAN#E RAeIATION AT 112.93 NM        F=0.001
#
# 2P3 E=11.054723  J=2
# ABOVE 100 EV S#ALEe BY 1/E

X2P3G7 = [11.0547, 13.0, 14.0, 15.0, 16.0, 18.0, 20.0, 25.0, 30.0, 40.0,
          50.0, 60.0, 80.0, 100.
          ]
Y2P3G7 = [0.00, 2.20, 3.00, 3.50, 3.60, 3.50, 3.20, 2.60, 2.20, 1.65,
          1.35, 1.10, 0.83, 0.65
          ]
YP2P3G7 = np.zeros(14)
# 2P2 E=11.069148  J=1
# ABOVE 100EV S#ALEe BY 1/E**2

X2P2G7 = [11.0691, 13.0, 14.0, 15.0, 16.0, 18.0, 20.0, 25.0, 30.0, 40.0,
          50.0, 60.0, 80.0, 100.
          ]
Y2P2G7 = [0.00, 0.75, 1.00, 1.08, 1.08, 0.97, 0.85, 0.56, 0.40, 0.22,
          .145, .100, .054, .035
          ]
YP2P2G7 = np.zeros(14)
# 2P1 E=11.141221  J=0
# ABOVE 100EV S#ALEe BY 1/E

X2P1G7 = [11.1412, 13.0, 14.0, 15.0, 16.0, 18.0, 20.0, 25.0, 30.0, 35.0,
          40.0, 50.0, 60.0, 80.0, 100.
          ]
Y2P1G7 = [0.00, 0.80, 1.50, 1.90, 1.90, 1.80, 1.60, 1.30, 1.05, 0.91,
          0.77, 0.64, 0.52, 0.39, 0.31
          ]
YP2P1G7 = np.zeros(15)
#
# 4e2 E=11.162564 EV  J=1 RESONAN#E RAeIATION AT 111.07 NM    F=0.0835
# 3S4 E=11.274184 EV  J=1 RESONAN#E RAeIATION AT 109.97 NM    F=0.0225
# 5e5 E=11.422451 EV  J=1 RESONAN#E RAeIATION AT 108.55 NM    F=0.0227
# 5e2 E=11.495075 EV  J=1 RESONAN#E RAeIATION AT 107.86 NM    F=0.002
# 4S4 E=11.582864 EV  J=1 RESONAN#E RAeIATION AT 107.04 NM    F=0.0005
# 3S1! E=11.60718 EV  J=1 RESONAN#E RAeIATION AT 106.82 NM    F=0.1910
# 6e5 E=11.682783 EV  J=1 RESONAN#E RAeIATION AT 106.13 NM    F=0.0088
# 6e2 E=11.739501 EV  J=1 RESONAN#E RAeIATION AT 105.61 NM    F=0.0967
# 5S4 E=11.752100 EV  J=1 RESONAN#E RAeIATION AT 105.50 NM    F=0.0288
# 7e5 E=11.806816 EV  J=1 RESONAN#E RAeIATION AT 105.01 NM    F=0.0042
# 7e2 E=11.84030  EV  J=1 RESONAN#E RAeIATION AT 104.71 NM    F=0.0625
# 6S4 E=11.85177  EV  J=1 RESONAN#E RAeIATION AT 104.61 NM    F=0.0025
# 2S2 E=11.877758 EV  J=1 RESONAN#E RAeIATION AT 104.38 NM    F=0.029
# 8e5 E=11.891681 EV  J=1 RESONAN#E RAeIATION AT 104.26 NM    F=0.0035
# 8e2 E=11.90816  EV  J=1 RESONAN#E RAeIATION AT 104.12 NM    F=0.0386
# 7S4 E=11.91770  EV  J=1 RESONAN#E RAeIATION AT 104.03 NM    F=0.005
# 9e5 E=11.94156  EV  J=1 RESONAN#E RAeIATION AT 103.83 NM    F=0.0005
# 9e2 E=11.95502  EV  J=1 RESONAN#E RAeIATION AT 103.71 NM    F=0.025
# 8S4 E=11.96207  EV  J=1 RESONAN#E RAeIATION AT 103.64 NM    F=0.0023
# 10e5 E=11.978893 EV J=1 RESONAN#E RAeIATION AT 103.50 NM    F=0.0005
# 10e2 E=11.98858 EV  J=1 RESONAN#E RAeIATION AT 103.42 NM    F=0.0164
# 9S4 E=11.993947 EV  J=1 RESONAN#E RAeIATION AT 103.37 NM    F=0.0014
# SUM HIGHER STATES E=12.0 EV                                 F=0.0831
#
# TOTAL OS#ILLATOR SUM =1.650
#
# BREMSSTRAHLUNG X-SE#TION WITH #UT OFF UNITS 10**-24

Z54TG7 = [4948., 4086., 2921., 2088., 1396., 776., 492., 328., 220., 189.,
          179.7, 178.6, 179.0, 179.3, 179.6, 180.2, 180.3, 181.5, 182.1, 182.7,
          183.6, 184.4, 184.7, 185.5, 185.7
          ]
EBRMG7 = [1000., 2000., 5000., 1.E4, 2.E4, 5.E4, 1.E5, 2.E5, 5.E5, 1.E6,
          2.E6, 3.E6, 4.E6, 5.E6, 6.E6, 8.E6, 1.E7, 1.5E7, 2.E7, 3.E7,
          4.E7, 5.E7, 6.E7, 8.E7, 1.E8]

gd['gas7/XEN'] = XENG7
gd['gas7/YMOM'] = YMOMG7
gd['gas7/XEL'] = XELG7
gd['gas7/YEL'] = YELG7
gd['gas7/XEPS'] = XEPSG7
gd['gas7/YEPS'] = YEPSG7
gd['gas7/XION'] = XIONG7
gd['gas7/YION'] = YIONG7
gd['gas7/YINC'] = YINCG7
gd['gas7/YIN1'] = YIN1G7
gd['gas7/XIN2'] = XIN2G7
gd['gas7/YIN2'] = YIN2G7
gd['gas7/XIN3'] = XIN3G7
gd['gas7/YIN3'] = YIN3G7
gd['gas7/XIN4'] = XIN4G7
gd['gas7/YIN4'] = YIN4G7
gd['gas7/XIN5'] = XIN5G7
gd['gas7/YIN5'] = YIN5G7
gd['gas7/XIN6'] = XIN6G7
gd['gas7/YIN6'] = YIN6G7
gd['gas7/XKSH'] = XKSHG7
gd['gas7/YKSH'] = YKSHG7
gd['gas7/XL1S'] = XL1SG7
gd['gas7/YL1S'] = YL1SG7
gd['gas7/XL2S'] = XL2SG7
gd['gas7/YL2S'] = YL2SG7
gd['gas7/XL3S'] = XL3SG7
gd['gas7/YL3S'] = YL3SG7
gd['gas7/XM1S'] = XM1SG7
gd['gas7/YM1S'] = YM1SG7
gd['gas7/XM2S'] = XM2SG7
gd['gas7/YM2S'] = YM2SG7
gd['gas7/XM3S'] = XM3SG7
gd['gas7/YM3S'] = YM3SG7
gd['gas7/XM4S'] = XM4SG7
gd['gas7/YM4S'] = YM4SG7
gd['gas7/XM5S'] = XM5SG7
gd['gas7/YM5S'] = YM5SG7
gd['gas7/X1S5'] = X1S5G7
gd['gas7/Y1S5'] = Y1S5G7
gd['gas7/YP1S5'] = YP1S5G7
gd['gas7/X1S4'] = X1S4G7
gd['gas7/Y1S4'] = Y1S4G7
gd['gas7/YP1S4'] = YP1S4G7
gd['gas7/X1S3'] = X1S3G7
gd['gas7/Y1S3'] = Y1S3G7
gd['gas7/YP1S3'] = YP1S3G7
gd['gas7/X1S2'] = X1S2G7
gd['gas7/Y1S2'] = Y1S2G7
gd['gas7/YP1S2'] = YP1S2G7
gd['gas7/X2P10'] = X2P10G7
gd['gas7/Y2P10'] = Y2P10G7
gd['gas7/YP2P10'] = YP2P10G7
gd['gas7/X2P9'] = X2P9G7
gd['gas7/Y2P9'] = Y2P9G7
gd['gas7/YP2P9'] = YP2P9G7
gd['gas7/X2P8'] = X2P8G7
gd['gas7/Y2P8'] = Y2P8G7
gd['gas7/YP2P8'] = YP2P8G7
gd['gas7/X2P7'] = X2P7G7
gd['gas7/Y2P7'] = Y2P7G7
gd['gas7/YP2P7'] = YP2P7G7
gd['gas7/X2P6'] = X2P6G7
gd['gas7/Y2P6'] = Y2P6G7
gd['gas7/YP2P6'] = YP2P6G7
gd['gas7/X3D6'] = X3D6G7
gd['gas7/Y3D6'] = Y3D6G7
gd['gas7/YP3D6'] = YP3D6G7
gd['gas7/X2P5'] = X2P5G7
gd['gas7/Y2P5'] = Y2P5G7
gd['gas7/YP2P5'] = YP2P5G7
gd['gas7/X3D4P'] = X3D4PG7
gd['gas7/Y3D4P'] = Y3D4PG7
gd['gas7/YP3D4P'] = YP3D4PG7
gd['gas7/X3D3'] = X3D3G7
gd['gas7/Y3D3'] = Y3D3G7
gd['gas7/YP3D3'] = YP3D3G7
gd['gas7/X3D4'] = X3D4G7
gd['gas7/Y3D4'] = Y3D4G7
gd['gas7/YP3D4'] = YP3D4G7
gd['gas7/X3D1PP'] = X3D1PPG7
gd['gas7/Y3D1PP'] = Y3D1PPG7
gd['gas7/YP3D1PP'] = YP3D1PPG7
gd['gas7/X3D1P'] = X3D1PG7
gd['gas7/Y3D1P'] = Y3D1PG7
gd['gas7/YP3D1P'] = YP3D1PG7
gd['gas7/X2S5'] = X2S5G7
gd['gas7/Y2S5'] = Y2S5G7
gd['gas7/YP2S5'] = YP2S5G7
gd['gas7/X3P105'] = X3P105G7
gd['gas7/Y3P105'] = Y3P105G7
gd['gas7/YP3P105'] = YP3P105G7
gd['gas7/X2P4'] = X2P4G7
gd['gas7/Y2P4'] = Y2P4G7
gd['gas7/YP2P4'] = YP2P4G7
gd['gas7/X4DSUM'] = X4DSUMG7
gd['gas7/Y4DSUM'] = Y4DSUMG7
gd['gas7/YP4DSUM'] = YP4DSUMG7
gd['gas7/X2P3'] = X2P3G7
gd['gas7/Y2P3'] = Y2P3G7
gd['gas7/YP2P3'] = YP2P3G7
gd['gas7/X2P2'] = X2P2G7
gd['gas7/Y2P2'] = Y2P2G7
gd['gas7/YP2P2'] = YP2P2G7
gd['gas7/X2P1'] = X2P1G7
gd['gas7/Y2P1'] = Y2P1G7
gd['gas7/YP2P1'] = YP2P1G7
gd['gas7/Z54T'] = Z54TG7
gd['gas7/EBRM'] = EBRMG7

XENG8 = [np.float32(0.00), np.float32(.0001), np.float32(.001), np.float32(.002), np.float32(.004), np.float32(.007),
         np.float32(0.01), np.float32(.012), np.float32(.014), np.float32(.017),
         np.float32(0.02), np.float32(.025), np.float32(0.03), np.float32(.035), np.float32(0.04), np.float32(0.05),
         np.float32(0.06), np.float32(0.07), np.float32(0.08), np.float32(0.09),
         np.float32(0.10), np.float32(0.12), np.float32(0.14), np.float32(0.17), np.float32(0.20), np.float32(0.24),
         np.float32(0.28), np.float32(0.32), np.float32(0.36), np.float32(0.40),
         np.float32(0.45), np.float32(0.50), np.float32(0.60), np.float32(0.70), np.float32(0.80), np.float32(1.00),
         np.float32(1.20), np.float32(1.40), np.float32(1.70), np.float32(2.00),
         np.float32(2.50), np.float32(3.00), np.float32(3.50), np.float32(4.00), np.float32(5.00), np.float32(6.00),
         np.float32(7.00), np.float32(8.00), np.float32(9.00), np.float32(10.0),
         np.float32(12.0), np.float32(15.0), np.float32(20.0), np.float32(25.0), np.float32(30.0), np.float32(40.0),
         np.float32(50.0), np.float32(60.0), np.float32(80.0), np.float32(100.),
         np.float32(150.), np.float32(200.), np.float32(300.), np.float32(400.), np.float32(500.), np.float32(600.),
         np.float32(800.), np.float32(1000.), np.float32(1500.), np.float32(2000.),
         np.float32(3000.), np.float32(4000.), np.float32(5000.), np.float32(6000.), np.float32(7000.),
         np.float32(8000.), np.float32(9000.), 1.e4, 1.25e4, 1.5e4,
         1.75e4, 2.0e4, 2.5e4, 3.0e4, 3.5e4, 4.0e4, 4.5e4, 5.0e4, 6.0e4, 7.0e4,
         8.0e4, 9.0e4, 1.0e5, 1.25e5, 1.5e5, 1.75e5, 2.0e5, 2.5e5, 3.0e5, 3.5e5,
         4.0e5, 4.5e5, 5.0e5, 6.0e5, 7.0e5, 8.0e5, 9.0e5, 1.0e6, 1.25e6, 1.5e6,
         1.75e6, 2.0e6, 2.5e6, 3.0e6, 3.5e6, 4.0e6, 4.5e6, 5.0e6, 6.0e6, 7.0e6,
         8.0e6, 9.0e6, 1.0e7, 1.25e7, 1.5e7, 1.75e7, 2.0e7, 2.5e7, 3.0e7, 3.5e7,
         4.0e7, 4.5e7, 5.0e7, 6.0e7, 7.0e7, 8.0e7, 9.0e7, 1.0e8, 1.25e8, 1.5e8,
         1.75e8, 2.0e8, 2.5e8, 3.0e8, 3.5e8, 4.0e8, 4.5e8, 5.0e8, 6.0e8, 7.0e8,
         8.0e9, 9.0e8, 1.0e9,
         ]
# ELASTIC MOMENTUM TRANSFER X-SECTION

YELMG8 = [np.float32(26.7), np.float32(25.4), np.float32(22.6), np.float32(21.0), np.float32(18.8), np.float32(16.5),
          np.float32(14.8), np.float32(13.9), np.float32(13.0), np.float32(12.0),
          np.float32(11.2), np.float32(10.05), np.float32(9.05), np.float32(8.20), np.float32(7.50), np.float32(6.25),
          np.float32(5.30), np.float32(4.60), np.float32(3.88), np.float32(3.22),
          np.float32(2.60), np.float32(1.74), np.float32(1.19), np.float32(0.70), np.float32(.440), np.float32(.290),
          np.float32(.270), np.float32(.270), np.float32(.325), np.float32(.410),
          np.float32(.540), np.float32(.645), np.float32(.850), np.float32(1.08), np.float32(1.30), np.float32(1.75),
          np.float32(2.25), np.float32(2.70), np.float32(3.50), np.float32(4.35),
          np.float32(6.00), np.float32(7.70), np.float32(9.70), np.float32(11.7), np.float32(14.9), np.float32(17.0),
          np.float32(18.4), np.float32(18.6), np.float32(18.6), np.float32(17.7),
          np.float32(14.6), np.float32(10.6), np.float32(6.90), np.float32(4.80), np.float32(3.90), np.float32(2.75),
          np.float32(2.15), np.float32(1.75), np.float32(1.24), np.float32(0.96),
          np.float32(0.59), np.float32(.400), np.float32(.235), np.float32(0.16), np.float32(.115), np.float32(0.09),
          np.float32(0.06), np.float32(.045), np.float32(.0223), np.float32(.0134),
          np.float32(.00654), np.float32(.0039), np.float32(.00261), np.float32(.00188), np.float32(.00142),
          np.float32(.00112), 9.01e-4, 7.44e-4,
          4.96e-4, 3.56e-4,
          2.69e-4, 2.11e-4, 1.41e-4, 1.01e-4, 7.67e-5, 6.03e-5, 4.88e-5, 4.04e-5,
          2.92e-5, 2.22e-5,
          1.76e-5, 1.43e-5, 1.19e-5, 8.09e-6, 5.93e-6, 4.57e-6, 3.66e-6, 2.54e-6,
          1.89e-6, 1.48e-6,
          1.20e-6, 9.96e-7, 8.45e-7, 6.38e-7, 5.04e-7, 4.11e-7, 3.43e-7, 2.92e-7,
          2.09e-7, 1.58e-7,
          1.24e-7, 1.00e-7, 7.01e-8, 5.21e-8, 4.04e-8, 3.24e-8, 2.66e-8, 2.22e-8,
          1.62e-8, 1.24e-8,
          9.84e-9, 8.00e-9, 6.64e-9, 4.45e-9, 3.20e-9, 2.42e-9, 1.90e-9, 1.26e-9,
          8.98e-10, 6.74e-10,
          5.25e-10, 4.21e-10, 3.45e-10, 2.44e-10, 1.82e-10, 1.40e-10, 1.12e-10,
          9.11e-11, 5.89e-11, 4.11e-11,
          3.03e-11, 2.32e-11, 1.49e-11, 1.04e-11, 7.63e-12, 5.84e-12, 4.62e-12,
          3.74e-12, 2.60e-12, 1.91e-12,
          1.46e-12, 1.16e-12, 9.36e-13,
          ]
# ELASTIC TOTAL X-SECTION

YELTG8 = [np.float32(26.7), np.float32(25.6), np.float32(23.3), np.float32(22.0), np.float32(19.9), np.float32(17.9),
          np.float32(16.4), np.float32(15.5), np.float32(14.8), np.float32(13.8),
          np.float32(12.9), np.float32(11.6), np.float32(10.6), np.float32(9.67), np.float32(8.89), np.float32(7.60),
          np.float32(6.57), np.float32(5.70), np.float32(4.90), np.float32(4.20),
          np.float32(3.70), np.float32(2.80), np.float32(2.20), np.float32(1.62), np.float32(1.23), np.float32(0.95),
          np.float32(0.82), np.float32(0.75), np.float32(0.72), np.float32(0.71),
          np.float32(0.73), np.float32(0.77), np.float32(0.95), np.float32(1.10), np.float32(1.28), np.float32(1.72),
          np.float32(2.25), np.float32(3.00), np.float32(3.96), np.float32(5.05),
          np.float32(6.93), np.float32(8.93), np.float32(11.2), np.float32(13.4), np.float32(17.9), np.float32(21.5),
          np.float32(23.3), np.float32(24.0), np.float32(24.1), np.float32(24.0),
          np.float32(22.2), np.float32(19.9), np.float32(16.0), np.float32(13.4), np.float32(11.6), np.float32(8.94),
          np.float32(7.57), np.float32(6.46), np.float32(5.11), np.float32(4.24),
          np.float32(2.79), np.float32(2.21), np.float32(1.56), np.float32(1.06), np.float32(0.80), np.float32(0.63),
          np.float32(0.50), np.float32(0.40), np.float32(0.31), np.float32(.252),
          np.float32(.202), np.float32(.167), np.float32(.147), np.float32(.123), np.float32(.106), np.float32(.093),
          np.float32(.083), np.float32(.075), np.float32(.060), np.float32(.051),
          np.float32(.044), np.float32(.039), np.float32(.0315), np.float32(.0266), np.float32(.0231),
          np.float32(.0205), np.float32(.0185), np.float32(.0169), np.float32(.0144), np.float32(.0127),
          np.float32(.0117), np.float32(.0104), np.float32(.00957), np.float32(.00812), np.float32(.00715),
          np.float32(.00647), np.float32(.00595), np.float32(.00524), np.float32(.00477),
          np.float32(.00444),
          np.float32(.00420), np.float32(.00401), np.float32(.00387), np.float32(.00365), np.float32(.00350),
          np.float32(.00340), np.float32(.00331), np.float32(.00325), np.float32(.00314),
          np.float32(.00308),
          np.float32(.00303), np.float32(.00300), np.float32(.00296), np.float32(.00294), np.float32(.00293),
          np.float32(.00292), np.float32(.00291), np.float32(.00290), np.float32(.00290),
          np.float32(.00289),
          np.float32(.00289), np.float32(.00289), np.float32(.00289), np.float32(.00288), np.float32(.00288),
          np.float32(.00288), np.float32(.00288), np.float32(.002879), np.float32(.002879), np.float32(.002879),
          np.float32(.002879), np.float32(.002879), np.float32(.002879), np.float32(.002879), np.float32(.002879),
          np.float32(.002879), np.float32(.002879), np.float32(.002879), np.float32(.002879), np.float32(.002879),
          np.float32(.002879), np.float32(.002879), np.float32(.002879), np.float32(.002879), np.float32(.002879),
          np.float32(.002879), np.float32(.002879), np.float32(.002879), np.float32(.002879), np.float32(.002879),
          np.float32(.002879), np.float32(.002879), np.float32(.002879),
          ]
# EPSILON FOR ELASTIC ANGULAR DISTRIBUTION

#  EPSILON=1.0-YEPS

YEPSG8 = [np.float32(1.00), np.float32(.9883), np.float32(.9550), np.float32(.9319), np.float32(.9172),
          np.float32(.8830), np.float32(.8543), np.float32(.8459), np.float32(.8188),
          np.float32(.8058),
          np.float32(.8039), np.float32(.8012), np.float32(.7827), np.float32(.7743), np.float32(.7680),
          np.float32(.7373), np.float32(.7149), np.float32(.7153), np.float32(.6937), np.float32(.6584),
          np.float32(.5712), np.float32(.4669), np.float32(.3718), np.float32(.2583), np.float32(.1913),
          np.float32(.1495), np.float32(.1680), np.float32(.1932), np.float32(.2771), np.float32(.4139),
          np.float32(.6212), np.float32(.7594), np.float32(.8429), np.float32(.9727), np.float32(1.0234),
          np.float32(1.0262), np.float32(1.000), np.float32(.8507), np.float32(.8268), np.float32(.7939),
          np.float32(.8003), np.float32(.7951), np.float32(.8007), np.float32(.8111), np.float32(.7518),
          np.float32(.6921), np.float32(.6907), np.float32(.6700), np.float32(.6655), np.float32(.6181),
          np.float32(.5124), np.float32(.3626), np.float32(.2575), np.float32(.1917), np.float32(.1736),
          np.float32(.1512), np.float32(.1338), np.float32(.1245), np.float32(.1054), np.float32(.0951),
          np.float32(.0859), np.float32(.0685), np.float32(.0526), np.float32(.0528), np.float32(.0493),
          np.float32(.0488), np.float32(.0383), np.float32(.0350), np.float32(.0192), np.float32(.0129),
          np.float32(.0069), np.float32(.0046), np.float32(.00326), np.float32(.00272), np.float32(.00232),
          np.float32(.00204), np.float32(.00180), np.float32(.00162), np.float32(.00130),
          np.float32(.00107),
          np.float32(.00091), np.float32(.000791), np.float32(.000634), np.float32(.000523), np.float32(.000448),
          np.float32(.000390), np.float32(.000344), np.float32(.000307),
          np.float32(.000254), np.float32(.000215),
          1.81e-4, 1.63e-4, 1.46e-4, 1.14e-4, 9.23e-5, 7.71e-5, 6.60e-5, 5.06e-5,
          4.04e-5, 3.33e-5,
          2.81e-5, 2.41e-5, 2.09e-5, 1.63e-5, 1.32e-5, 1.09e-5, 9.17e-6, 7.85e-6,
          5.64e-6, 4.24e-6,
          3.31e-6, 2.66e-6, 1.83e-6, 1.37e-6, 1.03e-6, 8.09e-7, 6.55e-7, 5.41e-7,
          3.88e-7, 2.92e-7,
          2.27e-7, 1.82e-7, 1.49e-7, 9.75e-8, 6.87e-8, 5.10e-8, 3.93e-8, 2.54e-8,
          1.78e-8, 1.31e-8,
          1.01e-8, 7.97e-9, 6.46e-9, 4.48e-9, 3.28e-9, 2.50e-9, 1.97e-9, 1.59e-9,
          1.00e-9, 6.86e-10,
          4.98e-10, 3.77e-10, 2.37e-10, 1.62e-10, 1.17e-10, 8.90e-11, 6.90e-11,
          5.60e-11, 3.80e-11, 2.70e-11,
          2.10e-11, 1.60e-11, 1.30e-11,
          ]
# V4 DIPOLE PART AS ANALYTIC FUNCTION IN SUBROUTINE

# ABOVE 100 EV SCALED BY 1/E**2

XVBV4G8 = [np.float32(.1625135), np.float32(0.20), np.float32(0.30), np.float32(0.40), np.float32(0.50),
           np.float32(0.60), np.float32(0.80), np.float32(1.00), np.float32(1.50), np.float32(2.00),
           np.float32(3.00), np.float32(5.00), np.float32(6.00), np.float32(7.00), np.float32(8.00), np.float32(9.00),
           np.float32(10.0), np.float32(12.5), np.float32(15.0), np.float32(20.0),
           np.float32(30.0), np.float32(40.0), np.float32(50.0), np.float32(60.0), np.float32(80.0), np.float32(100.),
           ]
YVBV4G8 = [np.float32(0.00), np.float32(.0001), np.float32(.060), np.float32(.057), np.float32(.055), np.float32(.050),
           np.float32(.040), np.float32(.035), np.float32(.041), np.float32(.056),
           np.float32(.082), np.float32(.278), np.float32(.406), np.float32(0.47), np.float32(0.44), np.float32(.383),
           np.float32(.323), np.float32(.266), np.float32(.201), np.float32(.126),
           np.float32(.056), np.float32(.031), np.float32(.020), np.float32(.014), np.float32(.0079), np.float32(.005),
           ]
# V2

XVBV2G8 = [np.float32(.1901087), np.float32(.195), np.float32(0.20), np.float32(0.21), np.float32(0.22),
           np.float32(0.23), np.float32(0.24), np.float32(0.26), np.float32(0.28), np.float32(0.30),
           np.float32(0.40), np.float32(0.50), np.float32(0.60), np.float32(0.80), np.float32(1.00), np.float32(1.50),
           np.float32(2.00), np.float32(3.00), np.float32(5.00), np.float32(6.00),
           np.float32(7.00), np.float32(8.00), np.float32(9.00), np.float32(10.0), np.float32(12.5), np.float32(15.0),
           np.float32(20.0), np.float32(30.0), np.float32(40.0),
           ]
YVBV2G8 = [np.float32(0.00), np.float32(.028), np.float32(.038), np.float32(.051), np.float32(.060), np.float32(.066),
           np.float32(.071), np.float32(.075), np.float32(.076), np.float32(.077),
           np.float32(.080), np.float32(.081), np.float32(.082), np.float32(.082), np.float32(.083), np.float32(.084),
           np.float32(.086), np.float32(.118), np.float32(.308), np.float32(.446),
           np.float32(0.49), np.float32(0.46), np.float32(.403), np.float32(.333), np.float32(.217), np.float32(.171),
           np.float32(.102), np.float32(.045), np.float32(.025),
           ]
# V1

XVBV1G8 = [np.float32(.3615974), np.float32(.363), np.float32(.365), np.float32(.367), np.float32(0.37),
           np.float32(.375), np.float32(0.38), np.float32(0.39), np.float32(0.40), np.float32(0.42),
           np.float32(0.45), np.float32(0.50), np.float32(0.60), np.float32(0.70), np.float32(0.80), np.float32(1.00),
           np.float32(1.50), np.float32(2.00), np.float32(3.00), np.float32(5.00),
           np.float32(6.00), np.float32(7.00), np.float32(8.00), np.float32(9.00), np.float32(10.0), np.float32(12.5),
           np.float32(15.0), np.float32(20.0), np.float32(30.0), np.float32(40.0),
           ]
YVBV1G8 = [np.float32(.0), np.float32(.0028), np.float32(.0043), np.float32(.0054), np.float32(.0066),
           np.float32(.0083), np.float32(.0095), np.float32(.0115), np.float32(.013), np.float32(.015),
           np.float32(.017), np.float32(.019), np.float32(0.02), np.float32(0.02), np.float32(.021), np.float32(.022),
           np.float32(.023), np.float32(.025), np.float32(.042), np.float32(.157),
           np.float32(.226), np.float32(.260), np.float32(.260), np.float32(.215), np.float32(.190), np.float32(.151),
           np.float32(.120), np.float32(.085), np.float32(.038), np.float32(.021),
           ]
# V3 DIPOLE PART AS ANALYTIC FUNCTION

XVBV3G8 = [np.float32(.3743690), np.float32(0.40), np.float32(0.50), np.float32(0.60), np.float32(0.70),
           np.float32(0.80), np.float32(1.00), np.float32(1.50), np.float32(2.00), np.float32(3.00),
           np.float32(5.00), np.float32(6.00), np.float32(7.00), np.float32(8.00), np.float32(9.00), np.float32(10.0),
           np.float32(12.5), np.float32(15.0), np.float32(20.0), np.float32(30.0),
           np.float32(40.0), np.float32(50.0), np.float32(60.0), np.float32(80.0), np.float32(100.),
           ]
YVBV3G8 = [np.float32(.0), np.float32(.004), np.float32(0.01), np.float32(.011), np.float32(.011), np.float32(.011),
           np.float32(.011), np.float32(.015), np.float32(.019), np.float32(.105),
           np.float32(.458), np.float32(.596), np.float32(.680), np.float32(.680), np.float32(.593), np.float32(.433),
           np.float32(.300), np.float32(.241), np.float32(.142), np.float32(.063),
           np.float32(.0355), np.float32(.0227), np.float32(.0158), np.float32(.0089), np.float32(.0057),
           ]
# VIBRATION HARMONIC

XVBH1G8 = [np.float32(.544), np.float32(1.00), np.float32(2.00), np.float32(3.00), np.float32(5.00), np.float32(6.00),
           np.float32(7.00), np.float32(8.00), np.float32(9.00), np.float32(10.0),
           np.float32(12.5), np.float32(15.0), np.float32(17.5), np.float32(20.0),
           ]
YVBH1G8 = [np.float32(0.00), np.float32(.0007), np.float32(.0028), np.float32(.014), np.float32(.053), np.float32(.068),
           np.float32(.075), np.float32(.075), np.float32(.061), np.float32(.044),
           np.float32(.031), np.float32(.021), np.float32(.015), np.float32(.011),
           ]
# VIBRATION HARMONIC

XVBH2G8 = [np.float32(.736), np.float32(1.00), np.float32(2.00), np.float32(3.00), np.float32(5.00), np.float32(6.00),
           np.float32(7.00), np.float32(8.00), np.float32(9.00), np.float32(10.0),
           np.float32(12.5), np.float32(15.0), np.float32(17.5), np.float32(20.0),
           ]
YVBH2G8 = [np.float32(0.00), np.float32(.0005), np.float32(.0022), np.float32(.0135), np.float32(.044),
           np.float32(.058), np.float32(.064), np.float32(.064), np.float32(.053), np.float32(.039),
           np.float32(.024), np.float32(.014), np.float32(.010), np.float32(.006),
           ]
# IONISATION  X-SECTION ABOVE 1KEV GIVEN BY BORN-BETHE

XIONG8 = [np.float32(12.65), np.float32(13.5), np.float32(14.0), np.float32(14.5), np.float32(15.0), np.float32(15.5),
          np.float32(16.0), np.float32(16.5), np.float32(17.0), np.float32(17.5),
          np.float32(18.0), np.float32(18.5), np.float32(19.0), np.float32(19.5), np.float32(21.0), np.float32(21.5),
          np.float32(22.0), np.float32(22.5), np.float32(23.0), np.float32(23.5),
          np.float32(24.0), np.float32(26.0), np.float32(28.0), np.float32(30.0), np.float32(32.0), np.float32(34.0),
          np.float32(36.0), np.float32(38.0), np.float32(40.0), np.float32(45.0),
          np.float32(50.0), np.float32(55.0), np.float32(60.0), np.float32(65.0), np.float32(70.0), np.float32(75.0),
          np.float32(80.0), np.float32(85.0), np.float32(90.0), np.float32(95.0),
          np.float32(100.), np.float32(105.), np.float32(110.), np.float32(115.), np.float32(120.), np.float32(125.),
          np.float32(130.), np.float32(135.), np.float32(140.), np.float32(145.),
          np.float32(150.), np.float32(160.), np.float32(180.), np.float32(200.), np.float32(250.), np.float32(300.),
          np.float32(350.), np.float32(400.), np.float32(450.), np.float32(500.),
          np.float32(550.), np.float32(600.), np.float32(650.), np.float32(700.), np.float32(750.), np.float32(800.),
          np.float32(850.), np.float32(900.), np.float32(950.), np.float32(1000.),
          ]
# GROSS IONISATION  WEIGHTED AVERAGE OF: RAP AND ENGLANDER,

#                LINDSAY AND STEBBINGS, AND NISHIMURA

YIONG8 = [np.float32(0.00), np.float32(.035), np.float32(.075), np.float32(.132), np.float32(.201), np.float32(.282),
          np.float32(.366), np.float32(.451), np.float32(.538), np.float32(.625),
          np.float32(.715), np.float32(.803), np.float32(.892), np.float32(.990), np.float32(1.26), np.float32(1.36),
          np.float32(1.44), np.float32(1.52), np.float32(1.60), np.float32(1.68),
          np.float32(1.75), np.float32(2.00), np.float32(2.23), np.float32(2.41), np.float32(2.58), np.float32(2.72),
          np.float32(2.83), np.float32(2.95), np.float32(3.06), np.float32(3.25),
          np.float32(3.41), np.float32(3.52), np.float32(3.61), np.float32(3.66), np.float32(3.71), np.float32(3.73),
          np.float32(3.74), np.float32(3.75), np.float32(3.74), np.float32(3.73),
          np.float32(3.71), np.float32(3.68), np.float32(3.66), np.float32(3.63), np.float32(3.60), np.float32(3.57),
          np.float32(3.53), np.float32(3.50), np.float32(3.46), np.float32(3.42),
          np.float32(3.36), np.float32(3.27), np.float32(3.12), np.float32(3.00), np.float32(2.69), np.float32(2.40),
          np.float32(2.22), np.float32(2.04), np.float32(1.88), np.float32(1.74),
          np.float32(1.64), np.float32(1.53), np.float32(1.44), np.float32(1.36), np.float32(1.30), np.float32(1.25),
          np.float32(1.19), np.float32(1.15), np.float32(1.10), np.float32(1.053),
          ]
# COUNTING IONISATION

YINCG8 = [np.float32(0.00), np.float32(.035), np.float32(.075), np.float32(.132), np.float32(.201), np.float32(.282),
          np.float32(.366), np.float32(.451), np.float32(.538), np.float32(.625),
          np.float32(.715), np.float32(.803), np.float32(.892), np.float32(.990), np.float32(1.26), np.float32(1.36),
          np.float32(1.44), np.float32(1.52), np.float32(1.60), np.float32(1.68),
          np.float32(1.75), np.float32(2.00), np.float32(2.22), np.float32(2.40), np.float32(2.57), np.float32(2.71),
          np.float32(2.82), np.float32(2.93), np.float32(3.04), np.float32(3.23),
          np.float32(3.38), np.float32(3.49), np.float32(3.57), np.float32(3.62), np.float32(3.67), np.float32(3.69),
          np.float32(3.70), np.float32(3.71), np.float32(3.70), np.float32(3.69),
          np.float32(3.67), np.float32(3.64), np.float32(3.62), np.float32(3.59), np.float32(3.56), np.float32(3.53),
          np.float32(3.49), np.float32(3.46), np.float32(3.43), np.float32(3.39),
          np.float32(3.33), np.float32(3.24), np.float32(3.09), np.float32(2.97), np.float32(2.66), np.float32(2.38),
          np.float32(2.20), np.float32(2.02), np.float32(1.86), np.float32(1.72),
          np.float32(1.62), np.float32(1.52), np.float32(1.43), np.float32(1.35), np.float32(1.29), np.float32(1.24),
          np.float32(1.18), np.float32(1.14), np.float32(1.09), np.float32(1.042),
          ]
# IONISATION TO DOUBLE CHARGE FINAL STATES

XINPPG8 = [np.float32(27.0), np.float32(28.0), np.float32(30.0), np.float32(32.0), np.float32(34.0), np.float32(36.0),
           np.float32(38.0), np.float32(40.0), np.float32(45.0),
           np.float32(50.0), np.float32(55.0), np.float32(60.0), np.float32(65.0), np.float32(70.0), np.float32(75.0),
           np.float32(80.0), np.float32(85.0), np.float32(90.0), np.float32(95.0),
           np.float32(100.), np.float32(105.), np.float32(110.), np.float32(115.), np.float32(120.), np.float32(125.),
           np.float32(130.), np.float32(135.), np.float32(140.), np.float32(145.),
           np.float32(150.), np.float32(160.), np.float32(180.), np.float32(200.), np.float32(250.), np.float32(300.),
           np.float32(350.), np.float32(400.), np.float32(450.), np.float32(500.),
           np.float32(550.), np.float32(600.), np.float32(650.), np.float32(700.), np.float32(750.), np.float32(800.),
           np.float32(850.), np.float32(900.), np.float32(950.), np.float32(1000.),
           ]
YINPPG8 = [np.float32(0.00), np.float32(.005), np.float32(.005), np.float32(.005), np.float32(.005), np.float32(.005),
           np.float32(0.01), np.float32(0.01), np.float32(0.01),
           np.float32(.015), np.float32(.015), np.float32(0.02), np.float32(0.02), np.float32(0.02), np.float32(0.02),
           np.float32(0.02), np.float32(0.02), np.float32(0.02), np.float32(0.02),
           np.float32(0.02), np.float32(0.02), np.float32(0.02), np.float32(0.02), np.float32(0.02), np.float32(0.02),
           np.float32(0.02), np.float32(0.02), np.float32(.015), np.float32(.015),
           np.float32(.015), np.float32(.015), np.float32(.015), np.float32(.015), np.float32(.015), np.float32(0.01),
           np.float32(0.01), np.float32(0.01), np.float32(0.01), np.float32(0.01),
           np.float32(0.01), np.float32(0.01), np.float32(0.01), np.float32(0.01), np.float32(0.01), np.float32(0.01),
           np.float32(0.01), np.float32(0.01), np.float32(0.01), np.float32(0.01),
           ]
# IONISATION TO CH4 +

XINFG8 = [np.float32(12.65), np.float32(13.5), np.float32(14.0), np.float32(14.5), np.float32(15.0), np.float32(15.5),
          np.float32(16.0), np.float32(16.5), np.float32(17.0), np.float32(17.5),
          np.float32(18.0), np.float32(18.5), np.float32(19.0), np.float32(19.5), np.float32(21.0), np.float32(21.5),
          np.float32(22.0), np.float32(22.5), np.float32(23.0), np.float32(23.5),
          np.float32(24.0), np.float32(26.0), np.float32(28.0), np.float32(30.0), np.float32(32.0), np.float32(34.0),
          np.float32(36.0), np.float32(38.0), np.float32(40.0), np.float32(45.0),
          np.float32(50.0), np.float32(55.0), np.float32(60.0), np.float32(65.0), np.float32(70.0), np.float32(75.0),
          np.float32(80.0), np.float32(85.0), np.float32(90.0), np.float32(95.0),
          np.float32(100.), np.float32(105.), np.float32(110.), np.float32(115.), np.float32(120.), np.float32(125.),
          np.float32(130.), np.float32(135.), np.float32(140.), np.float32(145.),
          np.float32(150.), np.float32(160.), np.float32(180.), np.float32(200.), np.float32(250.), np.float32(300.),
          np.float32(350.), np.float32(400.), np.float32(450.), np.float32(500.),
          np.float32(550.), np.float32(600.), np.float32(650.), np.float32(700.), np.float32(750.), np.float32(800.),
          np.float32(850.), np.float32(900.), np.float32(950.), np.float32(1000.),
          ]
YINFG8 = [np.float32(0.0), np.float32(.035), np.float32(.075), np.float32(.119), np.float32(.169), np.float32(.228),
          np.float32(.284), np.float32(.335), np.float32(.383), np.float32(.425),
          np.float32(.479), np.float32(.529), np.float32(.579), np.float32(.632), np.float32(.773), np.float32(.824),
          np.float32(.862), np.float32(.899), np.float32(.938), np.float32(.976),
          np.float32(1.008), np.float32(1.114), np.float32(1.199), np.float32(1.254), np.float32(1.308),
          np.float32(1.342), np.float32(1.363), np.float32(1.389), np.float32(1.412), np.float32(1.443),
          np.float32(1.477), np.float32(1.497), np.float32(1.502), np.float32(1.508), np.float32(1.514),
          np.float32(1.514), np.float32(1.510), np.float32(1.508), np.float32(1.499), np.float32(1.494),
          np.float32(1.485), np.float32(1.470), np.float32(1.459), np.float32(1.446), np.float32(1.434),
          np.float32(1.422), np.float32(1.409), np.float32(1.401), np.float32(1.392), np.float32(1.380),
          np.float32(1.359), np.float32(1.325), np.float32(1.269), np.float32(1.227), np.float32(1.119),
          np.float32(1.016), np.float32(.9535), np.float32(.8886), np.float32(.8206), np.float32(.7609),
          np.float32(.7199), np.float32(.6785), np.float32(.6419), np.float32(.6094), np.float32(.5824),
          np.float32(.5599), np.float32(.5355), np.float32(.5200), np.float32(.4990), np.float32(.4787),
          ]
# IONISATION TO CH3 +

XINF1G8 = [np.float32(14.25), np.float32(14.5), np.float32(15.0), np.float32(15.5), np.float32(16.0), np.float32(16.5),
           np.float32(17.0), np.float32(17.5),
           np.float32(18.0), np.float32(18.5), np.float32(19.0), np.float32(19.5), np.float32(21.0), np.float32(21.5),
           np.float32(22.0), np.float32(22.5), np.float32(23.0), np.float32(23.5),
           np.float32(24.0), np.float32(26.0), np.float32(28.0), np.float32(30.0), np.float32(32.0), np.float32(34.0),
           np.float32(36.0), np.float32(38.0), np.float32(40.0), np.float32(45.0),
           np.float32(50.0), np.float32(55.0), np.float32(60.0), np.float32(65.0), np.float32(70.0), np.float32(75.0),
           np.float32(80.0), np.float32(85.0), np.float32(90.0), np.float32(95.0),
           np.float32(100.), np.float32(105.), np.float32(110.), np.float32(115.), np.float32(120.), np.float32(125.),
           np.float32(130.), np.float32(135.), np.float32(140.), np.float32(145.),
           np.float32(150.), np.float32(160.), np.float32(180.), np.float32(200.), np.float32(250.), np.float32(300.),
           np.float32(350.), np.float32(400.), np.float32(450.), np.float32(500.),
           np.float32(550.), np.float32(600.), np.float32(650.), np.float32(700.), np.float32(750.), np.float32(800.),
           np.float32(850.), np.float32(900.), np.float32(950.), np.float32(1000.),
           ]
YINF1G8 = [np.float32(0.0), np.float32(.013), np.float32(.032), np.float32(.054), np.float32(.081), np.float32(.114),
           np.float32(.152), np.float32(.195),
           np.float32(.230), np.float32(.267), np.float32(.304), np.float32(.347), np.float32(.471), np.float32(.517),
           np.float32(.557), np.float32(.598), np.float32(.633), np.float32(.668),
           np.float32(.700), np.float32(.808), np.float32(.896), np.float32(.968), np.float32(1.017), np.float32(1.052),
           np.float32(1.073), np.float32(1.092), np.float32(1.110), np.float32(1.145),
           np.float32(1.178), np.float32(1.205), np.float32(1.221), np.float32(1.227), np.float32(1.233),
           np.float32(1.232), np.float32(1.227), np.float32(1.230), np.float32(1.226), np.float32(1.220),
           np.float32(1.211), np.float32(1.201), np.float32(1.194), np.float32(1.188), np.float32(1.181),
           np.float32(1.175), np.float32(1.163), np.float32(1.153), np.float32(1.144), np.float32(1.132),
           np.float32(1.113), np.float32(1.088), np.float32(1.047), np.float32(1.011), np.float32(.9249),
           np.float32(.8351), np.float32(.7766), np.float32(.7171), np.float32(.6676), np.float32(.6240),
           np.float32(.5890), np.float32(.5539), np.float32(.5237), np.float32(.4968), np.float32(.4769),
           np.float32(.4605), np.float32(.4381), np.float32(.4232), np.float32(.4048), np.float32(.3872),
           ]
# IONISATION TO CH2 +

XINF2G8 = [np.float32(15.2), np.float32(15.5), np.float32(16.0), np.float32(16.5), np.float32(17.0), np.float32(17.5),
           np.float32(18.0), np.float32(18.5), np.float32(19.0), np.float32(19.5), np.float32(21.0), np.float32(21.5),
           np.float32(22.0), np.float32(22.5), np.float32(23.0), np.float32(23.5),
           np.float32(24.0), np.float32(26.0), np.float32(28.0), np.float32(30.0), np.float32(32.0), np.float32(34.0),
           np.float32(36.0), np.float32(38.0), np.float32(40.0), np.float32(45.0),
           np.float32(50.0), np.float32(55.0), np.float32(60.0), np.float32(65.0), np.float32(70.0), np.float32(75.0),
           np.float32(80.0), np.float32(85.0), np.float32(90.0), np.float32(95.0),
           np.float32(100.), np.float32(105.), np.float32(110.), np.float32(115.), np.float32(120.), np.float32(125.),
           np.float32(130.), np.float32(135.), np.float32(140.), np.float32(145.),
           np.float32(150.), np.float32(160.), np.float32(180.), np.float32(200.), np.float32(250.), np.float32(300.),
           np.float32(350.), np.float32(400.), np.float32(450.), np.float32(500.),
           np.float32(550.), np.float32(600.), np.float32(650.), np.float32(700.), np.float32(750.), np.float32(800.),
           np.float32(850.), np.float32(900.), np.float32(950.), np.float32(1000.),
           ]
YINF2G8 = [np.float32(0.0), np.float32(.0004), np.float32(.0010), np.float32(.0019), np.float32(.0030),
           np.float32(.0044),
           np.float32(.0058), np.float32(.0073), np.float32(.0089), np.float32(.0108), np.float32(.0166),
           np.float32(.0189), np.float32(.0209), np.float32(.0231), np.float32(.0273), np.float32(.0318),
           np.float32(.0363), np.float32(.0593), np.float32(.0888), np.float32(.1208), np.float32(.1499),
           np.float32(.1797), np.float32(.2034), np.float32(.2220), np.float32(.2415), np.float32(.2684),
           np.float32(.2781), np.float32(.2866), np.float32(.2926), np.float32(.2953), np.float32(.2980),
           np.float32(.3008), np.float32(.3029), np.float32(.3001), np.float32(.2958), np.float32(.2968),
           np.float32(.2969), np.float32(.2949), np.float32(.2937), np.float32(.2902), np.float32(.2868),
           np.float32(.2834), np.float32(.2790), np.float32(.2755), np.float32(.2720), np.float32(.2677),
           np.float32(.2619), np.float32(.2528), np.float32(.2381), np.float32(.2286), np.float32(.1971),
           np.float32(.1729), np.float32(.1554), np.float32(.1386), np.float32(.1268), np.float32(.1164),
           np.float32(.1091), np.float32(.1019), np.float32(.0942), np.float32(.0874), np.float32(.0839),
           np.float32(.0809), np.float32(.0764), np.float32(.0732), np.float32(.0694), np.float32(.0658),
           ]
# IONISATION TO H +

XINF3G8 = [np.float32(22.2), np.float32(23.0), np.float32(23.5),
           np.float32(24.0), np.float32(26.0), np.float32(28.0), np.float32(30.0), np.float32(32.0), np.float32(34.0),
           np.float32(36.0), np.float32(38.0), np.float32(40.0), np.float32(45.0),
           np.float32(50.0), np.float32(55.0), np.float32(60.0), np.float32(65.0), np.float32(70.0), np.float32(75.0),
           np.float32(80.0), np.float32(85.0), np.float32(90.0), np.float32(95.0),
           np.float32(100.), np.float32(105.), np.float32(110.), np.float32(115.), np.float32(120.), np.float32(125.),
           np.float32(130.), np.float32(135.), np.float32(140.), np.float32(145.),
           np.float32(150.), np.float32(160.), np.float32(180.), np.float32(200.), np.float32(250.), np.float32(300.),
           np.float32(350.), np.float32(400.), np.float32(450.), np.float32(500.),
           np.float32(550.), np.float32(600.), np.float32(650.), np.float32(700.), np.float32(750.), np.float32(800.),
           np.float32(850.), np.float32(900.), np.float32(950.), np.float32(1000.),
           ]
YINF3G8 = [np.float32(0.0), np.float32(.00104), np.float32(.00218),
           np.float32(.00341), np.float32(.00962), np.float32(.0176), np.float32(.0265), np.float32(.0419),
           np.float32(.0585), np.float32(.0782), np.float32(.1016), np.float32(.1266), np.float32(.1885),
           np.float32(.2404), np.float32(.2799), np.float32(.3187), np.float32(.3435), np.float32(.3688),
           np.float32(.3845), np.float32(.3992), np.float32(.4088), np.float32(.4166), np.float32(.4188),
           np.float32(.4198), np.float32(.4193), np.float32(.4200), np.float32(.4154), np.float32(.4112),
           np.float32(.4067), np.float32(.4003), np.float32(.3951), np.float32(.3896), np.float32(.3834),
           np.float32(.3750), np.float32(.3622), np.float32(.3405), np.float32(.3219), np.float32(.2655),
           np.float32(.2247), np.float32(.2000), np.float32(.1765), np.float32(.1570), np.float32(.1398),
           np.float32(.1291), np.float32(.1187), np.float32(.1083), np.float32(.0990), np.float32(.0933),
           np.float32(.0883), np.float32(.0824), np.float32(.0780), np.float32(.0735), np.float32(.0692),
           ]
# IONISATION TO CH+ NOTE THRESHOLD INCREASED FROM 22.3 DUE TO EXC. STATE

XINF4G8 = [np.float32(23.5),
           np.float32(24.0), np.float32(26.0), np.float32(28.0), np.float32(30.0), np.float32(32.0), np.float32(34.0),
           np.float32(36.0), np.float32(38.0), np.float32(40.0), np.float32(45.0),
           np.float32(50.0), np.float32(55.0), np.float32(60.0), np.float32(65.0), np.float32(70.0), np.float32(75.0),
           np.float32(80.0), np.float32(85.0), np.float32(90.0), np.float32(95.0),
           np.float32(100.), np.float32(105.), np.float32(110.), np.float32(115.), np.float32(120.), np.float32(125.),
           np.float32(130.), np.float32(135.), np.float32(140.), np.float32(145.),
           np.float32(150.), np.float32(160.), np.float32(180.), np.float32(200.), np.float32(250.), np.float32(300.),
           np.float32(350.), np.float32(400.), np.float32(450.), np.float32(500.),
           np.float32(550.), np.float32(600.), np.float32(650.), np.float32(700.), np.float32(750.), np.float32(800.),
           np.float32(850.), np.float32(900.), np.float32(950.), np.float32(1000.),
           ]
YINF4G8 = [np.float32(0.0),
           np.float32(.00112), np.float32(.00758), np.float32(.0166), np.float32(.0269), np.float32(.0438),
           np.float32(.0621), np.float32(.0785), np.float32(.0933), np.float32(.1090), np.float32(.1308),
           np.float32(.1391), np.float32(.1490), np.float32(.1579), np.float32(.1629), np.float32(.1679),
           np.float32(.1680), np.float32(.1675), np.float32(.1689), np.float32(.1693), np.float32(.1665),
           np.float32(.1631), np.float32(.1611), np.float32(.1596), np.float32(.1570), np.float32(.1545),
           np.float32(.1520), np.float32(.1491), np.float32(.1467), np.float32(.1443), np.float32(.1415),
           np.float32(.1378), np.float32(.1320), np.float32(.1220), np.float32(.1138), np.float32(.0971),
           np.float32(.0824), np.float32(.0730), np.float32(.0641), np.float32(.0573), np.float32(.0513),
           np.float32(.0471), np.float32(.0430), np.float32(.0399), np.float32(.0370), np.float32(.0349),
           np.float32(.0332), np.float32(.0315), np.float32(.0304), np.float32(.0289), np.float32(.0274),
           ]
# IONISATION TO C +

XINF5G8 = [np.float32(25.2), np.float32(26.0), np.float32(28.0), np.float32(30.0), np.float32(32.0), np.float32(34.0),
           np.float32(36.0), np.float32(38.0), np.float32(40.0), np.float32(45.0),
           np.float32(50.0), np.float32(55.0), np.float32(60.0), np.float32(65.0), np.float32(70.0), np.float32(75.0),
           np.float32(80.0), np.float32(85.0), np.float32(90.0), np.float32(95.0),
           np.float32(100.), np.float32(105.), np.float32(110.), np.float32(115.), np.float32(120.), np.float32(125.),
           np.float32(130.), np.float32(135.), np.float32(140.), np.float32(145.),
           np.float32(150.), np.float32(160.), np.float32(180.), np.float32(200.), np.float32(250.), np.float32(300.),
           np.float32(350.), np.float32(400.), np.float32(450.), np.float32(500.),
           np.float32(550.), np.float32(600.), np.float32(650.), np.float32(700.), np.float32(750.), np.float32(800.),
           np.float32(850.), np.float32(900.), np.float32(950.), np.float32(1000.),
           ]
YINF5G8 = [np.float32(0.0), np.float32(.00092), np.float32(.0018), np.float32(.0028), np.float32(.0068),
           np.float32(.0112), np.float32(.0160), np.float32(.0212), np.float32(.0267),
           np.float32(.0331),
           np.float32(.0412), np.float32(.0446), np.float32(.0477), np.float32(.0508), np.float32(.0539),
           np.float32(.0561), np.float32(.0581), np.float32(.0581), np.float32(.0578), np.float32(.0579),
           np.float32(.0578), np.float32(.0581), np.float32(.0585), np.float32(.0581), np.float32(.0576),
           np.float32(.0571), np.float32(.0561), np.float32(.0553), np.float32(.0546), np.float32(.0536),
           np.float32(.0524), np.float32(.0501), np.float32(.0463), np.float32(.0436), np.float32(.0352),
           np.float32(.0303), np.float32(.0256), np.float32(.0213), np.float32(.0188), np.float32(.0166),
           np.float32(.0154), np.float32(.0142), np.float32(.0131), np.float32(.0122), np.float32(.0106),
           np.float32(.0099), np.float32(.0095), np.float32(.0093), np.float32(.0088), np.float32(.0083),
           ]
# IONISATION TO H2 +

XINF6G8 = [np.float32(27.9), np.float32(30.0), np.float32(32.0), np.float32(34.0), np.float32(36.0), np.float32(38.0),
           np.float32(40.0), np.float32(45.0),
           np.float32(50.0), np.float32(55.0), np.float32(60.0), np.float32(65.0), np.float32(70.0), np.float32(75.0),
           np.float32(80.0), np.float32(85.0), np.float32(90.0), np.float32(95.0),
           np.float32(100.), np.float32(105.), np.float32(110.), np.float32(115.), np.float32(120.), np.float32(125.),
           np.float32(130.), np.float32(135.), np.float32(140.), np.float32(145.),
           np.float32(150.), np.float32(160.), np.float32(180.), np.float32(200.), np.float32(250.), np.float32(300.),
           np.float32(350.), np.float32(400.), np.float32(450.), np.float32(500.),
           np.float32(550.), np.float32(600.), np.float32(650.), np.float32(700.), np.float32(750.), np.float32(800.),
           np.float32(850.), np.float32(900.), np.float32(950.), np.float32(1000.),
           ]
YINF6G8 = [np.float32(0.0),
           np.float32(.0010), np.float32(.0028), np.float32(.0047), np.float32(.0074), np.float32(.0109),
           np.float32(.0146), np.float32(.0214),
           np.float32(.0259), np.float32(.0286), np.float32(.0311), np.float32(.0326), np.float32(.0342),
           np.float32(.0349), np.float32(.0354), np.float32(.0359), np.float32(.0361), np.float32(.0361),
           np.float32(.0360), np.float32(.0356), np.float32(.0352), np.float32(.0348), np.float32(.0344),
           np.float32(.0341), np.float32(.0336), np.float32(.0332), np.float32(.0328), np.float32(.0324),
           np.float32(.0317), np.float32(.0300), np.float32(.0272), np.float32(.0248), np.float32(.0212),
           np.float32(.0185), np.float32(.0160), np.float32(.0138), np.float32(.0122), np.float32(.0109),
           np.float32(.0103), np.float32(.0098), np.float32(.0089), np.float32(.0082), np.float32(.0077),
           np.float32(.0073), np.float32(.0065), np.float32(.0059), np.float32(.0057), np.float32(.0054),
           ]
# K-SHELL IONISATION X-SECTION CARBON

XKSHG8 = [np.float32(285.), np.float32(298.), np.float32(307.), np.float32(316.), np.float32(325.), np.float32(335.),
          np.float32(345.), np.float32(365.), np.float32(398.), np.float32(422.),
          np.float32(447.), np.float32(473.), np.float32(501.), np.float32(531.), np.float32(613.), np.float32(668.),
          np.float32(708.), np.float32(750.), np.float32(817.), np.float32(917.),
          np.float32(1000.), np.float32(1122.), np.float32(1296.), np.float32(1496.), np.float32(1679.),
          np.float32(1884.), np.float32(2054.), np.float32(2238.), np.float32(2512.), np.float32(2985.),
          np.float32(3981.), np.float32(5012.), np.float32(7079.), 1.0e4, 1.50e4, 2.05e4, 2.51e4, 3.07e4, 4.10e4,
          5.01e4,
          6.13e4, 7.08e4, 8.18e4, 1.0e5, 1.54e5, 2.05e5, 2.99e5, 4.10e5, 5.01e5,
          6.13e5,
          7.08e5, 8.18e5, 1.0e6, 1.26e6, 1.5e6, 2.05e6, 3.07e6, 4.10e6, 5.01e6,
          6.13e6,
          7.08e6, 8.18e6, 1.0e7, 1.26e7, 1.5e7, 2.05e7, 3.07e7, 4.10e7, 5.01e7,
          6.13e7,
          7.08e7, 8.18e7, 1.0e8, 1.26e8, 1.5e8, 2.05e8, 3.07e8, 4.10e8, 5.01e8,
          6.13e8,
          7.08e8, 8.18e8, 1.0e9,
          ]
YKSHG8 = [np.float32(0.00), 1.66e-4, 3.48e-4, 5.25e-4, 6.96e-4, 8.63e-4, 1.02e-3,
          1.33e-3, 1.75e-3, 2.01e-3,
          2.24e-3, 2.46e-3, 2.66e-3, 2.84e-3, 3.21e-3, 3.38e-3, 3.47e-3, 3.55e-3,
          3.65e-3, 3.72e-3,
          3.75e-3, 3.74e-3, 3.68e-3, 3.57e-3, 3.45e-3, 3.31e-3, 3.19e-3, 3.07e-3,
          2.91e-3, 2.66e-3,
          2.25e-3, 1.95e-3, 1.55e-3, 1.21e-3, 8.97e-4, 7.07e-4, 6.07e-4, 5.21e-4,
          4.21e-4, 3.63e-4,
          3.14e-4, 2.84e-4, 2.57e-4, 2.25e-4, 1.74e-4, 1.50e-4, 1.28e-4, 1.15e-4,
          1.09e-4, 1.05e-4,
          1.03e-4, 1.02e-4, 1.01e-4, 1.005e-4, 1.01e-4, 1.03e-4, 1.07e-4, 1.11e-4,
          1.14e-4, 1.17e-4,
          1.20e-4, 1.22e-4, 1.25e-4, 1.29e-4, 1.32e-4, 1.38e-4, 1.45e-4, 1.50e-4,
          1.54e-4, 1.58e-4,
          1.60e-4, 1.63e-4, 1.67e-4, 1.71e-4, 1.74e-4, 1.80e-4, 1.87e-4, 1.92e-4,
          1.96e-4, 2.00e-4,
          2.02e-4, 2.05e-4, 2.09e-4,
          ]
# ATTACHMENT  - DEATTACHMENT VIA H- 9.8 EV RESONANCE (RAWAT ET AL)

XDETG8 = [np.float32(7.80), np.float32(8.00), np.float32(9.00), np.float32(9.80), np.float32(10.0), np.float32(11.0),
          np.float32(12.0), np.float32(13.0), np.float32(14.0),
          ]
YDETG8 = [np.float32(0.00), np.float32(.0049), np.float32(.0134), np.float32(.0153), np.float32(.0150),
          np.float32(.0113), np.float32(.0038), np.float32(.0095), np.float32(0.00),
          ]
# ATTACHMENT  VIA CH2- ONLY (RAWAT ET AL)

XATTG8 = [np.float32(9.00), np.float32(10.0), np.float32(10.4), np.float32(11.0), np.float32(12.0), np.float32(13.0),
          ]
YATTG8 = [np.float32(0.00), np.float32(0.00092), np.float32(.00112), np.float32(.00089), np.float32(.00027),
          np.float32(0.00),
          ]
# DISSOCIATION TRIPLET + SINGLETS ( SINGLETS GIVEN ANALYTICALLY)

# TRIPLETS

XTR1G8 = [np.float32(7.50), np.float32(8.50), np.float32(10.0), np.float32(11.0), np.float32(12.0), np.float32(13.0),
          np.float32(15.0), np.float32(17.0), np.float32(20.0), np.float32(23.0),
          np.float32(27.0), np.float32(30.0),
          ]
YTR1G8 = [np.float32(0.00), np.float32(.015), np.float32(.050), np.float32(.075), np.float32(.084), np.float32(.090),
          np.float32(.098), np.float32(.100), np.float32(.090), np.float32(.075),
          np.float32(.055), np.float32(.043),
          ]
XTR2G8 = [np.float32(8.50), np.float32(10.0), np.float32(11.0), np.float32(12.0), np.float32(13.0), np.float32(15.0),
          np.float32(17.0), np.float32(20.0), np.float32(23.0), np.float32(27.0),
          np.float32(30.0),
          ]
YTR2G8 = [np.float32(0.00), np.float32(.088), np.float32(.161), np.float32(.185), np.float32(.198), np.float32(.216),
          np.float32(.220), np.float32(.198), np.float32(.165), np.float32(.121),
          np.float32(.095),
          ]
XTR3G8 = [np.float32(10.0), np.float32(11.0), np.float32(12.0), np.float32(13.0), np.float32(15.0), np.float32(17.0),
          np.float32(20.0), np.float32(23.0), np.float32(27.0), np.float32(30.0),
          np.float32(35.0),
          ]
YTR3G8 = [np.float32(0.00), np.float32(.245), np.float32(.504), np.float32(.588), np.float32(.665), np.float32(.700),
          np.float32(.700), np.float32(.665), np.float32(.525), np.float32(.406),
          np.float32(.301),
          ]
# LIGHT EMISSION FROM CH(A2DELTA TO X2PI)

XCHDG8 = [np.float32(13.4), np.float32(13.5), np.float32(14.5), np.float32(18.5), np.float32(20.6), np.float32(21.6),
          np.float32(22.5), np.float32(23.6), np.float32(27.7), np.float32(31.8),
          np.float32(33.5), np.float32(33.9), np.float32(35.4), np.float32(37.5), np.float32(39.2), np.float32(40.0),
          np.float32(44.0), np.float32(49.1), np.float32(55.6), np.float32(58.3),
          np.float32(60.1), np.float32(63.2), np.float32(67.0), np.float32(71.3), np.float32(76.3), np.float32(80.3),
          np.float32(100.), np.float32(150.), np.float32(200.), np.float32(400.),
          np.float32(700.), np.float32(1000.),
          ]
YCHDG8 = [np.float32(0.00), np.float32(.0041), np.float32(.0065), np.float32(.0116), np.float32(.0169),
          np.float32(.0205), np.float32(.0232), np.float32(.0261), np.float32(.0299),
          np.float32(.0327),
          np.float32(.0339), np.float32(.0355), np.float32(.0363), np.float32(.0392), np.float32(.0411),
          np.float32(.0441), np.float32(.0462), np.float32(.0469), np.float32(.0476), np.float32(.0479),
          np.float32(.0481), np.float32(.0485), np.float32(.0489), np.float32(.0491), np.float32(.0487),
          np.float32(.0477), np.float32(.0403), np.float32(.0292), np.float32(.0232), np.float32(.0131),
          np.float32(.0082), np.float32(.0060),
          ]
# LIGHT EMISSION FROM CH(B2SIGMA- TO X2PI)

XCHBG8 = [np.float32(13.7), np.float32(13.8), np.float32(14.8), np.float32(18.8), np.float32(20.9), np.float32(21.9),
          np.float32(22.8), np.float32(23.9), np.float32(28.0), np.float32(32.1),
          np.float32(33.8), np.float32(34.2), np.float32(35.7), np.float32(37.8), np.float32(39.5), np.float32(42.1),
          np.float32(43.4), np.float32(44.3), np.float32(49.4), np.float32(56.0),
          np.float32(58.6), np.float32(60.4), np.float32(63.5), np.float32(67.3), np.float32(71.6), np.float32(76.6),
          np.float32(80.6), np.float32(100.), np.float32(150.), np.float32(200.),
          np.float32(400.), np.float32(700.), np.float32(1000.), np.float32(1500.), np.float32(2000.),
          ]
YCHBG8 = [np.float32(0.00), 2.44e-4, 3.91e-4, 6.96e-4, np.float32(.00102), np.float32(.00123), np.float32(.0014),
          np.float32(.00157),
          np.float32(.0018), np.float32(.00197),
          np.float32(.00204), np.float32(.00214), np.float32(.00219), np.float32(.00236), np.float32(.00248),
          np.float32(.00259), np.float32(.00265), np.float32(.00278), np.float32(.00283),
          np.float32(.00286),
          np.float32(.00289), np.float32(.00290), np.float32(.00292), np.float32(.00295), np.float32(.00296),
          np.float32(.00293), np.float32(.00287), np.float32(.00242), np.float32(.00176),
          np.float32(.00139),
          7.88e-4, 4.93e-4, 3.63e-4, 2.57e-4, 2.00e-4,
          ]
# LIGHT EMISSION FROM H(ALPHA)

XHALG8 = [np.float32(16.14), np.float32(16.3), np.float32(16.6), np.float32(16.9), np.float32(17.2), np.float32(18.1),
          np.float32(19.2), np.float32(20.0), np.float32(20.8), np.float32(22.6),
          np.float32(25.2), np.float32(30.0), np.float32(40.0), np.float32(50.0), np.float32(60.0), np.float32(70.0),
          np.float32(80.0), np.float32(90.0), np.float32(100.), np.float32(144.),
          np.float32(185.), np.float32(200.), np.float32(224.), np.float32(245.), np.float32(284.), np.float32(364.),
          np.float32(453.), np.float32(500.), np.float32(600.), np.float32(700.),
          np.float32(800.), np.float32(1000.), np.float32(1500.), np.float32(2000.),
          ]
YHALG8 = [np.float32(0.00), 2.54e-4, 3.80e-4, 5.05e-4, 6.60e-4, np.float32(.00101), np.float32(.00142),
          np.float32(.00175), np.float32(.00209), np.float32(.00288),
          np.float32(.00431), np.float32(.00686), np.float32(.01225), np.float32(.0156), np.float32(.0181),
          np.float32(.0195), np.float32(.0204), np.float32(.0203), np.float32(.0200), np.float32(.0181),
          np.float32(.0148), np.float32(.0134), np.float32(.0127), np.float32(.0119), np.float32(.0103),
          np.float32(.00789), np.float32(.00598), np.float32(.00529), np.float32(.00425), np.float32(.00357),
          np.float32(.00309), np.float32(.00227), np.float32(.0016), np.float32(.00125),
          ]
# LIGHT EMISSION FROM H(BETA)

XHBEG8 = [np.float32(16.8), np.float32(18.0), np.float32(21.9), np.float32(23.4), np.float32(24.5), np.float32(25.5),
          np.float32(26.4), np.float32(28.2), np.float32(30.0), np.float32(33.7),
          np.float32(37.2), np.float32(40.0), np.float32(50.0), np.float32(57.7), np.float32(80.0), np.float32(100.),
          np.float32(141.), np.float32(169.), np.float32(200.), np.float32(226.),
          np.float32(247.), np.float32(284.), np.float32(340.), np.float32(363.), np.float32(398.), np.float32(455.),
          np.float32(500.), np.float32(550.), np.float32(654.), np.float32(700.),
          np.float32(800.), np.float32(999.), np.float32(1500.), np.float32(2000.),
          ]
YHBEG8 = [np.float32(0.00), 1.53e-4, 5.44e-4, 7.19e-4, 8.85e-4, np.float32(.00114), np.float32(.00128),
          np.float32(.00159), np.float32(.00194), np.float32(.00228),
          np.float32(.00269), np.float32(.00316), np.float32(.00374), np.float32(.00419), np.float32(.00481),
          np.float32(.00463), np.float32(.00419), np.float32(.00374), np.float32(.00314),
          np.float32(.00288),
          np.float32(.00269), np.float32(.00227), np.float32(.00194), np.float32(.00179), np.float32(.00160),
          np.float32(.00140), np.float32(.00128), np.float32(.00114), 9.5e-4,
          8.85e-4,
          7.19e-4, 5.45e-4, 3.84e-4, 3.00e-4,
          ]
# BREMSSTRAHLUNG X-SECTION WITH CUT UNITS 10**-24

Z1TG8 = [np.float32(11.3), np.float32(6.18), np.float32(2.80), np.float32(1.54), np.float32(.858), np.float32(.407),
         np.float32(.251), np.float32(.176), np.float32(.145), np.float32(.150),
         np.float32(.167), np.float32(.178), np.float32(.187), np.float32(.193), np.float32(.198), np.float32(.205),
         np.float32(.210), np.float32(.218), np.float32(.222), np.float32(.228),
         np.float32(.231), np.float32(.233), np.float32(.234), np.float32(.235), np.float32(.235),
         ]
Z6TG8 = [np.float32(298.), np.float32(178.), np.float32(85.2), np.float32(47.5), np.float32(26.3), np.float32(12.2),
         np.float32(7.06), np.float32(4.45), np.float32(3.06), np.float32(2.82),
         np.float32(2.89), np.float32(2.99), np.float32(3.08), np.float32(3.13), np.float32(3.18), np.float32(3.25),
         np.float32(3.31), np.float32(3.39), np.float32(3.44), np.float32(3.49),
         np.float32(3.52), np.float32(3.54), np.float32(3.55), np.float32(3.57), np.float32(3.57),
         ]
EBRMG8 = [np.float32(1000.), np.float32(2000.), np.float32(5000.), np.float32(1.E4), np.float32(2.E4), np.float32(5.E4),
          np.float32(1.E5), np.float32(2.E5), np.float32(5.E5), np.float32(1.E6),
          np.float32(2.E6), np.float32(3.E6), np.float32(4.E6), np.float32(5.E6), np.float32(6.E6), np.float32(8.E6),
          np.float32(1.E7), np.float32(1.5E7), np.float32(2.E7), np.float32(3.E7),
          np.float32(4.E7), np.float32(5.E7), np.float32(6.E7), np.float32(8.E7), np.float32(1.E8),
          ]

EING8 = [np.float32(-0.1625135), np.float32(0.1625135), np.float32(-0.1901087), np.float32(0.1901087),
         np.float32(0.3615974), np.float32(0.3743690), np.float32(0.544), np.float32(0.736), np.float32(7.50),
         np.float32(7.80), np.float32(8.50), np.float32(8.75), np.float32(9.25), np.float32(9.75), np.float32(10.0),
         np.float32(10.25), np.float32(10.75), np.float32(11.25), np.float32(11.75), np.float32(12.25),
         np.float32(12.75), np.float32(13.25), np.float32(13.4), np.float32(13.7), np.float32(13.75), np.float32(14.25),
         np.float32(14.75), np.float32(15.25), np.float32(15.75), np.float32(16.0), np.float32(16.14), np.float32(16.8),
         np.float32(20.5), np.float32(22.0), np.float32(0.0), np.float32(0.0)]
for i in range(0, 250 - 36):
    EING8.append(0.0)
gd['gas8/XEN'] = XENG8
gd['gas8/YELM'] = YELMG8
gd['gas8/YELT'] = YELTG8
gd['gas8/YEPS'] = YEPSG8
gd['gas8/XATT'] = XATTG8
gd['gas8/YATT'] = YATTG8
gd['gas8/XVBV4'] = XVBV4G8
gd['gas8/YVBV4'] = YVBV4G8
gd['gas8/XVBV2'] = XVBV2G8
gd['gas8/YVBV2'] = YVBV2G8
gd['gas8/XVBV1'] = XVBV1G8
gd['gas8/YVBV1'] = YVBV1G8
gd['gas8/XVBV3'] = XVBV3G8
gd['gas8/YVBV3'] = YVBV3G8
gd['gas8/XVBH1'] = XVBH1G8
gd['gas8/YVBH1'] = YVBH1G8
gd['gas8/XVBH2'] = XVBH2G8
gd['gas8/YVBH2'] = YVBH2G8
gd['gas8/XION'] = XIONG8
gd['gas8/YION'] = YIONG8
gd['gas8/YINC'] = YINCG8
gd['gas8/XINF'] = XINFG8
gd['gas8/YINF'] = YINFG8
gd['gas8/XINF1'] = XINF1G8
gd['gas8/YINF1'] = YINF1G8
gd['gas8/XINF2'] = XINF2G8
gd['gas8/YINF2'] = YINF2G8
gd['gas8/XINF3'] = XINF3G8
gd['gas8/YINF3'] = YINF3G8
gd['gas8/XINF4'] = XINF4G8
gd['gas8/YINF4'] = YINF4G8
gd['gas8/XINF5'] = XINF5G8
gd['gas8/YINF5'] = YINF5G8
gd['gas8/XINF6'] = XINF6G8
gd['gas8/YINF6'] = YINF6G8
gd['gas8/XINPP'] = XINPPG8
gd['gas8/YINPP'] = YINPPG8
gd['gas8/XDET'] = XDETG8
gd['gas8/YDET'] = YDETG8
gd['gas8/XTR1'] = XTR1G8
gd['gas8/YTR1'] = YTR1G8
gd['gas8/XTR2'] = XTR2G8
gd['gas8/YTR2'] = YTR2G8
gd['gas8/XTR3'] = XTR3G8
gd['gas8/YTR3'] = YTR3G8
gd['gas8/XCHD'] = XCHDG8
gd['gas8/YCHD'] = YCHDG8
gd['gas8/XCHB'] = XCHBG8
gd['gas8/YCHB'] = YCHBG8
gd['gas8/XHAL'] = XHALG8
gd['gas8/YHAL'] = YHALG8
gd['gas8/XHBE'] = XHBEG8
gd['gas8/YHBE'] = YHBEG8
gd['gas8/XKSH'] = XKSHG8
gd['gas8/YKSH'] = YKSHG8
gd['gas8/Z1T'] = Z1TG8
gd['gas8/Z6T'] = Z6TG8
gd['gas8/EBRM'] = EBRMG8
gd['gas8/EIN'] = EING8
# ELASTIC MOMENTUM TRANSFER

XENG5 = [np.float32(1.00), np.float32(1.20), np.float32(1.50), np.float32(1.80), np.float32(2.00), np.float32(2.50),
         np.float32(3.00), np.float32(4.00), np.float32(5.00), np.float32(6.00),
         np.float32(7.00), np.float32(8.00), np.float32(8.71), np.float32(9.00), np.float32(10.0), np.float32(11.0),
         np.float32(13.6), np.float32(15.0), np.float32(16.5), np.float32(19.6),
         np.float32(20.0), np.float32(30.0), np.float32(40.0), np.float32(50.0), np.float32(60.0), np.float32(70.0),
         np.float32(77.0), np.float32(100.), np.float32(130.), np.float32(150.),
         np.float32(170.), np.float32(200.), np.float32(250.), np.float32(300.), np.float32(350.), np.float32(400.),
         np.float32(500.), np.float32(600.), np.float32(700.), np.float32(800.),
         np.float32(900.), np.float32(1000.), np.float32(1500.), np.float32(2000.), np.float32(2500.),
         np.float32(3000.), np.float32(3500.), np.float32(4000.), np.float32(5000.), np.float32(6000.),
         np.float32(7000.), np.float32(8000.), np.float32(9000.), 1.0e4, 1.5e4, 2.0e4, 2.5e4, 3.0e4, 4.0e4, 5.0e4,
         6.0e4, 7.0e4, 8.0e4, 9.0e4, 1.0e5, 1.25e5, 1.5e5, 1.75e5, 2.0e5, 2.5e5,
         3.0e5, 3.5e5, 4.0e5, 4.5e5, 5.0e5, 6.0e5, 7.0e5, 8.0e5, 9.0e5, 1.0e6,
         1.25e6, 1.5e6, 1.75e6, 2.0e6, 2.5e6, 3.0e6, 3.5e6, 4.0e6, 4.5e6, 5.0e6,
         6.0e6, 7.0e6, 8.0e6, 9.0e6, 1.0e7, 1.25e7, 1.5e7, 1.75e7, 2.0e7, 2.5e7,
         3.0e7, 3.5e7, 4.0e7, 4.5e7, 5.0e7, 6.0e7, 7.0e7, 8.0e7, 9.0e7, 1.0e8,
         1.25e8, 1.5e8, 1.75e8, 2.0e8, 2.5e8, 3.0e8, 3.5e8, 4.0e8, 4.5e8, 5.0e8,
         6.0e8, 7.0e8, 8.0e8, 9.0e8, 1.0e9,
         ]
YXSECG5 = [np.float32(1.6178), np.float32(1.69), np.float32(1.75), np.float32(1.79), np.float32(1.82), np.float32(1.86),
           np.float32(1.91), np.float32(1.98), np.float32(2.07), np.float32(2.14),
           np.float32(2.21), np.float32(2.29), np.float32(2.35), np.float32(2.37), np.float32(2.44), np.float32(2.51),
           np.float32(2.66), np.float32(2.71), np.float32(2.76), np.float32(2.83),
           np.float32(2.84), np.float32(2.84), np.float32(2.78), np.float32(2.58), np.float32(2.30), np.float32(2.12),
           np.float32(2.03), np.float32(1.53), np.float32(1.21), np.float32(1.03),
           np.float32(0.90), np.float32(.756), np.float32(.585), np.float32(.474), np.float32(.385), np.float32(.321),
           np.float32(.234), np.float32(.180), np.float32(.143), np.float32(.117),
           np.float32(.0977), np.float32(.0830), np.float32(.0435), np.float32(.0271), np.float32(.0187),
           np.float32(.0137), np.float32(.0105), np.float32(.00833), np.float32(.00565), np.float32(.00410),
           np.float32(.00312), np.float32(.00246), np.float32(.0020), np.float32(.00166), np.float32(.0008),
           np.float32(.000478), np.float32(.00032), np.float32(.000231), np.float32(.000138),
           9.28e-5,
           6.72e-5, 5.12e-5, 4.05e-5, 3.30e-5, 2.75e-5, 1.88e-5, 1.38e-5, 1.06e-5,
           8.54e-6, 5.9e-6,
           4.43e-6, 3.46e-6, 2.81e-6, 2.34e-6, 1.99e-6, 1.50e-6, 1.19e-6, 9.71e-7,
           8.12e-7, 6.91e-7,
           4.95e-7, 3.74e-7, 2.94e-7, 2.38e-7, 1.67e-7, 1.24e-7, 9.66e-8, 7.74e-8,
           6.35e-8, 5.31e-8,
           3.89e-8, 2.98e-8, 2.36e-8, 1.92e-8, 1.59e-8, 1.07e-8, 7.71e-9, 5.83e-9,
           4.57e-9, 3.03e-9,
           2.16e-9, 1.62e-9, 1.26e-9, 1.01e-9, 8.29e-10, 5.86e-10, 4.36e-10,
           3.36e-10, 2.67e-10, 2.18e-10,
           1.40e-10, 9.78e-11, 7.20e-11, 5.52e-11, 3.54e-11, 2.46e-11, 1.81e-11,
           1.38e-11, 1.09e-11, 8.86e-12,
           6.15e-12, 4.52e-12, 3.46e-12, 2.73e-12, 2.21e-12,
           ]
# ELASTIC TOTAL

XELG5 = [np.float32(1.00), np.float32(1.20), np.float32(1.50), np.float32(1.80), np.float32(2.00), np.float32(2.50),
         np.float32(3.00), np.float32(4.00), np.float32(5.00), np.float32(6.00),
         np.float32(8.00), np.float32(10.0), np.float32(12.0), np.float32(14.0), np.float32(16.0), np.float32(18.0),
         np.float32(20.0), np.float32(25.0), np.float32(30.0), np.float32(40.0),
         np.float32(50.0), np.float32(60.0), np.float32(70.0), np.float32(80.0), np.float32(90.0), np.float32(100.),
         np.float32(125.), np.float32(150.), np.float32(200.), np.float32(250.),
         np.float32(300.), np.float32(350.), np.float32(400.), np.float32(500.), np.float32(600.), np.float32(700.),
         np.float32(800.), np.float32(900.), np.float32(1000.), np.float32(1200.),
         np.float32(1500.), np.float32(2000.), np.float32(2500.), np.float32(3000.), np.float32(4000.),
         np.float32(5000.), np.float32(6000.), np.float32(7000.), np.float32(8000.), np.float32(9000.),
         1.0e4, 1.5e4, 2.0e4, 2.5e4, 3.0e4, 4.0e4, 5.0e4, 6.0e4, 7.0e4, 8.0e4,
         9.0e4, 1.0e5, 1.25e5, 1.5e5, 1.75e5, 2.0e5, 2.5e5, 3.0e5, 3.5e5, 4.0e5,
         4.5e5, 5.0e5, 6.0e5, 7.0e5, 8.0e5, 9.0e5, 1.0e6, 1.25e6, 1.5e6, 1.75e6,
         2.0e6, 2.5e6, 3.0e6, 3.5e6, 4.0e6, 4.5e6, 5.0e6, 6.0e6, 7.0e6, 8.0e6,
         9.0e6, 1.0e7, 1.25e7, 1.5e7, 1.75e7, 2.0e7, 2.5e7, 3.0e7, 3.5e7, 4.0e7,
         5.0e7, 6.0e7, 8.0e7, 9.0e7, 1.0e8, 1.25e8, 1.5e8, 1.75e8, 2.0e8, 2.5e8,
         3.0e8, 3.5e8, 4.0e8, 4.5e8, 5.0e8, 6.0e8, 7.0e8, 8.0e8, 9.0e8, 1.0e9,
         ]
YELG5 = [np.float32(1.5667), np.float32(1.68), np.float32(1.82), np.float32(1.94), np.float32(2.01), np.float32(2.16),
         np.float32(2.30), np.float32(2.55), np.float32(2.80), np.float32(2.98),
         np.float32(3.23), np.float32(3.39), np.float32(3.54), np.float32(3.63), np.float32(3.67), np.float32(3.68),
         np.float32(3.69), np.float32(3.61), np.float32(3.50), np.float32(3.27),
         np.float32(3.09), np.float32(2.90), np.float32(2.72), np.float32(2.54), np.float32(2.40), np.float32(2.25),
         np.float32(1.96), np.float32(1.74), np.float32(1.39), np.float32(1.21),
         np.float32(1.06), np.float32(.997), np.float32(.893), np.float32(.799), np.float32(.693), np.float32(.640),
         np.float32(.565), np.float32(.545), np.float32(.483), np.float32(.433),
         np.float32(.359), np.float32(.284), np.float32(.223), np.float32(.191), np.float32(.156), np.float32(.125),
         np.float32(.109), np.float32(.096), np.float32(.0850), np.float32(.0770),
         np.float32(.0710), np.float32(.0500), np.float32(.0389), np.float32(.0317), np.float32(.0269),
         np.float32(.0208), np.float32(.0172), np.float32(.0147), np.float32(.0129), np.float32(.0116),
         np.float32(.0106), np.float32(.00977), np.float32(.00829), np.float32(.00731), np.float32(.00661),
         np.float32(.00608), np.float32(.00536), np.float32(.00488), np.float32(.00455),
         np.float32(.00430),
         np.float32(.00411), np.float32(.00396), np.float32(.00374), np.float32(.00358), np.float32(.00347),
         np.float32(.00339), np.float32(.00333), np.float32(.00322), np.float32(.00315),
         np.float32(.00310),
         np.float32(.00307), np.float32(.00303), np.float32(.00301), np.float32(.00299), np.float32(.00298),
         np.float32(.00298), np.float32(.00297), np.float32(.00296), np.float32(.00296),
         np.float32(.00296),
         np.float32(.00295), np.float32(.00295), np.float32(.002945), np.float32(.002945), np.float32(.002945),
         np.float32(.002945), np.float32(.002945), np.float32(.002945), np.float32(.002945), np.float32(.002945),
         np.float32(.002945), np.float32(.002945), np.float32(.002945), np.float32(.002945), np.float32(.002945),
         np.float32(.002945), np.float32(.002945), np.float32(.002945), np.float32(.002945), np.float32(.002945),
         np.float32(.002945), np.float32(.002945), np.float32(.002945), np.float32(.002945), np.float32(.002945),
         np.float32(.002945), np.float32(.002945), np.float32(.002945), np.float32(.002945), np.float32(.002945),
         ]
# ANGULAR DISTRIBUTION PARAMETER EPSILON

XEPSG5 = [np.float32(0.0), np.float32(.0001), np.float32(.0002), np.float32(.0003), np.float32(.0004),
          np.float32(.0005), np.float32(.0006), np.float32(.0008), np.float32(.001),
          np.float32(.0012),
          np.float32(.0014), np.float32(.0016), np.float32(.0018), np.float32(.0020), np.float32(.0024),
          np.float32(.0028), np.float32(.0032), np.float32(.0036), np.float32(.0040), np.float32(.0045),
          np.float32(.0050), np.float32(.0055), np.float32(.0060), np.float32(.0070), np.float32(.0080),
          np.float32(.0090), np.float32(.0100), np.float32(.0120), np.float32(.0140), np.float32(.0160),
          np.float32(.0180), np.float32(.0200), np.float32(.0240), np.float32(.0280), np.float32(.0320),
          np.float32(.0360), np.float32(.0400), np.float32(.0450), np.float32(.0500), np.float32(.0550),
          np.float32(0.060), np.float32(0.070), np.float32(0.080), np.float32(0.090), np.float32(0.100),
          np.float32(0.120), np.float32(0.140), np.float32(0.160), np.float32(0.180), np.float32(0.200),
          np.float32(0.24), np.float32(0.28), np.float32(0.32), np.float32(0.36), np.float32(0.40), np.float32(0.45),
          np.float32(0.50), np.float32(0.55), np.float32(0.60), np.float32(0.70),
          np.float32(0.80), np.float32(0.90), np.float32(1.00), np.float32(1.20), np.float32(1.50), np.float32(1.80),
          np.float32(2.00), np.float32(2.50), np.float32(3.00), np.float32(4.00),
          np.float32(5.00), np.float32(6.00), np.float32(7.00), np.float32(8.00), np.float32(8.71), np.float32(9.00),
          np.float32(10.0), np.float32(11.0), np.float32(12.0), np.float32(13.6),
          np.float32(14.0), np.float32(15.0), np.float32(16.0), np.float32(16.5), np.float32(18.0), np.float32(19.6),
          np.float32(20.0), np.float32(25.0), np.float32(30.0), np.float32(40.0),
          np.float32(50.0), np.float32(60.0), np.float32(70.0), np.float32(77.0), np.float32(80.0), np.float32(90.0),
          np.float32(100.), np.float32(125.), np.float32(130.), np.float32(150.),
          np.float32(170.), np.float32(200.), np.float32(250.), np.float32(300.), np.float32(350.), np.float32(400.),
          np.float32(500.), np.float32(600.), np.float32(700.), np.float32(800.),
          np.float32(900.), np.float32(1000.), np.float32(1200.), np.float32(1500.), np.float32(2000.),
          np.float32(2500.), np.float32(3000.), np.float32(3500.), np.float32(4000.), np.float32(5000.),
          np.float32(6000.), np.float32(7000.), np.float32(8000.), np.float32(9000.), 1.0e4, 1.5e4, 2.0e4, 2.5e4, 3.0e4,
          4.0e4,
          5.0e4, 6.0e4, 7.0e4, 8.0e4, 9.0e4, 1.0e5, 1.25e5, 1.5e5, 1.75e5, 2.0e5,
          2.5e5, 3.0e5, 3.5e5, 4.0e5, 4.5e5, 5.0e5, 6.0e5, 7.0e5, 8.0e5, 9.0e5,
          1.0e6, 1.25e6, 1.5e6, 1.75e6, 2.0e6, 2.5e6, 3.0e6, 3.5e6, 4.0e6, 4.5e6,
          5.0e6, 6.0e6, 7.0e6, 8.0e6, 9.0e6, 1.0e7, 1.25e7, 1.5e7, 1.75e7, 2.0e7,
          2.5e7, 3.0e7, 3.5e7, 4.0e7, 4.5e7, 5.0e7, 6.0e7, 7.0e7, 8.0e7, 9.0e7,
          1.0e8, 1.25e8, 1.5e8, 1.75e8, 2.0e8, 2.5e8, 3.0e8, 3.5e8, 4.0e8, 4.5e8,
          5.0e8, 6.0e8, 7.0e8, 8.0e8, 9.0e8, 1.0e9,
          ]
# ELASTIC ANGULAR DISTRIBUTION PARAMETER EPSILON

# EPSILON =1.0-YEPS

YEPSG5 = [np.float32(1.0), np.float32(1.02100), np.float32(1.02805), np.float32(1.03494), np.float32(1.03914),
          np.float32(1.04259), np.float32(1.04678),
          np.float32(1.05337), np.float32(1.05831), np.float32(1.06325),
          np.float32(1.06804), np.float32(1.07208), np.float32(1.07522), np.float32(1.07761), np.float32(1.08388),
          np.float32(1.09015), np.float32(1.09478), np.float32(1.09866),
          np.float32(1.10254), np.float32(1.10730),
          np.float32(1.11177), np.float32(1.11579), np.float32(1.11891), np.float32(1.12531), np.float32(1.13154),
          np.float32(1.13659), np.float32(1.14163), np.float32(1.14918),
          np.float32(1.15613), np.float32(1.16248),
          np.float32(1.16779), np.float32(1.17310), np.float32(1.18075), np.float32(1.18722), np.float32(1.19324),
          np.float32(1.19778), np.float32(1.20202), np.float32(1.20656),
          np.float32(1.21006), np.float32(1.21313),
          np.float32(1.21604), np.float32(1.22041), np.float32(1.22362), np.float32(1.22580), np.float32(1.22725),
          np.float32(1.22929), np.float32(1.22929), np.float32(1.22856),
          np.float32(1.22711), np.float32(1.22478),
          np.float32(1.21852), np.float32(1.21196), np.float32(1.20422), np.float32(1.19734), np.float32(1.18766),
          np.float32(1.17649), np.float32(1.16544), np.float32(1.15332),
          np.float32(1.14133), np.float32(1.11787),
          np.float32(1.09463), np.float32(1.07058), np.float32(1.04888), np.float32(1.00900), np.float32(0.94235),
          np.float32(0.88434), np.float32(0.85878), np.float32(0.79346),
          np.float32(0.74891), np.float32(0.67211),
          np.float32(.62059), np.float32(.59185), np.float32(.58330), np.float32(.57958), np.float32(.58757),
          np.float32(.58901), np.float32(.59407), np.float32(.60031), np.float32(.60172),
          np.float32(.61669),
          np.float32(.61697), np.float32(.62494), np.float32(.63173), np.float32(.63741), np.float32(.64807),
          np.float32(.65936), np.float32(.66256), np.float32(.68649), np.float32(.72161),
          np.float32(.77748),
          np.float32(.75543), np.float32(.69554), np.float32(.67623), np.float32(.68068), np.float32(.66811),
          np.float32(.60509), np.float32(.54128), np.float32(.49618), np.float32(.47938),
          np.float32(.43104),
          np.float32(.39642), np.float32(.37516), np.float32(.30964), np.float32(.27292), np.float32(.21586),
          np.float32(.19276), np.float32(.14022), np.float32(.11680), np.float32(.09323),
          np.float32(.08333),
          np.float32(.06753), np.float32(.06353), np.float32(.05492), np.float32(.03879), np.float32(.02796),
          np.float32(.02349), np.float32(.01908), np.float32(.01656), np.float32(.01297),
          np.float32(.01046),
          np.float32(.00828), np.float32(.00689), np.float32(.00595), np.float32(.00520), np.float32(.00457),
          np.float32(.00287), np.float32(.00209), np.float32(.001374), np.float32(.001360),
          np.float32(.000953),
          7.88e-4, 6.50e-4, 5.51e-4, 4.75e-4, 4.16e-4, 3.71e-4, 2.89e-4, 2.34e-4,
          1.96e-4, 1.67e-4,
          1.278e-4, 1.020e-4, 8.40e-5, 7.07e-5, 6.06e-5, 5.27e-5, 4.11e-5, 3.33e-5,
          2.74e-5, 2.31e-5,
          1.975e-5, 1.418e-5, 1.065e-5, 8.32e-6, 6.69e-6, 4.60e-6, 3.36e-6,
          2.57e-6, 2.03e-6, 1.64e-6,
          1.355e-6, 9.70e-7, 7.29e-7, 5.68e-7, 4.55e-7, 3.73e-7, 2.43e-7, 1.71e-7,
          1.27e-7, 9.80e-8,
          6.33e-8, 4.42e-8, 3.26e-8, 2.49e-8, 1.97e-8, 1.60e-8, 1.10e-8, 8.10e-9,
          6.14e-9, 4.82e-9,
          3.88e-9, 2.44e-9, 1.67e-9, 1.21e-9, 9.1e-10, 5.7e-10, 3.9e-10, 2.8e-10,
          2.1e-10, 1.7e-10,
          1.3e-10, 9.1e-11, 6.6e-11, 5.0e-11, 3.9e-11, 3.1e-11,
          ]
# IONISATION (VALUES ABOVE 20KEV GENERATED BY BORN-BETHE IN SUB)

XIONG5 = [np.float32(21.56454), np.float32(22.0), np.float32(22.5), np.float32(23.0), np.float32(23.5),
          np.float32(24.0), np.float32(24.5), np.float32(25.0), np.float32(25.5), np.float32(26.0),
          np.float32(26.5), np.float32(27.0), np.float32(27.5), np.float32(28.0), np.float32(29.0), np.float32(30.0),
          np.float32(32.0), np.float32(34.0), np.float32(36.0), np.float32(40.0),
          np.float32(45.0), np.float32(50.0), np.float32(55.0), np.float32(60.0), np.float32(65.0), np.float32(70.0),
          np.float32(75.0), np.float32(80.0), np.float32(90.0), np.float32(100.),
          np.float32(110.), np.float32(120.), np.float32(130.), np.float32(140.), np.float32(150.), np.float32(160.),
          np.float32(170.), np.float32(180.), np.float32(190.), np.float32(200.),
          np.float32(225.), np.float32(250.), np.float32(275.), np.float32(300.), np.float32(350.), np.float32(400.),
          np.float32(500.), np.float32(600.), np.float32(700.), np.float32(800.),
          np.float32(900.), np.float32(1000.), np.float32(1200.), np.float32(1400.), np.float32(1600.),
          np.float32(1800.), np.float32(2000.), np.float32(2500.), np.float32(3000.), np.float32(3500.),
          np.float32(4000.), np.float32(4500.), np.float32(5000.), np.float32(5500.), np.float32(6000.),
          np.float32(7000.), np.float32(8000.), np.float32(9000.), np.float32(10000.), np.float32(12000.),
          np.float32(14000.), np.float32(16000.), np.float32(18000.), np.float32(20000.),
          ]
# GROSS IONISATION

YIONG5 = [np.float32(0.00), np.float32(.0031), np.float32(.0085), np.float32(.0139), np.float32(.0192),
          np.float32(.0248), np.float32(.0306), np.float32(.0362), np.float32(.0417),
          np.float32(.0474),
          np.float32(.0540), np.float32(.0602), np.float32(.0664), np.float32(.0726), np.float32(.0847),
          np.float32(.0971), np.float32(.122), np.float32(.147), np.float32(.170), np.float32(.217),
          np.float32(.269), np.float32(.322), np.float32(.372), np.float32(.414), np.float32(.454), np.float32(.490),
          np.float32(.521), np.float32(.549), np.float32(.598), np.float32(.635),
          np.float32(.667), np.float32(.690), np.float32(.707), np.float32(.721), np.float32(.735), np.float32(.746),
          np.float32(.747), np.float32(.748), np.float32(.746), np.float32(.745),
          np.float32(.737), np.float32(.723), np.float32(.703), np.float32(.682), np.float32(.648), np.float32(.607),
          np.float32(.549), np.float32(.501), np.float32(.457), np.float32(.420),
          np.float32(.387), np.float32(.363), np.float32(.320), np.float32(.287), np.float32(.261), np.float32(.239),
          np.float32(.222), np.float32(.186), np.float32(.163), np.float32(.143),
          np.float32(.130), np.float32(.117), np.float32(.108), np.float32(.100), np.float32(.0937), np.float32(.0826),
          np.float32(.0742), np.float32(.0678), np.float32(.0623), np.float32(.0540),
          np.float32(.0475), np.float32(.0426), np.float32(.0389), np.float32(.0357),
          ]
# COUNTING IONISATION

YINCG5 = [np.float32(0.00), np.float32(.0031), np.float32(.0085), np.float32(.0139), np.float32(.0192),
          np.float32(.0248), np.float32(.0306), np.float32(.0362), np.float32(.0417),
          np.float32(.0474),
          np.float32(.0540), np.float32(.0602), np.float32(.0664), np.float32(.0726), np.float32(.0847),
          np.float32(.0971), np.float32(.122), np.float32(.147), np.float32(.170), np.float32(.217),
          np.float32(.269), np.float32(.322), np.float32(.372), np.float32(.414), np.float32(.454), np.float32(.490),
          np.float32(.521), np.float32(.548), np.float32(.595), np.float32(.630),
          np.float32(.657), np.float32(.678), np.float32(.692), np.float32(.703), np.float32(.714), np.float32(.721),
          np.float32(.721), np.float32(.720), np.float32(.717), np.float32(.715),
          np.float32(.705), np.float32(.690), np.float32(.670), np.float32(.650), np.float32(.616), np.float32(.577),
          np.float32(.522), np.float32(.476), np.float32(.435), np.float32(.400),
          np.float32(.369), np.float32(.345), np.float32(.305), np.float32(.273), np.float32(.248), np.float32(.228),
          np.float32(.211), np.float32(.177), np.float32(.155), np.float32(.136),
          np.float32(.124), np.float32(.111), np.float32(.103), np.float32(.0951), np.float32(.0891), np.float32(.0786),
          np.float32(.0706), np.float32(.0645), np.float32(.0592), np.float32(.0513),
          np.float32(.0451), np.float32(.0406), np.float32(.0370), np.float32(.0340),
          ]
# IONISATION FOR CHARGE STATE =1

YIN1G5 = [np.float32(0.00), np.float32(.0031), np.float32(.0085), np.float32(.0139), np.float32(.0192),
          np.float32(.0248), np.float32(.0306), np.float32(.0362), np.float32(.0417),
          np.float32(.0474),
          np.float32(.0540), np.float32(.0602), np.float32(.0664), np.float32(.0726), np.float32(.0847),
          np.float32(.0971), np.float32(.122), np.float32(.147), np.float32(.170), np.float32(.217),
          np.float32(.269), np.float32(.322), np.float32(.372), np.float32(.414), np.float32(.454), np.float32(.490),
          np.float32(.521), np.float32(.547), np.float32(.592), np.float32(.624),
          np.float32(.648), np.float32(.666), np.float32(.677), np.float32(.684), np.float32(.693), np.float32(.698),
          np.float32(.696), np.float32(.693), np.float32(.689), np.float32(.685),
          np.float32(.673), np.float32(.658), np.float32(.637), np.float32(.619), np.float32(.586), np.float32(.548),
          np.float32(.496), np.float32(.454), np.float32(.416), np.float32(.383),
          np.float32(.354), np.float32(.331), np.float32(.293), np.float32(.262), np.float32(.238), np.float32(.219),
          np.float32(.202), np.float32(.170), np.float32(.149), np.float32(.130),
          np.float32(.119), np.float32(.106), np.float32(.0988), np.float32(.0912), np.float32(.0855),
          np.float32(.0754), np.float32(.0677), np.float32(.0619), np.float32(.0568), np.float32(.0492),
          np.float32(.0433), np.float32(.0390), np.float32(.0355), np.float32(.0326),
          ]
# IONISATION FOR CHARGE STATE =2

XIN2G5 = [np.float32(62.5275), np.float32(75.0), np.float32(80.0), np.float32(90.0), np.float32(100.), np.float32(110.),
          np.float32(120.), np.float32(130.), np.float32(140.), np.float32(150.),
          np.float32(160.), np.float32(170.), np.float32(180.), np.float32(190.), np.float32(200.), np.float32(225.),
          np.float32(250.), np.float32(275.), np.float32(300.), np.float32(350.),
          np.float32(400.), np.float32(500.), np.float32(600.), np.float32(700.), np.float32(800.), np.float32(900.),
          np.float32(1000.), np.float32(1200.), np.float32(1400.), np.float32(1600.),
          np.float32(1800.), np.float32(2000.), np.float32(2500.), np.float32(3000.), np.float32(3500.),
          np.float32(4000.), np.float32(4500.), np.float32(5000.), np.float32(5500.), np.float32(6000.),
          np.float32(7000.), np.float32(8000.), np.float32(9000.), np.float32(10000.), np.float32(12000.),
          np.float32(14000.), np.float32(16000.), np.float32(18000.), np.float32(20000.),
          ]
YIN2G5 = [np.float32(0.0), np.float32(.0005), np.float32(.00127), np.float32(.00319), np.float32(.00586),
          np.float32(.0094), np.float32(.0121), np.float32(.0155), np.float32(.0187),
          np.float32(.0214),
          np.float32(.0240), np.float32(.0254), np.float32(.0272), np.float32(.0280), np.float32(.0294),
          np.float32(.0316), np.float32(.0315), np.float32(.0315), np.float32(.0301), np.float32(.0291),
          np.float32(.0269), np.float32(.0243), np.float32(.0212), np.float32(.0185), np.float32(.0164),
          np.float32(.0148), np.float32(.0134), np.float32(.0118), np.float32(.0106), np.float32(.00962),
          np.float32(.00885), np.float32(.00819), np.float32(.00687), np.float32(.00601), np.float32(.00528),
          np.float32(.00481), np.float32(.00431), np.float32(.0040), np.float32(.00369),
          np.float32(.00346),
          np.float32(.00305), np.float32(.00274), np.float32(.0025), np.float32(.0023), np.float32(.0020),
          np.float32(.00175), np.float32(.00158), np.float32(.00144), np.float32(.00132),
          ]
# IONISATION FOR CHARGE STATE =3

XIN3G5 = [np.float32(125.9508), np.float32(150.), np.float32(160.), np.float32(170.), np.float32(180.),
          np.float32(190.), np.float32(200.), np.float32(225.), np.float32(250.), np.float32(275.),
          np.float32(300.), np.float32(350.), np.float32(400.), np.float32(500.), np.float32(600.), np.float32(700.),
          np.float32(800.), np.float32(900.), np.float32(1000.), np.float32(1200.),
          np.float32(1400.), np.float32(1600.), np.float32(1800.), np.float32(2000.), np.float32(2500.),
          np.float32(3000.), np.float32(3500.), np.float32(4000.), np.float32(4500.), np.float32(5000.),
          np.float32(5500.), np.float32(6000.), np.float32(7000.), np.float32(8000.), np.float32(9000.),
          np.float32(10000.), np.float32(12000.), np.float32(14000.), np.float32(16000.), np.float32(18000.),
          np.float32(20000.),
          ]
YIN3G5 = [np.float32(0.00), np.float32(.00005), np.float32(.000118), np.float32(.000173), np.float32(.000263),
          np.float32(.000377), np.float32(.000476),
          np.float32(.00072), np.float32(.00104), np.float32(.00126),
          np.float32(.00138), np.float32(.00156), np.float32(.00158), np.float32(.00143), np.float32(.00132),
          np.float32(.00121), np.float32(.00103), np.float32(.000852), np.float32(.000741),
          np.float32(.000656),
          np.float32(.000587), np.float32(.000533), np.float32(.000490), np.float32(.000454), np.float32(.000381),
          np.float32(.000333), np.float32(.000292), np.float32(.000267),
          np.float32(.000239), np.float32(.000221),
          np.float32(.000204), np.float32(.000192), np.float32(.000169), np.float32(.000146), np.float32(.000139),
          np.float32(.000127), np.float32(.000110), np.float32(.0000970),
          np.float32(.0000873), np.float32(.0000796), np.float32(.0000731),
          ]
# K-SHELL IONISATION X-SECTION

XKSHG5 = [np.float32(870.2), np.float32(874.7), np.float32(900.), np.float32(926.), np.float32(953.), np.float32(981.),
          np.float32(1009.), np.float32(1038.), np.float32(1068.), np.float32(1099.),
          np.float32(1131.), np.float32(1164.), np.float32(1232.), np.float32(1305.), np.float32(1381.),
          np.float32(1463.), np.float32(1594.), np.float32(1737.), np.float32(1948.), np.float32(2122.),
          np.float32(2313.), np.float32(2521.), np.float32(2747.), np.float32(2994.), np.float32(3264.),
          np.float32(3557.), np.float32(3877.), np.float32(4226.), np.float32(4606.), np.float32(5021.),
          np.float32(5473.), np.float32(5966.), np.float32(6503.), np.float32(7088.), np.float32(7727.),
          np.float32(8423.), np.float32(9182.), 1.0e4, 1.12e4, 1.26e4,
          1.41e4, 1.59e4, 1.78e4, 2.00e4, 2.24e4, 2.51e4, 2.82e4, 3.16e4, 3.55e4,
          3.98e4,
          4.47e4, 5.01e4, 5.62e4, 6.31e4, 7.08e4, 7.94e4, 8.91e4, 1.00e5, 1.12e5,
          1.30e5,
          1.50e5, 1.73e5, 2.00e5, 2.30e5, 2.66e5, 3.07e5, 3.55e5, 4.22e5, 5.01e5,
          6.13e5,
          7.50e5, 1.00e6, 1.22e6, 1.45e6, 1.73e6, 2.00e6, 2.51e6, 3.07e6, 4.00e6,
          5.01e6,
          6.13e6, 8.18e6, 1.00e7, 1.50e7, 2.05e7, 3.07e7, 3.98e7, 5.01e7, 6.13e7,
          8.18e7,
          1.00e8, 1.50e8, 2.05e8, 3.07e8, 3.98e8, 5.01e8, 6.13e8, 8.18e8, 1.00e9,
          ]
YKSHG5 = [np.float32(0.0), 7.15e-6, 2.96e-5, 5.13e-5, 7.23e-5, 9.26e-5, 1.12e-4,
          1.31e-4, 1.49e-4, 1.67e-4,
          1.84e-4, 2.00e-4, 2.31e-4, 2.59e-4, 2.84e-4, 3.08e-4, 3.39e-4, 3.65e-4,
          3.94e-4, 4.10e-4,
          4.22e-4, 4.31e-4, 4.36e-4, 4.38e-4, 4.37e-4, 4.34e-4, 4.28e-4, 4.20e-4,
          4.11e-4, 4.00e-4,
          3.88e-4, 3.75e-4, 3.61e-4, 3.47e-4, 3.33e-4, 3.18e-4, 3.04e-4, 2.90e-4,
          2.71e-4, 2.53e-4,
          2.36e-4, 2.19e-4, 2.04e-4, 1.89e-4, 1.75e-4, 1.62e-4, 1.50e-4, 1.38e-4,
          1.28e-4, 1.18e-4,
          1.09e-4, 1.01e-4, 9.32e-5, 8.63e-5, 8.00e-5, 7.43e-5, 6.90e-5, 6.43e-5,
          6.00e-5, 5.51e-5,
          5.09e-5, 4.73e-5, 4.41e-5, 4.13e-5, 3.89e-5, 3.69e-5, 3.52e-5, 3.36e-5,
          3.23e-5, 3.12e-5,
          3.05e-5, 3.01e-5, 3.01e-5, 3.04e-5, 3.07e-5, 3.11e-5, 3.19e-5, 3.27e-5,
          3.39e-5, 3.50e-5,
          3.60e-5, 3.76e-5, 3.87e-5, 4.11e-5, 4.30e-5, 4.54e-5, 4.69e-5, 4.83e-5,
          4.96e-5, 5.13e-5,
          5.25e-5, 5.50e-5, 5.69e-5, 5.94e-5, 6.10e-5, 6.24e-5, 6.36e-5, 6.54e-5,
          6.66e-5,
          ]
#

# 1S5 METASTABLE J=2  UNITS 10**-18 SCALED BY 1/E**3 ABOVE 50 EV

X1S5G5 = [np.float32(16.61907), np.float32(16.625), np.float32(16.63), np.float32(16.64), np.float32(16.65),
          np.float32(16.66), np.float32(16.67), np.float32(16.68),
          np.float32(16.69), np.float32(16.70),
          np.float32(16.71), np.float32(16.73), np.float32(16.75), np.float32(16.79), np.float32(16.80),
          np.float32(16.81), np.float32(16.82), np.float32(16.84), np.float32(16.85), np.float32(16.86),
          np.float32(16.87), np.float32(16.88), np.float32(16.89), np.float32(16.90), np.float32(16.91),
          np.float32(16.92), np.float32(16.93), np.float32(16.94), np.float32(16.95), np.float32(16.96),
          np.float32(16.97), np.float32(16.98), np.float32(16.99), np.float32(17.00), np.float32(17.02),
          np.float32(17.04), np.float32(17.06), np.float32(17.08), np.float32(17.10), np.float32(17.20),
          np.float32(17.30), np.float32(17.40), np.float32(17.50), np.float32(17.60), np.float32(17.70),
          np.float32(17.80), np.float32(17.90), np.float32(18.00), np.float32(18.10), np.float32(18.20),
          np.float32(18.30), np.float32(18.40), np.float32(18.41), np.float32(18.43), np.float32(18.45),
          np.float32(18.47), np.float32(18.50), np.float32(18.53), np.float32(18.55), np.float32(18.56),
          np.float32(18.57), np.float32(18.58), np.float32(18.59), np.float32(18.60), np.float32(18.61),
          np.float32(18.62), np.float32(18.625), np.float32(18.63), np.float32(18.64), np.float32(18.65),
          np.float32(18.66), np.float32(18.67), np.float32(18.68), np.float32(18.69), np.float32(18.70),
          np.float32(18.71), np.float32(18.72), np.float32(18.73), np.float32(18.75), np.float32(18.78),
          np.float32(18.80), np.float32(18.90), np.float32(18.96), np.float32(18.97), np.float32(18.98),
          np.float32(18.99), np.float32(19.00), np.float32(19.05), np.float32(19.10), np.float32(19.20),
          np.float32(19.50), np.float32(19.58), np.float32(19.60), np.float32(19.61), np.float32(19.63),
          np.float32(19.65), np.float32(19.70), np.float32(19.80), np.float32(19.90), np.float32(20.00),
          np.float32(21.0), np.float32(22.0), np.float32(23.0), np.float32(24.0), np.float32(26.0), np.float32(28.0),
          np.float32(30.0), np.float32(35.0), np.float32(40.0), np.float32(45.0),
          np.float32(50.0),
          ]
Y1S5G5 = [np.float32(0.0), np.float32(.114), np.float32(.142), np.float32(.190), np.float32(.228), np.float32(.256),
          np.float32(.275), np.float32(.304), np.float32(.342), np.float32(.399),
          np.float32(.446), np.float32(.532), np.float32(.598), np.float32(.646), np.float32(.665), np.float32(.674),
          np.float32(.693), np.float32(.750), np.float32(.788), np.float32(.845),
          np.float32(.902), np.float32(1.09), np.float32(1.27), np.float32(1.47), np.float32(1.59), np.float32(1.65),
          np.float32(1.65), np.float32(1.59), np.float32(1.52), np.float32(1.44),
          np.float32(1.35), np.float32(1.28), np.float32(1.20), np.float32(1.16), np.float32(1.03), np.float32(.988),
          np.float32(.931), np.float32(.893), np.float32(.864), np.float32(.807),
          np.float32(.807), np.float32(.826), np.float32(.864), np.float32(.912), np.float32(.978), np.float32(1.03),
          np.float32(1.11), np.float32(1.19), np.float32(1.26), np.float32(1.34),
          np.float32(1.40), np.float32(1.42), np.float32(1.30), np.float32(1.21), np.float32(1.15), np.float32(1.12),
          np.float32(1.07), np.float32(1.02), np.float32(1.24), np.float32(1.55),
          np.float32(2.13), np.float32(2.02), np.float32(1.64), np.float32(1.23), np.float32(1.12), np.float32(1.56),
          np.float32(1.70), np.float32(1.55), np.float32(1.10), np.float32(1.28),
          np.float32(1.58), np.float32(1.72), np.float32(1.65), np.float32(1.42), np.float32(1.25), np.float32(1.10),
          np.float32(.988), np.float32(.959), np.float32(.883), np.float32(.827),
          np.float32(.817), np.float32(.836), np.float32(.779), np.float32(.931), np.float32(1.21), np.float32(1.14),
          np.float32(1.02), np.float32(1.01), np.float32(1.04), np.float32(1.08),
          np.float32(1.15), np.float32(1.07), np.float32(1.01), np.float32(1.33), np.float32(1.27), np.float32(1.23),
          np.float32(1.21), np.float32(1.17), np.float32(1.14), np.float32(1.03),
          np.float32(1.04), np.float32(1.04), np.float32(1.03), np.float32(1.02), np.float32(.998), np.float32(.959),
          np.float32(.902), np.float32(.760), np.float32(.608), np.float32(.475),
          np.float32(.361),
          ]
# 1S4 RESONANCE LEVEL J=1 F=0.0118  UNITS 10**-18  74.3724 NM.

X1S4G5 = [np.float32(16.67083), np.float32(16.675), np.float32(16.68), np.float32(16.69), np.float32(16.70),
          np.float32(16.71), np.float32(16.72), np.float32(16.73),
          np.float32(16.74), np.float32(16.75),
          np.float32(16.76), np.float32(16.77), np.float32(16.78), np.float32(16.79), np.float32(16.80),
          np.float32(16.81), np.float32(16.82), np.float32(16.83), np.float32(16.84), np.float32(16.85),
          np.float32(16.86), np.float32(16.87), np.float32(16.88), np.float32(16.89), np.float32(16.90),
          np.float32(16.91), np.float32(16.92), np.float32(16.93), np.float32(16.94), np.float32(16.95),
          np.float32(16.96), np.float32(16.97), np.float32(16.98), np.float32(16.99), np.float32(17.00),
          np.float32(17.02), np.float32(17.04), np.float32(17.06), np.float32(17.08), np.float32(17.10),
          np.float32(17.20), np.float32(17.30), np.float32(17.40), np.float32(17.50), np.float32(17.60),
          np.float32(17.70), np.float32(17.80), np.float32(17.90), np.float32(18.00), np.float32(18.10),
          np.float32(18.20), np.float32(18.30), np.float32(18.40), np.float32(18.41), np.float32(18.42),
          np.float32(18.43), np.float32(18.44), np.float32(18.45), np.float32(18.47), np.float32(18.50),
          np.float32(18.52), np.float32(18.525), np.float32(18.53), np.float32(18.54), np.float32(18.55),
          np.float32(18.56), np.float32(18.57), np.float32(18.58), np.float32(18.59), np.float32(18.60),
          np.float32(18.61), np.float32(18.62), np.float32(18.63), np.float32(18.64), np.float32(18.65),
          np.float32(18.66), np.float32(18.67), np.float32(18.68), np.float32(18.69), np.float32(18.70),
          np.float32(18.71), np.float32(18.72), np.float32(18.73), np.float32(18.74), np.float32(18.75),
          np.float32(18.76), np.float32(18.78), np.float32(18.80), np.float32(18.90), np.float32(18.94),
          np.float32(18.96), np.float32(18.98), np.float32(18.99), np.float32(19.00), np.float32(19.05),
          np.float32(19.10), np.float32(19.20), np.float32(19.30), np.float32(19.40), np.float32(19.50),
          np.float32(19.7), np.float32(19.9), np.float32(20.0), np.float32(21.0), np.float32(22.0), np.float32(23.0),
          np.float32(24.0), np.float32(25.0), np.float32(26.0), np.float32(27.0),
          np.float32(28.0), np.float32(30.0), np.float32(32.0), np.float32(35.0), np.float32(40.0), np.float32(45.0),
          np.float32(50.0), np.float32(60.0), np.float32(70.0), np.float32(80.0),
          np.float32(90.0), np.float32(100.), np.float32(120.), np.float32(140.), np.float32(170.), np.float32(200.),
          np.float32(250.), np.float32(300.), np.float32(350.), np.float32(400.),
          np.float32(450.), np.float32(500.), np.float32(600.), np.float32(700.), np.float32(800.), np.float32(900.),
          np.float32(1000.),
          ]
Y1S4G5 = [np.float32(0.), np.float32(.082), np.float32(.109), np.float32(.149), np.float32(.192), np.float32(.239),
          np.float32(.295), np.float32(.364), np.float32(.439), np.float32(.510),
          np.float32(.572), np.float32(.623), np.float32(.665), np.float32(.697), np.float32(.728), np.float32(.762),
          np.float32(.798), np.float32(.845), np.float32(.900), np.float32(.959),
          np.float32(1.04), np.float32(1.13), np.float32(1.21), np.float32(1.23), np.float32(1.23), np.float32(1.18),
          np.float32(1.11), np.float32(1.04), np.float32(.978), np.float32(.918),
          np.float32(.852), np.float32(.824), np.float32(.784), np.float32(.750), np.float32(.722), np.float32(.674),
          np.float32(.646), np.float32(.608), np.float32(.598), np.float32(.580),
          np.float32(.541), np.float32(.541), np.float32(.551), np.float32(.570), np.float32(.598), np.float32(.627),
          np.float32(.665), np.float32(.712), np.float32(.760), np.float32(.807),
          np.float32(.855), np.float32(.893), np.float32(.893), np.float32(.855), np.float32(.836), np.float32(.807),
          np.float32(.798), np.float32(.798), np.float32(.779), np.float32(.760),
          np.float32(.760), np.float32(.874), np.float32(.770), np.float32(.788), np.float32(.836), np.float32(.978),
          np.float32(1.26), np.float32(1.29), np.float32(.978), np.float32(.760),
          np.float32(.788), np.float32(1.08), np.float32(.864), np.float32(.770), np.float32(.940), np.float32(1.19),
          np.float32(1.41), np.float32(1.33), np.float32(1.16), np.float32(1.04),
          np.float32(.959), np.float32(.931), np.float32(.827), np.float32(.779), np.float32(.732), np.float32(.693),
          np.float32(.646), np.float32(.617), np.float32(.589), np.float32(.560),
          np.float32(.570), np.float32(.817), np.float32(.712), np.float32(.684), np.float32(.693), np.float32(.712),
          np.float32(.741), np.float32(.760), np.float32(.779), np.float32(.798),
          np.float32(.817), np.float32(.808), np.float32(.770), np.float32(.810), np.float32(.850), np.float32(.890),
          np.float32(.920), np.float32(.940), np.float32(.960), np.float32(.990),
          np.float32(1.00), np.float32(1.02), np.float32(1.04), np.float32(1.05), np.float32(1.06), np.float32(1.06),
          np.float32(1.05), np.float32(1.04), np.float32(1.02), np.float32(.990),
          np.float32(.950), np.float32(.880), np.float32(.800), np.float32(.730), np.float32(.670), np.float32(.600),
          np.float32(.530), np.float32(.460), np.float32(.410), np.float32(.370),
          np.float32(.338), np.float32(.310), np.float32(.270), np.float32(.239), np.float32(.217), np.float32(.198),
          np.float32(.184),
          ]
# 1S3 METASTABLE LEVEL  J=0   UNITS 10**-18 SCALED BY 1/E**3 ABOVE 50 EV

X1S3G5 = [np.float32(16.71538), np.float32(16.72), np.float32(16.73), np.float32(16.74), np.float32(16.75),
          np.float32(16.76), np.float32(16.77), np.float32(16.78),
          np.float32(16.79), np.float32(16.80),
          np.float32(16.81), np.float32(16.82), np.float32(16.83), np.float32(16.84), np.float32(16.85),
          np.float32(16.86), np.float32(16.87), np.float32(16.88), np.float32(16.89), np.float32(16.90),
          np.float32(16.91), np.float32(16.92), np.float32(16.93), np.float32(16.94), np.float32(16.95),
          np.float32(16.96), np.float32(16.97), np.float32(16.98), np.float32(17.00), np.float32(17.02),
          np.float32(17.04), np.float32(17.06), np.float32(17.08), np.float32(17.10), np.float32(17.12),
          np.float32(17.14), np.float32(17.16), np.float32(17.18), np.float32(17.20), np.float32(17.22),
          np.float32(17.26), np.float32(17.34), np.float32(17.40), np.float32(17.45), np.float32(17.50),
          np.float32(17.60), np.float32(17.70), np.float32(17.80), np.float32(17.90), np.float32(18.00),
          np.float32(18.10), np.float32(18.20), np.float32(18.30), np.float32(18.40), np.float32(18.41),
          np.float32(18.43), np.float32(18.45), np.float32(18.47), np.float32(18.50), np.float32(18.52),
          np.float32(18.525), np.float32(18.53), np.float32(18.54), np.float32(18.55), np.float32(18.56),
          np.float32(18.57), np.float32(18.58), np.float32(18.59), np.float32(18.60), np.float32(18.61),
          np.float32(18.62), np.float32(18.63), np.float32(18.64), np.float32(18.65), np.float32(18.66),
          np.float32(18.67), np.float32(18.68), np.float32(18.69), np.float32(18.70), np.float32(18.71),
          np.float32(18.72), np.float32(18.73), np.float32(18.74), np.float32(18.75), np.float32(18.76),
          np.float32(18.78), np.float32(18.80), np.float32(18.82), np.float32(18.84), np.float32(18.86),
          np.float32(18.88), np.float32(18.90), np.float32(18.92), np.float32(18.94), np.float32(18.95),
          np.float32(18.96), np.float32(18.97), np.float32(18.98), np.float32(18.99), np.float32(19.00),
          np.float32(19.05), np.float32(19.10), np.float32(19.20), np.float32(19.30), np.float32(19.40),
          np.float32(19.50), np.float32(19.60), np.float32(19.65), np.float32(19.70), np.float32(19.80),
          np.float32(19.9), np.float32(20.0), np.float32(25.0), np.float32(30.0), np.float32(35.0), np.float32(40.0),
          np.float32(50.0),
          ]
Y1S3G5 = [np.float32(0.), np.float32(.025), np.float32(.038), np.float32(.046), np.float32(.054), np.float32(.063),
          np.float32(.078), np.float32(.095), np.float32(.117), np.float32(.144),
          np.float32(.175), np.float32(.205), np.float32(.238), np.float32(.274), np.float32(.311), np.float32(.350),
          np.float32(.387), np.float32(.415), np.float32(.420), np.float32(.408),
          np.float32(.387), np.float32(.361), np.float32(.341), np.float32(.319), np.float32(.298), np.float32(.284),
          np.float32(.268), np.float32(.251), np.float32(.229), np.float32(.201),
          np.float32(.197), np.float32(.186), np.float32(.176), np.float32(.170), np.float32(.165), np.float32(.161),
          np.float32(.159), np.float32(.157), np.float32(.155), np.float32(.153),
          np.float32(.152), np.float32(.152), np.float32(.154), np.float32(.157), np.float32(.161), np.float32(.168),
          np.float32(.178), np.float32(.190), np.float32(.203), np.float32(.217),
          np.float32(.231), np.float32(.243), np.float32(.256), np.float32(.255), np.float32(.244), np.float32(.229),
          np.float32(.226), np.float32(.225), np.float32(.218), np.float32(.210),
          np.float32(.335), np.float32(.220), np.float32(.218), np.float32(.226), np.float32(.253), np.float32(.343),
          np.float32(.427), np.float32(.315), np.float32(.230), np.float32(.235),
          np.float32(.325), np.float32(.260), np.float32(.223), np.float32(.247), np.float32(.376), np.float32(.537),
          np.float32(.524), np.float32(.457), np.float32(.402), np.float32(.365),
          np.float32(.328), np.float32(.299), np.float32(.274), np.float32(.251), np.float32(.229), np.float32(.201),
          np.float32(.179), np.float32(.166), np.float32(.158), np.float32(.154),
          np.float32(.150), np.float32(.146), np.float32(.141), np.float32(.130), np.float32(.126), np.float32(.134),
          np.float32(.214), np.float32(.249), np.float32(.199), np.float32(.189),
          np.float32(.188), np.float32(.194), np.float32(.204), np.float32(.212), np.float32(.218), np.float32(.223),
          np.float32(.226), np.float32(.219), np.float32(.213), np.float32(.232),
          np.float32(.228), np.float32(.221), np.float32(.210), np.float32(.175), np.float32(.145), np.float32(.125),
          np.float32(.085),
          ]
# 1S2 RESONANCE LEVEL J=1 F=0.159   UNITS 10**-18  73.5901 NM.

X1S2G5 = [np.float32(16.84805), np.float32(16.86), np.float32(16.87), np.float32(16.88), np.float32(16.89),
          np.float32(16.90), np.float32(16.91), np.float32(16.92),
          np.float32(16.93), np.float32(16.94),
          np.float32(16.95), np.float32(16.96), np.float32(16.98), np.float32(17.00), np.float32(17.05),
          np.float32(17.10), np.float32(17.20), np.float32(17.30), np.float32(17.40), np.float32(17.50),
          np.float32(17.60), np.float32(17.70), np.float32(17.80), np.float32(17.90), np.float32(18.00),
          np.float32(18.10), np.float32(18.20), np.float32(18.30), np.float32(18.40), np.float32(18.42),
          np.float32(18.44), np.float32(18.46), np.float32(18.49), np.float32(18.51), np.float32(18.53),
          np.float32(18.54), np.float32(18.55), np.float32(18.56), np.float32(18.57), np.float32(18.58),
          np.float32(18.59), np.float32(18.60), np.float32(18.61), np.float32(18.62), np.float32(18.63),
          np.float32(18.64), np.float32(18.65), np.float32(18.66), np.float32(18.67), np.float32(18.68),
          np.float32(18.69), np.float32(18.70), np.float32(18.71), np.float32(18.72), np.float32(18.73),
          np.float32(18.74), np.float32(18.76), np.float32(18.78), np.float32(18.80), np.float32(18.85),
          np.float32(18.90), np.float32(18.92), np.float32(18.94), np.float32(18.95), np.float32(18.96),
          np.float32(18.97), np.float32(18.98), np.float32(19.00), np.float32(19.05), np.float32(19.10),
          np.float32(19.20), np.float32(19.30), np.float32(19.40), np.float32(19.50), np.float32(19.60),
          np.float32(19.70), np.float32(19.80), np.float32(19.90), np.float32(20.00), np.float32(20.50),
          np.float32(21.0), np.float32(21.5), np.float32(22.0), np.float32(23.0), np.float32(24.0), np.float32(25.0),
          np.float32(26.0), np.float32(27.0), np.float32(28.0), np.float32(29.0),
          np.float32(30.0), np.float32(31.0), np.float32(32.0), np.float32(33.0), np.float32(34.0), np.float32(35.0),
          np.float32(36.0), np.float32(37.0), np.float32(38.0), np.float32(39.0),
          np.float32(40.0), np.float32(41.0), np.float32(42.0), np.float32(43.0), np.float32(45.0), np.float32(50.0),
          np.float32(60.0), np.float32(70.0), np.float32(80.0), np.float32(100.),
          np.float32(120.), np.float32(150.), np.float32(180.), np.float32(200.), np.float32(240.), np.float32(280.),
          np.float32(320.), np.float32(360.), np.float32(400.),
          ]
Y1S2G5 = [np.float32(0.), np.float32(.230), np.float32(.513), np.float32(.864), np.float32(1.23), np.float32(1.59),
          np.float32(1.83), np.float32(2.00), np.float32(2.10), np.float32(2.16),
          np.float32(2.18), np.float32(2.15), np.float32(2.12), np.float32(2.04), np.float32(1.86), np.float32(1.73),
          np.float32(1.57), np.float32(1.49), np.float32(1.46), np.float32(1.45),
          np.float32(1.46), np.float32(1.50), np.float32(1.54), np.float32(1.60), np.float32(1.67), np.float32(1.75),
          np.float32(1.82), np.float32(1.89), np.float32(1.99), np.float32(2.01),
          np.float32(2.03), np.float32(2.05), np.float32(2.06), np.float32(2.11), np.float32(2.05), np.float32(1.97),
          np.float32(2.06), np.float32(2.15), np.float32(2.14), np.float32(2.01),
          np.float32(1.96), np.float32(2.02), np.float32(2.00), np.float32(1.98), np.float32(1.94), np.float32(2.03),
          np.float32(2.25), np.float32(2.37), np.float32(2.30), np.float32(2.21),
          np.float32(2.13), np.float32(2.09), np.float32(2.04), np.float32(2.01), np.float32(1.99), np.float32(1.95),
          np.float32(1.91), np.float32(1.88), np.float32(1.88), np.float32(1.91),
          np.float32(2.01), np.float32(2.11), np.float32(2.27), np.float32(2.29), np.float32(1.96), np.float32(1.86),
          np.float32(1.93), np.float32(1.96), np.float32(1.99), np.float32(2.01),
          np.float32(2.06), np.float32(2.10), np.float32(2.15), np.float32(2.18), np.float32(2.25), np.float32(2.29),
          np.float32(2.28), np.float32(2.32), np.float32(2.36), np.float32(2.56),
          np.float32(2.66), np.float32(2.80), np.float32(3.07), np.float32(3.63), np.float32(4.22), np.float32(4.88),
          np.float32(5.45), np.float32(6.00), np.float32(6.57), np.float32(7.07),
          np.float32(7.52), np.float32(7.90), np.float32(8.28), np.float32(8.60), np.float32(8.87), np.float32(9.10),
          np.float32(9.30), np.float32(9.48), np.float32(9.63), np.float32(9.76),
          np.float32(9.87), np.float32(9.96), np.float32(10.0), np.float32(10.1), np.float32(10.2), np.float32(10.3),
          np.float32(10.4), np.float32(10.3), np.float32(10.0), np.float32(9.45),
          np.float32(9.00), np.float32(8.00), np.float32(7.20), np.float32(6.80), np.float32(6.10), np.float32(5.50),
          np.float32(5.05), np.float32(4.73), np.float32(4.45),
          ]
# 2P10 J=1   UNITS 10**-18   SCALE 1/E**2 ABOVE 100 EV

X2P10G5 = [np.float32(18.38162), np.float32(18.39), np.float32(18.40), np.float32(18.42), np.float32(18.43),
           np.float32(18.44), np.float32(18.46), np.float32(18.47),
           np.float32(18.48), np.float32(18.49),
           np.float32(18.50), np.float32(18.509), np.float32(18.51), np.float32(18.52), np.float32(18.53),
           np.float32(18.54), np.float32(18.55), np.float32(18.56), np.float32(18.57), np.float32(18.58),
           np.float32(18.59), np.float32(18.60), np.float32(18.61), np.float32(18.62), np.float32(18.63),
           np.float32(18.64), np.float32(18.65), np.float32(18.66), np.float32(18.67), np.float32(18.68),
           np.float32(18.69), np.float32(18.70), np.float32(18.71), np.float32(18.72), np.float32(18.74),
           np.float32(18.80), np.float32(18.90), np.float32(18.92), np.float32(18.95), np.float32(18.96),
           np.float32(18.97), np.float32(19.00), np.float32(19.10), np.float32(19.20), np.float32(19.30),
           np.float32(19.40), np.float32(19.50), np.float32(19.56), np.float32(19.57), np.float32(19.58),
           np.float32(19.59), np.float32(19.60), np.float32(19.70), np.float32(19.80), np.float32(19.90),
           np.float32(20.0), np.float32(21.0), np.float32(22.0), np.float32(23.0), np.float32(24.0),
           np.float32(25.0), np.float32(26.0), np.float32(28.0), np.float32(30.0), np.float32(32.0), np.float32(34.0),
           np.float32(36.0), np.float32(38.0), np.float32(40.0), np.float32(50.0),
           np.float32(60.0), np.float32(75.0), np.float32(100.),
           ]
Y2P10G5 = [np.float32(0.00), np.float32(.060), np.float32(.091), np.float32(.201), np.float32(.261), np.float32(.287),
           np.float32(.310), np.float32(.328), np.float32(.354), np.float32(.389),
           np.float32(.440), np.float32(.589), np.float32(.394), np.float32(.574), np.float32(.716), np.float32(.960),
           np.float32(1.23), np.float32(1.03), np.float32(.440), np.float32(.229),
           np.float32(.481), np.float32(1.16), np.float32(.777), np.float32(.606), np.float32(.863), np.float32(1.03),
           np.float32(1.08), np.float32(.690), np.float32(.346), np.float32(.191),
           np.float32(.117), np.float32(.085), np.float32(.081), np.float32(.074), np.float32(.068), np.float32(.062),
           np.float32(.064), np.float32(.095), np.float32(.597), np.float32(.580),
           np.float32(.278), np.float32(.164), np.float32(.143), np.float32(.138), np.float32(.136), np.float32(.135),
           np.float32(.136), np.float32(.147), np.float32(.163), np.float32(.201),
           np.float32(.142), np.float32(.135), np.float32(.123), np.float32(.120), np.float32(.142), np.float32(.153),
           np.float32(.200), np.float32(.237), np.float32(.275), np.float32(.294),
           np.float32(.309), np.float32(.318), np.float32(.328), np.float32(.332), np.float32(.328), np.float32(.323),
           np.float32(.313), np.float32(.304), np.float32(.285), np.float32(.200),
           np.float32(.140), np.float32(.090), np.float32(.049),
           ]
# 2P9 J=3  UNITS 10**-18    SCALE 1/E**2 ABOVE 100 EV

X2P9G5 = [np.float32(18.55511), np.float32(18.56), np.float32(18.57), np.float32(18.58), np.float32(18.59),
          np.float32(18.60), np.float32(18.61), np.float32(18.62),
          np.float32(18.63), np.float32(18.64),
          np.float32(18.65), np.float32(18.66), np.float32(18.67), np.float32(18.68), np.float32(18.69),
          np.float32(18.70), np.float32(18.71), np.float32(18.72), np.float32(18.73), np.float32(18.74),
          np.float32(18.75), np.float32(18.77), np.float32(18.80), np.float32(18.82), np.float32(18.85),
          np.float32(18.88), np.float32(18.90), np.float32(18.92), np.float32(18.94), np.float32(18.96),
          np.float32(18.97), np.float32(18.98), np.float32(18.99), np.float32(19.00), np.float32(19.10),
          np.float32(19.20), np.float32(19.30), np.float32(19.40), np.float32(19.50), np.float32(19.55),
          np.float32(19.59), np.float32(19.60), np.float32(19.70), np.float32(19.80), np.float32(19.90),
          np.float32(20.00), np.float32(20.10), np.float32(20.20), np.float32(20.30), np.float32(20.40),
          np.float32(20.6), np.float32(20.8), np.float32(21.0), np.float32(22.0), np.float32(24.0), np.float32(26.0),
          np.float32(28.0), np.float32(30.0), np.float32(32.0), np.float32(34.0),
          np.float32(38.0), np.float32(42.0), np.float32(46.0), np.float32(50.0), np.float32(55.0), np.float32(60.0),
          np.float32(70.0), np.float32(80.0), np.float32(90.0), np.float32(100.),
          ]
Y2P9G5 = [np.float32(0.0), np.float32(.093), np.float32(.157), np.float32(.233), np.float32(.183), np.float32(.114),
          np.float32(.092), np.float32(.132), np.float32(.102), np.float32(.116),
          np.float32(.164), np.float32(.322), np.float32(.472), np.float32(.392), np.float32(.286), np.float32(.218),
          np.float32(.175), np.float32(.148), np.float32(.133), np.float32(.123),
          np.float32(.119), np.float32(.116), np.float32(.120), np.float32(.124), np.float32(.131), np.float32(.139),
          np.float32(.147), np.float32(.163), np.float32(.193), np.float32(.300),
          np.float32(.320), np.float32(.180), np.float32(.128), np.float32(.131), np.float32(.135), np.float32(.142),
          np.float32(.151), np.float32(.159), np.float32(.171), np.float32(.179),
          np.float32(.213), np.float32(.143), np.float32(.178), np.float32(.195), np.float32(.215), np.float32(.205),
          np.float32(.222), np.float32(.242), np.float32(.257), np.float32(.268),
          np.float32(.286), np.float32(.307), np.float32(.328), np.float32(.418), np.float32(.465), np.float32(.503),
          np.float32(.513), np.float32(.503), np.float32(.484), np.float32(.456),
          np.float32(.404), np.float32(.332), np.float32(.285), np.float32(.256), np.float32(.204), np.float32(.171),
          np.float32(.128), np.float32(.097), np.float32(.078), np.float32(.062),
          ]
# 2P8 J=2  UNITS 10**-18    SCALE BY 1/E ABOVE 60 EV

X2P8G5 = [np.float32(18.57583), np.float32(18.58), np.float32(18.59), np.float32(18.60), np.float32(18.61),
          np.float32(18.62), np.float32(18.63), np.float32(18.64),
          np.float32(18.65), np.float32(18.66),
          np.float32(18.67), np.float32(18.68), np.float32(18.69), np.float32(18.70), np.float32(18.71),
          np.float32(18.72), np.float32(18.74), np.float32(18.76), np.float32(18.78), np.float32(18.80),
          np.float32(18.82), np.float32(18.84), np.float32(18.86), np.float32(18.88), np.float32(18.90),
          np.float32(18.92), np.float32(18.94), np.float32(18.96), np.float32(18.98), np.float32(19.00),
          np.float32(19.05), np.float32(19.10), np.float32(19.20), np.float32(19.30), np.float32(19.40),
          np.float32(19.50), np.float32(19.58), np.float32(19.60), np.float32(19.62), np.float32(19.65),
          np.float32(19.68), np.float32(19.70), np.float32(19.80), np.float32(19.90), np.float32(20.00),
          np.float32(20.10), np.float32(20.20), np.float32(20.40), np.float32(20.60), np.float32(20.80),
          np.float32(21.0), np.float32(22.0), np.float32(23.0), np.float32(24.0), np.float32(25.0), np.float32(26.0),
          np.float32(27.0), np.float32(28.0), np.float32(29.0), np.float32(30.0),
          np.float32(32.0), np.float32(34.0), np.float32(36.0), np.float32(38.0), np.float32(40.0), np.float32(42.0),
          np.float32(44.0), np.float32(46.0), np.float32(48.0), np.float32(50.0),
          np.float32(55.0), np.float32(60.0),
          ]
Y2P8G5 = [np.float32(0.0), np.float32(.142), np.float32(.198), np.float32(.206), np.float32(.250), np.float32(.193),
          np.float32(.158), np.float32(.172), np.float32(.403), np.float32(.506),
          np.float32(.467), np.float32(.420), np.float32(.381), np.float32(.353), np.float32(.326), np.float32(.308),
          np.float32(.275), np.float32(.249), np.float32(.229), np.float32(.214),
          np.float32(.201), np.float32(.195), np.float32(.192), np.float32(.192), np.float32(.194), np.float32(.200),
          np.float32(.215), np.float32(.271), np.float32(.206), np.float32(.177),
          np.float32(.177), np.float32(.179), np.float32(.185), np.float32(.192), np.float32(.200), np.float32(.207),
          np.float32(.205), np.float32(.243), np.float32(.228), np.float32(.224),
          np.float32(.228), np.float32(.192), np.float32(.218), np.float32(.239), np.float32(.260), np.float32(.272),
          np.float32(.289), np.float32(.315), np.float32(.339), np.float32(.364),
          np.float32(.385), np.float32(.437), np.float32(.475), np.float32(.513), np.float32(.537), np.float32(.546),
          np.float32(.551), np.float32(.551), np.float32(.546), np.float32(.532),
          np.float32(.513), np.float32(.494), np.float32(.475), np.float32(.456), np.float32(.437), np.float32(.423),
          np.float32(.408), np.float32(.394), np.float32(.385), np.float32(.370),
          np.float32(.337), np.float32(.313),
          ]
# 2P7 J=1  UNITS 10**-18    SCALE BY 1/E**2 ABOVE 60 EV

X2P7G5 = [np.float32(18.61270), np.float32(18.62), np.float32(18.63), np.float32(18.64), np.float32(18.65),
          np.float32(18.66), np.float32(18.67), np.float32(18.68),
          np.float32(18.69), np.float32(18.70),
          np.float32(18.71), np.float32(18.72), np.float32(18.74), np.float32(18.76), np.float32(18.80),
          np.float32(18.85), np.float32(18.90), np.float32(18.92), np.float32(18.93), np.float32(18.94),
          np.float32(18.95), np.float32(18.96), np.float32(18.97), np.float32(18.98), np.float32(18.99),
          np.float32(19.00), np.float32(19.05), np.float32(19.10), np.float32(19.20), np.float32(19.30),
          np.float32(19.50), np.float32(19.60), np.float32(19.68), np.float32(18.70), np.float32(19.80),
          np.float32(19.90), np.float32(20.00), np.float32(20.10), np.float32(20.20), np.float32(20.30),
          np.float32(20.4), np.float32(20.6), np.float32(20.8), np.float32(21.0), np.float32(21.5), np.float32(22.0),
          np.float32(23.0), np.float32(24.0), np.float32(25.0), np.float32(26.0),
          np.float32(27.0), np.float32(28.0), np.float32(30.0), np.float32(32.0), np.float32(34.0), np.float32(36.0),
          np.float32(38.0), np.float32(40.0), np.float32(42.0), np.float32(44.0),
          np.float32(46.0), np.float32(48.0), np.float32(50.0), np.float32(54.0), np.float32(60.0),
          ]
Y2P7G5 = [np.float32(0.0), np.float32(.123), np.float32(.127), np.float32(.095), np.float32(.145), np.float32(.153),
          np.float32(.126), np.float32(.104), np.float32(.091), np.float32(.085),
          np.float32(.080), np.float32(.077), np.float32(.072), np.float32(.067), np.float32(.061), np.float32(.060),
          np.float32(.066), np.float32(.071), np.float32(.076), np.float32(.082),
          np.float32(.096), np.float32(.118), np.float32(.112), np.float32(.074), np.float32(.066), np.float32(.067),
          np.float32(.070), np.float32(.075), np.float32(.084), np.float32(.088),
          np.float32(.099), np.float32(.101), np.float32(.115), np.float32(.101), np.float32(.114), np.float32(.122),
          np.float32(.126), np.float32(.117), np.float32(.124), np.float32(.134),
          np.float32(.141), np.float32(.154), np.float32(.164), np.float32(.177), np.float32(.198), np.float32(.215),
          np.float32(.232), np.float32(.244), np.float32(.252), np.float32(.252),
          np.float32(.250), np.float32(.248), np.float32(.243), np.float32(.233), np.float32(.218), np.float32(.201),
          np.float32(.184), np.float32(.169), np.float32(.156), np.float32(.144),
          np.float32(.134), np.float32(.124), np.float32(.117), np.float32(.103), np.float32(.081),
          ]
# 2P6 J=2  UNITS 10**-18   SCALE BY 1/E ABOVE 60 EV

X2P6G5 = [np.float32(18.63679), np.float32(18.64), np.float32(18.65), np.float32(18.66), np.float32(18.67),
          np.float32(18.68), np.float32(18.69), np.float32(18.70),
          np.float32(18.71), np.float32(18.72),
          np.float32(18.74), np.float32(18.76), np.float32(18.78), np.float32(18.80), np.float32(18.82),
          np.float32(18.84), np.float32(18.86), np.float32(18.90), np.float32(18.94), np.float32(18.96),
          np.float32(19.00), np.float32(19.05), np.float32(19.10), np.float32(19.20), np.float32(19.30),
          np.float32(19.40), np.float32(19.50), np.float32(19.60), np.float32(19.70), np.float32(19.80),
          np.float32(19.90), np.float32(20.00), np.float32(20.10), np.float32(20.20), np.float32(20.30),
          np.float32(20.40), np.float32(20.60), np.float32(20.80), np.float32(21.00), np.float32(21.50),
          np.float32(22.0), np.float32(23.0), np.float32(24.0), np.float32(26.0), np.float32(28.0), np.float32(30.0),
          np.float32(32.0), np.float32(34.0), np.float32(36.0), np.float32(38.0),
          np.float32(40.0), np.float32(42.0), np.float32(44.0), np.float32(46.0), np.float32(48.0), np.float32(50.0),
          np.float32(52.0), np.float32(54.0), np.float32(60.0),
          ]
Y2P6G5 = [np.float32(0.0), np.float32(.113), np.float32(.103), np.float32(.135), np.float32(.310), np.float32(.442),
          np.float32(.466), np.float32(.449), np.float32(.441), np.float32(.436),
          np.float32(.434), np.float32(.432), np.float32(.427), np.float32(.419), np.float32(.410), np.float32(.401),
          np.float32(.391), np.float32(.376), np.float32(.368), np.float32(.374),
          np.float32(.333), np.float32(.319), np.float32(.317), np.float32(.321), np.float32(.330), np.float32(.339),
          np.float32(.349), np.float32(.388), np.float32(.369), np.float32(.362),
          np.float32(.388), np.float32(.404), np.float32(.423), np.float32(.437), np.float32(.447), np.float32(.466),
          np.float32(.489), np.float32(.513), np.float32(.532), np.float32(.556),
          np.float32(.579), np.float32(.603), np.float32(.622), np.float32(.646), np.float32(.656), np.float32(.656),
          np.float32(.646), np.float32(.632), np.float32(.617), np.float32(.603),
          np.float32(.589), np.float32(.575), np.float32(.561), np.float32(.546), np.float32(.532), np.float32(.518),
          np.float32(.503), np.float32(.489), np.float32(.475),
          ]
# 2P5 J=1  UNITS 10**-18   SCALE BY 1/E**2 ABOVE 60 EV

X2P5G5 = [np.float32(18.69336), np.float32(18.70), np.float32(18.71), np.float32(18.72), np.float32(18.73),
          np.float32(18.74), np.float32(18.75), np.float32(18.76),
          np.float32(18.78), np.float32(18.80),
          np.float32(18.82), np.float32(18.84), np.float32(18.86), np.float32(18.88), np.float32(18.90),
          np.float32(18.92), np.float32(18.94), np.float32(18.96), np.float32(18.98), np.float32(19.00),
          np.float32(19.05), np.float32(19.10), np.float32(19.20), np.float32(19.30), np.float32(19.40),
          np.float32(19.50), np.float32(19.60), np.float32(19.67), np.float32(19.70), np.float32(19.80),
          np.float32(19.9), np.float32(20.0), np.float32(20.1), np.float32(20.2), np.float32(20.3), np.float32(20.4),
          np.float32(20.5), np.float32(20.6), np.float32(20.8), np.float32(21.0),
          np.float32(21.5), np.float32(22.0), np.float32(23.0), np.float32(24.0), np.float32(25.0), np.float32(26.0),
          np.float32(27.0), np.float32(28.0), np.float32(29.0), np.float32(30.0),
          np.float32(32.0), np.float32(34.0), np.float32(36.0), np.float32(38.0), np.float32(40.0), np.float32(42.0),
          np.float32(44.0), np.float32(46.0), np.float32(48.0), np.float32(50.0),
          np.float32(52.0), np.float32(54.0), np.float32(60.0),
          ]
Y2P5G5 = [np.float32(0.0), np.float32(.029), np.float32(.045), np.float32(.054), np.float32(.061), np.float32(.066),
          np.float32(.067), np.float32(.069), np.float32(.068), np.float32(.067),
          np.float32(.066), np.float32(.066), np.float32(.067), np.float32(.068), np.float32(.071), np.float32(.074),
          np.float32(.081), np.float32(.095), np.float32(.078), np.float32(.079),
          np.float32(.087), np.float32(.096), np.float32(.112), np.float32(.125), np.float32(.134), np.float32(.142),
          np.float32(.156), np.float32(.161), np.float32(.146), np.float32(.163),
          np.float32(.174), np.float32(.175), np.float32(.168), np.float32(.168), np.float32(.174), np.float32(.182),
          np.float32(.192), np.float32(.201), np.float32(.219), np.float32(.233),
          np.float32(.237), np.float32(.239), np.float32(.242), np.float32(.242), np.float32(.239), np.float32(.235),
          np.float32(.229), np.float32(.228), np.float32(.228), np.float32(.228),
          np.float32(.224), np.float32(.211), np.float32(.204), np.float32(.196), np.float32(.187), np.float32(.181),
          np.float32(.173), np.float32(.166), np.float32(.159), np.float32(.151),
          np.float32(.144), np.float32(.138), np.float32(.117),
          ]
# 2P4 J=2  UNITS 10**-18   SCALE BY 1/E ABOVE 60 EV

X2P4G5 = [np.float32(18.70407), np.float32(18.71), np.float32(18.72), np.float32(18.73), np.float32(18.74),
          np.float32(18.75), np.float32(18.76), np.float32(18.77),
          np.float32(18.78), np.float32(18.79),
          np.float32(18.80), np.float32(18.82), np.float32(18.84), np.float32(18.86), np.float32(18.88),
          np.float32(18.90), np.float32(18.92), np.float32(18.94), np.float32(18.96), np.float32(18.98),
          np.float32(19.00), np.float32(19.02), np.float32(19.10), np.float32(19.20), np.float32(19.30),
          np.float32(19.40), np.float32(19.50), np.float32(19.58), np.float32(19.60), np.float32(19.68),
          np.float32(19.70), np.float32(19.80), np.float32(19.90), np.float32(20.00), np.float32(20.10),
          np.float32(20.20), np.float32(20.30), np.float32(20.40), np.float32(20.60), np.float32(20.80),
          np.float32(21.0), np.float32(21.5), np.float32(22.0), np.float32(22.5), np.float32(23.0), np.float32(24.0),
          np.float32(25.0), np.float32(26.0), np.float32(27.0), np.float32(28.0),
          np.float32(29.0), np.float32(30.0), np.float32(31.0), np.float32(32.0), np.float32(34.0), np.float32(36.0),
          np.float32(38.0), np.float32(40.0), np.float32(42.0), np.float32(44.0),
          np.float32(46.0), np.float32(48.0), np.float32(50.0), np.float32(52.0), np.float32(54.0), np.float32(60.0),
          ]
Y2P4G5 = [np.float32(0.0), np.float32(.140), np.float32(.180), np.float32(.208), np.float32(.229), np.float32(.247),
          np.float32(.263), np.float32(.278), np.float32(.291), np.float32(.302),
          np.float32(.313), np.float32(.318), np.float32(.332), np.float32(.333), np.float32(.332), np.float32(.330),
          np.float32(.329), np.float32(.336), np.float32(.371), np.float32(.313),
          np.float32(.287), np.float32(.275), np.float32(.263), np.float32(.264), np.float32(.270), np.float32(.278),
          np.float32(.289), np.float32(.312), np.float32(.291), np.float32(.293),
          np.float32(.326), np.float32(.310), np.float32(.326), np.float32(.343), np.float32(.363), np.float32(.380),
          np.float32(.404), np.float32(.419), np.float32(.447), np.float32(.476),
          np.float32(.504), np.float32(.532), np.float32(.551), np.float32(.570), np.float32(.580), np.float32(.599),
          np.float32(.608), np.float32(.614), np.float32(.612), np.float32(.605),
          np.float32(.594), np.float32(.580), np.float32(.564), np.float32(.546), np.float32(.513), np.float32(.485),
          np.float32(.461), np.float32(.440), np.float32(.423), np.float32(.408),
          np.float32(.395), np.float32(.384), np.float32(.374), np.float32(.366), np.float32(.358), np.float32(.323),
          ]
# 2P3 J=0  UNITS 10**-18   SCALE BY 1/E ABOVE 60 EV

X2P3G5 = [np.float32(18.71138), np.float32(18.72), np.float32(18.73), np.float32(18.74), np.float32(18.75),
          np.float32(18.76), np.float32(18.77), np.float32(18.78),
          np.float32(18.79), np.float32(18.80),
          np.float32(18.82), np.float32(18.84), np.float32(18.86), np.float32(18.88), np.float32(18.90),
          np.float32(18.92), np.float32(18.94), np.float32(18.95), np.float32(18.96), np.float32(18.97),
          np.float32(18.98), np.float32(19.00), np.float32(19.10), np.float32(19.20), np.float32(19.30),
          np.float32(19.40), np.float32(19.50), np.float32(19.60), np.float32(19.70), np.float32(19.80),
          np.float32(19.9), np.float32(20.0), np.float32(20.1), np.float32(20.2), np.float32(20.3), np.float32(20.4),
          np.float32(20.6), np.float32(20.8), np.float32(21.0), np.float32(21.5),
          np.float32(22.0), np.float32(23.0), np.float32(24.0), np.float32(25.0), np.float32(26.0), np.float32(27.0),
          np.float32(28.0), np.float32(29.0), np.float32(30.0), np.float32(32.0),
          np.float32(34.0), np.float32(36.0), np.float32(38.0), np.float32(40.0), np.float32(42.0), np.float32(44.0),
          np.float32(46.0), np.float32(48.0), np.float32(50.0), np.float32(52.0),
          np.float32(54.0), np.float32(60.0),
          ]
Y2P3G5 = [np.float32(0.0), np.float32(.028), np.float32(.037), np.float32(.046), np.float32(.054), np.float32(.062),
          np.float32(.068), np.float32(.073), np.float32(.078), np.float32(.082),
          np.float32(.087), np.float32(.090), np.float32(.092), np.float32(.095), np.float32(.098), np.float32(.104),
          np.float32(.124), np.float32(.139), np.float32(.142), np.float32(.083),
          np.float32(.064), np.float32(.068), np.float32(.065), np.float32(.066), np.float32(.069), np.float32(.072),
          np.float32(.076), np.float32(.078), np.float32(.086), np.float32(.087),
          np.float32(.097), np.float32(.095), np.float32(.101), np.float32(.110), np.float32(.116), np.float32(.119),
          np.float32(.125), np.float32(.133), np.float32(.139), np.float32(.143),
          np.float32(.149), np.float32(.152), np.float32(.153), np.float32(.151), np.float32(.150), np.float32(.149),
          np.float32(.146), np.float32(.142), np.float32(.137), np.float32(.127),
          np.float32(.120), np.float32(.112), np.float32(.107), np.float32(.104), np.float32(.100), np.float32(.097),
          np.float32(.094), np.float32(.091), np.float32(.088), np.float32(.085),
          np.float32(.081), np.float32(.072),
          ]
# 2P2 J=1  UNITS 10**-18   SCALE BY 1/E**2 ABOVE 60 EV

X2P2G5 = [np.float32(18.72638), np.float32(18.73), np.float32(18.74), np.float32(18.75), np.float32(18.76),
          np.float32(18.77), np.float32(18.78), np.float32(18.79),
          np.float32(18.80), np.float32(18.82),
          np.float32(18.84), np.float32(18.86), np.float32(18.88), np.float32(18.90), np.float32(18.92),
          np.float32(18.94), np.float32(18.95), np.float32(18.96), np.float32(18.97), np.float32(18.98),
          np.float32(19.00), np.float32(19.10), np.float32(19.20), np.float32(19.30), np.float32(19.40),
          np.float32(19.50), np.float32(19.58), np.float32(19.60), np.float32(19.70), np.float32(19.80),
          np.float32(19.9), np.float32(20.0), np.float32(20.1), np.float32(20.2), np.float32(20.3), np.float32(20.4),
          np.float32(20.6), np.float32(20.8), np.float32(21.0), np.float32(21.5),
          np.float32(22.0), np.float32(23.0), np.float32(24.0), np.float32(25.0), np.float32(26.0), np.float32(27.0),
          np.float32(28.0), np.float32(29.0), np.float32(30.0), np.float32(32.0),
          np.float32(34.0), np.float32(36.0), np.float32(38.0), np.float32(40.0), np.float32(42.0), np.float32(44.0),
          np.float32(46.0), np.float32(48.0), np.float32(50.0), np.float32(52.0),
          np.float32(54.0), np.float32(60.0),
          ]
Y2P2G5 = [np.float32(0.0), np.float32(.006), np.float32(.025), np.float32(.046), np.float32(.063), np.float32(.078),
          np.float32(.090), np.float32(.099), np.float32(.109), np.float32(.122),
          np.float32(.128), np.float32(.131), np.float32(.133), np.float32(.137), np.float32(.134), np.float32(.143),
          np.float32(.154), np.float32(.179), np.float32(.163), np.float32(.137),
          np.float32(.125), np.float32(.128), np.float32(.140), np.float32(.150), np.float32(.159), np.float32(.166),
          np.float32(.183), np.float32(.163), np.float32(.187), np.float32(.187),
          np.float32(.198), np.float32(.201), np.float32(.204), np.float32(.203), np.float32(.204), np.float32(.207),
          np.float32(.209), np.float32(.211), np.float32(.215), np.float32(.223),
          np.float32(.228), np.float32(.233), np.float32(.238), np.float32(.238), np.float32(.235), np.float32(.226),
          np.float32(.219), np.float32(.214), np.float32(.207), np.float32(.192),
          np.float32(.178), np.float32(.163), np.float32(.150), np.float32(.140), np.float32(.129), np.float32(.122),
          np.float32(.115), np.float32(.108), np.float32(.103), np.float32(.096),
          np.float32(.090), np.float32(.078),
          ]
# 2P1 J=0 UNITS 10**-18   SCALE BY 1/E ABOVE 100 EV

X2P1G5 = [np.float32(18.96595), np.float32(18.97), np.float32(18.98), np.float32(18.99), np.float32(19.00),
          np.float32(19.01), np.float32(19.02), np.float32(19.03),
          np.float32(19.04), np.float32(19.06),
          np.float32(19.08), np.float32(19.10), np.float32(19.15), np.float32(19.20), np.float32(19.30),
          np.float32(19.40), np.float32(19.50), np.float32(19.57), np.float32(19.58), np.float32(19.60),
          np.float32(19.66), np.float32(19.70), np.float32(19.80), np.float32(19.90), np.float32(20.00),
          np.float32(20.10), np.float32(20.20), np.float32(20.30), np.float32(20.40), np.float32(20.60),
          np.float32(20.8), np.float32(21.0), np.float32(21.5), np.float32(22.0), np.float32(23.0), np.float32(24.0),
          np.float32(25.0), np.float32(26.0), np.float32(27.0), np.float32(28.0),
          np.float32(29.0), np.float32(30.0), np.float32(32.0), np.float32(34.0), np.float32(36.0), np.float32(38.0),
          np.float32(40.0), np.float32(42.0), np.float32(44.0), np.float32(46.0),
          np.float32(48.0), np.float32(50.0), np.float32(52.0), np.float32(54.0), np.float32(60.0), np.float32(70.0),
          np.float32(80.0), np.float32(90.0), np.float32(100.),
          ]
Y2P1G5 = [np.float32(0.0), np.float32(.134), np.float32(.170), np.float32(.194), np.float32(.206), np.float32(.216),
          np.float32(.223), np.float32(.230), np.float32(.235), np.float32(.243),
          np.float32(.250), np.float32(.256), np.float32(.269), np.float32(.280), np.float32(.303), np.float32(.327),
          np.float32(.345), np.float32(.279), np.float32(.437), np.float32(.411),
          np.float32(.342), np.float32(.352), np.float32(.371), np.float32(.394), np.float32(.418), np.float32(.442),
          np.float32(.461), np.float32(.480), np.float32(.499), np.float32(.541),
          np.float32(.580), np.float32(.618), np.float32(.722), np.float32(.826), np.float32(.969), np.float32(1.17),
          np.float32(1.35), np.float32(1.48), np.float32(1.60), np.float32(1.73),
          np.float32(1.81), np.float32(1.90), np.float32(1.97), np.float32(1.98), np.float32(1.99), np.float32(1.99),
          np.float32(1.98), np.float32(1.97), np.float32(1.97), np.float32(1.96),
          np.float32(1.95), np.float32(1.94), np.float32(1.92), np.float32(1.90), np.float32(1.86), np.float32(1.75),
          np.float32(1.61), np.float32(1.48), np.float32(1.38),
          ]
#

# 2S5 J=2  UNITS 10**-18    SCALE BY 1/E**2 ABOVE 50 EV

X2S5G5 = [np.float32(19.66403), np.float32(19.8), np.float32(19.9), np.float32(20.0), np.float32(20.5),
          np.float32(21.0), np.float32(22.0), np.float32(23.0), np.float32(24.0), np.float32(25.0),
          np.float32(26.0), np.float32(27.0), np.float32(28.0), np.float32(30.0), np.float32(32.0), np.float32(36.0),
          np.float32(40.0), np.float32(44.0), np.float32(50.0),
          ]
Y2S5G5 = [np.float32(0.0), np.float32(.0217), np.float32(.0374), np.float32(.0526), np.float32(.121), np.float32(.178),
          np.float32(.263), np.float32(.319), np.float32(.355), np.float32(.376),
          np.float32(.387), np.float32(.390), np.float32(.388), np.float32(.375), np.float32(.355), np.float32(.309),
          np.float32(.266), np.float32(.229), np.float32(.184),
          ]
# 2S4 J=1  RESONANCE LEVEL  USE BEF SCALING     F=0.0128     62.9743 NM

#

# 2S3 J=0  UNITS 10**-18    SCALE BY 1/E**2 ABOVE 50 EV

X2S3G5 = [np.float32(19.76060), np.float32(19.8), np.float32(19.9), np.float32(20.0), np.float32(20.5),
          np.float32(21.0), np.float32(22.0), np.float32(23.0), np.float32(24.0), np.float32(25.0),
          np.float32(26.0), np.float32(27.0), np.float32(28.0), np.float32(30.0), np.float32(32.0), np.float32(36.0),
          np.float32(40.0), np.float32(44.0), np.float32(50.0),
          ]
Y2S3G5 = [np.float32(0.0), np.float32(.0088), np.float32(.0245), np.float32(.0376), np.float32(.0870), np.float32(.122),
          np.float32(.168), np.float32(.195), np.float32(.209), np.float32(.215),
          np.float32(.216), np.float32(.214), np.float32(.209), np.float32(.196), np.float32(.181), np.float32(.151),
          np.float32(.126), np.float32(.105), np.float32(.081),
          ]
# 2S2 J=1  RESONANCE LEVEL  USE BEF SCALING     F=0.0166     62.6827 NM

#

# 3D6 J=0  UNITS 10**-18   SCALE BY 1/E**2 ABOVE 50 EV

X3D6G5 = [np.float32(20.02464), np.float32(22.0), np.float32(24.0), np.float32(26.0), np.float32(28.0),
          np.float32(30.0), np.float32(32.0), np.float32(34.0), np.float32(36.0), np.float32(40.0),
          np.float32(45.0), np.float32(50.0),
          ]
Y3D6G5 = [np.float32(0.0), np.float32(.013), np.float32(.022), np.float32(.029), np.float32(.032), np.float32(.033),
          np.float32(.032), np.float32(.030), np.float32(.025), np.float32(.020),
          np.float32(.016), np.float32(.011),
          ]
# 3D5 J=1 RESONANCE LEVEL  USE BEF SCALING      F=0.0048     61.9106 NM

#

# 3D4! J=4  UNITS 10**-18   SCALE BY 1/E**2 ABOVE 50 EV

X3D4PG5 = [np.float32(20.03465), np.float32(22.0), np.float32(24.0), np.float32(26.0), np.float32(28.0),
           np.float32(30.0), np.float32(32.0), np.float32(34.0), np.float32(36.0), np.float32(40.0),
           np.float32(45.0), np.float32(50.0),
           ]
Y3D4PG5 = [np.float32(0.0), np.float32(.013), np.float32(.022), np.float32(.029), np.float32(.032), np.float32(.033),
           np.float32(.032), np.float32(.030), np.float32(.025), np.float32(.020),
           np.float32(.016), np.float32(.011),
           ]
# 3D4  J=3  UNITS 10**-18   SCALE BY 1/E**2 ABOVE 50 EV

X3D4G5 = [np.float32(20.03487), np.float32(22.0), np.float32(24.0), np.float32(26.0), np.float32(28.0),
          np.float32(30.0), np.float32(32.0), np.float32(34.0), np.float32(36.0), np.float32(40.0),
          np.float32(45.0), np.float32(50.0),
          ]
Y3D4G5 = [np.float32(0.0), np.float32(.013), np.float32(.022), np.float32(.029), np.float32(.032), np.float32(.033),
          np.float32(.032), np.float32(.030), np.float32(.025), np.float32(.020),
          np.float32(.016), np.float32(.011),
          ]
# 3D3  J=2  UNITS 10**-18  SCALE BY 1/E**2 ABOVE  50 EV

X3D3G5 = [np.float32(20.03675), np.float32(22.0), np.float32(24.0), np.float32(26.0), np.float32(28.0),
          np.float32(30.0), np.float32(32.0), np.float32(34.0), np.float32(36.0), np.float32(40.0),
          np.float32(45.0), np.float32(50.0),
          ]
Y3D3G5 = [np.float32(0.0), np.float32(.013), np.float32(.022), np.float32(.029), np.float32(.032), np.float32(.033),
          np.float32(.032), np.float32(.030), np.float32(.025), np.float32(.020),
          np.float32(.016), np.float32(.011),
          ]
# 3D2 J=1 RESONANCE LEVEL   USE BEF SCALING      F=0.0146    61.8676 NM

#

# 3D1!! J=2  UNITS 10**-18  SCALE BY 1/E**2 ABOVE 50 EV

X3D1PPG5 = [np.float32(20.04820), np.float32(22.0), np.float32(24.0), np.float32(26.0), np.float32(28.0),
            np.float32(30.0), np.float32(32.0), np.float32(34.0), np.float32(36.0), np.float32(40.0),
            np.float32(45.0), np.float32(50.0),
            ]
Y3D1PPG5 = [np.float32(0.0), np.float32(.013), np.float32(.022), np.float32(.029), np.float32(.032), np.float32(.033),
            np.float32(.032), np.float32(.030), np.float32(.025), np.float32(.020),
            np.float32(.016), np.float32(.011),
            ]
# 3D1! J=3  UNITS 10**-18  SCALE BY 1/E**2 ABOVE 50 EV

X3D1PG5 = [np.float32(20.04842), np.float32(22.0), np.float32(24.0), np.float32(26.0), np.float32(28.0),
           np.float32(30.0), np.float32(32.0), np.float32(34.0), np.float32(36.0), np.float32(40.0),
           np.float32(45.0), np.float32(50.0),
           ]
Y3D1PG5 = [np.float32(0.0), np.float32(.013), np.float32(.022), np.float32(.029), np.float32(.032), np.float32(.033),
           np.float32(.032), np.float32(.030), np.float32(.025), np.float32(.020),
           np.float32(.016), np.float32(.011),
           ]
# 3S1!!!! J=2  UNITS 10**-18 SCALE BY 1/E**2 ABOVE 50 EV

X3S1PPPPG5 = [np.float32(20.13611), np.float32(22.), np.float32(24.), np.float32(26.0), np.float32(28.0),
              np.float32(30.0), np.float32(32.0), np.float32(34.0), np.float32(36.0), np.float32(40.0),
              np.float32(45.0), np.float32(50.0),
              ]
Y3S1PPPPG5 = [np.float32(0.0), np.float32(.013), np.float32(.022), np.float32(.029), np.float32(.032), np.float32(.033),
              np.float32(.032), np.float32(.030), np.float32(.025), np.float32(.020),
              np.float32(.016), np.float32(.011),
              ]
# 3S1!!! J=3   UNITS 10**-18 SCALE BY 1/E**2 ABOVE 50 EV

X3S1PPPG5 = [np.float32(20.13629), np.float32(22.), np.float32(24.), np.float32(26.0), np.float32(28.0),
             np.float32(30.0), np.float32(32.0), np.float32(34.0), np.float32(36.0), np.float32(40.0),
             np.float32(45.0), np.float32(50.0),
             ]
Y3S1PPPG5 = [np.float32(0.0), np.float32(.013), np.float32(.022), np.float32(.029), np.float32(.032), np.float32(.033),
             np.float32(.032), np.float32(.030), np.float32(.025), np.float32(.020),
             np.float32(.016), np.float32(.011),
             ]
# 3S1!! J=2    UNITS 10**-18 SCALE BY 1/E**2 ABOVE 50 EV

X3S1PPG5 = [np.float32(20.13751), np.float32(22.), np.float32(24.), np.float32(26.0), np.float32(28.0),
            np.float32(30.0), np.float32(32.0), np.float32(34.0), np.float32(36.0), np.float32(40.0),
            np.float32(45.0), np.float32(50.0),
            ]
Y3S1PPG5 = [np.float32(0.0), np.float32(.013), np.float32(.022), np.float32(.029), np.float32(.032), np.float32(.033),
            np.float32(.032), np.float32(.030), np.float32(.025), np.float32(.020),
            np.float32(.016), np.float32(.011),
            ]
# 3S1! J=1 RESONANCE LEVEL  USE BEF SCALING      F=0.00676   61.5632 NM

#

# 3P SUM 3P10-3P6  UNITS 10**-18  SCALE BY 1/E**1.5  ABOVE 50 EV

X3P106G5 = [np.float32(20.14965), np.float32(21.0), np.float32(22.0), np.float32(23.0), np.float32(24.0),
            np.float32(25.0), np.float32(26.0), np.float32(27.0), np.float32(28.0), np.float32(30.0),
            np.float32(32.0), np.float32(34.0), np.float32(36.0), np.float32(38.0), np.float32(40.0), np.float32(50.0),
            ]
Y3P106G5 = [np.float32(0.0), np.float32(.110), np.float32(.178), np.float32(.242), np.float32(.275), np.float32(.320),
            np.float32(.363), np.float32(.418), np.float32(.450), np.float32(.500),
            np.float32(.500), np.float32(.480), np.float32(.460), np.float32(.440), np.float32(.410), np.float32(.330),
            ]
# 3P SUM 3P5-3P2  UNITS 10**-18  SCALE BY 1/E**1.5  ABOVE 50 EV

X3P52G5 = [np.float32(20.25918), np.float32(21.0), np.float32(22.0), np.float32(23.0), np.float32(24.0),
           np.float32(25.0), np.float32(26.0), np.float32(27.0), np.float32(28.0), np.float32(30.0),
           np.float32(32.0), np.float32(34.0), np.float32(36.0), np.float32(38.0), np.float32(40.0), np.float32(50.0),
           ]
Y3P52G5 = [np.float32(0.0), np.float32(.088), np.float32(.142), np.float32(.194), np.float32(.220), np.float32(.256),
           np.float32(.290), np.float32(.335), np.float32(.360), np.float32(.400),
           np.float32(.400), np.float32(.380), np.float32(.370), np.float32(.350), np.float32(.330), np.float32(.270),
           ]
# 3P1 J=0  UNITS 10**-18   SCALE 1/E  BY ABOVE 50 EV

X3P1G5 = [np.float32(20.36885), np.float32(21.0), np.float32(22.0), np.float32(23.0), np.float32(24.0),
          np.float32(25.0), np.float32(26.0), np.float32(27.0), np.float32(28.0), np.float32(30.0),
          np.float32(32.0), np.float32(34.0), np.float32(36.0), np.float32(38.0), np.float32(40.0), np.float32(50.0),
          ]
Y3P1G5 = [np.float32(0.0), np.float32(.050), np.float32(.100), np.float32(.125), np.float32(.145), np.float32(.165),
          np.float32(.175), np.float32(.185), np.float32(.192), np.float32(.200),
          np.float32(.205), np.float32(.207), np.float32(.207), np.float32(.205), np.float32(.205), np.float32(.190),
          ]
#  HIGH RESONANCE LEVELS :

#

# 3S4  J=1  RESONANCE LEVEL  USE BEF SCALING     F=0.00635   60.2730 NM

# 3S2  J=1  RESONANCE LEVEL  USE BEF SCALING     F=0.0044    60.0041 NM

# 4D5  J=1  RESONANCE LEVEL  USE BEF SCALING     F=0.00705   59.8895 NM

# 4D2  J=1  RESONANCE LEVEL  USE BEF SCALING     F=0.00235   59.8710 NM

# 4S1! J=1  RESONANCE LEVEL  USE BEF SCALING     F=0.00435   59.5924 NM

# 4S4  J=1  RESONANCE LEVEL  USE BEF SCALING     F=0.00325   59.1834 NM

# 5D5  J=1  RESONANCE LEVEL  USE BEF SCALING     F=0.00383   59.0015 NM

# 5D2  J=1  RESONANCE LEVEL  USE BEF SCALING     F=0.00127   58.9915 NM

# 4S2  J=1  RESONANCE LEVEL  USE BEF SCALING     F=0.00165   58.9183 NM

# 5S1! J=1  RESONANCE LEVEL  USE BEF SCALING     F=0.0025    58.7217 NM

# SUM S STATES 5-INFINITY USE BEF SCALING        F=0.00962

# SUM D STATES 6-INFINITY USE BEF SCALING        F=0.01695

#  TOTAL OSCILLATOR SUM  F = 0.2926

#

# BREMSSTRAHLUNG X-SECTION WITH CUT OFF

Z10TG5 = [np.float32(671.), np.float32(424.), np.float32(215.), np.float32(123.), np.float32(69.3), np.float32(32.5),
          np.float32(18.8), np.float32(11.8), np.float32(7.95), np.float32(7.19),
          np.float32(7.27), np.float32(7.42), np.float32(7.59), np.float32(7.71), np.float32(7.80), np.float32(7.94),
          np.float32(8.05), np.float32(8.19), np.float32(8.29), np.float32(8.40),
          np.float32(8.47), np.float32(8.51), np.float32(8.52), np.float32(8.56), np.float32(8.57),
          ]
# UNITS 10**-24

EBRMG5 = [np.float32(1000.), np.float32(2000.), np.float32(5000.), np.float32(1.E4), np.float32(2.E4), np.float32(5.E4),
          np.float32(1.E5), np.float32(2.E5), np.float32(5.E5), np.float32(1.E6),
          np.float32(2.E6), np.float32(3.E6), np.float32(4.E6), np.float32(5.E6), np.float32(6.E6), np.float32(8.E6),
          np.float32(1.E7), np.float32(1.5E7), np.float32(2.E7), np.float32(3.E7),
          np.float32(4.E7), np.float32(5.E7), np.float32(6.E7), np.float32(8.E7), np.float32(1.E8),
          ]
EING5 = [np.float32(16.61907), np.float32(16.67083), np.float32(16.71538), np.float32(16.84805), np.float32(18.38162),
         np.float32(18.55511), np.float32(18.57583), np.float32(18.61270), np.float32(18.63679), np.float32(18.69336),
         np.float32(18.70407), np.float32(18.71138), np.float32(18.72638), np.float32(18.96595), np.float32(19.66403),
         np.float32(19.68819), np.float32(19.76060), np.float32(19.77977), np.float32(20.02464), np.float32(20.02644),
         np.float32(20.03465), np.float32(20.03487), np.float32(20.03675), np.float32(20.04039), np.float32(20.04820),
         np.float32(20.04842), np.float32(20.13611), np.float32(20.13629), np.float32(20.13751), np.float32(20.13946),
         np.float32(20.14965), np.float32(20.25918), np.float32(20.36885), np.float32(20.57056), np.float32(20.66277),
         np.float32(20.70230), np.float32(20.70871), np.float32(20.80551), np.float32(20.94928), np.float32(21.01388),
         np.float32(21.01743), np.float32(21.04354), np.float32(21.11401), np.float32(21.14638), np.float32(21.18286),
         np.float32(0.0), ]
for J in range(250 - 46):
    EING5.append(0.0)
gd['gas5/XEN'] = XENG5
gd['gas5/YXSEC'] = YXSECG5
gd['gas5/XEL'] = XELG5
gd['gas5/YEL'] = YELG5
gd['gas5/XEPS'] = XEPSG5
gd['gas5/YEPS'] = YEPSG5
gd['gas5/XION'] = XIONG5
gd['gas5/YION'] = YIONG5
gd['gas5/YINC'] = YINCG5
gd['gas5/YIN1'] = YIN1G5
gd['gas5/XIN2'] = XIN2G5
gd['gas5/YIN2'] = YIN2G5
gd['gas5/XIN3'] = XIN3G5
gd['gas5/YIN3'] = YIN3G5
gd['gas5/XKSH'] = XKSHG5
gd['gas5/YKSH'] = YKSHG5
gd['gas5/X1S5'] = X1S5G5
gd['gas5/Y1S5'] = Y1S5G5
gd['gas5/X1S4'] = X1S4G5
gd['gas5/Y1S4'] = Y1S4G5
gd['gas5/X1S3'] = X1S3G5
gd['gas5/Y1S3'] = Y1S3G5
gd['gas5/X1S2'] = X1S2G5
gd['gas5/Y1S2'] = Y1S2G5
gd['gas5/X2P10'] = X2P10G5
gd['gas5/Y2P10'] = Y2P10G5
gd['gas5/X2P9'] = X2P9G5
gd['gas5/Y2P9'] = Y2P9G5
gd['gas5/X2P8'] = X2P8G5
gd['gas5/Y2P8'] = Y2P8G5
gd['gas5/X2P7'] = X2P7G5
gd['gas5/Y2P7'] = Y2P7G5
gd['gas5/X2P6'] = X2P6G5
gd['gas5/Y2P6'] = Y2P6G5
gd['gas5/X2P5'] = X2P5G5
gd['gas5/Y2P5'] = Y2P5G5
gd['gas5/X2P4'] = X2P4G5
gd['gas5/Y2P4'] = Y2P4G5
gd['gas5/X2P3'] = X2P3G5
gd['gas5/Y2P3'] = Y2P3G5
gd['gas5/X2P2'] = X2P2G5
gd['gas5/Y2P2'] = Y2P2G5
gd['gas5/X2P1'] = X2P1G5
gd['gas5/Y2P1'] = Y2P1G5
gd['gas5/X2S5'] = X2S5G5
gd['gas5/Y2S5'] = Y2S5G5
gd['gas5/X2S3'] = X2S3G5
gd['gas5/Y2S3'] = Y2S3G5
gd['gas5/X3D6'] = X3D6G5
gd['gas5/Y3D6'] = Y3D6G5
gd['gas5/X3D4P'] = X3D4PG5
gd['gas5/Y3D4P'] = Y3D4PG5
gd['gas5/X3D4'] = X3D4G5
gd['gas5/Y3D4'] = Y3D4G5
gd['gas5/X3D3'] = X3D3G5
gd['gas5/Y3D3'] = Y3D3G5
gd['gas5/X3D1PP'] = X3D1PPG5
gd['gas5/Y3D1PP'] = Y3D1PPG5
gd['gas5/X3D1P'] = X3D1PG5
gd['gas5/Y3D1P'] = Y3D1PG5
gd['gas5/X3S1PPPP'] = X3S1PPPPG5
gd['gas5/Y3S1PPPP'] = Y3S1PPPPG5
gd['gas5/X3S1PPP'] = X3S1PPPG5
gd['gas5/Y3S1PPP'] = Y3S1PPPG5
gd['gas5/X3S1PP'] = X3S1PPG5
gd['gas5/Y3S1PP'] = Y3S1PPG5
gd['gas5/X3P106'] = X3P106G5
gd['gas5/Y3P106'] = Y3P106G5
gd['gas5/X3P52'] = X3P52G5
gd['gas5/Y3P52'] = Y3P52G5
gd['gas5/X3P1'] = X3P1G5
gd['gas5/Y3P1'] = Y3P1G5
gd['gas5/Z10T'] = Z10TG5
gd['gas5/EBRM'] = EBRMG5
gd['gas5/EIN'] = EING5

# gas 6
# ELASTIC MOMENTUM TRANSFER

XENG6 = [1.e-6, .001, .003, .005, .007, 0.01, .015, 0.02, 0.03, 0.04,
         0.05, 0.06, 0.07, 0.08, 0.09, 0.10, 0.12, 0.14, 0.17, 0.20,
         0.25, 0.30, 0.35, 0.40, 0.45, 0.50, 0.52, 0.54, 0.56, 0.60,
         0.70, 0.80, 0.90, 1.00, 1.20, 1.40, 1.75, 2.00, 2.50, 3.00,
         3.30, 3.60, 4.00, 4.40, 4.80, 5.20, 5.60, 6.00, 6.50, 7.00,
         7.50, 8.00, 8.50, 9.00, 10.0, 11.0, 12.0, 13.0, 14.0, 15.0,
         16.0, 20.0, 30.0, 40.0, 50.0, 60.0, 75.0, 100., 150., 200.,
         300., 400., 500., 700., 1000., 1250., 1500., 1750., 2000., 2500.,
         3000., 3500., 4000., 4500., 5000., 6000., 7000., 8000., 9000., 1.0e4,
         1.25e4, 1.5e4, 1.75e4, 2.0e4, 2.5e4, 3.0e4, 3.5e4, 4.0e4, 5.0e4, 6.0e4,
         8.0e4, 1.0e5, 1.25e5, 1.5e5, 1.75e5, 2.0e5, 2.5e5, 3.0e5, 3.5e5, 4.0e5,
         4.5e5, 5.0e5, 6.0e5, 7.0e5, 8.0e5, 9.0e5, 1.0e6, 1.25e6, 1.5e6, 1.75e6,
         2.0e6, 2.5e6, 3.0e6, 3.5e6, 4.0e6, 4.5e6, 5.0e6, 6.0e6, 7.0e6, 8.0e6,
         9.0e6, 1.0e7, 1.25e7, 1.5e7, 1.75e7, 2.0e7, 2.5e7, 3.0e7, 3.5e7, 4.0e7,
         4.5e7, 5.0e7, 6.0e7, 7.0e7, 8.0e7, 9.0e7, 1.0e8, 1.25e8, 1.5e8, 1.75e8,
         2.0e8, 2.5e8, 3.0e8, 3.5e8, 4.0e8, 4.5e8, 5.0e8, 6.0e8, 7.0e8, 8.0e8,
         9.0e8, 1.0e9]
# ELFORD UP TO 2.0 EV THEN FIT TO NAKAMURA eRIFT VELOCITY

YXSECG6 = [37.4, 33.1, 30.0, 27.9, 26.2, 24.2, 21.6, 19.5, 16.3, 13.9,
           12.1, 10.6, 9.30, 8.27, 7.29, 6.55, 5.27, 4.30, 3.18, 2.37,
           1.47, .908, .548, .321, .184, .111, .0956, .0870, .0844, .0945,
           .187, .339, .525, .729, 1.15, 1.63, 2.60, 3.38, 4.75, 6.35,
           7.32, 8.28, 9.51, 10.7, 11.9, 13.2, 14.3, 15.3, 16.6, 17.7,
           18.6, 19.0, 18.9, 18.7, 18.1, 17.1, 15.7, 14.2, 12.7, 11.1,
           9.60, 6.50, 2.95, 1.95, 1.40, 1.25, 1.20, 1.18, 0.94, 0.80,
           0.64, 0.54, 0.48, 0.41, .340, .270, .222, .183, .154, .113,
           .0881, .0711, .0591, .0501, .0432, .033, .026, .0212, .0176, .0149,
           .0104, .00778, .00605, .00486, .00336, .00248, .00192, .00153, .00105,
           .000773,
           4.76e-4, 3.28e-4, 2.26e-4, 1.68e-4, 1.30e-4, 1.05e-4, 7.35e-5, 5.51e-5,
           4.33e-5, 3.53e-5,
           2.94e-5, 2.51e-5, 1.90e-5, 1.51e-5, 1.23e-5, 1.03e-5, 8.81e-6, 6.19e-6,
           4.68e-6, 3.69e-6,
           2.99e-6, 2.10e-6, 1.57e-6, 1.22e-6, 9.76e-7, 8.02e-7, 6.71e-7, 4.92e-7,
           3.77e-7, 2.99e-7,
           2.43e-7, 2.02e-7, 1.35e-7, 9.74e-8, 7.36e-8, 5.76e-8, 3.81e-8, 2.71e-8,
           2.02e-8, 1.57e-8,
           1.25e-8, 1.02e-8, 7.13e-9, 5.26e-9, 4.03e-9, 3.19e-9, 2.58e-9, 1.65e-9,
           1.14e-9, 8.40e-10,
           6.43e-10, 4.11e-10, 2.85e-10, 2.09e-10, 1.60e-10, 1.26e-10, 1.02e-10,
           7.10e-11, 5.21e-11, 3.99e-11,
           3.15e-11, 2.55e-11]
# ELASTIC   CONSISTENT WITHIN 1% OF TOTAL X-SECTION SUM

XELG6 = [1.e-6, .001, .003, .005, .007, 0.01, .015, 0.02, 0.03, 0.04,
         0.05, 0.06, 0.07, 0.08, 0.09, 0.10, 0.12, 0.14, 0.17, 0.20,
         0.25, 0.30, 0.35, 0.40, 0.45, 0.50, 0.55, 0.60, 0.65, 0.70,
         0.72, 0.74, 0.76, 0.80, 0.85, 0.90, 0.95, 1.00, 1.10, 1.20,
         1.30, 1.40, 1.50, 1.75, 2.00, 2.25, 2.50, 3.00, 3.50, 4.00,
         5.00, 6.00, 7.00, 8.00, 9.00, 10.0, 11.0, 12.0, 13.0, 14.0,
         15.0, 16.0, 18.0, 20.0, 22.5, 25.0, 27.5, 30.0, 35.0, 40.0,
         45.0, 50.0, 60.0, 70.0, 80.0, 90.0, 100., 125., 150., 175.,
         200., 250., 300., 400., 500., 600., 700., 800., 1000., 1200.,
         1500., 1800., 2000., 2500., 3000., 3500., 4000., 4500., 5000., 5500.,
         6.0e3, 7.0e3, 8.0e3, 1.0e4, 1.25e4, 1.5e4, 1.75e4, 2.0e4, 2.5e4, 3.0e4,
         3.5e4, 4.0e4, 5.0e4, 6.0e4, 8.0e4, 1.0e5, 1.25e5, 1.5e5, 1.75e5, 2.0e5,
         2.5e5, 3.0e5, 3.5e5, 4.0e5, 4.5e5, 5.0e5, 6.0e5, 7.0e5, 8.0e5, 9.0e5,
         1.0e6, 1.25e6, 1.5e6, 1.75e6, 2.0e6, 2.5e6, 3.0e6, 3.5e6, 4.0e6, 4.5e6,
         5.0e6, 6.0e6, 7.0e6, 8.0e6, 9.0e6, 1.0e7, 1.25e7, 1.5e7, 1.75e7, 2.0e7,
         1.e9
         ]
YELG6 = [37.4, 34.6, 31.8, 29.9, 28.4, 26.6, 24.1, 22.2, 19.1, 16.8,
         14.9, 13.4, 12.1, 11.0, 10.0, 9.15, 7.71, 6.56, 5.21, 4.38,
         3.22, 2.31, 1.75, 1.30, 1.04, 0.83, 0.65, 0.60, 0.58, 0.58,
         0.59, 0.60, 0.62, 0.66, 0.73, 0.81, 0.90, 0.98, 1.17, 1.41,
         1.66, 1.96, 2.25, 3.14, 3.99, 4.74, 5.62, 7.66, 9.59, 12.0,
         16.0, 20.1, 23.0, 25.9, 27.2, 28.1, 28.2, 28.2, 27.5, 26.6,
         25.7, 24.2, 22.0, 20.5, 19.3, 17.4, 15.8, 14.9, 12.9, 11.7,
         10.8, 9.88, 8.85, 8.00, 7.12, 6.44, 5.84, 5.08, 4.38, 4.15,
         3.70, 3.56, 3.15, 2.90, 2.62, 2.44, 2.25, 2.20, 1.92, 1.72,
         1.61, 1.41, 1.40, 1.28, 1.13, 1.06, .951, .895, .826, .798,
         .744, .668, .617, .526, .450, .396, .354, .321, .272, .237,
         # SMOOTH JOIN TO SALVAT BETWEEN E=10**5 AND 2*10**5 EV
         .211, .191, .161, .141, .114, .0973, .0817, .0709, .0630, .0568,
         .0504, .0461, .0430, .0408, .0390, .0376, .0356, .0342, .0332, .0324,
         .0318, .0308, .0301, .0297, .0294, .0290, .0288, .0286, .0285, .0284,
         .0284, .0283, .0283, .0283, .0282, .0282, .0282, .0282, .0282, .0282,
         .0282]
# ELASTIC ANGULAR DISTRIBUTION (EPSILON)

XEPSG6 = [0.00, .001, .003, .005, .007, .010, .015, .020, .030, .040,
          0.05, 0.06, 0.07, 0.08, 0.09, 0.10, 0.12, 0.14, 0.17, 0.20,
          0.25, 0.30, 0.35, 0.40, 0.45, 0.50, 0.52, 0.54, 0.55, 0.56,
          0.60, 0.65, 0.70, 0.72, 0.74, 0.76, 0.80, 0.85, 0.90, 0.95,
          1.00, 1.10, 1.20, 1.30, 1.40, 1.50, 1.75, 2.00, 2.25, 2.50,
          3.00, 3.50, 4.00, 5.20, 5.60, 6.00, 6.50, 7.00, 7.50, 8.00,
          9.00, 10.0, 11.0, 12.0, 13.0, 14.0, 15.0, 16.0, 18.0, 20.0,
          22.5, 25.0, 27.5, 30.0, 35.0, 40.0, 45.0, 50.0, 60.0, 70.0,
          75.0, 80.0, 90.0, 100., 125., 150., 175., 200., 250., 300.,
          400., 500., 600., 700., 800., 1000., 1200., 1250., 1500., 1750.,
          1800., 2000., 2500., 3000., 3500., 4000., 4500., 5000., 5500., 6000.,
          7000., 8000., 9000., 1.0e4, 1.25e4, 1.5e4, 1.75e4, 2.0e4, 2.5e4, 3.0e4,
          3.5e4, 4.0e4, 5.0e4, 6.0e4, 8.0e4, 1.0e5, 1.25e5, 1.5e5, 1.75e5, 2.0e5,
          2.5e5, 3.0e5, 3.5e5, 4.0e5, 4.5e5, 5.0e5, 6.0e5, 7.0e5, 8.0e5, 9.0e5,
          1.0e6, 1.25e6, 1.5e6, 1.75e6, 2.0e6, 2.5e6, 3.0e6, 3.5e6, 4.0e6, 4.5e6,
          5.0e6, 6.0e6, 7.0e6, 8.0e6, 9.0e6, 1.0e7, 1.25e7, 1.5e7, 1.75e7, 2.0e7,
          2.5e7, 3.0e7, 3.5e7, 4.0e7, 4.5e7, 5.0e7, 6.0e7, 7.0e7, 8.0e7, 9.0e7,
          1.0e8, 1.25e8, 1.5e8, 1.75e8, 2.0e8, 2.5e8, 3.0e8, 3.5e8, 4.0e8, 4.5e8,
          5.0e8, 6.0e8, 7.0e8, 8.0e8, 9.0e8, 1.0e9]
# ELASTIC ANGULAR DISTRIBUTION PARAMETER EPSILON
# EPSILON= 1.0-YEPS

YEPSG6 = [1., .935, .9152, .8999, .8841, .8652, .8452, .8187, .7822, .7445,
          .7225, .6926, .6611, .6378, .6066, .5887, .5459, .5096, .4533, .3720,
          .2822, .2221, .1554, .1082, .0662, .0445, .0416, .0417, .0432, .0442,
          .0561, .0948, .1626, .1941, .2313, .2662, .3416, .4243, .5002, .5662,
          .6269, .6968, .7276, .7502, .7506, .7627, .7454, .7730, .7714, .7703,
          .7468, .7483, .6947, .6838, .6672, .6508, .6610, .6625, .6480, .6128,
          .5511, .4952, .4485, .3897, .3447, .3034, .2581, .2253, .1925, .1585,
          .1198, .1009, .0890, .0780, .0712, .0608, .0537, .0483, .0480, .0536,
          .0567, .0618, .0706, .0804, .0796, .0878, .0848, .0888, .0784, .0810,
          .0713, .0697, .0695, .0691, .0694, .0663, .0578, .0560, .0481, .0407,
          .0394, .0346, .0244, .0213, .0177, .0157, .0139, .0126, .0110, .0090,
          .0086, .0074, .0065, .0058, .0045, .0037, .0031, .0027, .0023, .0017,
          .0015, .00126, 9.84e-4, 8.03e-4, 5.85e-4, 4.56e-4, 3.64e-4, 3.04e-4,
          2.60e-4, 2.28e-4,
          1.746e-4, 1.395e-4, 1.149e-4, 9.68e-5, 8.30e-5, 7.22e-5, 5.64e-5,
          4.55e-5, 3.76e-5, 3.17e-5,
          2.72e-5, 1.91e-5, 1.43e-5, 1.12e-5, 9.02e-6, 6.21e-6, 4.54e-6, 3.47e-6,
          2.74e-6, 2.22e-6,
          1.83e-6, 1.31e-6, 9.90e-7, 7.67e-7, 6.15e-7, 5.03e-7, 3.28e-7, 2.31e-7,
          1.71e-7, 1.32e-7,
          8.46e-8, 5.88e-8, 4.31e-8, 3.29e-8, 2.58e-8, 2.08e-8, 1.43e-8, 1.03e-8,
          7.80e-9, 6.10e-9,
          4.87e-9, 3.04e-9, 2.07e-9, 1.49e-9, 1.12e-9, 7.0e-10, 4.8e-10, 3.5e-10,
          2.6e-10, 2.0e-10,
          1.6e-10, 1.1e-10, 8.1e-11, 6.1e-11, 4.7e-11, 3.8e-11]
# IONISATION ( VALUES ABOVE 1OKEV GENERATEe BY BORN BETHE IN SUB)

XIONG6 = [13.9996, 14.5, 15.0, 15.5, 16.0, 16.5, 17.0, 17.5, 18.0, 18.5,
          19.0, 19.5, 20.0, 21.0, 22.0, 23.0, 24.0, 26.0, 28.0, 30.0,
          32.0, 34.0, 36.0, 38.0, 40.0, 45.0, 50.0, 55.0, 60.0, 65.0,
          70.0, 80.0, 90.0, 100., 120., 140., 160., 180., 200., 250.,
          300., 400., 500., 600., 700., 800., 900., 1000., 1200., 1400.,
          1600., 1800., 2000., 2500., 3000., 3500., 4000., 4500., 5000., 5500.,
          6000., 7000., 8000., 9000., 10000.]
# GROSS IONISATION

YIONG6 = [0.00, .078, .160, .255, .360, .450, .552, .655, .766, .878,
          .980, 1.09, 1.20, 1.34, 1.53, 1.63, 1.84, 2.19, 2.43, 2.66,
          2.86, 3.02, 3.15, 3.27, 3.37, 3.55, 3.73, 3.86, 3.96, 4.06,
          4.09, 4.15, 4.13, 4.09, 3.97, 3.79, 3.63, 3.47, 3.34, 3.02,
          2.76, 2.37, 2.07, 1.86, 1.69, 1.53, 1.42, 1.31, 1.15, 1.03,
          .930, .854, .781, .667, .579, .510, .458, .415, .387, .356,
          .332, .293, .264, .240, .219]
# COUNTING IONISATION

YINCG6 = [0.00, .078, .160, .255, .360, .450, .552, .655, .766, .878,
          .980, 1.09, 1.20, 1.34, 1.53, 1.63, 1.84, 2.19, 2.43, 2.66,
          2.86, 3.02, 3.15, 3.27, 3.37, 3.53, 3.64, 3.72, 3.77, 3.83,
          3.83, 3.84, 3.81, 3.76, 3.62, 3.46, 3.31, 3.17, 3.05, 2.75,
          2.50, 2.12, 1.84, 1.65, 1.49, 1.34, 1.25, 1.14, .995, .886,
          .795, .726, .664, .567, .492, .434, .389, .353, .329, .303,
          .282, .249, .224, .204, .186]
# IONISATION CHARGE STATE =1

YIN1G6 = [0.00, .078, .160, .255, .360, .450, .552, .655, .766, .878,
          .980, 1.09, 1.20, 1.34, 1.53, 1.63, 1.84, 2.19, 2.43, 2.66,
          2.86, 3.02, 3.15, 3.27, 3.37, 3.51, 3.55, 3.58, 3.57, 3.60,
          3.57, 3.53, 3.49, 3.44, 3.30, 3.16, 3.02, 2.90, 2.79, 2.51,
          2.29, 1.93, 1.67, 1.49, 1.34, 1.21, 1.12, 1.03, .896, .798,
          .716, .654, .598, .511, .443, .391, .350, .318, .296, .273,
          .254, .224, .202, .184, .168]
# IONISATION CHARGE STATE =2

XIN2G6 = [38.35944, 45.0, 50.0, 55.0, 60.0, 65.0, 70.0, 80.0, 90.0, 100.,
          120., 140., 160., 180., 200., 250., 300., 400., 500., 600.,
          700., 800., 900., 1000., 1200., 1400., 1600., 1800., 2000., 2500.,
          3000., 3500., 4000., 4500., 5000., 5500., 6000., 7000., 8000., 9000.,
          10000.
          ]
YIN2G6 = [0.0, .0256, .0850, .141, .194, .233, .262, .307, .315, .318,
          .311, .283, .265, .246, .230, .197, .173, .143, .120, .106,
          .0958, .0850, .0790, .0699, .0610, .0543, .0487, .0445, .0407, .0348,
          .0302, .0266, .0238, .0216, .0202, .0186, .0173, .0153, .0137, .0125,
          .0114]
# IONISATION CHARGE STATE =3

XIN3G6 = [74.029, 80.0, 90.0, 100., 120., 140., 160., 180., 200., 250.,
          300., 400., 500., 600., 700., 800., 900., 1000., 1200., 1400.,
          1600., 1800., 2000., 2500., 3000., 3500., 4000., 4500., 5000., 5500.,
          6000., 7000., 8000., 9000., 10000.
          ]
YIN3G6 = [0.0, .001, .0036, .0071, .0168, .0216, .0258, .0287, .0303,
          .0343,
          .0364, .0390, .0393, .0383, .0382, .0360, .0351, .0332, .0290, .0258,
          .0231, .0211, .0193, .0165, .0143, .0126, .0113, .0103, .00957, .00882,
          .00821, .00725, .00652, .00594, .00541]
# IONISATION CHARGE STATE =4
XIN4G6 = [124.88, 140., 160., 180., 190., 200., 250., 300., 400., 500.,
          600., 700., 800., 900., 1000., 1200., 1400., 1600., 1800., 2000.,
          2500., 3000., 3500., 4000., 4500., 5000., 5500., 6000., 7000., 8000.,
          9000., 10000.
          ]
YIN4G6 = [0.0, .000001, .0001, .0004, .00083, .00123, .00332, .00506,
          .00835, .00938,
          .0102, .0101, .00991, .00984, .00940, .00816, .00727, .00652, .00595,
          .00544,
          .00465, .00403, .00356, .00319, .00289, .00270, .00248, .00231, .00204,
          .00184, .00167, .00153]
# K-SHELL IONISATION

XKSHG6 = [14327.26, 14585., 15010., 15447., 15896., 16360., 16835.,
          17325., 17830., 18349.,
          18882., 19432., 2.00e4, 2.06e4, 2.18e4, 2.31e4, 2.45e4, 2.59e4, 2.74e4,
          2.91e4,
          3.08e4, 3.26e4, 3.55e4, 3.87e4, 4.22e4, 4.60e4, 5.02e4, 5.47e4, 6.13e4,
          6.88e4,
          7.72e4, 8.66e4, 1.00e5, 1.15e5, 1.33e5, 1.54e5, 1.78e5, 2.05e5, 2.37e5,
          2.74e5,
          3.16e5, 3.76e5, 4.47e5, 5.31e5, 7.08e5, 8.17e5, 1.00e6, 1.22e6, 1.45e6,
          1.73e6,
          2.00e6, 2.51e6, 3.07e6, 4.00e6, 5.01e6, 6.13e6, 8.18e6, 1.00e7, 1.45e7,
          2.05e7,
          2.99e7, 4.10e7, 5.01e7, 6.13e7, 8.18e7, 1.00e8, 1.45e8, 2.05e8, 2.99e8,
          4.10e8,
          5.01e8, 6.13e8, 8.18e8, 1.00e9]

YKSHG6 = [0.0, 6.61e-8, 1.68e-7, 2.66e-7, 3.58e-7, 4.46e-7, 5.30e-7,
          6.10e-7, 6.86e-7, 7.57e-7,
          8.26e-7, 8.91e-7, 9.52e-7, 1.01e-6, 1.12e-6, 1.21e-6, 1.30e-6, 1.37e-6,
          1.44e-6, 1.50e-6,
          1.55e-6, 1.59e-6, 1.64e-6, 1.68e-6, 1.71e-6, 1.72e-6, 1.73e-6, 1.72e-6,
          1.70e-6, 1.67e-6,
          1.64e-6, 1.60e-6, 1.54e-6, 1.47e-6, 1.41e-6, 1.35e-6, 1.29e-6, 1.24e-6,
          1.19e-6, 1.15e-6,
          1.11e-6, 1.08e-6, 1.05e-6, 1.03e-6, 1.02e-6, 1.02e-6, 1.03e-6, 1.04e-6,
          1.06e-6, 1.09e-6,
          1.11e-6, 1.16e-6, 1.20e-6, 1.25e-6, 1.31e-6, 1.36e-6, 1.43e-6, 1.48e-6,
          1.58e-6, 1.68e-6,
          1.78e-6, 1.87e-6, 1.92e-6, 1.98e-6, 2.06e-6, 2.11e-6, 2.22e-6, 2.31e-6,
          2.41e-6, 2.50e-6,
          2.56e-6, 2.61e-6, 2.69e-6, 2.75e-6]
# L1-SHELL IONISATION

XL1SG6 = [1921.0, 1956.6, 2013.2, 2071.4, 2131.4, 2193., 2256., 2322.,
          2389., 2458.,
          2530., 2680., 2837., 3004., 3181., 3369., 3567., 3777., 4000., 4236.,
          4616., 5031., 5483., 5976., 6513., 7098., 7737., 8433., 9192., 1.00e4,
          1.15e4, 1.33e4, 1.54e4, 1.78e4, 2.05e4, 2.44e4, 2.90e4, 3.45e4, 4.10e4,
          5.01e4,
          6.13e4, 7.50e4, 8.91e4, 1.00e5, 1.22e5, 1.50e5, 1.83e5, 2.24e5, 2.82e5,
          3.55e5,
          4.47e5, 5.79e5, 7.50e5, 1.00e6, 1.22e6, 1.45e6, 1.73e6, 2.00e6, 2.51e6,
          3.07e6,
          4.00e6, 5.01e6, 6.13e6, 8.18e6, 1.00e7, 1.50e7, 2.05e7, 2.51e7, 3.07e7,
          4.10e7,
          5.16e7, 6.13e7, 8.18e7, 1.00e8, 1.50e8, 2.05e8, 2.51e8, 3.07e8, 4.10e8,
          5.16e8,
          6.13e8, 8.18e8, 1.00e9
          ]
YL1SG6 = [0.0, 3.47e-6, 8.56e-6, 1.34e-5, 1.80e-5, 2.23e-5, 2.65e-5,
          3.04e-5, 3.41e-5, 3.76e-5,
          4.10e-5, 4.71e-5, 5.27e-5, 5.76e-5, 6.19e-5, 6.58e-5, 6.91e-5, 7.20e-5,
          7.44e-5, 7.65e-5,
          7.88e-5, 8.04e-5, 8.12e-5, 8.15e-5, 8.11e-5, 8.03e-5, 7.90e-5, 7.74e-5,
          7.55e-5, 7.33e-5,
          6.93e-5, 6.49e-5, 6.04e-5, 5.59e-5, 5.14e-5, 4.64e-5, 4.17e-5, 3.74e-5,
          3.35e-5, 2.94e-5,
          2.59e-5, 2.28e-5, 2.05e-5, 1.91e-5, 1.70e-5, 1.52e-5, 1.38e-5, 1.26e-5,
          1.14e-5, 1.06e-5,
          9.97e-6, 9.49e-6, 9.21e-6, 9.08e-6, 9.10e-6, 9.16e-6, 9.27e-6, 9.39e-6,
          9.62e-6, 9.86e-6,
          1.02e-5, 1.05e-5, 1.09e-5, 1.13e-5, 1.17e-5, 1.24e-5, 1.29e-5, 1.33e-5,
          1.36e-5, 1.42e-5,
          1.46e-5, 1.49e-5, 1.54e-5, 1.58e-5, 1.65e-5, 1.71e-5, 1.74e-5, 1.78e-5,
          1.83e-5, 1.88e-5,
          1.91e-5, 1.96e-5, 2.00e-5]
# L2-SHELL IONISATION

XL2SG6 = [1730.9, 1780.7, 1832.6, 1886., 1941., 1998., 2056., 2116.,
          2178., 2241.,
          2306., 2373., 2443., 2514., 2663., 2820., 2987., 3164., 3352., 3550.,
          3870., 4219., 4734., 5311., 5959., 6685., 7500., 8660., 1.00e4, 1.15e4,
          1.33e4, 1.54e4, 1.78e4, 2.05e4, 2.44e4, 2.90e4, 3.45e4, 4.10e4, 5.01e4,
          6.13e4,
          7.50e4, 8.91e4, 1.00e5, 1.22e5, 1.50e5, 1.83e5, 2.24e5, 2.82e5, 3.55e5,
          4.47e5,
          5.79e5, 7.50e5, 1.00e6, 1.22e6, 1.45e6, 1.73e6, 2.00e6, 2.51e6, 3.07e6,
          4.00e6,
          5.01e6, 6.13e6, 8.18e6, 1.00e7, 1.45e7, 2.05e7, 2.51e7, 3.07e7, 4.10e7,
          5.01e7,
          6.13e7, 8.18e7, 1.00e8, 1.45e8, 2.05e8, 2.51e8, 3.07e8, 4.10e8, 5.01e8,
          6.13e8,
          8.18e8, 1.00e9
          ]
YL2SG6 = [0.0, 9.21e-6, 1.81e-5, 2.65e-5, 3.45e-5, 4.20e-5, 4.92e-5,
          5.59e-5, 6.22e-5, 6.81e-5,
          7.36e-5, 7.88e-5, 8.37e-5, 8.82e-5, 9.63e-5, 1.03e-4, 1.09e-4, 1.14e-4,
          1.18e-4, 1.22e-4,
          1.26e-4, 1.28e-4, 1.30e-4, 1.30e-4, 1.29e-4, 1.26e-4, 1.23e-4, 1.17e-4,
          1.11e-4, 1.04e-4,
          9.74e-5, 9.04e-5, 8.35e-5, 7.69e-5, 6.95e-5, 6.27e-5, 5.64e-5, 5.06e-5,
          4.46e-5, 3.93e-5,
          3.47e-5, 3.12e-5, 2.92e-5, 2.60e-5, 2.33e-5, 2.11e-5, 1.93e-5, 1.77e-5,
          1.64e-5, 1.55e-5,
          1.48e-5, 1.44e-5, 1.42e-5, 1.43e-5, 1.44e-5, 1.46e-5, 1.48e-5, 1.52e-5,
          1.57e-5, 1.63e-5,
          1.69e-5, 1.74e-5, 1.82e-5, 1.88e-5, 1.99e-5, 2.09e-5, 2.15e-5, 2.21e-5,
          2.30e-5, 2.36e-5,
          2.43e-5, 2.51e-5, 2.58e-5, 2.69e-5, 2.80e-5, 2.86e-5, 2.92e-5, 3.01e-5,
          3.08e-5, 3.14e-5,
          3.23e-5, 3.29e-5]
# L3-SHELL IONISATION

XL3SG6 = [1678.4, 1684.5, 1733.6, 1784., 1836., 1889., 1944., 2001.,
          2059., 2119.,
          2181., 2244., 2310., 2377., 2447., 2518., 2667., 2824., 2991., 3168.,
          3356., 3554., 3874., 4223., 4738., 5315., 5963., 6689., 7506., 8666.,
          1.00e4, 1.15e4, 1.33e4, 1.54e4, 1.78e4, 2.05e4, 2.44e4, 2.90e4, 3.45e4,
          4.10e4,
          5.01e4, 6.13e4, 7.50e4, 8.91e4, 1.00e5, 1.22e5, 1.50e5, 1.83e5, 2.24e5,
          2.82e5,
          3.55e5, 4.47e5, 5.79e5, 7.50e5, 1.00e6, 1.22e6, 1.45e6, 1.73e6, 2.00e6,
          2.51e6,
          3.07e6, 4.00e6, 5.01e6, 6.13e6, 8.18e6, 1.00e7, 1.50e7, 2.05e7, 2.51e7,
          3.07e7,
          4.10e7, 5.16e7, 6.31e7, 8.18e7, 1.00e8, 1.50e8, 2.05e8, 2.51e8, 3.07e8,
          4.10e8,
          5.16e8, 6.31e8, 8.18e8, 1.00e9
          ]
YL3SG6 = [0.0, 2.31e-6, 2.23e-5, 4.13e-5, 5.91e-5, 7.64e-5, 9.25e-5,
          1.08e-4, 1.22e-4, 1.36e-4,
          1.48e-4, 1.60e-4, 1.71e-4, 1.82e-4, 1.91e-4, 2.00e-4, 2.16e-4, 2.30e-4,
          2.42e-4, 2.52e-4,
          2.60e-4, 2.66e-4, 2.73e-4, 2.78e-4, 2.80e-4, 2.79e-4, 2.75e-4, 2.69e-4,
          2.61e-4, 2.49e-4,
          2.35e-4, 2.21e-4, 2.06e-4, 1.91e-4, 1.76e-4, 1.62e-4, 1.46e-4, 1.32e-4,
          1.18e-4, 1.06e-4,
          9.34e-5, 8.22e-5, 7.25e-5, 6.53e-5, 6.10e-5, 5.43e-5, 4.88e-5, 4.41e-5,
          4.03e-5, 3.69e-5,
          3.42e-5, 3.22e-5, 3.08e-5, 2.99e-5, 2.96e-5, 2.97e-5, 3.00e-5, 3.04e-5,
          3.08e-5, 3.17e-5,
          3.25e-5, 3.38e-5, 3.50e-5, 3.61e-5, 3.77e-5, 3.89e-5, 4.13e-5, 4.33e-5,
          4.46e-5, 4.58e-5,
          4.77e-5, 4.91e-5, 5.04e-5, 5.21e-5, 5.34e-5, 5.59e-5, 5.80e-5, 5.93e-5,
          6.06e-5, 6.24e-5,
          6.39e-5, 6.52e-5, 6.68e-5, 6.81e-5]
# M1-SHELL IONISATION

XM1SG6 = [292.8, 295.7, 303.9, 312.4, 321.1, 330.1, 339.3, 348.8, 358.6,
          368.7,
          389.7, 412.0, 435.5, 460.5, 487.0, 515.0, 544.7, 576.1, 609.5, 644.8,
          682.0, 742.0, 808.0, 880.0, 1014., 1164., 1344., 1554., 1794., 2064.,
          2454., 2914., 3464., 4234., 5174., 6324., 7514., 8674., 1.00e4, 1.22e4,
          1.50e4, 1.88e4, 2.37e4, 2.99e4, 3.87e4, 4.87e4, 5.96e4, 7.08e4, 8.66e4,
          1.00e5,
          1.22e5, 1.50e5, 1.88e5, 2.37e5, 2.99e5, 3.87e5, 4.87e5, 5.96e5, 7.08e5,
          8.66e5,
          1.00e6, 1.22e6, 1.50e6, 1.88e6, 2.37e6, 2.99e6, 3.87e6, 4.87e6, 5.96e6,
          7.08e6,
          8.66e6, 1.00e7, 1.22e7, 1.63e7, 2.05e7, 2.51e7, 3.07e7, 4.10e7, 5.16e7,
          6.31e7,
          8.66e7, 1.00e8, 1.50e8, 2.05e8, 2.51e8, 3.07e8, 4.10e8, 5.16e8, 6.31e8,
          8.66e8,
          1.00e9
          ]
YM1SG6 = [0.0, 3.29e-5, 1.10e-4, 1.89e-4, 2.72e-4, 3.57e-4, 4.44e-4,
          5.32e-4, 6.20e-4, 7.09e-4,
          8.86e-4, 1.06e-3, 1.23e-3, 1.39e-3, 1.54e-3, 1.67e-3, 1.80e-3, 1.91e-3,
          2.02e-3, 2.10e-3,
          2.18e-3, 2.27e-3, 2.33e-3, 2.37e-3, 2.38e-3, 2.35e-3, 2.27e-3, 2.17e-3,
          2.04e-3, 1.91e-3,
          1.75e-3, 1.58e-3, 1.42e-3, 1.25e-3, 1.09e-3, 9.49e-4, 8.38e-4, 7.53e-4,
          6.77e-4, 5.80e-4,
          4.96e-4, 4.15e-4, 3.46e-4, 2.89e-4, 2.37e-4, 1.99e-4, 1.71e-4, 1.51e-4,
          1.31e-4, 1.19e-4,
          1.05e-4, 9.27e-5, 8.16e-5, 7.29e-5, 6.60e-5, 6.02e-5, 5.65e-5, 5.41e-5,
          5.26e-5, 5.15e-5,
          5.09e-5, 5.06e-5, 5.07e-5, 5.11e-5, 5.19e-5, 5.29e-5, 5.43e-5, 5.57e-5,
          5.70e-5, 5.82e-5,
          5.96e-5, 6.07e-5, 6.22e-5, 6.43e-5, 6.61e-5, 6.76e-5, 6.92e-5, 7.14e-5,
          7.32e-5, 7.48e-5,
          7.72e-5, 7.84e-5, 8.15e-5, 8.40e-5, 8.56e-5, 8.72e-5, 8.95e-5, 9.13e-5,
          9.29e-5, 9.54e-5,
          9.65e-5]
# M2-SHELL IONISATION

XM2SG6 = [222.2, 224.1, 230.5, 237.0, 243.7, 250.7, 257.8, 265.1, 272.7,
          280.5,
          288.4, 305.1, 322.8, 341.6, 361.4, 382.4, 404.7, 428.3, 453.3, 479.8,
          508.0, 553.0, 602.0, 656.0, 715.0, 778.0, 848.0, 924.0, 1007., 1157.,
          1337., 1547., 1787., 2057., 2377., 2747., 3167., 3767., 4607., 5627.,
          6687., 7727., 8667., 1.00e4, 1.22e4, 1.50e4, 1.83e4, 2.37e4, 2.90e4,
          3.76e4,
          5.01e4, 6.49e4, 7.72e4, 8.66e4, 1.00e5, 1.22e5, 1.50e5, 1.78e5, 2.05e5,
          2.37e5,
          2.74e5, 3.25e5, 3.98e5, 4.87e5, 5.96e5, 7.29e5, 8.66e5, 1.00e6, 1.22e6,
          1.50e6,
          2.05e6, 2.99e6, 3.87e6, 4.87e6, 5.96e6, 7.08e6, 8.66e6, 1.00e7, 1.22e7,
          1.50e7,
          2.05e7, 2.99e7, 3.87e7, 4.87e7, 5.96e7, 7.08e7, 8.66e7, 1.00e8, 1.22e8,
          1.50e8,
          2.05e8, 2.99e8, 3.87e8, 4.87e8, 5.96e8, 7.08e8, 8.66e8, 1.00e9
          ]
YM2SG6 = [0.0, 4.89e-5, 1.82e-4, 3.18e-4, 4.56e-4, 5.95e-4, 7.35e-4,
          8.75e-4, 1.01e-3, 1.15e-3,
          1.29e-3, 1.56e-3, 1.82e-3, 2.07e-3, 2.31e-3, 2.53e-3, 2.74e-3, 2.93e-3,
          3.11e-3, 3.27e-3,
          3.41e-3, 3.59e-3, 3.74e-3, 3.84e-3, 3.92e-3, 3.96e-3, 3.97e-3, 3.96e-3,
          3.92e-3, 3.81e-3,
          3.65e-3, 3.46e-3, 3.25e-3, 3.02e-3, 2.80e-3, 2.57e-3, 2.35e-3, 2.10e-3,
          1.83e-3, 1.58e-3,
          1.39e-3, 1.25e-3, 1.14e-3, 1.02e-3, 8.74e-4, 7.46e-4, 6.36e-4, 5.18e-4,
          4.42e-4, 3.61e-4,
          2.90e-4, 2.39e-4, 2.12e-4, 1.95e-4, 1.77e-4, 1.56e-4, 1.38e-4, 1.25e-4,
          1.16e-4, 1.08e-4,
          1.02e-4, 9.52e-5, 8.89e-5, 8.42e-5, 8.06e-5, 7.82e-5, 7.68e-5, 7.60e-5,
          7.56e-5, 7.57e-5,
          7.68e-5, 7.91e-5, 8.13e-5, 8.34e-5, 8.54e-5, 8.72e-5, 8.94e-5, 9.10e-5,
          9.32e-5, 9.55e-5,
          9.91e-5, 1.04e-4, 1.07e-4, 1.09e-4, 1.12e-4, 1.14e-4, 1.16e-4, 1.18e-4,
          1.20e-4, 1.23e-4,
          1.26e-4, 1.31e-4, 1.34e-4, 1.37e-4, 1.39e-4, 1.41e-4, 1.44e-4, 1.45e-4]
# M3-SHELL IONISATION

XM3SG6 = [214.4, 218.8, 225.0, 231.3, 237.9, 244.6, 251.5, 258.6, 266.0,
          273.5,
          281.3, 289.3, 306.0, 323.7, 342.4, 362.3, 383.3, 405.6, 429.2, 454.2,
          481.0, 509.0, 554.0, 603.0, 657.0, 715.0, 779.0, 849.0, 925.0, 1007.,
          1157., 1337., 1547., 1787., 2057., 2377., 2747., 3167., 3767., 4607.,
          5627., 6687., 7727., 8667., 1.00e4, 1.22e4, 1.50e4, 1.83e4, 2.37e4, 2.90e4,
          3.76e4, 5.01e4, 6.49e4, 7.72e4, 8.66e4, 1.00e5, 1.22e5, 1.50e5, 1.78e5,
          2.05e5,
          2.37e5, 2.74e5, 3.25e5, 3.98e5, 4.87e5, 5.96e5, 7.29e5, 8.66e5, 1.00e6,
          1.22e6,
          1.50e6, 2.05e6, 2.99e6, 3.87e6, 4.87e6, 5.96e6, 7.08e6, 8.66e6, 1.00e7,
          1.22e7,
          1.50e7, 2.05e7, 2.99e7, 3.87e7, 4.87e7, 5.96e7, 7.08e7, 8.66e7, 1.00e8,
          1.22e8,
          1.50e8, 2.05e8, 2.99e8, 3.87e8, 4.87e8, 5.96e8, 7.08e8, 8.66e8, 1.00e9
          ]
YM3SG6 = [0.0, 2.05e-4, 4.91e-4, 7.83e-4, 1.08e-3, 1.38e-3, 1.68e-3,
          1.98e-3, 2.28e-3, 2.58e-3,
          2.87e-3, 3.17e-3, 3.74e-3, 4.29e-3, 4.81e-3, 5.31e-3, 5.78e-3, 6.21e-3,
          6.61e-3, 6.98e-3,
          7.31e-3, 7.60e-3, 7.97e-3, 8.27e-3, 8.48e-3, 8.62e-3, 8.70e-3, 8.71e-3,
          8.66e-3, 8.56e-3,
          8.30e-3, 7.94e-3, 7.51e-3, 7.04e-3, 6.55e-3, 6.04e-3, 5.55e-3, 5.08e-3,
          4.53e-3, 3.94e-3,
          3.40e-3, 3.00e-3, 2.69e-3, 2.46e-3, 2.20e-3, 1.88e-3, 1.61e-3, 1.37e-3,
          1.12e-3, 9.53e-4,
          7.79e-4, 6.26e-4, 5.17e-4, 4.57e-4, 4.22e-4, 3.83e-4, 3.37e-4, 2.98e-4,
          2.71e-4, 2.52e-4,
          2.35e-4, 2.20e-4, 2.06e-4, 1.93e-4, 1.82e-4, 1.75e-4, 1.69e-4, 1.66e-4,
          1.65e-4, 1.64e-4,
          1.64e-4, 1.67e-4, 1.72e-4, 1.77e-4, 1.81e-4, 1.86e-4, 1.90e-4, 1.95e-4,
          1.98e-4, 2.03e-4,
          2.08e-4, 2.16e-4, 2.26e-4, 2.32e-4, 2.38e-4, 2.44e-4, 2.48e-4, 2.54e-4,
          2.57e-4, 2.63e-4,
          2.68e-4, 2.76e-4, 2.86e-4, 2.93e-4, 2.99e-4, 3.04e-4, 3.09e-4, 3.14e-4,
          3.18e-4]
# M4-SHELL IONISATION

XM4SG6 = [95.0, 96.83, 99.67, 102.6, 105.6, 108.7, 111.9, 115.2, 118.5,
          122.0,
          125.6, 133.0, 141.0, 149.3, 158.2, 167.5, 177.5, 188.0, 199.2, 211.0,
          223.5, 243.7, 265.7, 289.8, 315.9, 344.4, 375.5, 409.4, 446.4, 486.7,
          546.1, 612.8, 687.6, 771.5, 866.0, 1000., 1150., 1330., 1540., 1780.,
          2050., 2370., 2740., 3160., 3760., 4600., 5620., 6680., 7720., 8660.,
          1.00e4, 1.22e4, 1.50e4, 1.83e4, 2.37e4, 2.90e4, 3.76e4, 5.01e4, 6.49e4,
          7.72e4,
          8.66e4, 1.00e5, 1.22e5, 1.50e5, 1.78e5, 2.05e5, 2.37e5, 2.74e5, 3.25e5,
          3.98e5,
          4.87e5, 5.96e5, 7.29e5, 8.66e5, 1.00e6, 1.22e6, 1.50e6, 2.05e6, 2.99e6,
          3.87e6,
          4.87e6, 5.96e6, 7.08e6, 8.66e6, 1.00e7, 1.22e7, 1.50e7, 2.05e7, 2.99e7,
          3.87e7,
          4.87e7, 5.96e7, 7.08e7, 8.66e7, 1.00e8, 1.22e8, 1.50e8, 2.05e8, 2.99e8,
          3.87e8,
          4.87e8, 5.96e8, 7.08e8, 8.66e8, 1.00e9
          ]
YM4SG6 = [0.0, 1.08e-3, 2.62e-3, 4.04e-3, 5.37e-3, 6.62e-3, 7.79e-3,
          8.90e-3, 9.96e-3, 1.10e-2,
          1.20e-2, 1.38e-2, 1.56e-2, 1.73e-2, 1.90e-2, 2.06e-2, 2.22e-2, 2.37e-2,
          2.52e-2, 2.67e-2,
          2.80e-2, 3.00e-2, 3.18e-2, 3.34e-2, 3.47e-2, 3.58e-2, 3.66e-2, 3.72e-2,
          3.76e-2, 3.77e-2,
          3.74e-2, 3.69e-2, 3.60e-2, 3.48e-2, 3.35e-2, 3.17e-2, 2.98e-2, 2.78e-2,
          2.58e-2, 2.39e-2,
          2.20e-2, 2.02e-2, 1.85e-2, 1.68e-2, 1.49e-2, 1.30e-2, 1.12e-2, 9.90e-3,
          8.90e-3, 8.16e-3,
          7.32e-3, 6.28e-3, 5.38e-3, 4.60e-3, 3.77e-3, 3.23e-3, 2.66e-3, 2.15e-3,
          1.79e-3, 1.58e-3,
          1.47e-3, 1.33e-3, 1.18e-3, 1.05e-3, 9.54e-4, 8.87e-4, 8.30e-4, 7.82e-4,
          7.33e-4, 6.88e-4,
          6.54e-4, 6.29e-4, 6.12e-4, 6.03e-4, 5.99e-4, 5.99e-4, 6.02e-4, 6.15e-4,
          6.39e-4, 6.60e-4,
          6.81e-4, 6.99e-4, 7.16e-4, 7.37e-4, 7.52e-4, 7.73e-4, 7.94e-4, 8.28e-4,
          8.69e-4, 8.98e-4,
          9.24e-4, 9.46e-4, 9.65e-4, 9.88e-4, 1.00e-3, 1.03e-3, 1.05e-3, 1.08e-3,
          1.13e-3, 1.16e-3,
          1.18e-3, 1.20e-3, 1.22e-3, 1.25e-3, 1.26e-3]
# M5-SHELL IONISATION

XM5SG6 = [93.8, 94.3, 97.0, 99.9, 102.8, 105.8, 108.9, 112.1, 115.3, 118.7,
          122.2, 125.8, 133.2, 141.1, 149.5, 158.4, 167.8, 177.7, 188.2, 199.4,
          211.2, 223.7, 243.9, 266.0, 290.0, 316.0, 345.0, 376.0, 410.0, 446.0,
          487.0, 546.0, 613.0, 688.0, 772.0, 866.0, 1000., 1150., 1330., 1540.,
          1780., 2050., 2370., 2740., 3160., 3760., 4600., 5620., 6680., 7720.,
          8660., 1.00e4, 1.22e4, 1.50e4, 1.83e4, 2.37e4, 2.90e4, 3.76e4, 5.01e4,
          6.49e4,
          7.72e4, 8.66e4, 1.00e5, 1.22e5, 1.50e5, 1.78e5, 2.05e5, 2.37e5, 2.74e5,
          3.25e5,
          3.98e5, 4.87e5, 5.96e5, 7.29e5, 8.66e5, 1.00e6, 1.22e6, 1.50e6, 2.05e6,
          2.99e6,
          3.87e6, 4.87e6, 5.96e6, 7.08e6, 8.66e6, 1.00e7, 1.22e7, 1.50e7, 2.05e7,
          2.99e7,
          3.87e7, 4.87e7, 5.96e7, 7.08e7, 8.66e7, 1.00e8, 1.22e8, 1.50e8, 2.05e8,
          2.99e8,
          3.87e8, 4.87e8, 5.96e8, 7.08e8, 8.66e8, 1.00e9
          ]
YM5SG6 = [0.0, 4.52e-4, 2.91e-3, 5.18e-3, 7.29e-3, 9.26e-3, 1.11e-2,
          1.29e-2, 1.45e-2, 1.61e-2,
          1.76e-2, 1.91e-2, 2.19e-2, 2.46e-2, 2.72e-2, 2.97e-2, 3.22e-2, 3.46e-2,
          3.69e-2, 3.92e-2,
          4.14e-2, 4.35e-2, 4.65e-2, 4.92e-2, 5.15e-2, 5.35e-2, 5.52e-2, 5.64e-2,
          5.73e-2, 5.77e-2,
          5.78e-2, 5.74e-2, 5.65e-2, 5.51e-2, 5.33e-2, 5.13e-2, 4.85e-2, 4.55e-2,
          4.25e-2, 3.95e-2,
          3.66e-2, 3.37e-2, 3.08e-2, 2.82e-2, 2.56e-2, 2.28e-2, 1.98e-2, 1.71e-2,
          1.51e-2, 1.36e-2,
          1.24e-2, 1.11e-2, 9.56e-3, 8.19e-3, 7.01e-3, 5.74e-3, 4.92e-3, 4.05e-3,
          3.27e-3, 2.72e-3,
          2.41e-3, 2.23e-3, 2.03e-3, 1.79e-3, 1.59e-3, 1.45e-3, 1.35e-3, 1.26e-3,
          1.19e-3, 1.11e-3,
          1.05e-3, 9.94e-4, 9.56e-4, 9.31e-4, 9.18e-4, 9.12e-4, 9.10e-4, 9.16e-4,
          9.36e-4, 9.72e-4,
          1.00e-3, 1.03e-3, 1.06e-3, 1.09e-3, 1.12e-3, 1.14e-3, 1.17e-3, 1.21e-3,
          1.26e-3, 1.32e-3,
          1.37e-3, 1.40e-3, 1.44e-3, 1.47e-3, 1.50e-3, 1.53e-3, 1.56e-3, 1.59e-3,
          1.65e-3, 1.71e-3,
          1.76e-3, 1.80e-3, 1.83e-3, 1.86e-3, 1.89e-3, 1.92e-3]
# 1S5  METASTABLE   E=9.91523166 EV  J=2
#      SHAPE FUNCTION BELOW 50 EV FROM BARTSCHAT AND ZATSARINNY
#      ABOVE 50 EV SCALED BY 1/E**3

X1S5G6 = [9.9152, 9.932, 9.959, 9.973, 9.987, 10.000, 10.027, 10.034,
          10.041, 10.048,
          10.055, 10.068, 10.082, 10.095, 10.109, 10.123, 10.136, 10.150, 10.163,
          10.177,
          10.184, 10.191, 10.204, 10.218, 10.231, 10.245, 10.259, 10.313, 10.367,
          10.422,
          10.476, 10.531, 10.585, 10.612, 10.640, 10.646, 10.653, 10.667, 10.680,
          10.694,
          10.708, 10.816, 10.925, 11.034, 11.089, 11.143, 11.197, 11.225, 11.252,
          11.263,
          11.265, 11.268, 11.271, 11.272, 11.274, 11.275, 11.276, 11.279, 11.282,
          11.284,
          11.287, 11.293, 11.295, 11.298, 11.301, 11.306, 11.309, 11.313, 11.320,
          11.327,
          11.334, 11.340, 11.347, 11.354, 11.361, 11.367, 11.374, 11.381, 11.388,
          11.395,
          11.402, 11.415, 11.429, 11.442, 11.456, 11.470, 11.483, 11.497, 11.510,
          11.524,
          11.538, 11.551, 11.565, 11.578, 11.592, 11.606, 11.619, 11.626, 11.633,
          11.640,
          11.644, 11.646, 11.649, 11.653, 11.660, 11.665, 11.674, 11.701, 11.755,
          11.796,
          11.851, 11.905, 11.959, 11.973, 11.976, 11.980, 11.984, 11.986, 11.989,
          11.993,
          12.000, 12.007, 12.014, 12.017, 12.021, 12.027, 12.041, 12.068, 12.095,
          12.150,
          12.204, 12.259, 12.304, 12.367, 12.422, 12.476, 12.531, 12.585, 12.640,
          12.694,
          12.748, 12.803, 12.871, 12.925, 12.993, 13.075, 13.197, 13.334, 13.470,
          13.578,
          13.742, 14.014, 14.558, 15.102, 15.646, 16.191, 16.735, 17.279, 17.959,
          19.048,
          20.0, 21.0, 22.0, 24.0, 27.0, 30.0, 35.0, 40.0, 50.0
          ]
Y1S5G6 = [0.00, 1.10, 2.18, 2.87, 3.63, 4.38, 5.69, 6.09, 6.58, 4.84,
          3.88, 3.18, 2.69, 2.46, 2.40, 2.44, 2.62, 3.01, 4.01, 6.71,
          7.86, 6.60, 3.55, 2.67, 2.42, 2.35, 2.35, 2.54, 2.84, 3.19,
          3.58, 4.02, 4.42, 4.70, 5.05, 5.19, 5.39, 5.33, 5.29, 5.42,
          5.54, 6.42, 7.20, 7.63, 7.68, 7.57, 7.21, 6.83, 6.10, 5.64,
          5.66, 6.12, 7.67, 8.69, 9.58, 9.36, 9.07, 8.29, 7.66, 7.20,
          6.87, 6.53, 6.64, 7.25, 8.85, 9.99, 8.47, 7.04, 5.99, 5.69,
          5.16, 5.23, 5.49, 6.00, 6.85, 8.06, 9.28, 9.92, 9.98, 9.87,
          9.62, 8.49, 7.26, 6.26, 5.51, 4.81, 4.19, 3.61, 3.03, 2.59,
          2.39, 3.10, 3.69, 3.90, 3.97, 3.97, 3.95, 4.03, 4.40, 5.31,
          5.79, 5.91, 5.89, 5.71, 5.34, 5.01, 4.83, 4.93, 5.11, 5.21,
          5.28, 5.30, 5.04, 4.80, 4.81, 5.16, 5.83, 5.86, 5.72, 5.48,
          5.13, 4.97, 5.85, 6.50, 7.12, 7.16, 6.71, 6.28, 5.89, 5.52,
          5.65, 5.63, 5.67, 5.41, 5.29, 5.41, 5.60, 5.77, 5.95, 6.00,
          5.83, 5.56, 5.55, 5.74, 5.91, 5.94, 5.99, 6.06, 6.11, 6.16,
          6.14, 6.01, 5.80, 6.07, 6.73, 7.37, 7.84, 8.23, 8.57, 8.64,
          8.20, 7.60, 7.00, 6.04, 4.70, 3.60, 2.30, 1.45, 0.70
          ]
YP1S5G6 = [0.0 for i in range(169)]
# 1S4  E=10.032400 EV  J=1    RESONANCE RAeIATION  123.585 NM
#     USEe  BEF SCALING ABOVE  20 EV    OSC STRENGTH=0.203
#     SHAPE FUNCTION BELOW 20 EV FROM BARTSCHAT AND ZATSARINNY

X1S4G6 = [10.0324, 10.034, 10.041, 10.048, 10.055, 10.068, 10.082,
          10.095, 10.109, 10.123,
          10.136, 10.150, 10.163, 10.204, 10.218, 10.231, 10.245, 10.259, 10.286,
          10.354,
          10.422, 10.490, 10.558, 10.626, 10.680, 10.748, 10.816, 10.884, 10.953,
          11.021,
          11.089, 11.157, 11.238, 11.252, 11.265, 11.271, 11.274, 11.276, 11.282,
          11.287,
          11.295, 11.301, 11.306, 11.309, 11.313, 11.320, 11.334, 11.347, 11.361,
          11.374,
          11.381, 11.388, 11.395, 11.402, 11.415, 11.429, 11.442, 11.456, 11.483,
          11.510,
          11.538, 11.565, 11.592, 11.619, 11.633, 11.644, 11.649, 11.660, 11.674,
          11.701,
          11.728, 11.755, 11.776, 11.796, 11.823, 11.851, 11.878, 11.905, 11.932,
          11.959,
          11.976, 11.984, 11.989, 12.000, 12.014, 12.021, 12.041, 12.068, 12.095,
          12.191,
          12.245, 12.300, 12.354, 12.408, 12.463, 12.517, 12.572, 12.626, 12.680,
          12.735,
          12.803, 12.871, 12.925, 12.966, 13.061, 13.157, 13.225, 13.279, 13.347,
          13.402,
          13.497, 13.606, 13.878, 14.150, 14.422, 14.694, 14.966, 15.238, 15.510,
          15.783,
          16.055, 16.327, 16.599, 16.871, 17.143, 17.415, 17.687, 17.959, 19.048,
          20.000
          ]
Y1S4G6 = [0.00, 0.69, 2.81, 5.49, 8.19, 6.82, 5.53, 5.15, 5.23, 5.74,
          6.94, 9.75, 17.4, 17.8, 9.03, 5.97, 4.62, 3.93, 3.42, 2.97,
          3.07, 3.35, 3.74, 4.37, 4.81, 5.24, 5.75, 6.37, 6.89, 7.33,
          7.66, 7.83, 7.61, 7.46, 7.20, 7.79, 8.62, 8.45, 8.03, 7.78,
          7.78, 8.89, 9.48, 8.73, 8.03, 7.38, 7.09, 7.08, 7.79, 9.35,
          9.77, 9.75, 9.60, 9.37, 8.58, 7.64, 6.70, 6.56, 6.73, 6.48,
          6.23, 7.15, 7.57, 7.95, 8.35, 8.28, 8.02, 7.80, 7.88, 8.06,
          8.16, 8.25, 8.31, 8.36, 8.43, 8.49, 8.55, 8.59, 8.62, 8.60,
          9.09, 9.57, 9.09, 8.89, 10.0, 10.2, 9.21, 8.96, 8.70, 9.02,
          9.25, 9.71, 9.84, 9.76, 9.75, 9.90, 10.1, 10.3, 10.4, 10.8,
          10.6, 10.8, 10.8, 10.8, 10.7, 11.0, 11.2, 11.4, 11.5, 11.6,
          11.6, 11.8, 11.7, 11.5, 11.4, 11.6, 12.0, 12.5, 13.1, 13.8,
          14.5, 15.2, 15.8, 16.4, 17.0, 17.9, 18.9, 20.1, 22.4, 23.7
          ]
YP1S4G6 = [0.0 for i in range(130)]
# 1S3  METASTABLE E=10.56241436 EV J=0
#      SHAPE FUNCTION BELOW  50 EV FROM BARTSCHAT AND ZATSARINNY
#      SCALED BY 1/E**3 ABOVE 50 EV

X1S3G6 = [10.5624, 10.572, 10.585, 10.599, 10.612, 10.626, 10.640,
          10.646, 10.653, 10.667,
          10.680, 10.694, 10.708, 10.735, 10.762, 10.789, 10.816, 10.844, 10.871,
          10.898,
          10.925, 10.953, 10.980, 11.007, 11.034, 11.061, 11.089, 11.116, 11.143,
          11.170,
          11.197, 11.225, 11.252, 11.263, 11.265, 11.268, 11.271, 11.272, 11.274,
          11.275,
          11.276, 11.279, 11.282, 11.284, 11.287, 11.293, 11.295, 11.298, 11.301,
          11.306,
          11.309, 11.313, 11.320, 11.327, 11.334, 11.340, 11.347, 11.354, 11.361,
          11.367,
          11.374, 11.381, 11.388, 11.395, 11.402, 11.415, 11.429, 11.442, 11.456,
          11.470,
          11.483, 11.497, 11.510, 11.524, 11.538, 11.551, 11.578, 11.606, 11.619,
          11.626,
          11.633, 11.640, 11.644, 11.646, 11.649, 11.653, 11.660, 11.665, 11.674,
          11.701,
          11.728, 11.755, 11.776, 11.796, 11.823, 11.851, 11.878, 11.905, 11.932,
          11.959,
          11.980, 11.993, 12.000, 12.007, 12.014, 12.017, 12.021, 12.027, 12.041,
          12.055,
          12.068, 12.082, 12.095, 12.110, 12.150, 12.163, 12.177, 12.204, 12.231,
          12.259,
          12.286, 12.313, 12.340, 12.354, 12.381, 12.435, 12.490, 12.544, 12.599,
          12.653,
          12.708, 12.762, 12.803, 12.871, 12.993, 13.089, 13.157, 13.225, 13.279,
          13.347,
          13.374, 13.388, 13.402, 13.415, 13.429, 13.470, 13.497, 13.551, 13.878,
          14.422,
          14.966, 15.510, 16.055, 16.599, 17.143, 17.687, 19.048, 20.408, 21.089,
          22.177,
          23.130, 24.490, 26.123, 28.572, 32.654, 38.096, 43.538, 50.0
          ]
Y1S3G6 = [0.00, .255, .560, .671, .508, .377, .265, .211, .263, .459,
          .428, .360, .330, .316, .320, .330, .344, .362, .375, .392,
          .411, .428, .448, .468, .488, .509, .529, .547, .564, .577,
          .581, .568, .511, .555, .674, 1.01, 1.74, 2.09, 2.21, 2.11,
          1.91, 1.53, 1.27, 1.11, 1.00, .875, .848, .865, .979, 1.17,
          1.07, .944, .815, .921, .792, .744, .718, .702, .698, .717,
          .780, .891, 1.04, 1.18, 1.28, 1.31, 1.22, 1.14, 1.10, 1.11,
          1.13, 1.15, 1.18, 1.24, 1.29, 1.30, 1.27, 1.28, 1.29, 1.29,
          1.26, 1.19, 1.16, 1.15, 1.16, 1.18, 1.21, 1.24, 1.24, 1.25,
          1.25, 1.25, 1.25, 1.25, 1.24, 1.23, 1.21, 1.18, 1.13, 1.06,
          .978, .885, .806, .806, 1.15, 1.36, 1.52, 1.47, 1.26, 1.15,
          1.04, .937, .816, .706, .412, .403, .444, .520, .609, .644,
          .686, .687, .729, .782, .840, .889, .919, .939, .951, .934,
          .915, .916, .921, .969, .993, .914, .919, .956, .989, 1.02,
          1.04, 1.05, 1.06, 1.05, 1.02, .936, .938, .947, 1.00, 1.07,
          1.07, 1.12, 1.23, 1.30, 1.38, 1.57, 1.86, 1.77, 1.68, 1.54,
          1.41, 1.25, 1.10, .906, .656, .422, .275, .172
          ]
YP1S3G6 = [0.0 for i in range(168)]
# 1S2  E=10.6436342 EV  J=1   RESONANCE RAeIATION  116.487 NM
#      USEe BEF SCALING ABOVE 20 EV      OSC STRENGTH=0.182
#      SHAPE FUNCTION BELOW 20 EV FROM BARTSCHAT AND ZATSARINNY

X1S2G6 = [10.6436, 10.646, 10.653, 10.667, 10.680, 10.694, 10.708,
          10.721, 10.748, 10.816,
          10.884, 10.953, 11.021, 11.089, 11.157, 11.225, 11.238, 11.252, 11.263,
          11.265,
          11.268, 11.271, 11.272, 11.274, 11.275, 11.276, 11.279, 11.282, 11.284,
          11.287,
          11.293, 11.295, 11.298, 11.301, 11.306, 11.309, 11.313, 11.334, 11.367,
          11.381,
          11.388, 11.395, 11.402, 11.415, 11.429, 11.456, 11.483, 11.510, 11.538,
          11.565,
          11.592, 11.619, 11.626, 11.633, 11.640, 11.644, 11.646, 11.649, 11.653,
          11.660,
          11.665, 11.674, 11.687, 11.714, 11.742, 11.762, 11.783, 11.810, 11.837,
          11.864,
          11.891, 11.918, 11.946, 11.973, 11.980, 11.986, 11.993, 12.000, 12.007,
          12.014,
          12.017, 12.021, 12.027, 12.041, 12.055, 12.068, 12.082, 12.095, 12.109,
          12.150,
          12.163, 12.177, 12.191, 12.204, 12.286, 12.340, 12.395, 12.449, 12.504,
          12.558,
          12.612, 12.667, 12.721, 12.735, 12.748, 12.762, 12.769, 12.776, 12.789,
          12.803,
          12.871, 12.884, 12.898, 12.912, 12.925, 12.966, 12.993, 13.061, 13.075,
          13.089,
          13.129, 13.170, 13.197, 13.238, 13.265, 13.293, 13.334, 13.361, 13.388,
          13.402,
          13.415, 13.429, 13.470, 13.497, 13.551, 13.606, 13.878, 14.150, 14.422,
          14.694,
          14.966, 15.238, 15.510, 15.783, 16.055, 16.327, 16.599, 17.959, 19.048,
          20.000
          ]
Y1S2G6 = [0.00, .367, 1.32, 4.25, 3.25, 2.45, 2.09, 1.91, 1.74, 1.66,
          1.70, 1.81, 1.98, 2.20, 2.45, 2.72, 2.79, 2.89, 3.35, 3.81,
          4.80, 6.47, 7.04, 6.96, 6.49, 5.87, 4.90, 4.36, 4.08, 3.94,
          3.91, 4.02, 4.24, 4.53, 3.87, 3.48, 3.28, 3.18, 3.37, 3.58,
          3.84, 4.15, 4.40, 4.50, 4.37, 4.26, 4.48, 4.70, 5.09, 5.29,
          5.41, 5.58, 5.61, 5.57, 5.35, 5.21, 5.18, 5.18, 5.23, 5.35,
          5.46, 5.52, 5.58, 5.66, 5.74, 5.79, 5.83, 5.88, 5.91, 5.91,
          5.89, 5.83, 5.69, 5.45, 5.36, 5.18, 5.04, 4.81, 4.67, 5.39,
          5.96, 6.52, 6.55, 6.08, 5.77, 5.48, 5.14, 4.66, 4.28, 3.67,
          3.80, 4.01, 4.29, 4.50, 5.24, 5.49, 5.77, 5.97, 6.14, 6.27,
          6.37, 6.45, 6.53, 6.55, 6.47, 6.32, 6.27, 6.22, 6.16, 6.33,
          6.39, 6.50, 6.79, 6.95, 6.97, 6.99, 6.88, 6.76, 6.71, 6.74,
          6.86, 6.98, 7.06, 7.18, 7.26, 7.35, 7.49, 7.54, 7.65, 7.68,
          7.67, 7.54, 7.44, 7.45, 7.52, 7.58, 7.87, 8.18, 8.29, 8.28,
          8.35, 8.58, 8.97, 9.50, 10.1, 10.7, 11.2, 14.3, 16.8, 18.0
          ]
YP1S2G6 = [0.0 for i in range(150)]
# 2P10 E=11.3034545 EV  J=1
# SHAPE FUNCTION FROM B  AND Z ABOVE 30 EV SCALED BY 1/E**3

X2P10G6 = [11.3035, 11.306, 11.309, 11.313, 11.320, 11.327, 11.333,
           11.340, 11.347, 11.354,
           11.361, 11.367, 11.374, 11.381, 11.388, 11.395, 11.402, 11.415, 11.429,
           11.442,
           11.456, 11.470, 11.483, 11.497, 11.510, 11.524, 11.538, 11.551, 11.565,
           11.578,
           11.592, 11.606, 11.619, 11.626, 11.633, 11.640, 11.644, 11.646, 11.649,
           11.653,
           11.660, 11.665, 11.674, 11.687, 11.701, 11.714, 11.728, 11.742, 11.755,
           11.762,
           11.776, 11.782, 11.796, 11.810, 11.823, 11.837, 11.850, 11.864, 11.878,
           11.891,
           11.905, 11.919, 11.932, 11.946, 11.959, 11.973, 11.976, 11.980, 11.984,
           11.987,
           11.989, 11.993, 12.000, 12.007, 12.014, 12.016, 12.021, 12.027, 12.041,
           12.055,
           12.068, 12.082, 12.095, 12.109, 12.150, 12.163, 12.177, 12.191, 12.204,
           12.218,
           12.231, 12.245, 12.259, 12.272, 12.286, 12.299, 12.313, 12.327, 12.340,
           12.354,
           12.367, 12.381, 12.395, 12.408, 12.422, 12.436, 12.449, 12.463, 12.476,
           12.490,
           12.504, 12.558, 12.612, 12.653, 12.708, 12.748, 12.803, 12.912, 12.966,
           13.061,
           13.129, 13.252, 13.347, 13.606, 14.014, 14.558, 14.966, 15.510, 16.055,
           16.463,
           17.007, 17.551, 17.959, 19.048, 20.000, 21.089, 22.041, 23.130, 24.490,
           26.123,
           28.572, 30.0
           ]
Y2P10G6 = [0.00, 0.64, 0.96, 1.18, 1.48, 1.74, 2.14, 2.61, 3.13, 3.72,
           4.35, 4.87, 5.00, 4.66, 4.16, 3.59, 2.85, 1.39, 0.71, 0.58,
           0.52, 0.54, 0.57, 0.62, 0.69, 0.76, 0.78, 0.78, 0.76, 0.75,
           0.76, 0.80, 0.92, 1.11, 1.54, 2.19, 2.35, 2.27, 2.12, 1.86,
           1.52, 1.29, 1.20, 1.15, 1.11, 1.08, 1.06, 1.04, 1.03, 1.03,
           1.02, 1.02, 1.02, 1.01, 1.01, 1.01, 1.02, 1.02, 1.03, 1.04,
           1.05, 1.06, 1.08, 1.12, 1.22, 1.70, 1.75, 1.63, 1.22, 1.11,
           1.13, 1.22, 1.44, 1.75, 1.84, 1.62, 1.21, 0.87, 0.82, 0.86,
           0.91, 0.95, 1.02, 1.12, 1.18, 1.17, 1.14, 1.08, 1.05, 1.06,
           1.10, 1.15, 1.15, 1.17, 1.17, 1.18, 1.16, 1.14, 1.12, 1.17,
           1.14, 1.13, 1.05, 1.01, 1.01, 1.01, 1.02, 1.04, 1.05, 1.06,
           1.07, 1.09, 1.10, 1.16, 1.44, 1.11, 1.11, 1.13, 1.07, 1.16,
           1.20, 1.25, 1.29, 1.21, 1.23, 1.60, 1.91, 2.64, 3.57, 4.38,
           5.45, 6.53, 7.73, 8.54, 8.17, 7.21, 6.26, 5.26, 4.25, 3.39,
           2.45, 2.05
           ]
YP2P10G6 = [0.0 for i in range(142)]
# 2P9 E=11.4430466 EV J=3
# SHAPE FUNCTION FROM B  AND Z ABOVE 30 EV SCALED BY 1/E**3

X2P9G6 = [11.4430, 11.456, 11.470, 11.483, 11.497, 11.510, 11.524,
          11.538, 11.551, 11.565,
          11.578, 11.592, 11.606, 11.619, 11.626, 11.633, 11.640, 11.644, 11.646,
          11.649,
          11.653, 11.660, 11.665, 11.674, 11.687, 11.701, 11.714, 11.728, 11.742,
          11.755,
          11.762, 11.776, 11.782, 11.796, 11.810, 11.823, 11.837, 11.850, 11.864,
          11.878,
          11.891, 11.905, 11.919, 11.932, 11.946, 11.959, 11.973, 11.976, 11.980,
          11.984,
          11.987, 11.989, 11.993, 12.000, 12.007, 12.014, 12.016, 12.021, 12.027,
          12.041,
          12.055, 12.068, 12.082, 12.095, 12.109, 12.150, 12.163, 12.177, 12.191,
          12.204,
          12.218, 12.231, 12.245, 12.259, 12.272, 12.286, 12.299, 12.313, 12.327,
          12.340,
          12.354, 12.367, 12.381, 12.395, 12.408, 12.422, 12.436, 12.449, 12.463,
          12.476,
          12.490, 12.504, 12.558, 12.612, 12.653, 12.748, 12.803, 12.898, 13.061,
          13.157,
          13.252, 13.497, 13.742, 14.014, 14.996, 16.055, 17.007, 17.959, 19.048,
          20.000,
          21.089, 22.041, 23.130, 24.490, 26.123, 28.572, 30.000
          ]
Y2P9G6 = [0.00, 0.42, 0.67, 0.75, 0.78, 0.83, 0.95, 1.03, 1.09, 1.02,
          1.00, 1.02, 1.08, 1.23, 1.38, 1.59, 1.69, 1.54, 1.40, 1.26,
          1.10, 0.97, 0.93, 0.96, 0.99, 1.01, 1.02, 1.04, 1.05, 1.06,
          1.06, 1.07, 1.07, 1.08, 1.09, 1.10, 1.11, 1.12, 1.13, 1.14,
          1.17, 1.16, 1.18, 1.19, 1.21, 1.23, 1.32, 1.35, 1.39, 1.42,
          1.44, 1.47, 1.56, 1.90, 2.82, 4.49, 4.71, 4.20, 3.05, 2.15,
          1.92, 1.84, 1.82, 1.80, 1.74, 1.98, 1.94, 1.60, 1.64, 1.73,
          1.79, 1.86, 1.85, 1.86, 1.84, 1.80, 1.86, 1.96, 2.05, 2.19,
          1.86, 1.68, 1.61, 1.60, 1.57, 1.57, 1.58, 1.60, 1.62, 1.64,
          1.66, 1.68, 1.76, 1.82, 1.80, 1.76, 2.00, 1.93, 1.92, 2.08,
          2.12, 2.13, 2.16, 2.22, 3.50, 5.50, 6.90, 7.83, 8.15, 7.72,
          6.77, 5.84, 4.92, 4.03, 3.31, 2.47, 2.11
          ]
YP2P9G6 = [0.0 for i in range(117)]
# 2P8 E=11.4446556 EV J=2
# SHAPE FUNCTION FROM B  AND Z ABOVE 30 EV SCALED BY 1/E

X2P8G6 = [11.4447, 11.456, 11.470, 11.483, 11.497, 11.510, 11.524,
          11.538, 11.551, 11.565,
          11.578, 11.592, 11.606, 11.619, 11.626, 11.633, 11.640, 11.644, 11.646,
          11.649,
          11.653, 11.660, 11.665, 11.674, 11.687, 11.701, 11.714, 11.728, 11.742,
          11.755,
          11.762, 11.776, 11.782, 11.796, 11.810, 11.823, 11.837, 11.850, 11.864,
          11.878,
          11.891, 11.905, 11.919, 11.932, 11.946, 11.959, 11.973, 11.976, 11.980,
          11.984,
          11.987, 11.989, 11.993, 12.000, 12.007, 12.014, 12.016, 12.021, 12.027,
          12.041,
          12.055, 12.068, 12.082, 12.095, 12.109, 12.150, 12.163, 12.177, 12.191,
          12.204,
          12.218, 12.231, 12.245, 12.259, 12.272, 12.286, 12.299, 12.313, 12.327,
          12.340,
          12.354, 12.367, 12.381, 12.395, 12.408, 12.422, 12.436, 12.449, 12.463,
          12.476,
          12.490, 12.504, 12.558, 12.599, 12.653, 12.708, 12.762, 12.803, 12.898,
          12.993,
          13.252, 13.497, 13.742, 14.014, 14.558, 14.966, 15.510, 16.055, 16.463,
          17.007,
          17.959, 19.048, 20.000, 21.089, 22.041, 23.130, 24.490, 26.123, 28.572,
          30.0
          ]
Y2P8G6 = [0.00, 0.36, 0.72, 1.01, 1.22, 1.36, 1.45, 1.43, 1.35, 1.29,
          1.30, 1.33, 1.38, 1.45, 1.50, 1.59, 1.64, 1.61, 1.57, 1.53,
          1.48, 1.44, 1.42, 1.41, 1.43, 1.45, 1.47, 1.48, 1.50, 1.52,
          1.53, 1.54, 1.55, 1.57, 1.58, 1.60, 1.61, 1.63, 1.64, 1.66,
          1.73, 1.68, 1.69, 1.69, 1.70, 1.71, 1.55, 1.67, 2.20, 2.64,
          2.50, 2.31, 2.11, 1.98, 2.05, 2.34, 2.44, 2.45, 2.30, 2.15,
          2.09, 2.06, 2.04, 2.06, 2.07, 1.97, 1.97, 1.92, 1.92, 1.95,
          2.00, 2.07, 2.12, 2.09, 2.12, 2.16, 2.21, 2.25, 2.33, 2.49,
          2.26, 2.08, 2.02, 2.03, 2.02, 1.99, 1.97, 1.96, 1.95, 1.96,
          1.97, 1.98, 2.03, 2.06, 1.97, 2.43, 2.30, 2.22, 2.24, 2.36,
          2.34, 2.43, 2.51, 2.61, 3.01, 3.52, 4.27, 4.97, 5.45, 5.98,
          6.96, 7.70, 7.85, 7.66, 7.37, 7.03, 6.65, 6.30, 5.82, 5.55
          ]
YP2P8G6 = [0.0 for i in range(120)]
# 2P7 E=11.5261152 EV J=1
# SHAPE FUNCTION FROM B  AND Z ABOVE 30 EV SCALED BY 1/E**3

X2P7G6 = [11.5261, 11.538, 11.551, 11.565, 11.578, 11.592, 11.606,
          11.619, 11.626, 11.633,
          11.640, 11.644, 11.646, 11.649, 11.653, 11.660, 11.665, 11.674, 11.687,
          11.701,
          11.714, 11.728, 11.742, 11.755, 11.762, 11.776, 11.782, 11.796, 11.810,
          11.823,
          11.837, 11.850, 11.864, 11.878, 11.891, 11.905, 11.919, 11.932, 11.946,
          11.959,
          11.973, 11.976, 11.980, 11.984, 11.987, 11.989, 11.993, 12.000, 12.007,
          12.014,
          12.016, 12.021, 12.027, 12.041, 12.055, 12.068, 12.082, 12.095, 12.109,
          12.150,
          12.163, 12.177, 12.191, 12.204, 12.218, 12.231, 12.245, 12.259, 12.272,
          12.286,
          12.299, 12.313, 12.327, 12.340, 12.354, 12.367, 12.381, 12.395, 12.408,
          12.422,
          12.463, 12.504, 12.558, 12.612, 12.653, 12.694, 12.708, 12.735, 12.762,
          12.993,
          13.197, 13.293, 13.497, 13.742, 14.014, 14.558, 14.966, 15.510, 16.055,
          16.599,
          17.007, 17.959, 19.048, 20.000, 21.089, 22.041, 23.130, 24.490, 26.123,
          28.572, 30.0
          ]
Y2P7G6 = [0.00, 0.21, 0.44, 0.45, 0.45, 0.45, 0.46, 0.49, 0.51, 0.55,
          0.57, 0.55, 0.53, 0.51, 0.50, 0.49, 0.50, 0.52, 0.57, 0.60,
          0.62, 0.65, 0.66, 0.67, 0.68, 0.68, 0.69, 0.69, 0.70, 0.70,
          0.71, 0.71, 0.72, 0.72, 0.72, 0.73, 0.74, 0.74, 0.75, 0.73,
          0.78, 0.92, 1.00, 0.80, 0.68, 0.64, 0.62, 0.60, 0.53, 0.51,
          0.56, 0.66, 0.74, 0.75, 0.76, 0.74, 0.70, 0.65, 0.81, 0.88,
          0.98, 1.20, 1.16, 1.18, 1.23, 1.28, 1.35, 1.31, 1.24, 1.15,
          1.10, 1.02, 0.99, 0.99, 0.97, 0.94, 0.88, 0.91, 0.88, 0.86,
          0.82, 0.83, 0.87, 0.91, 0.95, 1.05, 1.48, 1.17, 0.99, 1.07,
          1.03, 1.06, 1.06, 1.09, 1.19, 1.50, 1.81, 2.33, 2.78, 3.11,
          3.25, 3.32, 3.08, 2.76, 2.38, 2.07, 1.80, 1.54, 1.31, 1.03,
          0.90
          ]
YP2P7G6 = [0.0 for i in range(111)]
# 2P6 E=11.5458220 EV J=2
# SHAPE FUNCTION FROM B  AND Z   SCALED BY 1/E  ABOVE  30 EV

X2P6G6 = [11.5458, 11.551, 11.565, 11.578, 11.592, 11.606, 11.619,
          11.626, 11.633, 11.640,
          11.644, 11.646, 11.649, 11.653, 11.660, 11.665, 11.674, 11.687, 11.701,
          11.714,
          11.728, 11.742, 11.755, 11.762, 11.776, 11.837, 11.905, 11.959, 11.973,
          11.976,
          11.987, 12.000, 12.007, 12.014, 12.016, 12.021, 12.027, 12.041, 12.055,
          12.068,
          12.082, 12.095, 12.109, 12.150, 12.163, 12.177, 12.191, 12.204, 12.218,
          12.231,
          12.245, 12.259, 12.272, 12.286, 12.299, 12.313, 12.327, 12.340, 12.354,
          12.367,
          12.381, 12.395, 12.408, 12.422, 12.436, 12.449, 12.463, 12.476, 12.490,
          12.504,
          12.558, 12.599, 12.653, 12.708, 12.762, 12.803, 12.898, 12.993, 13.129,
          13.252,
          13.497, 13.742, 14.014, 14.558, 14.966, 15.510, 16.055, 16.599, 17.007,
          17.415,
          17.959, 19.048, 20.000, 21.089, 22.041, 23.130, 24.490, 26.123, 28.572,
          30.000
          ]
Y2P6G6 = [0.00, 0.27, 0.84, 1.06, 1.15, 1.20, 1.23, 1.25, 1.28, 1.29,
          1.29, 1.28, 1.27, 1.26, 1.26, 1.25, 1.24, 1.23, 1.23, 1.24,
          1.25, 1.25, 1.26, 1.26, 1.27, 1.28, 1.27, 1.24, 1.52, 1.49,
          1.50, 1.36, 1.45, 1.80, 1.93, 1.97, 1.83, 1.68, 1.62, 1.60,
          1.65, 1.91, 2.49, 2.06, 2.00, 1.94, 1.82, 1.75, 1.69, 1.59,
          1.51, 1.54, 1.64, 1.83, 1.83, 1.84, 1.80, 1.78, 1.73, 1.68,
          1.62, 1.63, 1.60, 1.58, 1.56, 1.53, 1.51, 1.49, 1.48, 1.47,
          1.46, 1.49, 1.54, 1.50, 1.66, 1.57, 1.50, 1.45, 1.47, 1.46,
          1.39, 1.39, 1.45, 1.70, 1.84, 2.17, 2.53, 2.83, 3.05, 3.16,
          3.25, 3.21, 3.07, 3.01, 2.97, 2.93, 2.86, 2.76, 2.55, 2.43
          ]
YP2P6G6 = [0.0 for i in range(100)]
# 2P5 E=11.6660274 EV J=0
# SHAPE FUNCTION FROM B  AND Z   SCALED BY 1/E ABOVE 108.84 EV

X2P5G6 = [11.6660, 11.674, 11.687, 11.701, 11.714, 11.728, 11.742,
          11.755, 11.762, 11.776,
          11.782, 11.796, 11.810, 11.823, 11.837, 11.850, 11.864, 11.878, 11.891,
          11.905,
          11.919, 11.932, 11.946, 11.959, 11.973, 11.976, 11.980, 11.984, 11.987,
          11.989,
          11.993, 12.000, 12.007, 12.014, 12.016, 12.021, 12.027, 12.041, 12.055,
          12.068,
          12.082, 12.095, 12.109, 12.150, 12.163, 12.177, 12.191, 12.204, 12.218,
          12.231,
          12.245, 12.259, 12.272, 12.286, 12.299, 12.313, 12.327, 12.340, 12.354,
          12.367,
          12.381, 12.395, 12.408, 12.422, 12.504, 12.558, 12.599, 12.694, 12.708,
          12.748,
          12.803, 12.912, 12.993, 13.089, 13.252, 13.497, 13.742, 14.014, 14.558,
          14.966,
          15.510, 16.055, 16.599, 17.007, 17.959, 19.048, 20.000, 21.089, 22.041,
          23.130,
          24.490, 26.123, 28.572, 30.000, 32.653, 38.096, 43.538, 54.422, 68.028,
          81.634,
          95.239, 108.84
          ]
Y2P5G6 = [0.00, 0.52, 0.75, 0.87, 0.94, 0.99, 1.03, 1.06, 1.08, 1.11,
          1.12, 1.14, 1.16, 1.18, 1.21, 1.23, 1.25, 1.27, 1.30, 1.32,
          1.35, 1.38, 1.42, 1.46, 1.33, 1.30, 1.28, 1.43, 1.57, 1.66,
          1.76, 1.96, 2.22, 2.24, 2.02, 1.66, 1.40, 1.42, 1.48, 1.54,
          1.60, 1.67, 1.89, 2.24, 2.28, 2.26, 2.25, 2.26, 2.25, 2.19,
          2.12, 2.16, 2.11, 2.02, 1.86, 1.66, 1.59, 1.74, 2.21, 2.19,
          2.18, 2.12, 2.09, 2.10, 2.14, 2.19, 2.24, 2.03, 2.21, 2.74,
          2.71, 2.65, 2.52, 2.98, 2.93, 2.87, 3.09, 3.48, 4.86, 6.32,
          8.30, 9.88, 10.9, 10.7, 10.7, 9.74, 8.95, 8.27, 7.85, 7.76,
          7.21, 6.91, 6.59, 6.42, 6.19, 5.82, 5.54, 5.00, 4.42, 3.92,
          3.51, 3.16
          ]
YP2P5G6 = [0.0 for i in range(102)]
# 3e6 E=11.998135 J=0
#  SHAPE FUNCTION FROM B AND Z SCALED BY 1/E**3 ABOVE 54.422 EV

X3D6G6 = [11.9981, 12.014, 12.068, 12.082, 12.095, 12.109, 12.150,
          12.163, 12.177, 12.191,
          12.204, 12.218, 12.231, 12.245, 12.259, 12.272, 12.286, 12.299, 12.313,
          12.327,
          12.340, 12.354, 12.367, 12.381, 12.395, 12.408, 12.449, 12.463, 12.476,
          12.490,
          12.504, 12.517, 12.558, 12.599, 12.626, 12.640, 12.653, 12.694, 12.748,
          12.871,
          12.993, 13.129, 13.197, 13.293, 13.402, 13.524, 13.606, 14.014, 14.422,
          14.966,
          15.510, 16.055, 16.599, 17.007, 17.551, 17.959, 19.048, 20.000, 21.089,
          22.041,
          23.130, 24.490, 25.851, 28.572, 30.000, 32.653, 38.096, 43.538, 54.422
          ]
Y3D6G6 = [0.00, .053, .058, .069, .088, .119, .155, .155, .157, .136,
          .135, .136, .149, .118, .112, .113, .117, .120, .120, .117,
          .126, .147, .140, .136, .126, .123, .123, .122, .121, .119,
          .118, .117, .117, .118, .117, .113, .107, .124, .157, .151,
          .163, .194, .230, .245, .248, .265, .280, .344, .442, .548,
          .802, 1.09, 1.38, 1.61, 1.87, 2.25, 2.53, 2.55, 2.45, 2.33,
          2.16, 1.94, 1.79, 1.48, 1.35, 1.14, .765, .539, .269
          ]
YP3D6G6 = [0.0 for i in range(69)]
# 3e5 E=12.037029 J=1  RESONANCE RADIATION  103.003 NM   F=0.0053
# SHAPE FUNCTION FROM B AND Z UP TO 68 EV
# ABOVE  68 EV USE BEF SCALING

X3D5G6 = [12.0370, 12.041, 12.055, 12.068, 12.082, 12.095, 12.109,
          12.150, 12.163, 12.177,
          12.191, 12.204, 12.218, 12.231, 12.245, 12.259, 12.272, 12.286, 12.299,
          12.313,
          12.327, 12.340, 12.354, 12.367, 12.381, 12.395, 12.408, 12.422, 12.436,
          12.449,
          12.463, 12.476, 12.490, 12.504, 12.558, 12.612, 12.653, 12.708, 12.762,
          12.803,
          12.898, 13.061, 13.252, 13.524, 13.742, 14.014, 14.286, 14.558, 14.830,
          14.966,
          15.238, 15.510, 15.783, 16.055, 16.327, 16.599, 16.871, 17.007, 17.279,
          17.551,
          17.959, 19.048, 20.000, 21.089, 22.041, 23.130, 24.490, 26.123, 28.572,
          30.000,
          32.653, 38.096, 43.538, 54.422, 68.028
          ]
Y3D5G6 = [0.00, .084, .113, .139, .173, .216, .238, .352, .381, .395,
          .409, .439, .505, .568, .427, .392, .403, .407, .390, .348,
          .353, .369, .431, .417, .412, .393, .397, .406, .414, .420,
          .423, .425, .426, .427, .429, .434, .416, .476, .492, .548,
          .581, .646, .773, .851, .955, 1.08, 1.27, 1.50, 1.67, 1.80,
          2.16, 2.53, 2.88, 3.27, 3.74, 4.17, 4.63, 4.79, 5.23, 5.61,
          6.40, 7.40, 7.54, 7.31, 6.96, 6.48, 5.90, 5.37, 4.63, 4.25,
          3.66, 2.73, 2.05, 1.28, .812
          ]
YP3D5G6 = [0.0 for i in range(75)]
# 2P4 E=12.1003506  J=1
#  SHAPE FUNCTION FROM B AND Z  SCALED BY 1/E**3 ABOVE 30.0 EV

X2P4G6 = [12.1004, 12.109, 12.150, 12.163, 12.177, 12.191, 12.204,
          12.218, 12.231, 12.245,
          12.259, 12.272, 12.286, 12.299, 12.313, 12.327, 12.340, 12.354, 12.367,
          12.381,
          12.395, 12.408, 12.449, 12.463, 12.476, 12.490, 12.504, 12.517, 12.531,
          12.544,
          12.558, 12.599, 12.653, 12.708, 12.762, 12.803, 12.898, 12.993, 13.089,
          13.197,
          13.293, 13.402, 13.497, 13.606, 13.878, 14.014, 14.558, 14.966, 15.238,
          15.510,
          15.919, 16.463, 17.007, 17.551, 17.959, 19.048, 20.000, 21.089, 22.041,
          23.130,
          24.490, 26.123, 28.572, 30.0
          ]
Y2P4G6 = [0.00, .121, .308, .308, .320, .339, .352, .369, .395, .408,
          .435, .454, .453, .456, .473, .510, .552, .531, .482, .459,
          .463, .465, .467, .469, .471, .475, .479, .483, .488, .493,
          .499, .519, .571, .625, .633, .617, .822, .739, .627, .671,
          .706, .800, .781, .785, .831, .854, .904, 1.09, 1.26, 1.50,
          1.80, 2.27, 2.62, 2.88, 3.20, 3.49, 3.48, 3.15, 2.76, 2.34,
          1.93, 1.54, 1.17, 1.00
          ]
YP2P4G6 = [0.0 for i in range(64)]
# 3e3 E=12.111740 J=2
# SHAPE FUNCTION FROM B AND Z  SCALED BY 1/E**3 ABOVE 95.239 EV

X3D3G6 = [12.1117, 12.150, 12.163, 12.177, 12.191, 12.204, 12.218,
          12.231, 12.245, 12.259,
          12.272, 12.286, 12.299, 12.313, 12.327, 12.340, 12.354, 12.367, 12.381,
          12.395,
          12.408, 12.422, 12.436, 12.449, 12.463, 12.476, 12.490, 12.504, 12.517,
          12.531,
          12.558, 12.572, 12.612, 12.626, 12.640, 12.653, 12.667, 12.694, 12.748,
          12.803,
          12.898, 12.993, 13.061, 13.129, 13.197, 13.293, 13.402, 13.606, 13.878,
          14.150,
          14.558, 14.966, 15.510, 16.055, 16.599, 17.007, 17.551, 17.959, 19.048,
          20.000,
          21.089, 22.041, 23.130, 24.490, 26.123, 28.572, 30.000, 32.653, 38.096,
          43.538,
          54.422, 68.028, 81.634, 95.239
          ]
Y3D3G6 = [0.00, .573, .543, .494, .395, .352, .346, .389, .400, .364,
          .352, .345, .335, .318, .269, .246, .325, .343, .389, .413,
          .420, .432, .447, .460, .472, .480, .486, .490, .492, .494,
          .496, .496, .495, .493, .488, .482, .476, .447, .584, .610,
          .616, .578, .663, .735, .815, .860, .870, .949, 1.12, 1.33,
          1.85, 2.49, 3.35, 4.06, 4.96, 5.51, 6.45, 7.54, 8.83, 9.11,
          8.82, 8.32, 7.70, 6.95, 6.18, 5.19, 4.70, 3.89, 2.63, 1.79,
          .876, .409, .215, .126
          ]
YP3D3G6 = [0.0 for i in range(74)]
# 3D4! E=12.125317  J=4
# SHAPE FUNCTION FROM B AND Z  SCALED BY 1/E**3 ABOVE  81.634 EV

X3D4PG6 = [12.1253, 12.150, 12.163, 12.177, 12.191, 12.204, 12.218,
           12.231, 12.245, 12.259,
           12.272, 12.286, 12.299, 12.313, 12.327, 12.340, 12.354, 12.367, 12.381,
           12.395,
           12.408, 12.422, 12.436, 12.449, 12.463, 12.476, 12.490, 12.504, 12.517,
           12.531,
           12.558, 12.572, 12.612, 12.626, 12.640, 12.653, 12.667, 12.694, 12.748,
           12.803,
           12.898, 12.993, 13.061, 13.129, 13.197, 13.293, 13.402, 13.606, 13.878,
           14.150,
           14.558, 14.966, 15.510, 16.055, 16.599, 17.007, 17.551, 17.959, 19.048,
           20.000,
           21.089, 22.041, 23.130, 24.490, 26.123, 28.572, 30.000, 32.653, 38.096,
           43.538,
           54.422, 68.028, 81.634
           ]
Y3D4PG6 = [0.00, .057, .081, .179, .137, .150, .184, .210, .245, .290,
           .328, .327, .324, .305, .285, .303, .318, .296, .313, .330,
           .334, .349, .363, .373, .380, .385, .390, .393, .397, .401,
           .408, .412, .424, .427, .430, .447, .498, .525, .571, .713,
           .691, .640, .702, .790, .836, .889, .944, 1.02, 1.20, 1.47,
           1.99, 2.69, 3.74, 4.77, 5.64, 6.27, 7.23, 7.37, 8.24, 8.35,
           7.91, 7.30, 6.58, 5.73, 4.92, 3.88, 3.41, 2.69, 1.68, 1.09,
           .508, .232, .122
           ]
YP3D4PG6 = [0.0 for i in range(73)]
# 2P3 E=12.1404262  J=1
# SHAPE FUNCTION FROM B AND Z  SCALED BY 1/E**3 ABOVE  81.634 EV

X2P3G6 = [12.1404, 12.150, 12.163, 12.177, 12.191, 12.204, 12.218,
          12.231, 12.245, 12.259,
          12.272, 12.286, 12.299, 12.313, 12.327, 12.340, 12.354, 12.367, 12.381,
          12.395,
          12.408, 12.422, 12.436, 12.449, 12.463, 12.476, 12.490, 12.504, 12.517,
          12.531,
          12.558, 12.572, 12.612, 12.626, 12.640, 12.653, 12.667, 12.694, 12.748,
          12.803,
          12.898, 12.993, 13.061, 13.129, 13.197, 13.293, 13.402, 13.606, 13.878,
          14.150,
          14.558, 14.966, 15.510, 16.055, 16.599, 17.007, 17.551, 17.959, 19.048,
          20.000,
          21.089, 22.041, 23.130, 24.490, 26.123, 28.572, 30.000, 32.653, 38.096,
          43.538,
          54.422, 68.028, 81.634
          ]
Y2P3G6 = [0.00, .108, .284, .400, .456, .485, .496, .544, .568, .536,
          .506, .485, .484, .495, .509, .559, .593, .581, .576, .562,
          .559, .551, .543, .537, .533, .532, .532, .534, .536, .540,
          .551, .557, .580, .586, .591, .613, .729, .777, .646, .678,
          .873, .725, .672, .632, .644, .667, .723, .657, .690, .652,
          .676, .818, 1.07, 1.26, 1.74, 2.23, 2.61, 2.94, 3.35, 3.27,
          2.86, 2.50, 2.40, 1.75, 1.42, 1.05, .890, .665, .384, .249,
          .138, .080, .048
          ]
YP2P3G6 = [0.0 for i in range(73)]
# 2P2 E=12.1436522  J=2
# SHAPE FUNCTION FROM B AND Z  SCALED BY 1/E  ABOVE  108.84 EV

X2P2G6 = [12.1437, 12.150, 12.163, 12.177, 12.191, 12.204, 12.218,
          12.231, 12.245, 12.259,
          12.272, 12.286, 12.299, 12.313, 12.327, 12.340, 12.354, 12.367, 12.381,
          12.395,
          12.408, 12.422, 12.436, 12.449, 12.463, 12.476, 12.490, 12.504, 12.517,
          12.531,
          12.558, 12.572, 12.612, 12.626, 12.640, 12.653, 12.667, 12.694, 12.748,
          12.803,
          12.898, 12.993, 13.061, 13.129, 13.197, 13.293, 13.402, 13.606, 13.878,
          14.150,
          14.558, 14.966, 15.510, 16.055, 16.599, 17.007, 17.551, 17.959, 19.048,
          20.000,
          21.089, 22.041, 23.130, 24.490, 26.123, 28.572, 30.000, 32.653, 38.096,
          43.538,
          54.422, 68.028, 81.634, 95.239, 108.84
          ]
Y2P2G6 = [0.00, .181, .402, .577, .690, .760, .798, .852, .876, .915,
          .965, 1.01, 1.02, 1.05, 1.09, 1.17, 1.17, 1.15, 1.15, 1.14,
          1.12, 1.11, 1.11, 1.11, 1.12, 1.12, 1.14, 1.15, 1.16, 1.18,
          1.21, 1.22, 1.27, 1.28, 1.29, 1.29, 1.35, 1.49, 1.43, 1.66,
          1.53, 1.76, 1.52, 1.45, 1.50, 1.56, 1.75, 1.70, 1.64, 1.71,
          1.91, 2.24, 2.93, 3.26, 3.79, 4.23, 4.62, 5.05, 5.59, 5.74,
          5.62, 5.34, 5.00, 4.65, 4.29, 3.88, 3.66, 3.31, 2.76, 2.38,
          1.90, 1.53, 1.28, 1.10, .962
          ]
YP2P2G6 = [0.0 for i in range(75)]
# 3D4 E=12.178504  J=3
# SHAPE FUNCTION FROM B AND Z  SCALED  BY 1/E  ABOVE 108.84 EV

X3D4G6 = [12.1785, 12.191, 12.204, 12.218, 12.231, 12.245, 12.259,
          12.272, 12.286, 12.299,
          12.313, 12.327, 12.340, 12.354, 12.367, 12.381, 12.395, 12.408, 12.422,
          12.436,
          12.449, 12.463, 12.476, 12.558, 12.653, 12.748, 12.803, 12.993, 13.089,
          13.388,
          13.606, 14.014, 14.286, 14.558, 14.830, 15.102, 15.510, 15.919, 16.463,
          17.007,
          17.551, 17.959, 19.048, 20.000, 21.089, 22.041, 23.130, 24.490, 26.123,
          28.572,
          30.000, 32.653, 38.096, 43.538, 54.422, 68.028, 81.634, 95.239, 108.84
          ]
Y3D4G6 = [0.00, .363, .381, .395, .437, .491, .560, .630, .684, .700,
          .655, .613, .672, .717, .706, .725, .735, .718, .702, .693,
          .691, .691, .693, .717, .890, .870, .844, .734, .831, .857,
          .864, .976, 1.20, 1.52, 1.88, 2.20, 2.69, 3.08, 3.67, 3.93,
          4.10, 4.36, 4.66, 4.67, 4.50, 4.26, 3.97, 3.62, 3.28, 2.84,
          2.63, 2.31, 1.83, 1.52, 1.21, 1.01, .878, .781, .704
          ]
YP3D4G6 = [0.0 for i in range(59)]
# 2P1 E=12.2564658  J=0
# SHAPE FUNCTION FROM B AND Z  SCALED BY 1/E ABOVE 108.84 EV

X2P1G6 = [12.2565, 12.272, 12.286, 12.299, 12.313, 12.327, 12.340,
          12.354, 12.367, 12.381,
          12.463, 12.504, 12.558, 12.612, 12.653, 12.708, 12.762, 12.803, 12.898,
          12.966,
          13.061, 13.197, 13.402, 13.551, 13.742, 14.014, 14.558, 14.966, 15.510,
          16.055,
          16.463, 17.007, 17.551, 17.959, 19.048, 20.000, 21.089, 22.041, 23.130,
          24.490,
          26.123, 28.572, 30.000, 32.653, 38.096, 43.538, 54.422, 68.028, 81.634,
          95.239, 108.84
          ]
Y2P1G6 = [0.00, .200, .261, .282, .298, .321, .378, .554, .540, .517,
          .478, .489, .518, .560, .508, .642, .789, .647, 1.01, .822,
          .922, .866, .995, 1.06, 1.11, 1.20, 1.59, 2.23, 3.27, 4.28,
          4.85, 5.41, 5.75, 5.98, 5.74, 5.35, 4.96, 4.70, 4.49, 4.30,
          4.14, 3.95, 3.86, 3.73, 3.53, 3.38, 3.09, 2.75, 2.46, 2.20, 2.00
          ]
YP2P1G6 = [0.0 for i in range(51)]
# 3e1!! E=12.257998  J=2
# SHAPE FUNCTION FROM B AND Z  SCALED BY 1/E**3 ABOVE 68.028 EV

X3D1PPG6 = [12.2580, 12.272, 12.286, 12.299, 12.313, 12.327, 12.340,
            12.354, 12.367, 12.381,
            12.463, 12.504, 12.558, 12.612, 12.653, 12.708, 12.762, 12.803, 12.898,
            12.966,
            13.061, 13.197, 13.402, 13.551, 13.742, 14.014, 14.558, 14.966, 15.510,
            16.055,
            16.463, 17.007, 17.551, 17.959, 19.048, 20.000, 21.089, 22.041, 23.130,
            24.490,
            26.123, 28.572, 30.000, 32.653, 38.096, 43.538, 54.422, 68.028
            ]
Y3D1PPG6 = [0.00, .038, .055, .073, .093, .107, .125, .158, .178, .204,
            .231, .253, .283, .319, .380, .368, .399, .473, .318, .348,
            .450, .455, .524, .516, .552, .631, .926, 1.24, 1.54, 1.75,
            1.99, 2.41, 2.63, 2.60, 2.66, 2.63, 2.50, 2.35, 2.18, 1.97,
            1.79, 1.48, 1.33, 1.08, .689, .444, .221, .116
            ]
YP3D1PPG6 = [0.0 for i in range(48)]
# 3e1! E=12.284275  J=3
# SHAPE FUNCTION FROM B AND Z  SCALED BY 1/E ABOVE  38 EV

X3D1PG6 = [12.2843, 12.327, 12.340, 12.354, 12.367, 12.381, 12.463,
           12.504, 12.558, 12.612,
           12.653, 12.708, 12.762, 12.803, 12.898, 12.966, 13.061, 13.197, 13.402,
           13.551,
           13.742, 14.014, 14.558, 14.966, 15.510, 16.055, 16.463, 17.007, 17.551,
           17.959,
           19.048, 20.000, 21.089, 22.041, 23.130, 24.490, 26.123, 28.572, 30.000,
           32.653, 38.096
           ]
Y3D1PG6 = [0.00, .313, .357, .448, .451, .465, .527, .568, .604, .637,
           .685, .742, .625, .781, .553, .538, .588, .591, .606, .566,
           .535, .529, .688, .891, 1.24, 1.50, 1.53, 1.59, 1.78, 1.68,
           1.56, 1.47, 1.42, 1.41, 1.40, 1.40, 1.37, 1.29, 1.23, 1.11, .913
           ]
YP3D1PG6 = [0.0 for i in range(41)]
# 2S5 E=12.352158  J=2
# SHAPE FUNCTION FROM B AND Z  SCALED BY 1/E**3 ABOVE 68  EV

X2S5G6 = [12.3522, 12.367, 12.381, 12.395, 12.408, 12.422, 12.463,
          12.504, 12.558, 12.612,
          12.653, 12.708, 12.762, 12.803, 12.898, 12.966, 13.061, 13.197, 13.402,
          13.551,
          13.742, 14.014, 14.558, 14.966, 15.510, 16.055, 16.463, 17.007, 17.551,
          17.959,
          19.048, 20.000, 21.089, 22.041, 23.130, 24.490, 26.123, 28.572, 30.000,
          32.653,
          38.096, 43.538, 54.422, 68.028
          ]
Y2S5G6 = [0.00, .235, .250, .475, .598, .674, .773, .845, .945, 1.04,
          1.06, 1.18, .748, .861, 1.05, 1.05, 1.17, 1.14, 1.12, 1.07,
          1.03, .989, 1.09, 1.22, 1.49, 1.76, 1.85, 1.93, 1.98, 2.03,
          1.89, 1.73, 1.55, 1.41, 1.28, 1.12, .995, .812, .725, .586,
          .377, .246, .119, .058
          ]
YP2S5G6 = [0.0 for i in range(44)]
# 3e2 E=12.354555  J=1 RESONANCE RADIATION  100.356 NM  F=0.082
#       USE BEF SCALING
#
# 2S4 E=12.3852827 J=1 RESONANCE RADIATION  100.107 NM  F=0.154
#        USE BEF SCALING
#
# 3P10 E=12.7563854 EV J=1
#       SHAPE FUNCTION FROM B AND Z SCALED BY 1/E**3 ABOVE 68 EV

X3P10G6 = [12.7564, 12.993, 14.014, 14.966, 16.055, 17.007, 17.959,
           19.048, 20.000, 21.089,
           22.041, 23.130, 24.490, 26.123, 28.572, 30.000, 38.096, 43.538, 54.422,
           68.028
           ]
Y3P10G6 = [0.00, .459, .956, 1.41, 2.20, 2.55, 3.05, 2.96, 2.74, 2.38,
           2.04, 1.70, 1.36, 1.07, 0.75, 0.61, 0.23, 0.14, .078, .046
           ]
YP3P10G6 = [0.0 for i in range(20)]
# 3P9  E=12.7847085 EV J=3
#       SHAPE FUNCTION FROM B AND Z SCALED BY 1/E**3 ABOVE 68 EV

X3P9G6 = [12.7847, 12.993, 14.014, 14.966, 16.055, 17.007, 17.959,
          19.048, 20.000, 21.089,
          22.041, 23.130, 24.490, 26.123, 28.572, 30.000, 38.096, 43.538, 54.422,
          68.028
          ]
Y3P9G6 = [0.00, .511, 1.48, 2.40, 3.02, 3.44, 3.57, 3.57, 3.36, 2.94,
          2.54, 2.12, 1.72, 1.40, 1.02, 0.86, 0.38, 0.24, .122, .061
          ]
YP3P9G6 = [0.0 for i in range(20)]
# 3P8  E=12.7853913 EV J=2
#       SHAPE FUNCTION FROM B AND Z SCALED BY 1/EN  ABOVE 68 EV

X3P8G6 = [12.7854, 12.993, 14.014, 14.966, 16.055, 17.007, 17.959,
          19.048, 20.000, 21.089,
          22.041, 23.130, 24.490, 26.123, 28.572, 30.000, 38.096, 43.538, 54.422,
          68.028
          ]
Y3P8G6 = [0.00, .575, 1.19, 2.00, 2.64, 2.86, 3.08, 3.11, 3.06, 2.91,
          2.74, 2.56, 2.36, 2.17, 1.95, 1.83, 1.38, 1.19, 0.94, 0.75
          ]
YP3P8G6 = [0.0 for i in range(20)]
# 3S1PP E=12.8033935 EV J=2
#        SHAPE FUNCTION FROM B AND Z SCALED BY 1/EN**3 ABOVE 68 EV

X3S1PPG6 = [12.8034, 12.993, 14.014, 14.966, 16.055, 17.007, 17.959,
            19.048, 20.000, 21.089,
            22.041, 23.130, 24.490, 26.123, 28.572, 30.000, 38.096, 43.538, 54.422,
            68.028
            ]
Y3S1PPG6 = [0.00, .328, 0.84, 1.39, 2.05, 3.41, 4.82, 6.11, 6.68, 6.68,
            6.40, 5.94, 5.36, 4.81, 4.05, 3.69, 2.14, 1.49, 0.76, 0.36
            ]
YP3S1PPG6 = [0.0 for i in range(20)]
# 3P7 E=12.8092373 EV J=1
#        SHAPE FUNCTION FROM B AND Z SCALED BY 1/EN**3 ABOVE 68 EV

X3P7G6 = [12.8092, 12.993, 14.014, 14.966, 16.055, 17.007, 17.959,
          19.048, 20.000, 21.089,
          22.041, 23.130, 24.490, 26.123, 28.572, 30.000, 38.096, 43.538, 54.422,
          68.028
          ]
Y3P7G6 = [0.00, 0.29, 0.64, 1.05, 1.31, 1.26, 1.27, 1.10, 0.96, 0.81,
          0.70, 0.60, 0.51, 0.44, 0.35, 0.31, 0.17, 0.12, .088, .067
          ]
YP3P7G6 = [0.0 for i in range(20)]
# 3P6 E=12.8153298 EV J=2
#        SHAPE FUNCTION FROM B AND Z SCALED BY 1/EN ABOVE 68 EV

X3P6G6 = [12.8153, 12.993, 14.014, 14.966, 16.055, 17.007, 17.959,
          19.048, 20.000, 21.089,
          22.041, 23.130, 24.490, 26.123, 28.572, 30.000, 38.096, 43.538, 54.422,
          68.028
          ]
Y3P6G6 = [0.00, 0.33, 1.18, 1.44, 1.73, 1.98, 1.95, 1.71, 1.50, 1.34,
          1.23, 1.14, 1.04, 0.95, 0.81, 0.75, 0.51, 0.42, 0.32, 0.25
          ]
YP3P6G6 = [0.0 for i in range(20)]
# 3S1PPPP E=12.8252582 EV J=2
#        SHAPE FUNCTION FROM B AND Z SCALED  BY 1/EN**3 ABOVE 68 EV

X3S1PPPPG6 = [12.8253, 12.993, 14.014, 14.966, 16.055, 17.007, 17.959,
              19.048, 20.000, 21.089,
              22.041, 23.130, 24.490, 26.123, 28.572, 30.000, 38.096, 43.538, 54.422,
              68.028
              ]
Y3S1PPPPG6 = [0.00, 0.16, 0.41, 0.83, 1.71, 2.50, 3.10, 3.56, 3.83, 3.78,
              3.57, 3.26, 2.89, 2.45, 1.97, 1.75, 0.89, 0.58, 0.27, 0.13
              ]
YP3S1PPPPG6 = [0.0 for i in range(20)]
# 3S1PPP E=12.8573390 EV J=3
#        SHAPE FUNCTION FROM B AND Z SCALED BY 1/EN ABOVE 68 EV

X3S1PPPG6 = [12.8573, 12.993, 14.014, 14.966, 16.055, 17.007, 17.959,
             19.048, 20.000, 21.089,
             22.041, 23.130, 24.490, 26.123, 28.572, 30.000, 38.096, 43.538, 54.422,
             68.028
             ]
Y3S1PPPG6 = [0.00, 0.29, 0.54, 0.99, 2.02, 2.69, 3.38, 3.90, 4.10, 4.05,
             3.84, 3.55, 3.20, 2.80, 2.33, 2.11, 1.27, 0.98, 0.67, 0.50
             ]
YP3S1PPPG6 = [0.0 for i in range(20)]
# 3P5 E=12.8648022 EV J=0
#        SHAPE FUNCTION FROM B AND Z SCALED BY 1/EN ABOVE 68 EV

X3P5G6 = [12.8648, 12.993, 14.014, 14.966, 16.055, 17.007, 17.959,
          19.048, 20.000, 21.089,
          22.041, 23.130, 24.490, 26.123, 28.572, 30.000, 38.096, 43.538, 54.422,
          68.028
          ]
Y3P5G6 = [0.00, 0.56, 2.30, 4.54, 6.23, 6.30, 6.01, 5.23, 4.62, 4.10,
          3.79, 3.71, 3.29, 3.07, 2.86, 2.75, 2.39, 2.25, 2.02, 1.79
          ]
YP3P5G6 = [0.0 for i in range(20)]
# 4e5 E=12.8698 EV J=1 RESONANCE RADIATION   96.3338NM  F=0.0140
#       USE BEF SCALING
# 4e6 E=12.9034651 EV J=0
#        SHAPE FUNCTION FROM B AND Z SCALED BY 1/EN**3 ABOVE 68 EV

X4D6G6 = [12.9035, 12.993, 14.014, 14.966, 16.055, 17.007, 17.959,
          19.048, 20.000, 21.089,
          22.041, 23.130, 24.490, 26.123, 28.572, 30.000, 38.096, 43.538, 54.422,
          68.028
          ]
Y4D6G6 = [0.00, 0.07, 0.21, 0.32, 0.57, 0.76, 1.09, 1.24, 1.30, 1.28,
          1.22, 1.12, 0.98, 0.90, 0.74, 0.67, 0.34, 0.25, 0.12, .056
          ]
YP4D6G6 = [0.0 for i in range(20)]
# 4d4P E=12.972537 EV J=4
#        SHAPE FUNCTION FROM B AND Z SCALED BY 1/EN**3 ABOVE 68 EV

X4D4PG6 = [12.9725, 12.993, 14.014, 14.966, 16.055, 17.007, 17.959,
           19.048, 20.000, 21.089,
           22.041, 23.130, 24.490, 26.123, 28.572, 30.000, 38.096, 43.538, 54.422,
           68.028
           ]
Y4D4PG6 = [0.00, 0.14, 0.89, 1.48, 2.18, 3.01, 3.72, 4.15, 4.25, 4.08,
           3.81, 3.48, 3.07, 2.64, 2.09, 1.84, 0.92, 0.60, 0.28, 0.13
           ]
YP4D4PG6 = [0.0 for i in range(20)]
# 3S1P E=13.0043688 EV J=1 RESONANCE RADIATION 95.341 NM F=0.0435
#       USE BEF SCALING
#
# 4D4 E=13.0079847 EV J=3
#        SHAPE FUNCTION FROM B AND Z SCALED BY 1/EN  ABOVE 68 EV

X4D4G6 = [13.0080, 14.014, 14.966, 16.055, 17.007, 17.959, 19.048,
          20.000, 21.089, 22.041,
          23.130, 24.490, 26.123, 28.572, 30.000, 38.096, 43.538, 54.422, 68.028
          ]
Y4D4G6 = [0.00, 1.10, 1.37, 1.85, 2.26, 2.34, 2.14, 1.95, 1.78, 1.67,
          1.56, 1.46, 1.38, 1.26, 1.20, 0.95, 0.90, 0.84, 0.78
          ]
YP4D4G6 = [0.0 for i in range(19)]
# 4D3 E=13.0192383 EV J=2
#        SHAPE FUNCTION FROM B AND Z SCALED BY 1/EN**3  ABOVE 68 EV

X4D3G6 = [13.0192, 14.014, 14.966, 16.055, 17.007, 17.959, 19.048,
          20.000, 21.089, 22.041,
          23.130, 24.490, 26.123, 28.572, 30.000, 38.096, 43.538, 54.422, 68.028
          ]
Y4D3G6 = [0.00, 0.65, 1.06, 1.66, 2.16, 2.15, 2.16, 2.08, 1.91, 1.74,
          1.58, 1.41, 1.29, 1.05, 0.94, 0.48, 0.32, 0.16, 0.09
          ]
YP4D3G6 = [0.0 for i in range(19)]
# 2S3 E=13.029666  EV J=0
#        SHAPE FUNCTION FROM B AND Z SCALED BY 1/EN**3  ABOVE 68 EV

X2S3G6 = [13.0297, 14.014, 14.966, 16.055, 17.007, 17.959, 19.048,
          20.000, 21.089, 22.041,
          23.130, 24.490, 26.123, 28.572, 30.000, 38.096, 43.538, 54.422, 68.028
          ]
Y2S3G6 = [0.00, 0.13, 0.13, 0.17, 0.27, 0.29, 0.29, 0.27, 0.25, 0.23,
          0.21, 0.19, 0.17, 0.15, 0.14, .073, .054, .028, .015
          ]
YP2S3G6 = [0.0 for i in range(19)]
# 2S2  E=13.036483  EV J=1 RESONANCE RADIATION 95.106 NM F=0.0105
#       USE BEF SCALING
#
# 4D1PP E=13.0386113  J=2
#        SHAPE FUNCTION FROM B AND Z SCALED BY 1/EN**3  ABOVE 68 EV

X4D1PPG6 = [13.0386, 14.014, 14.966, 16.055, 17.007, 17.959, 19.048,
            20.000, 21.089, 22.041,
            23.130, 24.490, 26.123, 28.572, 30.000, 38.096, 43.538, 54.422, 68.028
            ]
Y4D1PPG6 = [0.00, 0.50, 0.80, 1.12, 1.46, 1.64, 1.49, 1.40, 1.29, 1.19,
            1.17, 1.02, 0.94, 0.80, 0.73, 0.32, 0.22, .109, .059
            ]
YP4D1PPG6 = [0.0 for i in range(19)]
# 4D1P E=13.0441877  J=3
#        SHAPE FUNCTION FROM B AND Z SCALED BY 1/EN**3  ABOVE 68 EV

X4D1PG6 = [13.0442, 14.014, 14.966, 16.055, 17.007, 17.959, 19.048,
           20.000, 21.089, 22.041,
           23.130, 24.490, 26.123, 28.572, 30.000, 38.096, 43.538, 54.422, 68.028
           ]
Y4D1PG6 = [0.00, 0.63, 0.92, 1.47, 1.58, 1.70, 1.50, 1.30, 1.13, 1.02,
           0.95, 0.88, 0.84, 0.71, 0.64, 0.33, 0.22, .123, .084
           ]
YP4D1PG6 = [0.0 for i in range(19)]
# 3S5  E=13.0986140  J=2
#        SHAPE FUNCTION FROM B AND Z SCALED BY 1/EN**3  ABOVE 68 EV

X3S5G6 = [13.0986, 14.014, 14.966, 16.055, 17.007, 17.959, 19.048,
          20.000, 21.089, 22.041,
          23.130, 24.490, 26.123, 28.572, 30.000, 38.096, 43.538, 54.422, 68.028
          ]
Y3S5G6 = [0.00, 0.88, 1.56, 1.89, 1.82, 2.08, 2.37, 2.40, 2.21, 1.96,
          1.65, 1.30, 1.02, 0.69, 0.57, 0.22, 0.13, .058, .027
          ]
YP3S5G6 = [0.0 for i in range(19)]
# 4D2  E=13.0987356 EV J=1 RESONANCE RADIATION 94.654 NM F=0.0970
#       USE BEF SCALING
#
# 3S4  E=13.1138948 EV J=1 RESONANCE RADIATION 94.545 NM F=0.0808
#       USE BEF SCALING
#
# SUM 4F STATES   E=13.14  J=1,2,5,4,3,2,4,4
#        SHAPE FUNCTION FROM B AND Z SCALED BY 1/EN  ABOVE 68 EV

X4FSG6 = [13.14, 14.014, 14.966, 16.055, 17.007, 17.959, 19.048,
          20.000, 21.089, 22.041,
          23.130, 24.490, 26.123, 28.572, 30.000, 38.096, 43.538, 54.422, 68.028
          ]
Y4FSG6 = [0.00, 1.58, 3.51, 4.86, 4.89, 4.50, 3.60, 2.89, 2.24, 1.85,
          1.49, 1.19, 0.93, 0.69, 0.59, 0.32, 0.25, 0.18, 0.14
          ]
YP4FSG6 = [0.0 for i in range(19)]
# 5D5  E=13.3501402 EV J=1 RESONANCE RADIATION 92.872 NM F=0.0015
#       USE BEF SCALING
#
# 5D2  E=13.4223741 EV J=1 RESONANCE RADIATION 92.372 NM F=0.0439
#         USE BEF SCALING
#
# 4S4  E=13.4365439 EV J=1 RESONANCE RADIATION 92.274 NM F=0.0203
#         USE BEF SCALING
#
# HIGH E=13.6 EV  SUM OF HIGHER DIPOLE STATES            F=0.168
#         USE BEF SCALING
#
#    TOTAL OSCILLATOR STRENGTH =1.1258 1.1058
#
#  BREMSSTRAHLUNG X-SECTION WITH CUT OFF UNITS 10**-24

Z36TG6 = [3500., 2633., 1689., 1126., 708., 367., 226., 146., 97.2, 84.6,
          82.1, 82.5, 83.1, 83.6, 84.0, 84.5, 85.1, 86.0, 86.5, 87.3,
          87.4, 87.8, 88.0, 88.3, 88.4
          ]
EBRMG6 = [1000., 2000., 5000., 1.E4, 2.E4, 5.E4, 1.E5, 2.E5, 5.E5, 1.E6,
          2.E6, 3.E6, 4.E6, 5.E6, 6.E6, 8.E6, 1.E7, 1.5E7, 2.E7, 3.E7,
          4.E7, 5.E7, 6.E7, 8.E7, 1.E8]

EING6 = [9.9152, 10.0324, 10.5624, 10.6436, 11.3035, 11.4430, 11.4447, 11.5261, 11.5458, 11.6660, 11.9981, 12.0370,
         12.1004, 12.1117, 12.1253, 12.1404, 12.1437, 12.1785, 12.2565, 12.2580, 12.2843, 12.3522, 12.3546, 12.3853,
         12.7564, 12.7847, 12.7854, 12.8034, 12.8092, 12.8153, 12.8253, 12.8573, 12.8648, 12.8698, 12.9035, 12.9725,
         13.0044, 13.0080, 13.0192, 13.0297, 13.0365, 13.0386, 13.0442, 13.0986, 13.0987, 13.1139, 13.14, 13.3501,
         13.4224, 13.4365, 13.6, 0.0]
for i in range(250 - 52):
    EING6.append(0.0)
gd['gas6/XEN'] = XENG6
gd['gas6/YXSEC'] = YXSECG6
gd['gas6/XEL'] = XELG6
gd['gas6/YEL'] = YELG6
gd['gas6/XEPS'] = XEPSG6
gd['gas6/YEPS'] = YEPSG6
gd['gas6/XION'] = XIONG6
gd['gas6/YION'] = YIONG6
gd['gas6/YINC'] = YINCG6
gd['gas6/YIN1'] = YIN1G6
gd['gas6/XIN2'] = XIN2G6
gd['gas6/YIN2'] = YIN2G6
gd['gas6/XIN3'] = XIN3G6
gd['gas6/YIN3'] = YIN3G6
gd['gas6/XIN4'] = XIN4G6
gd['gas6/YIN4'] = YIN4G6
gd['gas6/XKSH'] = XKSHG6
gd['gas6/YKSH'] = YKSHG6
gd['gas6/XL1S'] = XL1SG6
gd['gas6/YL1S'] = YL1SG6
gd['gas6/XL2S'] = XL2SG6
gd['gas6/YL2S'] = YL2SG6
gd['gas6/XL3S'] = XL3SG6
gd['gas6/YL3S'] = YL3SG6
gd['gas6/XM1S'] = XM1SG6
gd['gas6/YM1S'] = YM1SG6
gd['gas6/XM2S'] = XM2SG6
gd['gas6/YM2S'] = YM2SG6
gd['gas6/XM3S'] = XM3SG6
gd['gas6/YM3S'] = YM3SG6
gd['gas6/XM4S'] = XM4SG6
gd['gas6/YM4S'] = YM4SG6
gd['gas6/XM5S'] = XM5SG6
gd['gas6/YM5S'] = YM5SG6
gd['gas6/X1S5'] = X1S5G6
gd['gas6/Y1S5'] = Y1S5G6
gd['gas6/YP1S5'] = YP1S5G6
gd['gas6/X1S4'] = X1S4G6
gd['gas6/Y1S4'] = Y1S4G6
gd['gas6/YP1S4'] = YP1S4G6
gd['gas6/X1S3'] = X1S3G6
gd['gas6/Y1S3'] = Y1S3G6
gd['gas6/YP1S3'] = YP1S3G6
gd['gas6/X1S2'] = X1S2G6
gd['gas6/Y1S2'] = Y1S2G6
gd['gas6/YP1S2'] = YP1S2G6
gd['gas6/X2P10'] = X2P10G6
gd['gas6/Y2P10'] = Y2P10G6
gd['gas6/YP2P10'] = YP2P10G6
gd['gas6/X2P9'] = X2P9G6
gd['gas6/Y2P9'] = Y2P9G6
gd['gas6/YP2P9'] = YP2P9G6
gd['gas6/X2P8'] = X2P8G6
gd['gas6/Y2P8'] = Y2P8G6
gd['gas6/YP2P8'] = YP2P8G6
gd['gas6/X2P7'] = X2P7G6
gd['gas6/Y2P7'] = Y2P7G6
gd['gas6/YP2P7'] = YP2P7G6
gd['gas6/X2P6'] = X2P6G6
gd['gas6/Y2P6'] = Y2P6G6
gd['gas6/YP2P6'] = YP2P6G6
gd['gas6/X2P5'] = X2P5G6
gd['gas6/Y2P5'] = Y2P5G6
gd['gas6/YP2P5'] = YP2P5G6
gd['gas6/X3D6'] = X3D6G6
gd['gas6/Y3D6'] = Y3D6G6
gd['gas6/YP3D6'] = YP3D6G6
gd['gas6/X3D5'] = X3D5G6
gd['gas6/Y3D5'] = Y3D5G6
gd['gas6/YP3D5'] = YP3D5G6
gd['gas6/X2P4'] = X2P4G6
gd['gas6/Y2P4'] = Y2P4G6
gd['gas6/YP2P4'] = YP2P4G6
gd['gas6/X3D3'] = X3D3G6
gd['gas6/Y3D3'] = Y3D3G6
gd['gas6/YP3D3'] = YP3D3G6
gd['gas6/X3D4P'] = X3D4PG6
gd['gas6/Y3D4P'] = Y3D4PG6
gd['gas6/YP3D4P'] = YP3D4PG6
gd['gas6/X2P3'] = X2P3G6
gd['gas6/Y2P3'] = Y2P3G6
gd['gas6/YP2P3'] = YP2P3G6
gd['gas6/X2P2'] = X2P2G6
gd['gas6/Y2P2'] = Y2P2G6
gd['gas6/YP2P2'] = YP2P2G6
gd['gas6/X3D4'] = X3D4G6
gd['gas6/Y3D4'] = Y3D4G6
gd['gas6/YP3D4'] = YP3D4G6
gd['gas6/X2P1'] = X2P1G6
gd['gas6/Y2P1'] = Y2P1G6
gd['gas6/YP2P1'] = YP2P1G6
gd['gas6/X3D1PP'] = X3D1PPG6
gd['gas6/Y3D1PP'] = Y3D1PPG6
gd['gas6/YP3D1PP'] = YP3D1PPG6
gd['gas6/X3D1P'] = X3D1PG6
gd['gas6/Y3D1P'] = Y3D1PG6
gd['gas6/YP3D1P'] = YP3D1PG6
gd['gas6/X2S5'] = X2S5G6
gd['gas6/Y2S5'] = Y2S5G6
gd['gas6/YP2S5'] = YP2S5G6
gd['gas6/X3P10'] = X3P10G6
gd['gas6/Y3P10'] = Y3P10G6
gd['gas6/YP3P10'] = YP3P10G6
gd['gas6/X3P9'] = X3P9G6
gd['gas6/Y3P9'] = Y3P9G6
gd['gas6/YP3P9'] = YP3P9G6
gd['gas6/X3P8'] = X3P8G6
gd['gas6/Y3P8'] = Y3P8G6
gd['gas6/YP3P8'] = YP3P8G6
gd['gas6/X3S1PP'] = X3S1PPG6
gd['gas6/Y3S1PP'] = Y3S1PPG6
gd['gas6/YP3S1PP'] = YP3S1PPG6
gd['gas6/X3P7'] = X3P7G6
gd['gas6/Y3P7'] = Y3P7G6
gd['gas6/YP3P7'] = YP3P7G6
gd['gas6/X3P6'] = X3P6G6
gd['gas6/Y3P6'] = Y3P6G6
gd['gas6/YP3P6'] = YP3P6G6
gd['gas6/X3S1PPPP'] = X3S1PPPPG6
gd['gas6/Y3S1PPPP'] = Y3S1PPPPG6
gd['gas6/YP3S1PPPP'] = YP3S1PPPPG6
gd['gas6/X3S1PPP'] = X3S1PPPG6
gd['gas6/Y3S1PPP'] = Y3S1PPPG6
gd['gas6/YP3S1PPP'] = YP3S1PPPG6
gd['gas6/X3P5'] = X3P5G6
gd['gas6/Y3P5'] = Y3P5G6
gd['gas6/YP3P5'] = YP3P5G6
gd['gas6/X4D6'] = X4D6G6
gd['gas6/Y4D6'] = Y4D6G6
gd['gas6/YP4D6'] = YP4D6G6
gd['gas6/X4D4P'] = X4D4PG6
gd['gas6/Y4D4P'] = Y4D4PG6
gd['gas6/YP4D4P'] = YP4D4PG6
gd['gas6/X4D4'] = X4D4G6
gd['gas6/Y4D4'] = Y4D4G6
gd['gas6/YP4D4'] = YP4D4G6
gd['gas6/X4D3'] = X4D3G6
gd['gas6/Y4D3'] = Y4D3G6
gd['gas6/YP4D3'] = YP4D3G6
gd['gas6/X2S3'] = X2S3G6
gd['gas6/Y2S3'] = Y2S3G6
gd['gas6/YP2S3'] = YP2S3G6
gd['gas6/X4D1PP'] = X4D1PPG6
gd['gas6/Y4D1PP'] = Y4D1PPG6
gd['gas6/YP4D1PP'] = YP4D1PPG6
gd['gas6/X4D1P'] = X4D1PG6
gd['gas6/Y4D1P'] = Y4D1PG6
gd['gas6/YP4D1P'] = YP4D1PG6
gd['gas6/X3S5'] = X3S5G6
gd['gas6/Y3S5'] = Y3S5G6
gd['gas6/YP3S5'] = YP3S5G6
gd['gas6/X4FS'] = X4FSG6
gd['gas6/Y4FS'] = Y4FSG6
gd['gas6/YP4FS'] = YP4FSG6
gd['gas6/Z36T'] = Z36TG6
gd['gas6/EBRM'] = EBRMG6
gd['gas6/EIN'] = EING6

XENG9 = [0.00, .001, .002, .003, .004, .005, .007, 0.01, .014, 0.02, .025,
         0.03, 0.04, 0.05, 0.06, 0.07, 0.08, 0.09, 0.10, 0.11, 0.12,
         0.13, 0.14, 0.16, 0.18, 0.20, 0.25, 0.30, 0.35, 0.40, 0.50,
         0.60, 0.70, 0.80, 1.00, 1.50, 2.00, 2.50, 3.00, 4.00, 5.00,
         6.00, 7.00, 8.00, 9.00, 10.0, 12.0, 14.0, 16.0, 18.0, 20.0,
         25.0, 30.0, 40.0, 50.0, 60.0, 70.0, 80.0, 100., 125., 150.,
         175., 200., 250., 300., 350., 400., 450., 500., 600., 700.,
         800., 900., 1000., 1250., 1500., 1750., 2000., 2500., 3000., 3500.,
         4000., 4500., 5000., 6000., 7000., 8000., 9000., 1.0e4, 1.25e4, 1.5e4,
         1.75e4, 2.0e4, 2.5e4, 3.0e4, 3.5e4, 4.0e4, 4.5e4, 5.0e4, 6.0e4, 7.0e4,
         8.0e4, 9.0e4, 1.0e5, 1.25e5, 1.5e5, 1.75e5, 2.0e5, 2.5e5, 3.0e5, 3.5e5,
         4.0e5, 4.5e5, 5.0e5, 6.0e5, 7.0e5, 8.0e5, 9.0e5, 1.0e6, 1.25e6, 1.5e6,
         1.75e6, 2.0e6, 2.5e6, 3.0e6, 3.5e6, 4.0e6, 4.5e6, 5.0e6, 6.0e6, 7.0e6,
         8.0e6, 9.0e6, 1.0e7, 1.25e7, 1.5e7, 1.75e7, 2.0e7, 2.5e7, 3.0e7, 3.5e7,
         4.0e7, 4.5e7, 5.0e7, 6.0e7, 7.0e7, 8.0e7, 9.0e7, 1.0e8, 1.25e8, 1.5e8,
         1.75e8, 2.0e8, 2.5e8, 3.0e8, 3.5e8, 4.0e8, 4.5e8, 5.0e8, 6.0e8, 7.0e8,
         8.0e8, 9.0e8, 1.0e9
         ]
YMTG9 = [32.0, 31.0, 29.0, 27.0, 26.0, 25.0, 23.0, 20.0, 17.6, 15.2, 13.0,
         11.2, 7.25, 4.70, 3.25, 2.40, 1.80, 1.40, 1.15, 1.10, 1.08,
         1.08, 1.10, 1.25, 1.50, 1.85, 2.40, 3.15, 4.10, 4.85, 6.10,
         6.90, 7.15, 7.30, 7.70, 8.45, 9.10, 10.3, 11.6, 13.9, 17.8,
         20.7, 21.4, 21.3, 20.0, 17.6, 13.9, 11.3, 9.40, 8.00, 7.20,
         5.75, 4.90, 3.76, 3.00, 2.50, 2.15, 1.80, 1.41, 1.10, 0.91,
         .770, .680, .540, .440, .370, .325, .280, .252, .200, .159,
         .127, .104, .0870, .0592, .0431, .0329, .0260, .0175, .0127, .00961,
         .00756, .00612, .00506, .00364, .00276, .00216, .00175, .00144, 9.62e-4,
         6.91e-4,
         5.22e-4, 4.10e-4, 2.74e-4, 1.97e-4, 1.49e-4, 1.17e-4, 9.48e-5, 7.85e-5,
         5.67e-5, 4.31e-5,
         3.41e-5, 2.77e-5, 2.31e-5, 1.57e-5, 1.15e-5, 8.88e-6, 7.11e-6, 4.93e-6,
         3.67e-6, 2.87e-6,
         2.33e-6, 1.94e-6, 1.64e-6, 1.24e-6, 9.79e-7, 7.98e-7, 6.67e-7, 5.68e-7,
         4.06e-7, 3.06e-7,
         2.41e-7, 1.95e-7, 1.36e-7, 1.01e-7, 7.87e-8, 6.30e-8, 5.17e-8, 4.32e-8,
         3.16e-8, 2.42e-8,
         1.92e-8, 1.56e-8, 1.29e-8, 8.67e-9, 6.23e-9, 4.71e-9, 3.69e-9, 2.45e-9,
         1.75e-9, 1.31e-9,
         1.02e-9, 8.19e-10, 6.71e-10, 4.75e-10, 3.53e-10, 2.73e-10, 2.18e-10,
         1.77e-10, 1.14e-10, 7.99e-11,
         5.89e-11, 4.52e-11, 2.90e-11, 2.02e-11, 1.48e-11, 1.14e-11, 8.98e-12,
         7.28e-12, 5.06e-12, 3.71e-12,
         2.85e-12, 2.25e-12, 1.82e-12]
# ASSUME ELASTIC = MOMENTUM TRANSFER UP TO 3.0 EV (NO GOOe ELASTIC DATA)

YELG9 = [32.0, 31.0, 29.0, 27.0, 26.0, 25.0, 23.0, 20.0, 17.6, 15.2, 13.0,
         11.2, 7.25, 4.70, 3.25, 2.40, 1.80, 1.40, 1.15, 1.10, 1.08,
         1.08, 1.10, 1.25, 1.50, 1.85, 2.40, 3.15, 4.10, 4.85, 6.10,
         6.90, 7.15, 7.30, 7.70, 8.45, 9.10, 10.3, 15.2, 18.9, 23.4,
         27.2, 29.6, 31.9, 31.0, 30.1, 27.7, 25.9, 24.1, 23.3, 22.1,
         20.0, 17.3, 13.4, 11.9, 10.7, 9.85, 9.02, 7.40, 6.25, 5.50,
         4.95, 4.50, 3.90, 3.43, 3.04, 2.74, 2.49, 2.29, 1.97, 1.73,
         1.54, 1.39, 1.27, 1.04, .877, .760, .671, .544, .458, .395,
         .348, .311, .281, .235, .203, .178, .159, .144, .116, .0978,
         .0845, .0745, .0605, .0512, .0445, .0395, .0356, .0325, .0278, .0244,
         .0226, .0200, .0184, .0156, .0138, .0124, .0115, .0101, .00918, .00855,
         .00808, .00772, .00744, .00702, .00674, .00653, .00637, .00625, .00605,
         .00592,
         .00584, .00578, .00570, .00566, .00563, .00561, .00560, .00559, .00557,
         .00556,
         .00556, .00555, .00555, .00555
         ]
for J in range(29):
    YELG9.append(.00554)
YEPSG9 = []
for J in range(38):
    YEPSG9.append(1.0)
YEPSG9.extend([.65352, .61534, .65007,
               .65056, .59839, .52532, .49651, .42242, .32895, .26232, .21931, .17939,
               .16529,
               .13630, .13322, .13133, .11165, .09963, .09005, .07893, .07377, .06576,
               .06017,
               .05510, .05287, .04673, .04198, .03896, .03770, .03497, .03403, .03050,
               .02667,
               .02302, .02024, .01805, .01418, .01167, .00990, .00860, .00681, .00563,
               .00480,
               .00418, .00370, .00332, .00276, .00235, .00205, .00182, .00163, .00130,
               .00108,
               .000924, .000806, .000641, .000531, .000452, .000393, .000348, 3.11e-4,
               2.56e-4, 2.17e-4,
               1.82e-4, 1.65e-4, 1.47e-4, 1.15e-4, 9.32e-5, 7.80e-5, 6.67e-5, 5.10e-5,
               4.08e-5, 3.36e-5,
               2.83e-5, 2.43e-5, 2.11e-5, 1.65e-5, 1.33e-5, 1.10e-5, 9.27e-6, 7.94e-6,
               5.71e-6, 4.29e-6,
               3.35e-6, 2.69e-6, 1.86e-6, 1.36e-6, 1.04e-6, 8.19e-7, 6.63e-7, 5.48e-7,
               3.93e-7, 2.95e-7,
               2.30e-7, 1.84e-7, 1.57e-7, 9.87e-8, 6.96e-8, 5.16e-8, 3.98e-8, 2.58e-8,
               1.80e-8, 1.33e-8,
               1.02e-8, 8.06e-9, 6.54e-9, 4.53e-9, 3.32e-9, 2.53e-9, 1.99e-9, 1.61e-9,
               1.01e-9, 6.94e-10,
               5.04e-10, 3.82e-10, 2.40e-10, 1.64e-10, 1.19e-10, 9.0e-11, 7.00e-11,
               5.6e-11, 3.8e-11, 2.8e-11,
               2.1e-11, 1.6e-11, 1.3e-11])

XVIB1G9 = [.117, 0.13, 0.15, 0.17, 0.20, 0.23, 0.25, 0.30, 0.40, 0.50,
           0.60, 0.70, 0.85, 1.00, 1.50, 2.00, 2.50, 3.00, 3.50, 4.00,
           5.00, 6.00, 7.50, 8.50, 10.0, 15.0, 20.0, 30.0, 40.0
           ]
YVIB1G9 = [0.00, .070, .105, .126, .135, .140, .140, .129, .105, .082,
           .067, .057, .049, .049, .064, .087, .108, .129, .152, .187,
           .246, .316, .433, .433, .351, .246, .164, .073, .042
           ]
XVIB2G9 = [.148, 0.16, 0.17, 0.20, 0.23, 0.25, 0.30, 0.40, 0.50, 0.60,
           0.70, 0.85, 1.00, 1.50, 2.00, 2.50, 3.00, 3.50, 4.00, 5.00,
           6.00, 7.50, 8.50, 10.0, 15.0, 20.0, 30.0, 40.0
           ]
YVIB2G9 = [0.00, .044, .077, .108, .115, .123, .123, .108, .092, .077,
           .065, .055, .054, .062, .077, .096, .115, .139, .169, .223,
           .293, .370, .370, .308, .216, .142, .065, .037
           ]
XVIB3G9 = [.182, 0.19, 0.20, 0.23, 0.25, 0.30, 0.35, 0.40, 0.50, 0.60,
           0.70, 0.85, 1.00, 1.50, 2.00, 2.50, 3.00, 3.50, 4.00, 5.00,
           6.00, 7.50, 8.50, 10.0, 15.0, 20.0, 30.0, 40.0
           ]
YVIB3G9 = [0.00, .070, .091, .189, .231, .259, .266, .259, .224, .182,
           .164, .154, .157, .171, .189, .210, .252, .301, .364, .490,
           .623, .805, .805, .665, .434, .294, .133, .077
           ]
XVIB4G9 = [.366, .367, .368, .370, .375, .380, .385, .390, .395, .400,
           .410, .420, .430, .440, .450, .460, .480, .500, .520, .550,
           .600, .650, .700, .800, .900, 1.00, 1.10, 1.20, 1.30, 1.40,
           1.50, 1.70, 2.00, 2.50, 3.00, 3.50, 4.00, 5.00, 6.00, 7.50,
           8.50, 10.0, 15.0, 20.0, 30.0, 40.0
           ]
YVIB4G9 = [0.00, .03782, .05336, .07494, .1107, .1361, .1561, .1727,
           .1864, .2002,
           .2210, .2382, .2520, .2641, .2728, .2814, .2952, .3056, .3125, .3194,
           .3246, .3246, .3229, .3143, .3026, .3026, .3048, .3071, .3115, .3160,
           .320, .329, .343, .387, .472, .570, .694, .908, 1.16, 1.32,
           1.16, .935, .507, .289, .129, .715
           ]
XVIB5G9 = [.548, 1.00, 1.50, 2.00, 3.00, 3.50, 4.00, 5.00, 6.00, 7.50,
           8.50, 10.0, 15.0, 20.0, 30.0, 40.0
           ]
YVIB5G9 = [0.00, .001, .002, .003, .0055, .011, .044, .094, .134, .143,
           .134, .116, .068, .0383, .0171, .0096]
# GROSS IONISATION X-SECTION  AVERAGE OF TIAN AND VIDAL AND
# NISHIMURA AND TAWARA  (WITHIN 4% OF EACH OTHER) TYPICALLY REDUCE
# NISHIMURA BY 2% ...
# BELOW 20 EV USE AVERAGE OVER ALL DATA
# ABOVE 3 KEV USE SCALED SCHRAM TO 60 KEV THEN SMOOTH JOIN 
# TO MATRIX ELEMENT FIT OF DATA BY  RIEKE AND PREPJCHAL

XIONG9 = [11.52, 12.0, 12.5, 13.0, 14.0, 15.0, 16.0, 17.0, 18.0, 19.0,
          20.0, 25.0, 30.0, 35.0, 40.0, 45.0, 50.0, 60.0, 70.0, 80.0,
          90.0, 100., 125., 150., 175., 200., 225., 250., 275., 300.,
          350., 400., 450., 500., 550., 600., 700., 800., 900., 1000.,
          1250., 1500., 1750., 2000., 2500., 3000., 4000., 7000., 10000., 60000.]
# GROSS IONISATION 

YIONGG9 = [0.00, .017, .038, .061, .270, .518, 0.87, 1.28, 1.62, 1.95,
           2.24, 3.48, 4.45, 4.96, 5.54, 5.87, 6.09, 6.63, 6.80, 6.78,
           6.82, 6.83, 6.46, 6.18, 5.86, 5.57, 5.31, 4.96, 4.71, 4.51,
           4.08, 3.80, 3.44, 3.28, 3.13, 2.94, 2.66, 2.33, 2.21, 1.99,
           1.72, 1.49, 1.34, 1.20, 1.06, .881, .657, .411, .290, .0599]
# COUNTING IONISATION

YIONCG9 = [0.0, .017, .038, .061, .270, .518, 0.87, 1.28, 1.62, 1.95,
           2.24, 3.48, 4.45, 4.94, 5.47, 5.65, 5.78, 6.27, 6.42, 6.39,
           6.44, 6.45, 6.07, 5.79, 5.47, 5.18, 4.94, 4.61, 4.38, 4.19,
           3.80, 3.53, 3.20, 3.05, 2.91, 2.74, 2.47, 2.17, 2.06, 1.85,
           1.60, 1.39, 1.25, 1.12, .986, .820, .611, .382, .270, .0557]
# ALL INDIVIDUAL BREAKUP CHANNELS FROM TIAN AND VIeAL
# CORRECTEe BY WANG AND VIeAL FOR DISSOCIATION OF C2H6++
#
#   C2H6+   

XION1G9 = [11.52, 13.0, 14.0, 15.0, 17.5, 20.0, 25.0, 30.0, 35.0, 40.0,
           45.0, 50.0, 60.0, 70.0, 80.0, 90.0, 100., 125., 150., 175.,
           200., 225., 250., 275., 300., 350., 400., 450., 500., 550., 600.
           ]
YION1G9 = [0.0, .055, .095, .130, .215, .366, .566, .664, .684, .747,
           .734, .724, .773, .768, .758, .749, .751, .717, .692, .665,
           .642, .618, .583, .560, .544, .499, .473, .430, .417, .401, .377]
#  C2H4+

XION2G9 = [12.05, 13.0, 14.0, 15.0, 17.5, 20.0, 25.0, 30.0, 35.0, 40.0,
           45.0, 50.0, 60.0, 70.0, 80.0, 90.0, 100., 125., 150., 175.,
           200., 225., 250., 275., 300., 350., 400., 450., 500., 550., 600.
           ]
YION2G9 = [.0, .005, .140, .290, .672, 1.068, 1.705, 2.240, 2.350, 2.461,
           2.481, 2.473, 2.607, 2.568, 2.517, 2.510, 2.492, 2.346, 2.273, 2.179,
           2.103, 2.031, 1.925, 1.841, 1.777, 1.635, 1.542, 1.408, 1.352, 1.301, 1.226]
# C2H5+

XION3G9 = [12.65, 13.0, 14.0, 15.0, 17.5, 20.0, 25.0, 30.0, 35.0, 40.0,
           45.0, 50.0, 60.0, 70.0, 80.0, 90.0, 100., 125., 150., 175.,
           200., 225., 250., 275., 300., 350., 400., 450., 500., 550., 600.
           ]
YION3G9 = [0.0, .001, .034, .070, .156, .266, .412, .507, .556, .568,
           .569, .565, .597, .603, .589, .595, .588, .566, .546, .529,
           .514, .490, .468, .451, .432, .401, .381, .349, .337, .321, .302]
#  CH3+

XION4G9 = [13.65, 14.0, 15.0, 17.5, 20.0, 25.0, 30.0, 35.0, 40.0, 45.0,
           50.0, 60.0, 70.0, 80.0, 90.0, 100., 125., 150., 175., 200.,
           225., 250., 275., 300., 350., 400., 450., 500., 550., 600.]

YION4G9 = [0.0, .001, .018, .051, .070, .083, .095, .104, .120, .114,
           .130, .176, .203, .216, .218, .218, .197, .178, .159, .138,
           .130, .114, .106, .099, .084, .071, .063, .058, .051, .047]
#  C2H3+

XION5G9 = [14.8, 15.0, 17.5, 20.0, 25.0, 30.0, 35.0, 40.0, 45.0, 50.0,
           60.0, 70.0, 80.0, 90.0, 100., 125., 150., 175., 200., 225.,
           250., 275., 300., 350., 400., 450., 500., 550., 600.
           ]
YION5G9 = [0.0, .005, .175, .294, .432, .553, .709, .814, .836, .827,
           .882, .889, .862, .855, .847, .786, .746, .702, .658, .630,
           .586, .564, .540, .489, .455, .415, .391, .373, .351]
#  C2H2+

XION6G9 = [14.8, 15.0, 17.5, 20.0, 25.0, 30.0, 35.0, 40.0, 45.0, 50.0,
           60.0, 70.0, 80.0, 90.0, 100., 125., 150., 175., 200., 225.,
           250., 275., 300., 350., 400., 450., 500., 550., 600.]

YION6G9 = [0.0, .005, .118, .174, .268, .322, .394, .503, .550, .578,
           .614, .626, .611, .609, .600, .543, .500, .459, .426, .396,
           .364, .338, .324, .289, .259, .232, .217, .206, .192]
#  H+

XION7G9 = [20.5, 25.0, 30.0, 35.0, 40.0, 45.0, 50.0, 60.0, 70.0, 80.0,
           90.0, 100., 125., 150., 175., 200., 225., 250., 275., 300.,
           350., 400., 450., 500., 550., 600.
           ]
YION7G9 = [0.0, .011, .041, .053, .055, .001, .001, .001, .062, .111,
           .166, .189, .189, .166, .135, .094, .080, .063, .046, .035,
           .014, .004, .001, .0003, .0001, .00003]
#  H2+

XION8G9 = [21.5, 25.0, 30.0, 35.0, 40.0, 45.0, 50.0, 60.0, 70.0, 80.0,
           90.0, 100., 125., 150., 175., 200., 225., 250., 275., 300.,
           350., 400., 450., 500., 550., 600.
           ]
YION8G9 = [0.0, .002, .007, .013, .015, .020, .008, .023, .039, .041,
           .048, .050, .042, .034, .028, .023, .020, .014, .012, .010,
           .006, .004, .003, .002, .0015, .001]
#  CH2+

XION9G9 = [25.8, 30.0, 35.0, 40.0, 45.0, 50.0, 60.0, 70.0, 80.0, 90.0,
           100., 125., 150., 175., 200., 225., 250., 275., 300., 350.,
           400., 450., 500., 550., 600.
           ]
YION9G9 = [0.0, .020, .036, .056, .054, .065, .098, .109, .110, .117,
           .117, .106, .094, .083, .069, .064, .057, .051, .048, .040,
           .034, .026, .023, .020, .018]
#  C2H+

XION10G9 = [26.2, 35.0, 40.0, 45.0, 50.0, 60.0, 70.0, 80.0, 90.0, 100.,
            125., 150., 175., 200., 225., 250., 275., 300., 350., 400.,
            450., 500., 550., 600.
            ]
YION10G9 = [0.0, .021, .044, .059, .074, .096, .109, .113, .114, .116,
            .105, .092, .081, .070, .064, .053, .050, .043, .036, .031,
            .025, .022, .019, .017]
#  C2H6++

XION11G9 = [32.0, 35.0, 40.0, 45.0, 50.0, 60.0, 70.0, 80.0, 90.0, 100.,
            125., 150., 175., 200., 225., 250., 275., 300., 350., 400.,
            450., 500., 550., 600.
            ]
YION11G9 = [0.0, .019, .074, .219, .313, .360, .380, .385, .383, .384,
            .385, .390, .390, .389, .370, .347, .331, .315, .285, .265,
            .240, .228, .217, .204]
#  H3+

XION12G9 = [32.5, 35.0, 40.0, 45.0, 50.0, 60.0, 70.0, 80.0, 90.0, 100.,
            125., 150., 175., 200., 225., 250., 275., 300., 350., 400.,
            450., 500., 550., 600.
            ]
YION12G9 = [0.0, .001, .002, .001, .001, .011, .012, .017, .015, .015,
            .013, .011, .008, .006, .005, .003, .002, .001, .0005, .00025,
            .00013, .000062, .000045, .00003]
#  CH+

XION13G9 = [36.0, 40.0, 45.0, 50.0, 60.0, 70.0, 80.0, 90.0, 100., 125.,
            150., 175., 200., 225., 250., 275., 300., 350., 400., 450.,
            500., 550., 600.
            ]
YION13G9 = [0.0, .006, .012, .016, .026, .038, .041, .046, .047, .043,
            .036, .029, .025, .023, .019, .015, .014, .010, .007, .005,
            .003, .002, .0015]
#  C2+

XION14G9 = [37.0, 50.0, 60.0, 70.0, 80.0, 90.0, 100., 125., 150., 175.,
            200., 225., 250., 275., 300., 350., 400., 450., 500., 550.,
            600.
            ]
YION14G9 = [0.0, .001, .003, .007, .011, .014, .017, .017, .015, .013,
            .011, .009, .007, .006, .005, .003, .0017, .0007, .0003, .00017,
            .00009]
#  C+

XION15G9 = [37.0, 50.0, 60.0, 70.0, 80.0, 90.0, 100., 125., 150., 175.,
            200., 225., 250., 275., 300., 350., 400., 450., 500., 550.,
            600.
            ]
YION15G9 = [0.0, .001, .004, .008, .011, .015, .016, .017, .015, .013,
            .011, .010, .008, .007, .006, .005, .004, .003, .0018, .0009,
            .0005]
# K-SHELL IONISATION X-SECTION CARBON (SCALED BY 2 IN SUBROUTINE) 

XION16G9 = [285., 298., 307., 316., 325., 335., 345., 365., 398., 422.,
            447., 473., 501., 531., 613., 668., 708., 750., 817., 917.,
            1000., 1122., 1296., 1496., 1679., 1884., 2054., 2238., 2512., 2985.,
            3981., 5012., 7079., 1.0e4, 1.50e4, 2.05e4, 2.51e4, 3.07e4, 4.10e4, 5.01e4,
            6.13e4, 7.08e4, 8.18e4, 1.0e5, 1.54e5, 2.05e5, 2.99e5, 4.10e5, 5.01e5,
            6.13e5,
            7.08e5, 8.18e5, 1.0e6, 1.26e6, 1.5e6, 2.05e6, 3.07e6, 4.10e6, 5.01e6,
            6.13e6,
            7.08e6, 8.18e6, 1.0e7, 1.26e7, 1.5e7, 2.05e7, 3.07e7, 4.10e7, 5.01e7,
            6.13e7,
            7.08e7, 8.18e7, 1.0e8, 1.26e8, 1.5e8, 2.05e8, 3.07e8, 4.10e8, 5.01e8,
            6.13e8,
            7.08e8, 8.18e8, 1.0e9
            ]
YION16G9 = [0.00, 1.66e-4, 3.48e-4, 5.25e-4, 6.96e-4, 8.63e-4, 1.02e-3,
            1.33e-3, 1.75e-3, 2.01e-3,
            2.24e-3, 2.46e-3, 2.66e-3, 2.84e-3, 3.21e-3, 3.38e-3, 3.47e-3, 3.55e-3,
            3.65e-3, 3.72e-3,
            3.75e-3, 3.74e-3, 3.68e-3, 3.57e-3, 3.45e-3, 3.31e-3, 3.19e-3, 3.07e-3,
            2.91e-3, 2.66e-3,
            2.25e-3, 1.95e-3, 1.55e-3, 1.21e-3, 8.97e-4, 7.07e-4, 6.07e-4, 5.21e-4,
            4.21e-4, 3.63e-4,
            3.14e-4, 2.84e-4, 2.57e-4, 2.25e-4, 1.74e-4, 1.50e-4, 1.28e-4, 1.15e-4,
            1.09e-4, 1.05e-4,
            1.03e-4, 1.02e-4, 1.01e-4, 1.005e-4, 1.01e-4, 1.03e-4, 1.07e-4, 1.11e-4,
            1.14e-4, 1.17e-4,
            1.20e-4, 1.22e-4, 1.25e-4, 1.29e-4, 1.32e-4, 1.38e-4, 1.45e-4, 1.50e-4,
            1.54e-4, 1.58e-4,
            1.60e-4, 1.63e-4, 1.67e-4, 1.71e-4, 1.74e-4, 1.80e-4, 1.87e-4, 1.92e-4,
            1.96e-4, 2.00e-4,
            2.02e-4, 2.05e-4, 2.09e-4]
# ATTACHMENT  H-  EXCLUeING ION PAIRS

XATT1G9 = [7.00, 7.50, 8.00, 8.50, 9.00, 9.18, 9.50, 10.0, 10.5, 11.0,
           11.5
           ]
YATT1G9 = [0.00, 7.65e-5, 2.52e-4, 8.42e-4, 1.55e-3, 1.70e-3, 1.50e-3,
           8.33e-4, 2.50e-4, 7.65e-5, 0.00]
# ATTACHMENT CH2- EXCLUeING ION PAIRS

XATT2G9 = [7.90, 8.40, 8.90, 9.40, 9.90, 10.1, 10.4, 10.9, 11.4
           ]
YATT2G9 = [0.00, 1.53e-5, 5.04e-5, 1.68e-4, 3.10e-4, 3.40e-4, 3.00e-4,
           1.67e-4, 0.0]
#                
# NON DIPOLE AT 6.85 EV

XTR1G9 = [6.85, 8.00, 9.00, 10.0, 11.0, 12.0, 14.0, 16.0, 19.0, 22.0,
          26.0, 30.0
          ]
YTR1G9 = [0.00, .030, .042, .048, .054, .057, .060, .060, .054, .048,
          .036, .026]
# NON DIPOLE AT 8.00 EV

XTR2G9 = [8.00, 9.50, 10.5, 11.5, 12.5, 14.5, 16.5, 19.5, 22.5, 26.5,
          30.0
          ]
YTR2G9 = [0.00, .205, .295, .336, .353, .369, .369, .344, .295, .230,
          .181]
# NON DIPOLE AT 10.0 EV

XTR3G9 = [10.0, 11.0, 12.0, 13.0, 14.0, 17.0, 20.0, 23.0, 27.0, 30.0,
          35.0
          ]
YTR3G9 = [0.00, .331, .680, .794, .898, .945, .945, .898, .777, .675,
          .513]
#                                      
# BREMSSTRAHLUNG X-SECTION WITH CUT UNITS 10**-24

Z1TG9 = [11.3, 6.18, 2.80, 1.54, .858, .407, .251, .176, .145, .150,
         .167, .178, .187, .193, .198, .205, .210, .218, .222, .228,
         .231, .233, .234, .235, .235
         ]
Z6TG9 = [298., 178., 85.2, 47.5, 26.3, 12.2, 7.06, 4.45, 3.06, 2.82,
         2.89, 2.99, 3.08, 3.13, 3.18, 3.25, 3.31, 3.39, 3.44, 3.49,
         3.52, 3.54, 3.55, 3.57, 3.57
         ]
EBRMG9 = [1000., 2000., 5000., 1.E4, 2.E4, 5.E4, 1.E5, 2.E5, 5.E5, 1.E6,
          2.E6, 3.E6, 4.E6, 5.E6, 6.E6, 8.E6, 1.E7, 1.5E7, 2.E7, 3.E7,
          4.E7, 5.E7, 6.E7, 8.E7, 1.E8]
# WINTERS CHEM.PHYS.36(1979)353  (NULL COLLISION)  
#   REeUCEe  BY 0.9 IN SUBROUTINE

XNUL1G9 = [8.4, 10.3, 15.0, 20.0, 25.0, 30.0, 40.0, 50.0, 60.0, 70.0,
           80.0, 90.0, 100., 125., 150., 175., 200., 250., 300., 350.,
           400., 450., 500., 550., 600.
           ]
YNUL1G9 = [0.0, 0.20, 1.30, 3.20, 4.00, 5.60, 6.40, 7.00, 7.40, 7.60,
           7.65, 7.60, 7.50, 7.30, 7.10, 6.90, 6.70, 6.40, 6.00, 5.60,
           5.30, 4.90, 4.60, 4.30, 4.10]
# LIGHT EMISSION FROM H ALPHA     
#  MOHLMANN  CHEM PHYS 19(1977)233

XNUL2G9 = [20.0, 40.0, 60.0, 80.0, 100., 150., 200., 300., 500., 1000.,
           1300., 1700., 2000.
           ]
YNUL2G9 = [0.0, .0116, .0196, .0241, .0250, .0222, .0186, .0121, .007,
           .0034,
           .0026, .0020, .0017]
# LIGHT EMISSION FROM CH2(A2DELTA -X2PI)
#  MOHLMANN  CHEM PHYS 19(1977)233

XNUL3G9 = [16.0, 20.0, 40.0, 60.0, 80.0, 100., 150., 200., 300., 500.,
           1000., 1300., 1700., 2000.
           ]
YNUL3G9 = [0.0, .0011, .0041, .0057, .0062, .0061, .0050, .0041, .0028,
           .0017,
           .0008, .0006, .0005, .0004]
EING9 = [-0.0358, 0.0358, -0.117, 0.117, -0.148, 0.148, -0.182, 0.182, 0.366, 0.548, 6.85, 7.93, 8.00, 8.15, 8.48,
         8.723, 8.865, 9.007, 9.149, 9.291, 9.433, 9.575, 9.717, 9.859, 10.0, 10.115, 10.45, 10.672, 10.816, 10.960,
         11.104, 11.248, 11.392, 11.732, 12.4, 13.0, 13.5, 14.1, 14.7, 15.3, 15.9, 16.5, 17.1, 17.7, 18.5, 19.5, 20.5,
         21.5, 22.5, 23.5, 24.5, 25.5, 26.5, 27.5, 28.5, 0.0, 0.0]
for i in range(250 - 57):
    EING9.append(0.0)
gd['gas9/XEN'] = XENG9
gd['gas9/YMT'] = YMTG9
gd['gas9/YEL'] = YELG9
gd['gas9/YEPS'] = YEPSG9
gd['gas9/XATT1'] = XATT1G9
gd['gas9/YATT1'] = YATT1G9
gd['gas9/XATT2'] = XATT2G9
gd['gas9/YATT2'] = YATT2G9
gd['gas9/XVIB1'] = XVIB1G9
gd['gas9/YVIB1'] = YVIB1G9
gd['gas9/XVIB2'] = XVIB2G9
gd['gas9/YVIB2'] = YVIB2G9
gd['gas9/XVIB3'] = XVIB3G9
gd['gas9/YVIB3'] = YVIB3G9
gd['gas9/XVIB4'] = XVIB4G9
gd['gas9/YVIB4'] = YVIB4G9
gd['gas9/XVIB5'] = XVIB5G9
gd['gas9/YVIB5'] = YVIB5G9
gd['gas9/XTR1'] = XTR1G9
gd['gas9/YTR1'] = YTR1G9
gd['gas9/XTR2'] = XTR2G9
gd['gas9/YTR2'] = YTR2G9
gd['gas9/XTR3'] = XTR3G9
gd['gas9/YTR3'] = YTR3G9
gd['gas9/XNUL1'] = XNUL1G9
gd['gas9/YNUL1'] = YNUL1G9
gd['gas9/XNUL2'] = XNUL2G9
gd['gas9/YNUL2'] = YNUL2G9
gd['gas9/XNUL3'] = XNUL3G9
gd['gas9/YNUL3'] = YNUL3G9
gd['gas9/XION1'] = XION1G9
gd['gas9/YION1'] = YION1G9
gd['gas9/XION2'] = XION2G9
gd['gas9/YION2'] = YION2G9
gd['gas9/XION3'] = XION3G9
gd['gas9/YION3'] = YION3G9
gd['gas9/XION4'] = XION4G9
gd['gas9/YION4'] = YION4G9
gd['gas9/XION5'] = XION5G9
gd['gas9/YION5'] = YION5G9
gd['gas9/XION6'] = XION6G9
gd['gas9/YION6'] = YION6G9
gd['gas9/XION7'] = XION7G9
gd['gas9/YION7'] = YION7G9
gd['gas9/XION8'] = XION8G9
gd['gas9/YION8'] = YION8G9
gd['gas9/XION9'] = XION9G9
gd['gas9/YION9'] = YION9G9
gd['gas9/XION10'] = XION10G9
gd['gas9/YION10'] = YION10G9
gd['gas9/XION11'] = XION11G9
gd['gas9/YION11'] = YION11G9
gd['gas9/XION12'] = XION12G9
gd['gas9/YION12'] = YION12G9
gd['gas9/XION13'] = XION13G9
gd['gas9/YION13'] = YION13G9
gd['gas9/XION14'] = XION14G9
gd['gas9/YION14'] = YION14G9
gd['gas9/XION15'] = XION15G9
gd['gas9/YION15'] = YION15G9
gd['gas9/XION16'] = XION16G9
gd['gas9/YION16'] = YION16G9
gd['gas9/XION'] = XIONG9
gd['gas9/YIONG'] = YIONGG9
gd['gas9/YIONC'] = YIONCG9
gd['gas9/Z1T'] = Z1TG9
gd['gas9/Z6T'] = Z6TG9
gd['gas9/EBRM'] = EBRMG9
gd['gas9/EIN'] = EING9

XENG10 = [0.00, 0.001, 0.002, 0.003, 0.004, 0.005, 0.007, 0.01, 0.014, 0.02,
          0.03, 0.04, 0.05, 0.06, 0.07, 0.08, 0.09, 0.10, 0.11, 0.12,
          0.13, 0.14, 0.16, 0.18, 0.20, 0.22, 0.24, 0.27, 0.30, 0.35,
          0.40, 0.50, 0.60, 0.80, 1.00, 1.40, 2.00, 2.50, 3.00, 3.50,
          4.00, 5.00, 6.00, 7.00, 7.50, 8.50, 10.0, 12.5, 15.0, 17.5,
          20.0, 25.0, 30.0, 35.0, 40.0, 50.0, 60.0, 70.0, 80.0, 90.0,
          100., 125., 150., 175., 200., 250., 300., 350., 400., 450.,
          500., 600., 700., 800., 900., 1000., 1250., 1500., 1750., 2000.,
          2500., 3000., 3500., 4000., 4500., 5000., 6000., 7000., 8000., 9000.,
          1.0e4, 1.25e4, 1.5e4, 1.75e4, 2.0e4, 2.5e4, 3.0e4, 3.5e4, 4.0e4, 4.5e4,
          5.0e4, 6.0e4, 7.0e4, 8.0e4, 9.0e4, 1.0e5, 1.25e5, 1.5e5, 1.75e5, 2.0e5,
          2.5e5, 3.0e5, 3.5e5, 4.0e5, 4.5e5, 5.0e5, 6.0e5, 7.0e5, 8.0e5, 9.0e5,
          1.0e6, 1.25e6, 1.5e6, 1.75e6, 2.0e6, 2.5e6, 3.0e6, 3.5e6, 4.0e6, 4.5e6,
          5.0e6, 6.0e6, 7.0e6, 8.0e6, 9.0e6, 1.0e7, 1.25e7, 1.5e7, 1.75e7, 2.0e7,
          2.5e7, 3.0e7, 3.5e7, 4.0e7, 4.5e7, 5.0e7, 6.0e7, 7.0e7, 8.0e7, 9.0e7,
          1.0e8, 1.25e8, 1.5e8, 1.75e8, 2.0e8, 2.5e8, 3.0e8, 3.5e8, 4.0e8, 4.5e8,
          5.0e8, 6.0e8, 7.0e8, 8.0e8, 9.0e8, 1.0e9]
# ELASTIC MT : ABOVE 250EV FROM THEORY
#              BELOW 250EV FIT TO TRANSPORT eATA

YMTG10 = [50.9, 50.9, 42.6, 37.0, 33.3, 29.6, 25.5, 20.8, 18.0, 15.3,
          13.1, 11.6, 10.4, 9.08, 7.79, 6.36, 5.03, 3.61, 2.85, 2.52,
          2.47, 2.47, 2.75, 3.23, 3.94, 4.80, 5.40, 6.45, 7.35, 8.35,
          9.07, 10.05, 10.9, 11.8, 12.3, 12.8, 13.6, 14.4, 15.7, 17.5,
          19.5, 23.3, 27.2, 29.0, 29.0, 28.0, 25.5, 21.5, 18.5, 17.0,
          15.5, 12.8, 11.0, 9.50, 8.40, 6.90, 5.80, 5.00, 4.40, 4.00,
          3.60, 2.85, 2.27, 1.85, 1.59, 1.22, .921, .725, .587, .486,
          .410, .304, .236, .188, .154, .129, .0878, .0639, .0488, .0386,
          .0260, .0188, .0143, .0112, 9.08e-3, 7.51e-3, 5.41e-3, 4.09e-3, 3.21e-3,
          2.59e-3,
          2.14e-3, 1.43e-3, 1.03e-3, 7.76e-4, 6.08e-4, 4.06e-4, 2.92e-4, 2.21e-4,
          1.74e-4, 1.41e-4,
          1.17e-4, 8.42e-5, 6.41e-5, 5.06e-5, 4.12e-5, 3.43e-5, 2.33e-5, 1.71e-5,
          1.32e-5, 1.06e-5,
          7.32e-6, 5.45e-6, 4.26e-6, 3.46e-6, 2.87e-6, 2.44e-6, 1.84e-6, 1.45e-6,
          1.19e-6, 9.91e-7,
          8.44e-7, 6.04e-7, 4.55e-7, 3.58e-7, 2.90e-7, 2.03e-7, 1.51e-7, 1.17e-7,
          9.36e-8, 7.68e-8,
          6.42e-8, 4.70e-8, 3.60e-8, 2.85e-8, 2.31e-8, 1.92e-8, 1.29e-8, 9.27e-9,
          7.01e-9, 5.49e-9,
          3.64e-9, 2.60e-9, 1.95e-9, 1.52e-9, 1.22e-9, 9.98e-10, 7.06e-10,
          5.25e-10, 4.06e-10, 3.23e-10,
          2.63e-10, 1.70e-10, 1.19e-10, 8.76e-11, 6.72e-11, 4.31e-11, 3.00e-11,
          2.20e-11, 1.69e-11, 1.33e-11,
          1.08e-11, 7.51e-12, 5.52e-12, 4.23e-12, 3.34e-12, 2.71e-12]
# ELASTIC: ABOVE 150EV FROM THEORY
#            BETWEEN 0.5 ANe 150 EV FROM CONSISTENCY IN TOTAL X-SECTION
#           BELOW 0.5EV SIMILAR TO MERZ ANe  LINeER

YELG10 = [50.9, 50.9, 42.6, 37.0, 33.0, 29.6, 25.5, 20.8, 18.4, 16.4,
          14.2, 12.6, 11.4, 10.5, 9.70, 9.00, 8.30, 7.70, 7.10, 6.60,
          6.20, 5.80, 5.50, 6.15, 6.85, 7.60, 8.20, 9.00, 9.70, 10.5,
          11.3, 12.1, 12.7, 13.1, 14.1, 15.5, 17.4, 18.7, 20.5, 22.0,
          24.6, 30.8, 37.7, 41.2, 42.9, 44.6, 42.8, 38.5, 35.8, 33.4,
          31.3, 27.5, 24.7, 22.8, 21.3, 19.1, 17.2, 15.5, 14.0, 13.0,
          11.9, 9.90, 8.50, 7.57, 6.86, 5.80, 5.05, 4.48, 4.03, 3.67,
          3.37, 2.90, 2.55, 2.27, 2.05, 1.87, 1.53, 1.30, 1.12, .993,
          .805, .677, .585, .515, .460, .416, .349, .301, .264, .236,
          .213, .172, .145, .125, .110, .0896, .0758, .0659, .0585, .0527,
          .0480, .0411, .0362, .0334, .0296, .0273, .0231, .0204, .0184, .0169,
          .0149, .0136, .0127, .0120, .0114, .0110, .0104, .00997, .00970, .00944,
          .00926, .00895, .00877, .00864, .00855, .00844, .00838, .00833, .00831,
          .00829,
          .00827, .00825, .00824, .00823, .00822, .00822, .00821, .00821, .00821,
          .00820,
          .00820, .00820, .00820]
for i in range(23):
    YELG10.append(0.00820)
YEPSG10 = [1.00, 1.00, 1.00, 1.00, 1.00, 1.00, 1.00, 1.00, .96740, .89959,
           .88412, .88129, .86888, .79880, .70972, .57649, .44800, .29459, .22957,
           .21203,
           .22682, .25233, .32703, .35433, .41118, .47945, .51353, .58989, .64598,
           .69856,
           .70909, .74912, .78931, .85180, .80991, .74224, .67932, .66312, .65727,
           .69887,
           .69494, .66427, .59639, .57278, .53606, .47475, .43564, .39174, .34508,
           .33665,
           .32195, .29117, .27113, .24366, .22319, .19428, .17440, .16276, .15632,
           .15128,
           .14738, .13657, .12181, .10656, .09845, .08527, .06923, .05829, .05019,
           .04390,
           .039014, .031780, .026828, .023104, .020285, .018120, .014236, .011650,
           9.981e-3, 8.631e-3,
           6.832e-3, 5.656e-3, 4.828e-3, 4.180e-3, 3.711e-3, 3.327e-3, 2.765e-3,
           2.358e-3, 2.063e-3, 1.824e-3,
           1.642e-3, 1.311e-3, 1.089e-3, 9.288e-4, 8.106e-4, 6.428e-4, 5.323e-4,
           4.534e-4, 3.948e-4, 3.495e-4,
           3.140e-4, 2.573e-4, 2.179e-4, 1.824e-4, 1.657e-4, 1.475e-4, 1.151e-4,
           9.342e-5, 7.843e-5, 6.746e-5,
           5.133e-5, 4.090e-5, 3.356e-5, 2.837e-5, 2.439e-5, 2.122e-5, 1.653e-5,
           1.332e-5, 1.105e-5, 9.308e-6,
           7.972e-6, 5.738e-6, 4.306e-6, 3.371e-6, 2.711e-6, 1.867e-6, 1.365e-6,
           1.043e-6, 8.219e-7, 6.658e-7,
           5.504e-7, 3.946e-7, 2.968e-7, 2.313e-7, 1.849e-7, 1.517e-7, 9.933e-8,
           6.983e-8, 5.185e-8, 4.003e-8,
           2.586e-8, 1.810e-8, 1.334e-8, 1.025e-8, 8.120e-9, 6.566e-9, 4.555e-9,
           3.332e-9, 2.541e-9, 1.997e-9,
           1.608e-9, 1.016e-9, 6.98e-10, 5.06e-10, 3.83e-10, 2.40e-10, 1.64e-10,
           1.19e-10, 9.0e-11, 7.0e-11,
           5.6e-11, 3.8e-11, 2.8e-11, 2.1e-11, 1.6e-11, 1.3e-11]
# GROSS IONISATION X-SECTION AVERAGE OF 1) WANG ANe VIeAL
#  And 2) TAWARA ANe NISHIMURA
# ABOVE 2KEV USE SCHRAM NORMALISEe TO 2KEV eATA POINT OF TAWARA
# ABOVE 10KEV USE UPeATEe FIT TO RIEKE ANe PREPJCHAL WITH CORRECTEe
# IONISATION OSCILLATOR STRENGTH
#

XIONG10 = [11.12, 12.0, 15.0, 17.5, 20.0, 25.0, 30.0, 35.0, 40.0, 45.0,
           50.0, 60.0, 70.0, 80.0, 90.0, 100., 125., 150., 175., 200.,
           250., 300., 350., 400., 450., 500., 600., 700., 800., 900.,
           1000., 1250., 1500., 1750., 2000., 2500., 3000., 3500., 4000., 5000.,
           6000., 7000., 8000., 9000., 10000.]
# GROSS IONISATION

YIONGG10 = [0.00, .206, 1.14, 2.30, 3.31, 5.21, 6.47, 7.37, 8.00, 8.54,
            9.22, 9.79, 10.09, 10.20, 10.24, 10.23, 9.90, 9.36, 8.84, 8.35,
            7.80, 6.84, 6.25, 5.78, 5.26, 4.93, 4.33, 3.99, 3.67, 3.27,
            3.05, 2.64, 2.27, 2.06, 1.88, 1.57, 1.35, 1.19, 1.06, .887,
            .764, .673, .603, .548, .5024]
# COUNTING IONISATION

YIONCG10 = [0.00, .206, 1.14, 2.30, 3.31, 5.21, 6.47, 7.32, 7.81, 8.00,
            8.43, 8.83, 9.019, 9.118, 9.154, 9.145, 8.85, 8.37, 7.90, 7.46,
            6.97, 6.11, 5.59, 5.17, 4.70, 4.41, 3.87, 3.57, 3.28, 2.92,
            2.73, 2.36, 2.03, 1.84, 1.68, 1.40, 1.21, 1.06, .952, .793,
            .683, .602, .539, .490, .4491]
# BREAKUP CHANNELS FROM SCALEe WANG ANe VIeAL CORRECTEe FOR eISSOCIATION
# FROM ++ STATES
#
#  C3H8+

XION1G10 = [11.11, 12.0, 15.0, 17.5, 20.0, 25.0, 30.0, 35.0, 40.0, 45.0,
            50.0, 60.0, 70.0, 80.0, 90.0, 100., 125., 150., 175., 200.,
            250., 300., 350., 400., 450., 500., 600., 700., 800., 900.,
            1000., 1250., 1500., 1750., 2000., 2500., 3000., 3500., 4000., 5000.,
            6000., 7000., 8000., 9000., 10000.
            ]
YION1G10 = [0.00, .055, .213, .337, .456, .722, .854, .877, .960, .920,
            .931, .964, .936, .945, .949, .948, .917, .867, .819, .773,
            .722, .634, .579, .535, .487, .457, .401, .370, .340, .303,
            .282, .245, .210, .191, .174, .145, .125, .110, .0987, .0822,
            .0708, .0624, .0559, .0508, .0465]
#  C3H7+

XION2G10 = [11.55, 12.0, 15.0, 17.5, 20.0, 25.0, 30.0, 35.0, 40.0, 45.0,
            50.0, 60.0, 70.0, 80.0, 90.0, 100., 125., 150., 175., 200.,
            250., 300., 350., 400., 450., 500., 600., 700., 800., 900.,
            1000., 1250., 1500., 1750., 2000., 2500., 3000., 3500., 4000., 5000.,
            6000., 7000., 8000., 9000., 10000.
            ]
YION2G10 = [0.00, .020, .126, .219, .295, .468, .579, .634, .649, .634,
            .646, .662, .666, .673, .675, .675, .653, .617, .583, .551,
            .514, .451, .412, .381, .347, .325, .286, .263, .242, .216,
            .201, .174, .150, .136, .124, .103, .0893, .0782, .0702, .0585,
            .0504, .0444, .0398, .0361, .0331]
#  C3H6+

XION3G10 = [11.75, 12.0, 15.0, 17.5, 20.0, 25.0, 30.0, 35.0, 40.0, 45.0,
            50.0, 60.0, 70.0, 80.0, 90.0, 100., 125., 150., 175., 200.,
            250., 300., 350., 400., 450., 500., 600., 700., 800., 900.,
            1000., 1250., 1500., 1750., 2000., 2500., 3000., 3500., 4000., 5000.,
            6000., 7000., 8000., 9000., 10000.
            ]
YION3G10 = [0.00, .003, .031, .051, .071, .113, .140, .153, .157, .153,
            .156, .160, .161, .162, .163, .163, .157, .149, .140, .133,
            .124, .109, .0993, .0919, .0836, .0784, .0688, .0634, .0583, .0520,
            .0485, .0420, .0361, .0327, .0299, .0249, .0215, .0188, .0169, .0141,
            .0121, .0107, .00958, .00871, .00798]
#  C2H4+

XION4G10 = [11.75, 12.0, 15.0, 17.5, 20.0, 25.0, 30.0, 35.0, 40.0, 45.0,
            50.0, 60.0, 70.0, 80.0, 90.0, 100., 125., 150., 175., 200.,
            250., 300., 350., 400., 450., 500., 600., 700., 800., 900.,
            1000., 1250., 1500., 1750., 2000., 2500., 3000., 3500., 4000., 5000.,
            6000., 7000., 8000., 9000., 10000.
            ]
YION4G10 = [0.00, .027, .257, .444, .604, .957, 1.188, 1.298, 1.330, 1.300,
            1.324, 1.356, 1.366, 1.379, 1.385, 1.383, 1.339, 1.266, 1.195, 1.129,
            1.055, .9248, .8451, .7816, .7112, .6666, .5855, .5396, .4963, .4421,
            .4123, .3570, .3069, .2785, .2543, .2118, .1830, .1603, .1440, .1200,
            .1033, .0911, .0815, .0741, .0679]
#  C2H5+

XION5G10 = [11.91, 12.0, 15.0, 17.5, 20.0, 25.0, 30.0, 35.0, 40.0, 45.0,
            50.0, 60.0, 70.0, 80.0, 90.0, 100., 125., 150., 175., 200.,
            250., 300., 350., 400., 450., 500., 600., 700., 800., 900.,
            1000., 1250., 1500., 1750., 2000., 2500., 3000., 3500., 4000., 5000.,
            6000., 7000., 8000., 9000., 10000.
            ]
YION5G10 = [0.00, .016, .394, .684, .954, 1.512, 1.877, 2.050, 2.100, 2.053,
            2.091, 2.141, 2.156, 2.178, 2.186, 2.184, 2.114, 1.998, 1.887, 1.783,
            1.665, 1.460, 1.334, 1.234, 1.123, 1.053, .9245, .8519, .7836, .6981,
            .6511, .5637, .4846, .4397, .4015, .3344, .2890, .2532, .2274, .1894,
            .1631, .1438, .1287, .1170, .1073]
#  C3H5+

XION6G10 = [13.48, 15.0, 17.5, 20.0, 25.0, 30.0, 35.0, 40.0, 45.0, 50.0,
            60.0, 70.0, 80.0, 90.0, 100., 125., 150., 175., 200., 250.,
            300., 350., 400., 450., 500., 600., 700., 800., 900., 1000.,
            1250., 1500., 1750., 2000., 2500., 3000., 3500., 4000., 5000., 6000.,
            7000., 8000., 9000., 10000.
            ]
YION6G10 = [0.00, .044, .107, .163, .259, .321, .351, .359, .351, .358,
            .366, .369, .373, .374, .374, .362, .342, .323, .305, .285,
            .250, .228, .211, .192, .180, .158, .146, .134, .119, .111,
            .0964, .0829, .0752, .0687, .0572, .0494, .0433, .0389, .0324, .0279,
            .0246, .0220, .0200, .0184]
#  CH3+

XION7G10 = [13.65, 15.0, 17.5, 20.0, 25.0, 30.0, 35.0, 40.0, 45.0, 50.0,
            60.0, 70.0, 80.0, 90.0, 100., 125., 150., 175., 200., 250.,
            300., 350., 400., 450., 500., 600., 700., 800., 900., 1000.,
            1250., 1500., 1750., 2000., 2500., 3000., 3500., 4000., 5000., 6000.,
            7000., 8000., 9000., 10000.
            ]
YION7G10 = [0.00, .019, .049, .078, .123, .153, .167, .171, .167, .170,
            .174, .175, .177, .177, .177, .171, .162, .153, .145, .135,
            .118, .108, .100, .0911, .0854, .0750, .0691, .0636, .0566, .0528,
            .0457, .0393, .0357, .0326, .0271, .0234, .0205, .0184, .0154, .0132,
            .0117, .0104, .00949, .00870]

#  C3H4+

XION8G10 = [13.79, 15.0, 17.5, 20.0, 25.0, 30.0, 35.0, 40.0, 45.0, 50.0,
            60.0, 70.0, 80.0, 90.0, 100., 125., 150., 175., 200., 250.,
            300., 350., 400., 450., 500., 600., 700., 800., 900., 1000.,
            1250., 1500., 1750., 2000., 2500., 3000., 3500., 4000., 5000., 6000.,
            7000., 8000., 9000., 10000.
            ]
YION8G10 = [0.00, .0061, .0171, .0270, .0406, .0525, .0670, .0672, .0674,
            .0686,
            .0702, .0708, .0715, .0718, .0717, .0694, .0656, .0620, .0585, .0547,
            .0479, .0438, .0405, .0369, .0346, .0304, .0280, .0257, .0229, .0214,
            .0185, .0159, .0144, .0132, .0110, .00949, .00831, .00747, .00622, .00536,
            .00472, .00423, .00384, .00352]
#  C2H2+

XION9G10 = [14.1, 15.0, 17.5, 20.0, 25.0, 30.0, 35.0, 40.0, 45.0, 50.0,
            60.0, 70.0, 80.0, 90.0, 100., 125., 150., 175., 200., 250.,
            300., 350., 400., 450., 500., 600., 700., 800., 900., 1000.,
            1250., 1500., 1750., 2000., 2500., 3000., 3500., 4000., 5000., 6000.,
            7000., 8000., 9000., 10000.
            ]
YION9G10 = [0.00, .013, .047, .078, .117, .151, .193, .223, .223, .226,
            .234, .229, .231, .232, .232, .224, .212, .200, .189, .177,
            .155, .142, .131, .119, .112, .0981, .0904, .0832, .0741, .0691,
            .0598, .0514, .0467, .0426, .0355, .0307, .0269, .0241, .0201, .173,
            .0153, .0137, .0124, .0114]
#  C2H3+

XION10G10 = [14.5, 15.0, 17.5, 20.0, 25.0, 30.0, 35.0, 40.0, 45.0, 50.0,
             60.0, 70.0, 80.0, 90.0, 100., 125., 150., 175., 200., 250.,
             300., 350., 400., 450., 500., 600., 700., 800., 900., 1000.,
             1250., 1500., 1750., 2000., 2500., 3000., 3500., 4000., 5000., 6000.,
             7000., 8000., 9000., 10000.
             ]
YION10G10 = [0.00, .038, .219, .387, .582, .742, .964, .987, .965, .983,
             1.006, 1.013, 1.024, 1.028, 1.027, .9934, .9392, .8870, .8379, .7826,
             .6863, .6272, .5800, .5278, .4947, .4345, .4004, .3683, .3281, .3060,
             .2649, .2278, .2067, .1887, .1572, .1358, .1190, .1069, .0890, .0767,
             .0676, .0605, .0550, .0504]
#  C3H3+

XION11G10 = [16.5, 17.5, 20.0, 25.0, 30.0, 35.0, 40.0, 45.0, 50.0, 60.0,
             70.0, 80.0, 90.0, 100., 125., 150., 175., 200., 250., 300.,
             350., 400., 450., 500., 600., 700., 800., 900., 1000., 1250.,
             1500., 1750., 2000., 2500., 3000., 3500., 4000., 5000., 6000., 7000.,
             8000., 9000., 10000.
             ]
YION11G10 = [0.00, .125, .197, .312, .387, .423, .434, .424, .432, .442,
             .446, .450, .452, .451, .437, .413, .390, .368, .344, .302,
             .276, .255, .232, .218, .191, .176, .162, .144, .135, .116,
             .1001, .0909, .0830, .0691, .0597, .0523, .0470, .0391, .0337, .0297,
             .0266, .0242, .0222]
#  H+

XION12G10 = [20.0, 25.0, 30.0, 35.0, 40.0, 45.0, 50.0, 60.0, 70.0, 80.0,
             90.0, 100., 125., 150., 175., 200., 250., 300., 350., 400.,
             450., 500., 600., 700., 800., 900., 1000., 1250., 1500., 1750.,
             2000., 2500., 3000., 3500., 4000., 5000., 6000., 7000., 8000., 9000.,
             10000.
             ]
YION12G10 = [0.00, .00175, .00656, .00845, .00879, .00016, .00016, .00016,
             .0093, .0172,
             .0173, .0173, .0167, .0158, .0149, .0141, .0131, .0115, .0105, .00973,
             .00886, .00830, .00729, .00672, .00618, .00551, .00514, .00445, .00382,
             .00347,
             .00317, .00264, .00228, .00200, .00179, .00149, .00129, .00113, .00102,
             .000923, .000846]
#  H2+ ANe H3+

XION13G10 = [21.5, 25.0, 30.0, 35.0, 40.0, 45.0, 50.0, 60.0, 70.0, 80.0,
             90.0, 100., 125., 150., 175., 200., 250., 300., 350., 400.,
             450., 500., 600., 700., 800., 900., 1000., 1250., 1500., 1750.,
             2000., 2500., 3000., 3500., 4000., 5000., 6000., 7000., 8000., 9000.,
             10000.
             ]
YION13G10 = [0.00, .00070, .00246, .00455, .00527, .00685, .00710, .00784,
             .00916, .00925,
             .00929, .00928, .00898, .00849, .00802, .00758, .00708, .00621, .00567,
             .00524,
             .00477, .00447, .00393, .00362, .00333, .00297, .00277, .00240, .00206,
             .00187,
             .00171, .00142, .00123, .00108, .000966, .000805, .000693, .000611,
             .000547, .000497,
             .000456]
#  CH2+

XION14G10 = [25.0, 30.0, 35.0, 40.0, 45.0, 50.0, 60.0, 70.0, 80.0, 90.0,
             100., 125., 150., 175., 200., 250., 300., 350., 400., 450.,
             500., 600., 700., 800., 900., 1000., 1250., 1500., 1750., 2000.,
             2500., 3000., 3500., 4000., 5000., 6000., 7000., 8000., 9000., 10000.
             ]
YION14G10 = [0.00, .0146, .0262, .0409, .0385, .0475, .0527, .0573, .0578,
             .0581,
             .0580, .0561, .0531, .0501, .0473, .0442, .0388, .0354, .0328, .0298,
             .0279, .0245, .0226, .0208, .0185, .0173, .0150, .0129, .0117, .0107,
             .00888, .00767, .00672, .00604, .00503, .00433, .00382, .00342, .00311,
             .00285]
#  C3H2+

XION15G10 = [26.5, 35.0, 40.0, 45.0, 50.0, 60.0, 70.0, 80.0, 90.0, 100.,
             125., 150., 175., 200., 250., 300., 350., 400., 450., 500.,
             600., 700., 800., 900., 1000., 1250., 1500., 1750., 2000., 2500.,
             3000., 3500., 4000., 5000., 6000., 7000., 8000., 9000., 10000.
             ]
YION15G10 = [0.00, .032, .067, .088, .113, .116, .121, .128, .123, .123,
             .119, .112, .106, .100, .0934, .0819, .0749, .0692, .0630, .0591,
             .0519, .0478, .0440, .0392, .0365, .0316, .0272, .0247, .0225, .0188,
             .0162, .0142, .0128, .0106, .00915, .00807, .00722, .00657, .00602]
# C3H+

XION16G10 = [29.0, 35.0, 40.0, 45.0, 50.0, 60.0, 70.0, 80.0, 90.0, 100.,
             125., 150., 175., 200., 250., 300., 350., 400., 450., 500.,
             600., 700., 800., 900., 1000., 1250., 1500., 1750., 2000., 2500.,
             3000., 3500., 4000., 5000., 6000., 7000., 8000., 9000., 10000.
             ]
YION16G10 = [0.00, .0196, .0412, .0539, .0694, .0724, .0744, .0751, .0754,
             .0754,
             .0729, .0689, .0651, .0615, .0574, .0504, .0460, .0426, .0387, .0363,
             .0319, .0294, .0270, .0241, .0225, .0194, .0167, .0152, .0139, .0115,
             .00997, .00873, .00784, .00653, .00563, .00496, .00444, .00404, .00370]
#  C2H+

XION17G10 = [30.4, 35.0, 40.0, 45.0, 50.0, 60.0, 70.0, 80.0, 90.0, 100.,
             125., 150., 175., 200., 250., 300., 350., 400., 450., 500.,
             600., 700., 800., 900., 1000., 1250., 1500., 1750., 2000., 2500.,
             3000., 3500., 4000., 5000., 6000., 7000., 8000., 9000., 10000.
             ]
YION17G10 = [0.00, .0048, .0121, .0131, .0169, .0176, .0181, .0183, .0183,
             .0183,
             .0177, .0168, .0158, .0150, .0140, .0123, .0112, .0104, .00942, .00883,
             .00776, .00715, .00658, .00586, .00546, .00473, .00407, .00369, .00337,
             .00281,
             .00242, .00212, .00191, .00159, .00137, .00121, .00108, .000982, .000900]
# ALL STABLE  ++ STATES

XION18G10 = [32.0, 40.0, 45.0, 50.0, 60.0, 70.0, 80.0, 90.0, 100., 125.,
             150., 175., 200., 250., 300., 350., 400., 450., 500., 600.,
             700., 800., 900., 1000., 1250., 1500., 1750., 2000., 2500., 3000.,
             3500., 4000., 5000., 6000., 7000., 8000., 9000., 10000.
             ]
YION18G10 = [0.00, .0062, .0178, .0262, .0321, .0369, .0372, .0374, .0374,
             .0362,
             .0342, .0323, .0305, .0285, .0250, .0228, .0211, .0192, .0180, .0158,
             .0146, .0134, .0119, .0111, .00964, .00829, .00752, .00687, .00572, .00494,
             .00433, .00389, .00324, .00279, .00246, .00220, .00200, .00183]
#  ALL eISSOCIATING ++ STATES

XION19G10 = [32.0, 35.0, 40.0, 45.0, 50.0, 60.0, 70.0, 80.0, 90.0, 100.,
             125., 150., 175., 200., 250., 300., 350., 400., 450., 500.,
             600., 700., 800., 900., 1000., 1250., 1500., 1750., 2000., 2500.,
             3000., 3500., 4000., 5000., 6000., 7000., 8000., 9000., 10000.
             ]
YION19G10 = [0.00, .0460, .1797, .5189, .7608, .9316, 1.0718, 1.0824,
             1.0867, 1.0856,
             1.0506, .9933, .9381, .8861, .8277, .7258, .6633, .6134, .5582, .5232,
             .4595, .4235, .3895, .3470, .3236, .2802, .2409, .2186, .1996, .1662,
             .1436, .1258, .1130, .0941, .0811, .0715, .0640, .0582, .0533]
#  CH+

XION20G10 = [36.0, 40.0, 45.0, 50.0, 60.0, 70.0, 80.0, 90.0, 100., 125.,
             150., 175., 200., 250., 300., 350., 400., 450., 500., 600.,
             700., 800., 900., 1000., 1250., 1500., 1750., 2000., 2500., 3000.,
             3500., 4000., 5000., 6000., 7000., 8000., 9000., 10000.
             ]
YION20G10 = [0.00, .0040, .0077, .0106, .0145, .0187, .0189, .0189, .0189,
             .0183,
             .0173, .0164, .0155, .0144, .0127, .0116, .0107, .00973, .00912, .00801,
             .00738, .00679, .00605, .00564, .00489, .00420, .00381, .00348, .00290,
             .00250,
             .00219, .00197, .00164, .00141, .00125, .00112, .00101, .000930]
#  C+

XION21G10 = [39.0, 50.0, 60.0, 70.0, 80.0, 90.0, 100., 125., 150., 175.,
             200., 250., 300., 350., 400., 450., 500., 600., 700., 800.,
             900., 1000., 1250., 1500., 1750., 2000., 2500., 3000., 3500., 4000.,
             5000., 6000., 7000., 8000., 9000., 10000.
             ]
YION21G10 = [0.00, .00080, .00388, .00756, .00763, .00766, .00765, .00741,
             .00700, .00661,
             .00625, .00584, .00512, .00468, .00432, .00394, .00369, .00324, .00299,
             .00275,
             .00245, .00228, .00198, .00170, .00154, .00141, .00117, .00101, .000887,
             .000797,
             .000664, .000572, .000504, .000451, .000410, .000376]
#  C2+

XION22G10 = [39.0, 50.0, 60.0, 70.0, 80.0, 90.0, 100., 125., 150., 175.,
             200., 250., 300., 350., 400., 450., 500., 600., 700., 800.,
             900., 1000., 1250., 1500., 1750., 2000., 2500., 3000., 3500., 4000.,
             5000., 6000., 7000., 8000., 9000., 10000.
             ]
YION22G10 = [0.00, .000054, .000264, .000515, .000520, .000522, .000521,
             .000504, .000477, .000450,
             .000425, .000397, .000348, .000318, .000295, .000268, .000251, .000221,
             .000203, .000187,
             .000167, .000155, .000135, .000116, .000105, .000096, .000080, .000069,
             .000060, .000054,
             .000045, .000039, .000034, .000031, .000028, .0000256]
#  C3+

XION23G10 = [39.0, 50.0, 60.0, 70.0, 80.0, 90.0, 100., 125., 150., 175.,
             200., 250., 300., 350., 400., 450., 500., 600., 700., 800.,
             900., 1000., 1250., 1500., 1750., 2000., 2500., 3000., 3500., 4000.,
             5000., 6000., 7000., 8000., 9000., 10000.
             ]
YION23G10 = [0.00, .00099, .00481, .00934, .00943, .00947, .00946, .00915,
             .00865, .00817,
             .00772, .00721, .00632, .00578, .00534, .00486, .00456, .00400, .00369,
             .00339,
             .00302, .00282, .00244, .00210, .00190, .00174, .00145, .00125, .00110,
             .00098,
             .00082, .00071, .00062, .00056, .00051, .000464]
# K-SHELL IONISATION X-SECTION CARBON (SCALEe BY 3 IN SUBROUTINE)

XION24G10 = [285., 298., 307., 316., 325., 335., 345., 365., 398., 422.,
             447., 473., 501., 531., 613., 668., 708., 750., 817., 917.,
             1000., 1122., 1296., 1496., 1679., 1884., 2054., 2238., 2512., 2985.,
             3981., 5012., 7079., 1.0e4, 1.50e4, 2.05e4, 2.51e4, 3.07e4, 4.10e4, 5.01e4,
             6.13e4, 7.08e4, 8.18e4, 1.0e5, 1.54e5, 2.05e5, 2.99e5, 4.10e5, 5.01e5,
             6.13e5,
             7.08e5, 8.18e5, 1.0e6, 1.26e6, 1.5e6, 2.05e6, 3.07e6, 4.10e6, 5.01e6,
             6.13e6,
             7.08e6, 8.18e6, 1.0e7, 1.26e7, 1.5e7, 2.05e7, 3.07e7, 4.10e7, 5.01e7,
             6.13e7,
             7.08e7, 8.18e7, 1.0e8, 1.26e8, 1.5e8, 2.05e8, 3.07e8, 4.10e8, 5.01e8,
             6.13e8,
             7.08e8, 8.18e8, 1.0e9
             ]
YION24G10 = [0.00, 1.66e-4, 3.48e-4, 5.25e-4, 6.96e-4, 8.63e-4, 1.02e-3,
             1.33e-3, 1.75e-3, 2.01e-3,
             2.24e-3, 2.46e-3, 2.66e-3, 2.84e-3, 3.21e-3, 3.38e-3, 3.47e-3, 3.55e-3,
             3.65e-3, 3.72e-3,
             3.75e-3, 3.74e-3, 3.68e-3, 3.57e-3, 3.45e-3, 3.31e-3, 3.19e-3, 3.07e-3,
             2.91e-3, 2.66e-3,
             2.25e-3, 1.95e-3, 1.55e-3, 1.21e-3, 8.97e-4, 7.07e-4, 6.07e-4, 5.21e-4,
             4.21e-4, 3.63e-4,
             3.14e-4, 2.84e-4, 2.57e-4, 2.25e-4, 1.74e-4, 1.50e-4, 1.28e-4, 1.15e-4,
             1.09e-4, 1.05e-4,
             1.03e-4, 1.02e-4, 1.01e-4, 1.005e-4, 1.01e-4, 1.03e-4, 1.07e-4, 1.11e-4,
             1.14e-4, 1.17e-4,
             1.20e-4, 1.22e-4, 1.25e-4, 1.29e-4, 1.32e-4, 1.38e-4, 1.45e-4, 1.50e-4,
             1.54e-4, 1.58e-4,
             1.60e-4, 1.63e-4, 1.67e-4, 1.71e-4, 1.74e-4, 1.80e-4, 1.87e-4, 1.92e-4,
             1.96e-4, 2.00e-4,
             2.02e-4, 2.05e-4, 2.09e-4]
#
# CH3-  ATTACHMENT

XATT1G10 = [7.60, 8.00, 8.50, 9.00, 9.50, 10.0, 10.5, 11.0, 11.5
            ]
YATT1G10 = [0.00, 2.4e-6, 1.1e-5, 5.1e-5, 6.0e-5, 5.1e-5, 1.1e-5, 2.4e-6,
            0.0]
# H- ATTACHMENT

XATT2G10 = [7.80, 8.00, 8.50, 9.00, 9.50, 10.0, 10.5, 11.0, 11.5
            ]
YATT2G10 = [0.00, 1.6e-5, 7.2e-5, 2.8e-4, 4.0e-4, 2.8e-4, 7.2e-5, 1.6e-5,
            0.0]
#

XVIB1G10 = [.108, .125, 0.14, 0.15, .175, 0.20, .225, 0.25, 0.30, 0.40,
            0.50, 0.70, 1.00, 1.50, 2.00, 3.00, 4.00, 5.00, 6.00, 7.50,
            8.50, 10.0, 12.5, 15.0, 20.0
            ]
YVIB1G10 = [0.00, .137, .222, .265, .312, .359, .368, .368, .333, .282,
            .248, .205, .162, .162, .197, .291, .432, .567, .731, .957,
            1.02, .787, .585, .475, .325
            ]
XVIB2G10 = [.173, 0.18, 0.19, 0.20, .215, 0.23, 0.25, 0.30, 0.40, 0.50,
            0.70, 1.00, 1.50, 2.00, 3.00, 4.00, 5.00, 6.00, 7.50, 8.50,
            10.0, 12.5, 15.0, 20.0
            ]
YVIB2G10 = [0.00, .085, .180, .248, .299, .325, .351, .368, .351, .325,
            .274, .222, .205, .214, .332, .493, .647, .835, 1.09, 1.16,
            .898, .665, .531, .370
            ]
XVIB3G10 = [.363, 0.38, 0.40, .425, 0.45, .475, 0.50, 0.55, 0.60, 0.65,
            0.70, 0.80, 1.00, 1.50, 2.00, 3.00, 4.00, 5.00, 6.00, 7.00,
            8.50, 10.0, 12.5, 15.0, 20.0
            ]
YVIB3G10 = [0.00, .226, .314, .379, .420, .446, .465, .485, .493, .493,
            .489, .474, .437, .418, .456, .665, .950, 1.23, 1.65, 2.00,
            1.70, 1.32, 1.02, 0.80, 0.56
            ]
XVIB4G10 = [.519, 1.00, 1.25, 1.50, 2.00, 2.50, 3.00, 3.50, 4.00, 5.00,
            6.00, 7.50, 8.50, 10.0, 12.5, 15.0, 20.0
            ]
YVIB4G10 = [0.00, .000, .005, .0075, .0163, .030, .0513, .080, .118, .218,
            .363, .613, .625, .500, .350, .269, .175]
# EFFECTIVE TRIPLET LEVELS
# NON eIPOLE LEVEL AT 6.60 EV

XTR1G10 = [6.60, 7.15, 7.70, 8.00, 8.70, 9.70, 10.7, 11.7, 13.7, 15.7,
           18.7, 21.7, 25.7, 29.7
           ]
YTR1G10 = [0.00, .072, .216, .304, .384, .409, .424, .432, .424, .408,
           .352, .296, .216, .160]
# NON eIPOLE LEVEL AT 7.70 EV

XTR2G10 = [7.70, 9.20, 10.2, 11.2, 12.2, 14.2, 16.2, 19.2, 22.2,
           26.2, 29.7
           ]
YTR2G10 = [0.00, .164, .236, .265, .282, .295, .295, .275, .235,
           .175, .140]
# NON eIPOLE LEVEL AT 9.60 EV

XTR3G10 = [9.60, 10.6, 11.6, 12.6, 13.6, 16.6, 19.6, 22.6, 26.6,
           29.6, 34.6
           ]
YTR3G10 = [0.00, .298, .614, .716, .810, .853, .853, .810, .702,
           .610, .464]
# NON eIPOLE LEVEL AT 26.0 EV

XTR4G10 = [26.0, 27.0, 28.0, 29.0, 30.0, 33.0, 36.0, 39.0, 43.0,
           46.0, 51.0
           ]
YTR4G10 = [0.00, 1.61, 2.95, 3.44, 3.89, 4.08, 4.08, 3.89, 3.37,
           2.93, 2.23]
#
# BREMSSTRAHLUNG X-SECTION WITH CUT UNITS 10**-24

Z1TG10 = [11.3, 6.18, 2.80, 1.54, .858, .407, .251, .176, .145, .150,
          .167, .178, .187, .193, .198, .205, .210, .218, .222, .228,
          .231, .233, .234, .235, .235
          ]
Z6TG10 = [298., 178., 85.2, 47.5, 26.3, 12.2, 7.06, 4.45, 3.06, 2.82,
          2.89, 2.99, 3.08, 3.13, 3.18, 3.25, 3.31, 3.39, 3.44, 3.49,
          3.52, 3.54, 3.55, 3.57, 3.57
          ]
EBRMG10 = [1000., 2000., 5000., 1.E4, 2.E4, 5.E4, 1.E5, 2.E5, 5.E5, 1.E6,
           2.E6, 3.E6, 4.E6, 5.E6, 6.E6, 8.E6, 1.E7, 1.5E7, 2.E7, 3.E7,
           4.E7, 5.E7, 6.E7, 8.E7, 1.E8]
# LIGHT EMISSION FROM H ALPHA
#  MOHLMANN  CHEM PHYS 19(1977)233

XNUL1G10 = [18.0, 20.0, 40.0, 60.0, 80.0, 100., 150., 200., 300., 500.,
            1000., 1300., 1700., 2000.
            ]
YNUL1G10 = [0.0, .0019, .0073, .0140, .0162, .0178, .0181, .0144, .0093,
            .0053,
            .0025, .0019, .0014, .0012]
# LIGHT EMISSION FROM CH2(A2eELTA -X2PI)
#  MOHLMANN  CHEM PHYS 19(1977)233

XNUL2G10 = [16.0, 20.0, 40.0, 60.0, 80.0, 100., 150., 200., 300., 500.,
            1000., 1300., 1700., 2000.
            ]
YNUL2G10 = [0.0, .000, .0037, .0054, .0056, .0053, .0048, .0041, .0028,
            .0016,
            .0007, .0005, .0004, .0003]

EING10 = [-0.036, 0.036, -0.108, 0.108, -0.173, 0.173, 0.363, 0.519, 6.60, 7.65, 7.70, 7.95, 8.25, 8.55, 8.85, 9.15,
          9.45, 9.60, 9.75, 10.05, 10.35, 10.65, 10.9, 11.1, 11.3, 11.5, 11.7, 11.9, 12.1, 12.3, 12.5, 12.7, 12.9, 13.1,
          13.3, 13.5, 13.7, 13.9, 14.1, 14.3, 14.5, 14.7, 14.9, 15.2, 15.6, 16.0, 16.4, 16.8, 17.25, 17.75, 18.25,
          18.75, 19.25, 19.75, 20.25, 20.75, 21.5, 22.5, 23.5, 24.5, 25.5, 26.0, 26.5, 27.5, 0.0, 0.0]

for i in range(250 - 66):
    EING10.append(0.0)

gd['gas10/XEN'] = XENG10
gd['gas10/YMT'] = YMTG10
gd['gas10/YEL'] = YELG10
gd['gas10/YEPS'] = YEPSG10
gd['gas10/XION'] = XIONG10
gd['gas10/YIONG'] = YIONGG10
gd['gas10/YIONC'] = YIONCG10
gd['gas10/XION1'] = XION1G10
gd['gas10/YION1'] = YION1G10
gd['gas10/XION2'] = XION2G10
gd['gas10/YION2'] = YION2G10
gd['gas10/XION3'] = XION3G10
gd['gas10/YION3'] = YION3G10
gd['gas10/XION4'] = XION4G10
gd['gas10/YION4'] = YION4G10
gd['gas10/XION5'] = XION5G10
gd['gas10/YION5'] = YION5G10
gd['gas10/XION6'] = XION6G10
gd['gas10/YION6'] = YION6G10
gd['gas10/XION7'] = XION7G10
gd['gas10/YION7'] = YION7G10
gd['gas10/XION8'] = XION8G10
gd['gas10/YION8'] = YION8G10
gd['gas10/XION9'] = XION9G10
gd['gas10/YION9'] = YION9G10
gd['gas10/XION10'] = XION10G10
gd['gas10/YION10'] = YION10G10
gd['gas10/XION11'] = XION11G10
gd['gas10/YION11'] = YION11G10
gd['gas10/XION12'] = XION12G10
gd['gas10/YION12'] = YION12G10
gd['gas10/XION13'] = XION13G10
gd['gas10/YION13'] = YION13G10
gd['gas10/XION14'] = XION14G10
gd['gas10/YION14'] = YION14G10
gd['gas10/XION15'] = XION15G10
gd['gas10/YION15'] = YION15G10
gd['gas10/XION16'] = XION16G10
gd['gas10/YION16'] = YION16G10
gd['gas10/XION17'] = XION17G10
gd['gas10/YION17'] = YION17G10
gd['gas10/XION18'] = XION18G10
gd['gas10/YION18'] = YION18G10
gd['gas10/XION19'] = XION19G10
gd['gas10/YION19'] = YION19G10
gd['gas10/XION20'] = XION20G10
gd['gas10/YION20'] = YION20G10
gd['gas10/XION21'] = XION21G10
gd['gas10/YION21'] = YION21G10
gd['gas10/XION22'] = XION22G10
gd['gas10/YION22'] = YION22G10
gd['gas10/XION23'] = XION23G10
gd['gas10/YION23'] = YION23G10
gd['gas10/XION24'] = XION24G10
gd['gas10/YION24'] = YION24G10
gd['gas10/XATT1'] = XATT1G10
gd['gas10/YATT1'] = YATT1G10
gd['gas10/XATT2'] = XATT2G10
gd['gas10/YATT2'] = YATT2G10
gd['gas10/XVIB1'] = XVIB1G10
gd['gas10/YVIB1'] = YVIB1G10
gd['gas10/XVIB2'] = XVIB2G10
gd['gas10/YVIB2'] = YVIB2G10
gd['gas10/XVIB3'] = XVIB3G10
gd['gas10/YVIB3'] = YVIB3G10
gd['gas10/XVIB4'] = XVIB4G10
gd['gas10/YVIB4'] = YVIB4G10
gd['gas10/XTR1'] = XTR1G10
gd['gas10/YTR1'] = YTR1G10
gd['gas10/XTR2'] = XTR2G10
gd['gas10/YTR2'] = YTR2G10
gd['gas10/XTR3'] = XTR3G10
gd['gas10/YTR3'] = YTR3G10
gd['gas10/XTR4'] = XTR4G10
gd['gas10/YTR4'] = YTR4G10
gd['gas10/XNUL1'] = XNUL1G10
gd['gas10/YNUL1'] = YNUL1G10
gd['gas10/XNUL2'] = XNUL2G10
gd['gas10/YNUL2'] = YNUL2G10
gd['gas10/Z1T'] = Z1TG10
gd['gas10/Z6T'] = Z6TG10
gd['gas10/EBRM'] = EBRMG10
gd['gas10/EIN'] = EING10

# ELASTIC                                          

XENG11 = [0.00, 0.001, 0.002, 0.003, 0.004, 0.005, 0.007, 0.01, 0.014, 0.02,
          .025, 0.03, .035, 0.04, 0.05, 0.06, 0.07, 0.08, 0.09, 0.10,
          0.11, 0.12, 0.13, 0.14, 0.16, 0.18, 0.20, 0.23, 0.26, 0.30,
          0.35, 0.40, 0.50, 0.60, 0.80, 1.00, 1.40, 2.00, 3.00, 4.00,
          5.00, 6.00, 7.00, 8.00, 9.00, 10.0, 12.5, 15.0, 20.0, 25.0,
          30.0, 40.0, 50.0, 60.0, 70.0, 80.0, 100., 120., 140., 170.,
          200., 250., 300., 400., 500., 750., 1000., 1250., 1500., 1750.,
          2000., 2500., 3000., 3500., 4000., 4500., 5000., 6000., 7000., 8000.,
          9000., 1.e4, 1.25e4, 1.5e4, 1.75e4, 2.e4, 2.5e4, 3.e4, 3.5e4, 4.e4,
          4.5e4, 5.e4, 6.e4, 7.e4, 8.e4, 9.e4, 1.e5, 1.25e5, 1.5e5, 1.75e5,
          2.0e5, 2.5e5, 3.e5, 3.5e5, 4.e5, 4.5e5, 5.e5, 6.e5, 7.e5, 8.e5,
          9.0e5, 1.0e6, 1.25e6, 1.5e6, 1.75e6, 2.0e6, 2.5e6, 3.0e6, 3.5e6, 4.0e6,
          4.5e6, 5.0e6, 6.0e6, 7.0e6, 8.0e6, 9.0e6, 1.0e7, 1.25e7, 1.5e7, 1.75e7,
          2.0e7, 2.5e7, 3.0e7, 3.5e7, 4.0e7, 4.5e7, 5.0e7, 6.0e7, 7.0e7, 8.0e7,
          9.0e7, 1.0e8, 1.25e8, 1.5e8, 1.75e8, 2.0e8, 2.5e8, 3.0e8, 3.5e8, 4.0e8,
          4.5e8, 5.0e8, 6.0e8, 7.0e8, 8.0e8, 9.0e8, 1.0e9]
# ELASTIC MOMENTUM TRANSFER X-SECTION

YELMG11 = [255., 255., 255., 255., 255., 210., 150., 105., 74.5, 52.0,
           41.4, 34.5, 29.6, 25.9, 20.7, 17.2, 14.8, 13.0, 11.7, 10.8,
           10.0, 9.30, 8.60, 8.00, 7.00, 5.50, 3.50, 3.60, 4.80, 7.50,
           9.60, 11.2, 12.9, 13.8, 14.7, 15.3, 16.1, 17.3, 19.8, 23.2,
           27.8, 32.3, 35.0, 35.0, 33.0, 30.0, 25.0, 21.5, 17.0, 13.7,
           11.5, 9.00, 7.30, 6.10, 5.20, 4.50, 3.50, 2.80, 2.21, 1.72,
           1.40, 1.10, 0.87, 0.61, 0.47, 0.28, .171, .116, .0848, .0648,
           .0505, .0345, .0249, .0189, .0149, .0120, .00996, .00717, .00542, .00426,
           .00344, .00284, .00190, .00136, .00103, .000807, .000539, .000387,
           .000293, .000231,
           1.87e-4, 1.55e-4, 1.12e-4, 8.50e-5, 6.72e-5, 5.46e-5, 4.55e-5, 3.10e-5,
           2.27e-5, 1.75e-5,
           1.40e-5, 9.71e-6, 7.24e-6, 5.66e-6, 4.59e-6, 3.81e-6, 3.24e-6, 2.44e-6,
           1.93e-6, 1.57e-6,
           1.31e-6, 1.12e-6, 8.01e-7, 6.04e-7, 4.75e-7, 3.84e-7, 2.69e-7, 2.00e-7,
           1.55e-7, 1.24e-7,
           1.02e-7, 8.52e-8, 6.23e-8, 4.77e-8, 3.78e-8, 3.07e-8, 2.55e-8, 1.71e-8,
           1.23e-8, 9.30e-9,
           7.28e-9, 4.83e-9, 3.45e-9, 2.59e-9, 2.02e-9, 1.61e-9, 1.32e-9, 9.36e-10,
           6.97e-10, 5.39e-10,
           4.29e-10, 3.50e-10, 2.26e-10, 1.58e-10, 1.16e-10, 8.92e-11, 5.72e-11,
           3.98e-11, 2.92e-11, 2.24e-11,
           1.77e-11, 1.44e-11, 9.97e-12, 7.33e-12, 5.61e-12, 4.43e-12, 3.59e-12]
# ELASTIC X-SECTION ASSUMEe ISOTROPIC BELOW     2.0 EV

YELTG11 = [255., 255., 255., 255., 255., 210., 150., 105., 74.5, 52.0,
           41.4, 34.5, 29.6, 25.9, 20.7, 17.2, 14.8, 13.0, 11.7, 10.8,
           10.0, 9.30, 8.60, 8.00, 7.00, 5.50, 3.50, 3.60, 4.80, 7.50,
           9.60, 11.2, 12.9, 13.8, 14.7, 15.3, 16.1, 17.3, 25.0, 32.0,
           39.0, 43.0, 46.0, 48.0, 48.0, 46.0, 43.5, 41.5, 37.0, 32.0,
           27.5, 22.5, 19.0, 16.5, 14.7, 13.3, 11.0, 9.60, 8.40, 7.20,
           6.40, 5.30, 4.60, 3.65, 3.05, 2.20, 1.72, 1.42, 1.21, 1.08,
           0.96, 0.80, .690, .600, .545, .490, .450, .385, .335, .305,
           .275, .250, .210, .180, .158, .142, .119, .100, .0873, .0774,
           .0698, .0636, .0545, .0479, .0443, .0392, .0361, .0306, .0270, .0244,
           .0225, .0198, .0180, .0168, .0158, .0151, .0146, .0138, .0132, .0128,
           .0125, .0123, .0119, .0116, .0114, .0113, .0112, .0111, .0110, .0110,
           .0110, .0110, .0109, .0109, .0109, .0109, .0109]
for i in range(30):
    YELTG11.append(0.01086)
# EPSILON FOR ELASTIC ANGULAR eISTRIBUTION
# EPSILON=1.0-YEPS

YEPSG11 = []
for j in range(38):
    YEPSG11.append(1.0)
YEPSG11.extend([.6940, .6011,
                .5847, .6369, .6507, .6068, .5511, .5054, .4106, .3465, .2851, .2545,
                .2451, .2283, .2141, .2015, .1880, .1753, .1593, .1393, .1191, .1030,
                .0903, .0836, .0730, .0610, .0544, .0415, .0296, .0227, .0185, .0151,
                .01272, .00985, .00786, .00662, .00555, .00484, .00427, .00346, .00291,
                .00244,
                .00213, .00190, .001449, .001171, 9.84e-4, 8.38e-4, 6.43e-4, 5.35e-4,
                4.54e-4, 3.97e-4,
                3.50e-4, 3.14e-4, 2.58e-4, 2.19e-4, 1.83e-4, 1.658e-4, 1.481e-4,
                1.157e-4, 9.37e-5, 7.84e-5,
                6.69e-5, 5.12e-5, 4.11e-5, 3.37e-5, 2.86e-5, 2.45e-5, 2.12e-5, 1.65e-5,
                1.34e-5, 1.11e-5,
                9.33e-6, 7.99e-6, 5.75e-6, 4.32e-6, 3.37e-6, 2.71e-6, 1.87e-6, 1.37e-6,
                1.04e-6, 8.24e-7,
                6.67e-7, 5.52e-7, 3.95e-7, 2.97e-7, 2.32e-7, 1.86e-7, 1.52e-7, 9.94e-8,
                7.00e-8, 5.20e-8,
                4.01e-8, 2.59e-8, 1.81e-8, 1.34e-8, 1.03e-8, 8.12e-9, 6.58e-9, 4.56e-9,
                3.34e-9, 2.55e-9,
                2.00e-9, 1.62e-9, 1.02e-9, 7.00e-10, 5.07e-10, 3.84e-10, 2.41e-10,
                1.65e-10, 1.19e-10, 9.00e-11,
                7.1e-11, 5.7e-11, 3.9e-11, 2.8e-11, 2.1e-11, 1.6e-11, 1.3e-11])
# IONISATION

XIONG11 = [10.67, 11.0, 12.0, 13.0, 14.0, 15.0, 16.0, 17.0, 18.0, 19.0,
           20.0, 25.0, 30.0, 35.0, 40.0, 45.0, 50.0, 60.0, 70.0, 75.0,
           85.0, 100., 125., 150., 175., 200., 250., 300., 350., 400.,
           450., 500., 550., 600., 650., 700., 750., 800., 850., 900.,
           950., 1000.]
# GROSS IONISATION

YIONG11 = [0.00, .004, .070, 0.18, 0.37, 0.59, 0.84, 1.10, 1.60, 2.20,
           3.00, 5.11, 6.71, 8.00, 8.82, 9.51, 10.0, 10.5, 10.7, 10.8,
           10.7, 10.5, 10.0, 9.41, 8.87, 8.33, 7.29, 6.51, 5.90, 5.40,
           4.99, 4.65, 4.36, 4.11, 3.88, 3.69, 3.52, 3.36, 3.22, 3.09,
           2.98, 2.872]
# K-SHELL IONISATION X-SECTION CARBON (MUTILPY BY 4 FOR MOLECULE)  

XKSHG11 = [285., 298., 307., 316., 325., 335., 345., 365., 398., 422.,
           447., 473., 501., 531., 613., 668., 708., 750., 817., 917.,
           1000., 1122., 1296., 1496., 1679., 1884., 2054., 2238., 2512., 2985.,
           3981., 5012., 7079., 1.0e4, 1.50e4, 2.05e4, 2.51e4, 3.07e4, 4.10e4, 5.01e4,
           6.13e4, 7.08e4, 8.18e4, 1.0e5, 1.54e5, 2.05e5, 2.99e5, 4.10e5, 5.01e5,
           6.13e5,
           7.08e5, 8.18e5, 1.0e6, 1.26e6, 1.5e6, 2.05e6, 3.07e6, 4.10e6, 5.01e6,
           6.13e6,
           7.08e6, 8.18e6, 1.0e7, 1.26e7, 1.5e7, 2.05e7, 3.07e7, 4.10e7, 5.01e7,
           6.13e7,
           7.08e7, 8.18e7, 1.0e8, 1.26e8, 1.5e8, 2.05e8, 3.07e8, 4.10e8, 5.01e8,
           6.13e8,
           7.08e8, 8.18e8, 1.0e9
           ]
YKSHG11 = [0.00, 1.66e-4, 3.48e-4, 5.25e-4, 6.96e-4, 8.63e-4, 1.02e-3,
           1.33e-3, 1.75e-3, 2.01e-3,
           2.24e-3, 2.46e-3, 2.66e-3, 2.84e-3, 3.21e-3, 3.38e-3, 3.47e-3, 3.55e-3,
           3.65e-3, 3.72e-3,
           3.75e-3, 3.74e-3, 3.68e-3, 3.57e-3, 3.45e-3, 3.31e-3, 3.19e-3, 3.07e-3,
           2.91e-3, 2.66e-3,
           2.25e-3, 1.95e-3, 1.55e-3, 1.21e-3, 8.97e-4, 7.07e-4, 6.07e-4, 5.21e-4,
           4.21e-4, 3.63e-4,
           3.14e-4, 2.84e-4, 2.57e-4, 2.25e-4, 1.74e-4, 1.50e-4, 1.28e-4, 1.15e-4,
           1.09e-4, 1.05e-4,
           1.03e-4, 1.02e-4, 1.01e-4, 1.005e-4, 1.01e-4, 1.03e-4, 1.07e-4, 1.11e-4,
           1.14e-4, 1.17e-4,
           1.20e-4, 1.22e-4, 1.25e-4, 1.29e-4, 1.32e-4, 1.38e-4, 1.45e-4, 1.50e-4,
           1.54e-4, 1.58e-4,
           1.60e-4, 1.63e-4, 1.67e-4, 1.71e-4, 1.74e-4, 1.80e-4, 1.87e-4, 1.92e-4,
           1.96e-4, 2.00e-4,
           2.02e-4, 2.05e-4, 2.09e-4]
# COUNTING IONISATION

YINCG11 = [0.0]
for i in range(41):
    YINCG11.append(0.0)
# ATTACHMENT

XATTG11 = [0.0]
YATTG11 = [0.0]

for i in range(9):
    XATTG11.append(0.0)
    YATTG11.append(0.0)
# VIBRATION/TORSION
# ABOVE 40EV SCALE BY 1/E                                   

XVIB1G11 = [.052, .055, .060, .065, .070, .075, 0.08, 0.10, 0.12, 0.14,
            0.20, 0.25, 0.30, 0.40, 0.50, 0.70, 1.00, 1.50, 2.00, 3.00,
            4.00, 5.00, 6.00, 7.00, 8.00, 10.0, 15.0, 20.0, 30.0, 40.0
            ]
YVIB1G11 = [0.00, .014, .021, .024, .026, .027, .028, .028, .027, .025,
            .021, .018, .016, .014, .012, .009, .008, .012, .015, .024,
            .036, .047, .060, .079, .079, .065, .038, .025, .012, .008]
# VIBRATION                          
# ABOVE 40EV SCALE BY 1/E             

XVIB2G11 = [.108, .125, 0.15, 0.20, 0.23, 0.25, 0.30, 0.40, 0.50, 0.70,
            1.00, 1.50, 2.00, 3.00, 4.00, 5.00, 6.00, 7.00, 8.00, 10.0,
            15.0, 20.0, 30.0, 40.0]

YVIB2G11 = [0.00, 0.27, 0.52, 0.71, 0.73, 0.73, 0.66, 0.56, 0.49, 0.41,
            0.32, 0.32, 0.39, 0.63, 0.93, 1.22, 1.57, 2.06, 2.06, 1.69,
            1.00, 0.66, 0.35, 0.22]
# VIBRATION              
# ABOVE 40EV SCALE BY 1/E         

XVIB3G11 = [.173, 0.18, 0.19, 0.20, 0.23, 0.25, 0.30, 0.40, 0.50, 0.70,
            1.00, 1.50, 2.00, 3.00, 4.00, 5.00, 6.00, 7.00, 8.00, 10.0,
            15.0, 20.0, 30.0, 40.0
            ]
YVIB3G11 = [0.00, 0.13, 0.27, 0.38, 0.49, 0.53, 0.56, 0.53, 0.49, 0.42,
            0.34, 0.31, 0.33, 0.48, 0.72, 0.94, 1.21, 1.59, 1.59, 1.35,
            0.80, 0.52, 0.28, .175]
# VIBRATION     
# ABOVE 40EV SCALE BY 1/E                  

XVIB4G11 = [.363, .365, 0.37, 0.38, 0.39, 0.40, 0.42, 0.45, 0.50, 0.55,
            0.60, 0.70, 0.80, 0.90, 1.00, 1.20, 1.50, 2.00, 3.00, 4.00,
            5.00, 6.00, 7.00, 8.00, 10.0, 15.0, 20.0, 30.0, 40.0
            ]
YVIB4G11 = [0.00, .108, .198, .299, .366, .416, .487, .555, .615, .645,
            .655, .650, .630, .605, .580, 0.55, 0.57, 0.67, 1.05, 1.50,
            2.00, 2.45, 2.70, 2.70, 2.10, 1.15, 0.76, 0.42, 0.27]
# VIBRATION HARMONICS         
# ABOVE 40EV SCALE BY 1/E                             

XVIB5G11 = [.519, 1.00, 1.50, 2.00, 3.00, 4.00, 5.00, 6.00, 7.00, 8.00,
            10.0, 15.0, 20.0, 30.0, 40.0
            ]
YVIB5G11 = [0.00, .001, 0.01, .033, .085, 0.16, 0.20, 0.27, 0.30, 0.30,
            0.23, .125, .085, .047, .032]
# EXCITATION TRIPLET               

XEXC1G11 = [7.20, 8.00, 9.00, 10.0, 12.0, 14.0, 16.0, 20.0, 25.0, 30.0,
            40.0, 50.0, 60.0, 70.0, 80.0, 100.]

YEXC1G11 = [0.00, 0.10, 0.30, 0.45, 0.52, 0.55, 0.51, 0.45, 0.30, 0.20,
            0.10, 0.06, .037, .026, .019, .011]
# EXCITATION  TRIPLET                                     

XEXC2G11 = [8.60, 9.40, 10.4, 11.4, 13.4, 15.4, 17.4, 21.4, 26.0, 30.0,
            40.0, 50.0, 60.0, 70.0, 80.0, 100.
            ]
YEXC2G11 = [0.00, 0.10, 0.30, 0.45, 0.52, 0.55, 0.51, 0.45, 0.30, 0.20,
            0.10, 0.06, .037, .026, .019, .011]
# BREMSSTRAHLUNG X-SECTION WITH CUT OFF  UNITS 10**-24 CM**2

Z6TG11 = [298., 178., 85.2, 47.5, 26.3, 12.2, 7.06, 4.45, 3.06, 2.82,
          2.89, 2.99, 3.08, 3.13, 3.18, 3.25, 3.31, 3.39, 3.44, 3.49,
          3.52, 3.54, 3.55, 3.57, 3.57
          ]
Z1TG11 = [11.3, 6.18, 2.80, 1.54, .858, .407, .251, .176, .145, .150,
          .167, .178, .187, .193, .198, .205, .210, .218, .222, .228,
          .231, .233, .234, .235, .235
          ]
EBRMG11 = [1000., 2000., 5000., 1.E4, 2.E4, 5.E4, 1.E5, 2.E5, 5.E5, 1.E6,
           2.E6, 3.E6, 4.E6, 5.E6, 6.E6, 8.E6, 1.E7, 1.5E7, 2.E7, 3.E7,
           4.E7, 5.E7, 6.E7, 8.E7, 1.E8]
EING11 = [-0.032, 0.032, -0.108, 0.108, -0.173, 0.173, -0.363, 0.363, 0.519, 7.2, 8.6, 7.50, 8.0, 8.5, 9.0, 9.5, 10.0,
          10.5, 11.0, 11.5, 12.0, 12.5, 13.0, 13.5, 0.0, 0.0]
for i in range(250 - 26):
    EING11.append(0.0)
gd['gas11/XEN'] = XENG11
gd['gas11/YELM'] = YELMG11
gd['gas11/YELT'] = YELTG11
gd['gas11/YEPS'] = YEPSG11
gd['gas11/XION'] = XIONG11
gd['gas11/YION'] = YIONG11
gd['gas11/YINC'] = YINCG11
gd['gas11/XATT'] = XATTG11
gd['gas11/YATT'] = YATTG11
gd['gas11/XKSH'] = XKSHG11
gd['gas11/YKSH'] = YKSHG11
gd['gas11/XVIB1'] = XVIB1G11
gd['gas11/YVIB1'] = YVIB1G11
gd['gas11/XVIB2'] = XVIB2G11
gd['gas11/YVIB2'] = YVIB2G11
gd['gas11/XVIB3'] = XVIB3G11
gd['gas11/YVIB3'] = YVIB3G11
gd['gas11/XVIB4'] = XVIB4G11
gd['gas11/YVIB4'] = YVIB4G11
gd['gas11/XVIB5'] = XVIB5G11
gd['gas11/YVIB5'] = YVIB5G11
gd['gas11/XEXC1'] = XEXC1G11
gd['gas11/YEXC1'] = YEXC1G11
gd['gas11/XEXC2'] = XEXC2G11
gd['gas11/YEXC2'] = YEXC2G11
gd['gas11/Z6T'] = Z6TG11
gd['gas11/Z1T'] = Z1TG11
gd['gas11/EBRM'] = EBRMG11
gd['gas11/EIN'] = EING11
# ELASTIC +ROTATIONAL

XENG12 = [1.e-6, np.float32(.001), np.float32(.002), np.float32(.004), np.float32(.007), np.float32(.010),
          np.float32(.014), np.float32(.020), np.float32(.030), np.float32(.040),
          np.float32(0.05), np.float32(0.06), np.float32(0.08), np.float32(0.10), np.float32(.125), np.float32(.150),
          np.float32(.175), np.float32(0.20), np.float32(0.25), np.float32(0.30),
          np.float32(0.35), np.float32(0.40), np.float32(0.50), np.float32(0.60), np.float32(0.70), np.float32(0.85),
          np.float32(1.00), np.float32(1.25), np.float32(1.50), np.float32(1.70),
          np.float32(1.90), np.float32(2.10), np.float32(2.30), np.float32(2.50), np.float32(2.80), np.float32(3.00),
          np.float32(3.30), np.float32(3.60), np.float32(3.80), np.float32(4.00),
          np.float32(4.50), np.float32(5.00), np.float32(5.50), np.float32(6.00), np.float32(7.00), np.float32(8.00),
          np.float32(10.0), np.float32(12.0), np.float32(15.0), np.float32(17.0),
          np.float32(20.0), np.float32(25.0), np.float32(30.0), np.float32(40.0), np.float32(50.0), np.float32(60.0),
          np.float32(70.0), np.float32(80.0), np.float32(90.0), np.float32(100.),
          np.float32(120.), np.float32(150.), np.float32(170.), np.float32(200.), np.float32(250.), np.float32(300.),
          np.float32(350.), np.float32(400.), np.float32(450.), np.float32(500.),
          np.float32(600.), np.float32(700.), np.float32(800.), np.float32(900.), np.float32(1000.), np.float32(1500.),
          np.float32(2000.), np.float32(3000.), np.float32(4000.), np.float32(5000.),
          np.float32(6000.), np.float32(8000.), 1.0e4, 1.25e4, 1.5e4, 1.75e4, 2.0e4, 2.5e4, 3.0e4, 3.5e4,
          4.0e4, 4.5e4, 5.0e4, 6.0e4, 7.0e4, 8.0e4, 9.0e4, 1.0e5, 1.25e5, 1.5e5,
          1.75e5, 2.0e5, 2.5e5, 3.0e5, 3.5e5, 4.0e5, 4.5e5, 5.0e5, 6.0e5, 7.0e5,
          8.0e5, 9.0e5, 1.0e6, 1.25e6, 1.5e6, 1.75e6, 2.0e6, 2.5e6, 3.0e6, 3.5e6,
          4.0e6, 4.5e6, 5.0e6, 6.0e6, 7.0e6, 8.0e6, 9.0e6, 1.0e7, 1.25e7, 1.5e7,
          1.75e7, 2.0e7, 2.5e7, 3.0e7, 3.5e7, 4.0e7, 4.5e7, 5.0e7, 6.0e7, 7.0e7,
          8.0e7, 9.0e7, 1.0e8, 1.25e8, 1.5e8, 1.75e8, 2.0e8, 2.5e8, 3.0e8, 3.5e8,
          4.0e8, 4.5e8, 5.0e8, 6.0e8, 7.0e8, 8.0e8, 9.0e8, 1.0e9,
          ]
# GROUND STATE AND BEND MODE ELASTIC + ROTATION.  MOMENTUM TRANSFER

#  AT 293.15 KELVIN

YMOMG12 = [np.float32(148.), np.float32(148.), np.float32(146.), np.float32(141.), np.float32(134.), np.float32(128.),
           np.float32(119.), np.float32(109.), np.float32(95.0), np.float32(85.0),
           np.float32(76.5), np.float32(69.5), np.float32(59.0), np.float32(52.5), np.float32(47.5), np.float32(41.0),
           np.float32(36.0), np.float32(30.0), np.float32(22.0), np.float32(16.2),
           np.float32(12.8), np.float32(10.6), np.float32(8.20), np.float32(6.45), np.float32(5.35), np.float32(4.30),
           np.float32(3.90), np.float32(3.65), np.float32(3.60), np.float32(3.65),
           np.float32(3.75), np.float32(3.85), np.float32(4.00), np.float32(4.20), np.float32(4.60), np.float32(4.90),
           np.float32(5.30), np.float32(5.80), np.float32(6.00), np.float32(6.00),
           np.float32(5.50), np.float32(5.10), np.float32(5.00), np.float32(5.20), np.float32(6.10), np.float32(7.30),
           np.float32(8.80), np.float32(9.80), np.float32(10.5), np.float32(10.5),
           np.float32(9.80), np.float32(8.50), np.float32(7.00), np.float32(5.10), np.float32(4.00), np.float32(3.50),
           np.float32(3.10), np.float32(2.90), np.float32(2.70), np.float32(2.50),
           np.float32(2.20), np.float32(1.88), np.float32(1.67), np.float32(1.50), np.float32(1.25), np.float32(1.04),
           np.float32(.832), np.float32(.682), np.float32(.571), np.float32(.486),
           np.float32(.367), np.float32(.287), np.float32(.232), np.float32(.192), np.float32(.161), np.float32(.0819),
           np.float32(.0501), np.float32(.0247), np.float32(.0149), np.float32(.0100),
           np.float32(.00721), np.float32(.00430), np.float32(.00288), np.float32(.00192), np.float32(.00138),
           np.float32(.00105), 8.23e-4, 5.5e-4, 3.96e-4,
           3.0e-4,
           2.36e-4, 1.91e-4, 1.59e-4, 1.15e-4, 8.73e-5, 6.90e-5, 5.62e-5, 4.68e-5,
           3.19e-5, 2.34e-5,
           1.81e-5, 1.45e-5, 1.00e-5, 7.48e-6, 5.86e-6, 4.75e-6, 3.95e-6, 3.36e-6,
           2.54e-6, 2.00e-6,
           1.63e-6, 1.37e-6, 1.16e-6, 8.32e-7, 6.28e-7, 4.94e-7, 4.00e-7, 2.80e-7,
           2.08e-7, 1.62e-7,
           1.30e-7, 1.06e-7, 8.89e-8, 6.51e-8, 4.98e-8, 3.95e-8, 3.21e-8, 2.66e-8,
           1.79e-8, 1.29e-8,
           9.73e-9, 7.63e-9, 5.06e-9, 3.61e-9, 2.71e-9, 2.11e-9, 1.69e-9, 1.38e-9,
           9.79e-10, 7.28e-10,
           5.63e-10, 4.48e-10, 3.65e-10, 2.35e-10, 1.64e-10, 1.21e-10, 9.27e-11,
           5.95e-11, 4.13e-11, 3.04e-11,
           2.33e-11, 1.84e-11, 1.49e-11, 1.03e-11, 7.61e-12, 5.83e-12, 4.60e-12,
           3.73e-12,
           ]
# GROUND STATE AND BEND MODE ELASTIC + ROTATION.  AT 293.15 KELVIN

YELG12 = [np.float32(148.), np.float32(148.), np.float32(146.), np.float32(141.), np.float32(135.), np.float32(129.),
          np.float32(120.), np.float32(110.), np.float32(96.0), np.float32(86.0),
          np.float32(77.5), np.float32(70.5), np.float32(60.0), np.float32(53.5), np.float32(48.5), np.float32(42.0),
          np.float32(37.0), np.float32(31.5), np.float32(24.8), np.float32(20.4),
          np.float32(17.4), np.float32(15.5), np.float32(13.0), np.float32(10.7), np.float32(9.20), np.float32(7.50),
          np.float32(6.30), np.float32(5.30), np.float32(4.65), np.float32(4.46),
          np.float32(4.45), np.float32(4.45), np.float32(4.60), np.float32(4.75), np.float32(5.10), np.float32(5.55),
          np.float32(6.80), np.float32(7.90), np.float32(8.50), np.float32(7.80),
          np.float32(6.25), np.float32(6.15), np.float32(6.60), np.float32(7.10), np.float32(8.20), np.float32(9.60),
          np.float32(11.5), np.float32(13.1), np.float32(14.0), np.float32(14.2),
          np.float32(14.3), np.float32(14.4), np.float32(14.0), np.float32(12.2), np.float32(10.4), np.float32(9.20),
          np.float32(8.20), np.float32(7.75), np.float32(7.40), np.float32(7.00),
          np.float32(6.25), np.float32(5.50), np.float32(5.10), np.float32(4.75), np.float32(4.25), np.float32(3.85),
          np.float32(3.56), np.float32(3.24), np.float32(2.99), np.float32(2.77),
          np.float32(2.42), np.float32(2.16), np.float32(1.95), np.float32(1.78), np.float32(1.63), np.float32(1.16),
          np.float32(.907), np.float32(.630), np.float32(.484), np.float32(.393),
          np.float32(.331), np.float32(.252), np.float32(.204), np.float32(.165), np.float32(.139), np.float32(.120),
          np.float32(.106), np.float32(.0865), np.float32(.0731), np.float32(.0636),
          np.float32(.0565), np.float32(.0509), np.float32(.0465), np.float32(.0398), np.float32(.0350),
          np.float32(.0317), np.float32(.0286), np.float32(.0264), np.float32(.0224), np.float32(.0197),
          np.float32(.0178), np.float32(.0164), np.float32(.0145), np.float32(.0132), np.float32(.0123),
          np.float32(.0116), np.float32(.0111), np.float32(.0107), np.float32(.0101), np.float32(.00967),
          np.float32(.00937), np.float32(.00915), np.float32(.00897), np.float32(.00868), np.float32(.00849),
          np.float32(.00837), np.float32(.00829), np.float32(.00818), np.float32(.00812),
          np.float32(.00808),
          np.float32(.00805), np.float32(.00803), np.float32(.00801), np.float32(.00799), np.float32(.00798),
          np.float32(.00797), np.float32(.00797), np.float32(.007965), np.float32(.007957),
          np.float32(.007954),
          np.float32(.007951), np.float32(.007951), np.float32(.007948), np.float32(.007948), np.float32(.007948),
          np.float32(.007948), np.float32(.007946), np.float32(.007945),
          np.float32(.007945), np.float32(.007945), np.float32(.007945), np.float32(.007945), np.float32(.007945),
          np.float32(.007945), np.float32(.007945), np.float32(.007945), np.float32(.007945), np.float32(.007945),
          np.float32(.007945), np.float32(.007945), np.float32(.007945), np.float32(.007945), np.float32(.007945),
          np.float32(.007945), np.float32(.007945), np.float32(.007945), np.float32(.007945), np.float32(.007945),
          ]
# ELASTIC FOR BEND MODE VIBRATIONS.   MOMENTUM TRANSFER

YVBMOMG12 = [np.float32(148.), np.float32(148.), np.float32(146.), np.float32(141.), np.float32(134.), np.float32(128.),
             np.float32(119.), np.float32(109.), np.float32(95.0), np.float32(85.0),
             np.float32(76.5), np.float32(69.5), np.float32(59.0), np.float32(53.5), np.float32(50.0), np.float32(46.5),
             np.float32(45.5), np.float32(45.0), np.float32(43.0), np.float32(37.0),
             np.float32(28.5), np.float32(22.5), np.float32(16.0), np.float32(11.5), np.float32(8.95), np.float32(6.80),
             np.float32(5.80), np.float32(5.05), np.float32(4.80), np.float32(4.65),
             np.float32(4.65), np.float32(4.70), np.float32(4.80), np.float32(5.00), np.float32(5.35), np.float32(5.65),
             np.float32(6.00), np.float32(6.20), np.float32(6.20), np.float32(6.10),
             np.float32(5.50), np.float32(5.10), np.float32(5.00), np.float32(5.20), np.float32(6.10), np.float32(7.30),
             np.float32(8.80), np.float32(9.80), np.float32(10.5), np.float32(10.5),
             np.float32(9.80), np.float32(8.50), np.float32(7.00), np.float32(5.10), np.float32(4.00), np.float32(3.50),
             np.float32(3.10), np.float32(2.90), np.float32(2.70), np.float32(2.50),
             np.float32(2.20), np.float32(1.88), np.float32(1.67), np.float32(1.50), np.float32(1.25), np.float32(1.04),
             np.float32(.832), np.float32(.682), np.float32(.571), np.float32(.486),
             np.float32(.367), np.float32(.287), np.float32(.232), np.float32(.192), np.float32(.161),
             np.float32(.0819), np.float32(.0501), np.float32(.0247), np.float32(.0149), np.float32(.0100),
             np.float32(.00721), np.float32(.00430), np.float32(.00288), np.float32(.00192), np.float32(.00138),
             np.float32(.00105), 8.23e-4, 5.5e-4, 3.96e-4,
             3.0e-4,
             2.36e-4, 1.91e-4, 1.59e-4, 1.15e-4, 8.73e-5, 6.90e-5, 5.62e-5, 4.68e-5,
             3.19e-5, 2.34e-5,
             1.81e-5, 1.45e-5, 1.00e-5, 7.48e-6, 5.86e-6, 4.75e-6, 3.95e-6, 3.36e-6,
             2.54e-6, 2.00e-6,
             1.63e-6, 1.37e-6, 1.16e-6, 8.32e-7, 6.28e-7, 4.94e-7, 4.00e-7, 2.80e-7,
             2.08e-7, 1.62e-7,
             1.30e-7, 1.06e-7, 8.89e-8, 6.51e-8, 4.98e-8, 3.95e-8, 3.21e-8, 2.66e-8,
             1.79e-8, 1.29e-8,
             9.73e-9, 7.63e-9, 5.06e-9, 3.61e-9, 2.71e-9, 2.11e-9, 1.69e-9, 1.38e-9,
             9.79e-10, 7.28e-10,
             5.63e-10, 4.48e-10, 3.65e-10, 2.35e-10, 1.64e-10, 1.21e-10, 9.27e-11,
             5.95e-11, 4.13e-11, 3.04e-11,
             2.33e-11, 1.84e-11, 1.49e-11, 1.03e-11, 7.61e-12, 5.83e-12, 4.60e-12,
             3.73e-12,
             ]
# ELASTIC FOR BEND MODE VIBRATIONS.

YVBELG12 = [np.float32(148.), np.float32(148.), np.float32(146.), np.float32(141.), np.float32(135.), np.float32(129.),
            np.float32(120.), np.float32(110.), np.float32(96.0), np.float32(86.0),
            np.float32(77.5), np.float32(70.5), np.float32(60.0), np.float32(54.5), np.float32(51.1), np.float32(47.6),
            np.float32(46.8), np.float32(47.2), np.float32(48.5), np.float32(46.6),
            np.float32(38.7), np.float32(32.9), np.float32(25.4), np.float32(19.1), np.float32(15.4), np.float32(11.9),
            np.float32(9.37), np.float32(7.33), np.float32(6.20), np.float32(5.68),
            np.float32(5.52), np.float32(5.43), np.float32(5.52), np.float32(5.65), np.float32(5.93), np.float32(6.40),
            np.float32(7.70), np.float32(8.44), np.float32(8.78), np.float32(7.93),
            np.float32(6.25), np.float32(6.15), np.float32(6.60), np.float32(7.10), np.float32(8.20), np.float32(9.60),
            np.float32(11.5), np.float32(13.1), np.float32(14.0), np.float32(14.2),
            np.float32(14.3), np.float32(14.4), np.float32(14.0), np.float32(12.2), np.float32(10.4), np.float32(9.20),
            np.float32(8.20), np.float32(7.75), np.float32(7.40), np.float32(7.00),
            np.float32(6.25), np.float32(5.50), np.float32(5.10), np.float32(4.75), np.float32(4.25), np.float32(3.85),
            np.float32(3.56), np.float32(3.24), np.float32(2.99), np.float32(2.77),
            np.float32(2.42), np.float32(2.16), np.float32(1.95), np.float32(1.78), np.float32(1.63), np.float32(1.16),
            np.float32(.907), np.float32(.630), np.float32(.484), np.float32(.393),
            np.float32(.331), np.float32(.252), np.float32(.204), np.float32(.165), np.float32(.139), np.float32(.120),
            np.float32(.106), np.float32(.0865), np.float32(.0731), np.float32(.0636),
            np.float32(.0565), np.float32(.0509), np.float32(.0465), np.float32(.0398), np.float32(.0350),
            np.float32(.0317), np.float32(.0286), np.float32(.0264), np.float32(.0224), np.float32(.0197),
            np.float32(.0178), np.float32(.0164), np.float32(.0145), np.float32(.0132), np.float32(.0123),
            np.float32(.0116), np.float32(.0111), np.float32(.0107), np.float32(.0101), np.float32(.00967),
            np.float32(.00937), np.float32(.00915), np.float32(.00897), np.float32(.00868), np.float32(.00849),
            np.float32(.00837), np.float32(.00829), np.float32(.00818), np.float32(.00812),
            np.float32(.00808),
            np.float32(.00805), np.float32(.00803), np.float32(.00801), np.float32(.00799), np.float32(.00798),
            np.float32(.00797), np.float32(.00797), np.float32(.007965), np.float32(.007957),
            np.float32(.007954),
            np.float32(.007951), np.float32(.007951), np.float32(.007948), np.float32(.007948), np.float32(.007948),
            np.float32(.007948), np.float32(.007946), np.float32(.007945),
            np.float32(.007945), np.float32(.007945), np.float32(.007945), np.float32(.007945), np.float32(.007945),
            np.float32(.007945), np.float32(.007945), np.float32(.007945), np.float32(.007945), np.float32(.007945),
            np.float32(.007945), np.float32(.007945), np.float32(.007945), np.float32(.007945), np.float32(.007945),
            np.float32(.007945), np.float32(.007945), np.float32(.007945), np.float32(.007945), np.float32(.007945),
            ]
# EPSILON FOR ELASTIC ANGULAR DISTRIBUTION

# EPSILON= 1.0-YEPS

YEPSG12 = [np.float32(1.0), np.float32(.99999), np.float32(.9999), np.float32(.999), np.float32(.98889),
           np.float32(.98838), np.float32(.98751), np.float32(.98637),
           np.float32(.98437), np.float32(.98256),
           np.float32(.98065), np.float32(.97873), np.float32(.97500), np.float32(.97197), np.float32(.96908),
           np.float32(.96429), np.float32(.95947), np.float32(.92864),
           np.float32(.83162), np.float32(.69698),
           np.float32(.61559), np.float32(.54634), np.float32(.47845), np.float32(.44409), np.float32(.41864),
           np.float32(.40901), np.float32(.46393), np.float32(.55266),
           np.float32(.66891), np.float32(.73158),
           np.float32(.76665), np.float32(.79940), np.float32(.80584), np.float32(.82736), np.float32(.85357),
           np.float32(.82540), np.float32(.67623), np.float32(.61361),
           np.float32(.57544), np.float32(.66197),
           np.float32(.82116), np.float32(.74722), np.float32(.64577), np.float32(.61117), np.float32(.62691),
           np.float32(.64971), np.float32(.65638), np.float32(.63267),
           np.float32(.63530), np.float32(.62080),
           np.float32(.54823), np.float32(.42904), np.float32(.32703), np.float32(.24494), np.float32(.21449),
           np.float32(.21081), np.float32(.20872), np.float32(.20537),
           np.float32(.19735), np.float32(.19081),
           np.float32(.18652), np.float32(.17814), np.float32(.16660), np.float32(.15748), np.float32(.14114),
           np.float32(.12395), np.float32(.099839), np.float32(.085294),
           np.float32(.074236), np.float32(.065563),
           np.float32(.052933), np.float32(.044215), np.float32(.037873), np.float32(.033074), np.float32(.029321),
           np.float32(.018575), np.float32(.013522), np.float32(.008720),
           np.float32(.006419), np.float32(.005074),
           np.float32(.00419), np.float32(.00311), np.float32(.00247), np.float32(.00196), np.float32(.001619),
           np.float32(.001393), np.float32(.001209), np.float32(.000954),
           7.917e-4, 6.736e-4,
           5.847e-4, 5.164e-4, 4.637e-4, 3.818e-4, 3.224e-4, 2.758e-4, 2.454e-4,
           2.182e-4, 1.701e-4, 1.385e-4,
           1.162e-4, 9.92e-5, 7.50e-5, 6.02e-5, 4.96e-5, 4.19e-5, 3.58e-5, 3.12e-5,
           2.44e-5, 1.97e-5,
           1.63e-5, 1.37e-5, 1.17e-5, 8.44e-6, 6.34e-6, 4.95e-6, 3.98e-6, 2.74e-6,
           2.00e-6, 1.53e-6,
           1.21e-6, 9.78e-7, 8.09e-7, 5.79e-7, 4.36e-7, 3.39e-7, 2.72e-7, 2.23e-7,
           1.46e-7, 1.026e-7,
           7.610e-8, 5.868e-8, 3.796e-8, 2.652e-8, 1.955e-8, 1.499e-8, 1.186e-8,
           9.60e-9, 6.65e-9, 4.87e-9,
           3.71e-9, 2.91e-9, 2.35e-9, 1.48e-9, 1.01e-9, 7.34e-10, 5.55e-10,
           3.48e-10, 2.38e-10, 1.72e-10,
           1.30e-10, 1.02e-10, 8.2e-11, 5.6e-11, 4.0e-11, 3.0e-11, 2.4e-11, 1.9e-11,
           ]
#

# V(010)  BEND MODE  ( ANALYTICAL DIPOLE FUNCTION AT THRESHOLD)

# ABOVE 70EV SCALED BY 1/E

XV2G12 = [np.float32(.08275), np.float32(2.00), np.float32(2.50), np.float32(3.00), np.float32(3.50), np.float32(3.80),
          np.float32(4.00), np.float32(4.50), np.float32(5.00), np.float32(6.00),
          np.float32(8.00), np.float32(10.0), np.float32(15.0), np.float32(20.0), np.float32(30.0), np.float32(50.0),
          np.float32(70.0),
          ]
YV2G12 = [np.float32(0.00), np.float32(0.00), np.float32(0.24), np.float32(0.48), np.float32(1.29), np.float32(1.70),
          np.float32(1.70), np.float32(1.17), np.float32(0.74), np.float32(0.42),
          np.float32(0.01), np.float32(0.08), np.float32(0.05), np.float32(0.08), np.float32(0.12), np.float32(0.07),
          np.float32(.001),
          ]
# V(020)  BEND MODE HARMONIC  RESONANCE    ABOVE 70EV SCALED BY 1/E

X2V2G12 = [np.float32(.15937), np.float32(0.18), np.float32(0.50), np.float32(1.00), np.float32(2.00), np.float32(3.00),
           np.float32(3.50), np.float32(3.80), np.float32(4.00), np.float32(4.50),
           np.float32(5.00), np.float32(6.00), np.float32(8.00), np.float32(10.0), np.float32(15.0), np.float32(20.0),
           np.float32(30.0), np.float32(50.0), np.float32(70.0),
           ]
Y2V2G12 = [np.float32(0.00), np.float32(0.02), np.float32(0.01), np.float32(.003), np.float32(.025), np.float32(0.09),
           np.float32(0.31), np.float32(0.44), np.float32(0.56), np.float32(0.49),
           np.float32(0.35), np.float32(0.17), np.float32(0.08), np.float32(0.10), np.float32(0.02), np.float32(.008),
           np.float32(.015), np.float32(.008), np.float32(.001),
           ]
# V(100) SYMMETRIC STRETCH                ABOVE 70EV SCALED BY 1/E

XV1G12 = [np.float32(.17211), np.float32(0.18), np.float32(0.20), np.float32(0.23), np.float32(0.25), np.float32(0.30),
          np.float32(0.40), np.float32(0.50), np.float32(0.60), np.float32(1.00),
          np.float32(2.00), np.float32(2.50), np.float32(3.00), np.float32(3.50), np.float32(3.80), np.float32(4.00),
          np.float32(4.50), np.float32(5.00), np.float32(6.00), np.float32(8.00),
          np.float32(10.0), np.float32(15.0), np.float32(20.0), np.float32(30.0), np.float32(50.0), np.float32(70.0),
          ]
YV1G12 = [np.float32(0.00), np.float32(.475), np.float32(.790), np.float32(0.91), np.float32(0.91), np.float32(0.82),
          np.float32(0.58), np.float32(0.43), np.float32(0.34), np.float32(0.32),
          np.float32(0.38), np.float32(0.66), np.float32(0.89), np.float32(1.27), np.float32(1.32), np.float32(1.04),
          np.float32(0.53), np.float32(0.18), np.float32(.084), np.float32(.075),
          np.float32(.077), np.float32(.030), np.float32(.009), np.float32(.030), np.float32(.008), np.float32(.001),
          ]
# V(030) + V(110)                          ABOVE 10EV SCALED BY 1/E

X3V2G12 = [np.float32(.251), np.float32(2.00), np.float32(2.50), np.float32(3.00), np.float32(3.50), np.float32(3.80),
           np.float32(4.00), np.float32(4.50), np.float32(5.00), np.float32(6.00),
           np.float32(10.0),
           ]
Y3V2G12 = [np.float32(0.00), np.float32(0.00), np.float32(0.01), np.float32(0.17), np.float32(0.36), np.float32(0.58),
           np.float32(0.58), np.float32(0.36), np.float32(0.17), np.float32(0.01),
           np.float32(.001),
           ]
# V(001) ASYMMETRIC STRETCH  (ANALYTICAL DIPOLE FUNCTION AT THRESHOLD)

# ABOVE 10EV SCALED BY 1/E

XV3G12 = [np.float32(.29126), np.float32(2.00), np.float32(3.00), np.float32(3.50), np.float32(3.80), np.float32(4.00),
          np.float32(4.50), np.float32(5.00), np.float32(6.00), np.float32(8.00),
          np.float32(10.0),
          ]
YV3G12 = [np.float32(0.00), np.float32(0.00), np.float32(.002), np.float32(.005), np.float32(.010), np.float32(.005),
          np.float32(.002), np.float32(.001), np.float32(.001), np.float32(.001),
          np.float32(.001),
          ]
# V(040) + V(120) + V(200)  POLYAD 3        ABOVE 10EV SCALED BY 1/E

XVPD3G12 = [np.float32(.335), np.float32(0.35), np.float32(0.50), np.float32(0.80), np.float32(2.00), np.float32(2.50),
            np.float32(3.00), np.float32(3.50), np.float32(3.80), np.float32(4.00),
            np.float32(4.50), np.float32(5.00), np.float32(6.00), np.float32(10.0),
            ]
YVPD3G12 = [np.float32(0.00), np.float32(0.09), np.float32(.035), np.float32(0.02), np.float32(0.02), np.float32(0.02),
            np.float32(0.21), np.float32(0.43), np.float32(0.70), np.float32(0.70),
            np.float32(0.43), np.float32(0.21), np.float32(0.05), np.float32(.020),
            ]
#  V(130) + V(210)                          ABOVE 20EV SCALED BY 1/E

XV130G12 = [np.float32(0.422), np.float32(2.00), np.float32(2.50), np.float32(3.00), np.float32(3.50), np.float32(3.80),
            np.float32(4.00), np.float32(4.50), np.float32(5.00), np.float32(6.00),
            np.float32(10.0), np.float32(20.0),
            ]
YV130G12 = [np.float32(0.00), np.float32(0.00), np.float32(.005), np.float32(0.10), np.float32(0.22), np.float32(0.35),
            np.float32(0.35), np.float32(0.22), np.float32(0.10), np.float32(.025),
            np.float32(.005), np.float32(.002),
            ]
#  POLYAD 4                                ABOVE 10EV SCALED BY 1/E

XVPD4G12 = [np.float32(0.505), np.float32(0.55), np.float32(0.65), np.float32(1.00), np.float32(2.00), np.float32(2.50),
            np.float32(3.00), np.float32(3.50), np.float32(3.80), np.float32(4.00),
            np.float32(4.50), np.float32(5.00), np.float32(6.00), np.float32(10.0),
            ]
YVPD4G12 = [np.float32(0.00), np.float32(.0017), np.float32(.0005), np.float32(.0001), np.float32(.0001),
            np.float32(.005), np.float32(0.12), np.float32(0.24), np.float32(0.40), np.float32(0.40),
            np.float32(0.24), np.float32(0.13), np.float32(0.01), np.float32(.001),
            ]
#  POLYAD 5                                ABOVE 10EV SCALED BY 1/E

XVPD5G12 = [np.float32(0.685), np.float32(2.00), np.float32(2.50), np.float32(3.00), np.float32(3.50), np.float32(3.80),
            np.float32(4.00), np.float32(4.50), np.float32(5.00), np.float32(6.00),
            np.float32(10.0),
            ]
YVPD5G12 = [np.float32(0.00), np.float32(0.00), np.float32(.003), np.float32(0.07), np.float32(0.14), np.float32(0.24),
            np.float32(0.24), np.float32(0.14), np.float32(0.08), np.float32(.006),
            np.float32(.001),
            ]
#  POLYAD 6                                ABOVE 10EV SCALED BY 1/E

XVPD6G12 = [np.float32(0.825), np.float32(2.00), np.float32(2.50), np.float32(3.00), np.float32(3.50), np.float32(3.80),
            np.float32(4.00), np.float32(4.50), np.float32(5.00), np.float32(6.00),
            np.float32(10.0),
            ]
YVPD6G12 = [np.float32(0.00), np.float32(0.00), np.float32(.001), np.float32(0.05), np.float32(0.10), np.float32(0.16),
            np.float32(0.16), np.float32(0.10), np.float32(0.05), np.float32(.004),
            np.float32(.001),
            ]
#  POLYAD 7                                ABOVE 10EV SCALED BY 1/E

XVPD7G12 = [np.float32(0.995), np.float32(2.00), np.float32(2.50), np.float32(3.00), np.float32(3.50), np.float32(3.80),
            np.float32(4.00), np.float32(4.50), np.float32(5.00), np.float32(6.00),
            np.float32(10.0),
            ]
YVPD7G12 = [np.float32(0.00), np.float32(0.00), np.float32(.001), np.float32(0.03), np.float32(0.06), np.float32(0.10),
            np.float32(0.10), np.float32(0.06), np.float32(0.03), np.float32(.003),
            np.float32(.001),
            ]
#  POLYAD 8                                ABOVE 10EV SCALED BY 1/E

XVPD8G12 = [np.float32(1.160), np.float32(2.00), np.float32(2.50), np.float32(3.00), np.float32(3.50), np.float32(3.80),
            np.float32(4.00), np.float32(4.50), np.float32(5.00), np.float32(6.00),
            np.float32(10.0),
            ]
YVPD8G12 = [np.float32(0.00), np.float32(0.00), np.float32(.001), np.float32(0.03), np.float32(0.06), np.float32(0.10),
            np.float32(0.10), np.float32(0.06), np.float32(0.03), np.float32(.003),
            np.float32(.001),
            ]
#  POLYAD 9                                ABOVE 10EV SCALED BY 1/E

XVPD9G12 = [np.float32(1.320), np.float32(2.00), np.float32(2.50), np.float32(3.00), np.float32(3.50), np.float32(3.80),
            np.float32(4.00), np.float32(4.50), np.float32(5.00), np.float32(6.00),
            np.float32(10.0),
            ]
YVPD9G12 = [np.float32(0.00), np.float32(0.00), np.float32(.001), np.float32(0.03), np.float32(0.06), np.float32(0.10),
            np.float32(0.10), np.float32(0.06), np.float32(0.03), np.float32(.003),
            np.float32(.001),
            ]
#  SUM HIGHER POLYADS                      ABOVE 10EV SCALED BY 1/E

XVPDHG12 = [np.float32(2.50), np.float32(3.00), np.float32(3.50), np.float32(3.80), np.float32(4.00), np.float32(4.50),
            np.float32(5.00), np.float32(6.00), np.float32(10.0),
            ]
YVPDHG12 = [np.float32(0.00), np.float32(0.01), np.float32(0.36), np.float32(0.58), np.float32(0.58), np.float32(0.36),
            np.float32(0.16), np.float32(.045), np.float32(.001),
            ]
# DATA FROM RAP AND BRIGLIA ( SCALED BY 1.031 FROM INCREASE IN CO2

#                              IONISATION X-SEC)

# ABOVE 10EV SCALED BY 1/E**3

XATTG12 = [np.float32(3.30), np.float32(3.40), np.float32(3.50), np.float32(3.60), np.float32(3.70), np.float32(3.80),
           np.float32(3.90), np.float32(4.00), np.float32(4.10), np.float32(4.20),
           np.float32(4.30), np.float32(4.40), np.float32(4.50), np.float32(4.60), np.float32(4.70), np.float32(4.80),
           np.float32(4.90), np.float32(5.00), np.float32(5.10), np.float32(5.20),
           np.float32(5.30), np.float32(5.40), np.float32(5.50), np.float32(5.60), np.float32(5.70), np.float32(5.80),
           np.float32(5.90), np.float32(6.00), np.float32(6.10), np.float32(6.20),
           np.float32(6.30), np.float32(6.40), np.float32(6.50), np.float32(6.60), np.float32(6.70), np.float32(6.80),
           np.float32(6.90), np.float32(7.00), np.float32(7.10), np.float32(7.20),
           np.float32(7.30), np.float32(7.40), np.float32(7.50), np.float32(7.60), np.float32(7.70), np.float32(7.80),
           np.float32(7.90), np.float32(8.00), np.float32(8.10), np.float32(8.20),
           np.float32(8.30), np.float32(8.40), np.float32(8.50), np.float32(8.60), np.float32(8.70), np.float32(8.80),
           np.float32(8.90), np.float32(9.00), np.float32(9.10), np.float32(9.20),
           np.float32(9.30), np.float32(9.40), np.float32(9.50), np.float32(9.60), np.float32(9.70), np.float32(9.80),
           np.float32(9.90), np.float32(10.0),
           ]
YATTG12 = [np.float32(.0), 1.81e-5, 6.35e-5, 1.45e-4, 2.81e-4, 5.44e-4, 8.43e-4,
           1.09e-3, 1.32e-3, 1.45e-3,
           1.53e-3, 1.40e-3, 1.25e-3, 1.01e-3, 7.98e-4, 6.17e-4, 4.54e-4, 2.91e-4,
           2.00e-4, 1.36e-4,
           9.98e-5, 6.35e-5, 2.72e-5, 1.81e-5, 9.07e-6, 1.00e-6, 9.07e-6, 1.81e-5,
           2.72e-5, 4.54e-5,
           6.35e-5, 1.09e-4, 1.45e-4, 2.08e-4, 2.99e-4, 3.99e-4, 5.44e-4, 9.25e-4,
           9.25e-4, 1.18e-3,
           1.49e-3, 1.84e-3, 2.23e-3, 2.75e-3, 3.22e-3, 3.68e-3, 4.08e-3, 4.37e-3,
           4.41e-3, 4.26e-3,
           3.92e-3, 3.46e-3, 2.92e-3, 2.22e-3, 1.77e-3, 1.40e-3, 1.05e-3, 8.07e-4,
           6.35e-4, 4.99e-4,
           3.80e-4, 2.99e-4, 2.36e-4, 1.81e-4, 1.36e-4, 1.09e-4, 8.17e-5, 1.00e-6,
           ]
# USE 1/EN**2 EXTRAPOLATION ABOVE 30EV

XTRP1G12 = [np.float32(8.89), np.float32(10.0), np.float32(11.0), np.float32(12.0), np.float32(13.0), np.float32(15.0),
            np.float32(17.0), np.float32(20.0), np.float32(23.0), np.float32(27.0),
            np.float32(30.0),
            ]
YTRP1G12 = [np.float32(0.00), np.float32(.110), np.float32(.201), np.float32(.231), np.float32(.248), np.float32(.270),
            np.float32(.275), np.float32(.248), np.float32(.206), np.float32(.151),
            np.float32(.122),
            ]
#  USE 1/E**2 EXTRAPOLATION ABOVE 36EV

XTRP2G12 = [np.float32(11.3), np.float32(12.0), np.float32(13.0), np.float32(14.0), np.float32(16.0), np.float32(18.0),
            np.float32(21.0), np.float32(24.0), np.float32(28.0), np.float32(31.0),
            np.float32(36.0),
            ]
YTRP2G12 = [np.float32(0.00), np.float32(.322), np.float32(.662), np.float32(.772), np.float32(.873), np.float32(.919),
            np.float32(.919), np.float32(.873), np.float32(.689), np.float32(.562),
            np.float32(.417),
            ]
# IONISATION VALUES ABOVE 1KEV GENERATED BY BORN BETHE IN SUB)

# DATA FROM RAPP, LINDSAY AND RIEKE ALSO BB THEORY

# C    DATA XION/13.776,14.5,15.0,15.5,16.0,16.5,17.0,17.5,18.0,18.5,

#    /19.0,19.5,21.0,21.5,22.0,22.5,23.0,23.5,24.0,26.0,

#    /28.0,30.0,32.0,34.0,36.0,38.0,40.0,45.0,50.0,55.0,

#    /60.0,65.0,70.0,75.0,80.0,85.0,90.0,100.,110.,130.,

#    /140.,160.,180.,200.,225.,250.,275.,300.,350.,400.,

#    /450.,500.,550.,600.,650.,700.,750.,800.,850.,900.,

#    /950.,1000./

# GROSS IONISATION

#     DATA YION/0.00,.055,.097,.135,.174,.215,.255,.293,.333,.373,

#    /.428,.452,.577,.623,.676,.727,.777,.828,.880,1.14,

#    /1.37,1.54,1.70,1.84,1.96,2.07,2.19,2.45,2.67,2.84,

#    /3.02,3.16,3.27,3.36,3.45,3.51,3.56,3.64,3.66,3.65,

#    /3.63,3.52,3.43,3.32,3.21,3.05,2.97,2.82,2.58,2.43,

#    /2.23,2.09,1.96,1.85,1.77,1.68,1.61,1.53,1.45,1.41,

#    /1.36,1.30/

# COUNTING IONISATION

#     DATA YINC/0.00,.055,.097,.135,.174,.215,.255,.293,.333,.373,

#    /.428,.452,.577,.623,.676,.727,.777,.828,.880,1.14,

#    /1.37,1.54,1.70,1.84,1.96,2.07,2.19,2.45,2.67,2.84,

#    /3.01,3.14,3.26,3.33,3.43,3.48,3.54,3.62,3.63,3.62,

#    /3.60,3.48,3.40,3.29,3.17,3.02,2.94,2.79,2.55,2.41,

#    /2.21,2.08,1.94,1.84,1.75,1.66,1.60,1.51,1.44,1.40,

#    /1.35,1.29/

#

# IONISATION VALUES ABOVE 1KEV GENERATED BY BORN BETHE IN SUB)

# DATA FROM RAPP, LINDSAY AND RIEKE ALSO BB THEORY

XION1G12 = [np.float32(13.776), np.float32(14.5), np.float32(15.0), np.float32(15.5), np.float32(16.0),
            np.float32(16.5), np.float32(17.0), np.float32(17.5), np.float32(18.0), np.float32(18.5),
            np.float32(19.0), np.float32(19.5), np.float32(21.0), np.float32(21.5), np.float32(22.0), np.float32(22.5),
            np.float32(23.0), np.float32(23.5), np.float32(24.0), np.float32(26.0),
            np.float32(28.0), np.float32(30.0), np.float32(32.0), np.float32(34.0), np.float32(36.0), np.float32(38.0),
            np.float32(40.0), np.float32(45.0), np.float32(50.0), np.float32(55.0),
            np.float32(60.0), np.float32(65.0), np.float32(70.0), np.float32(75.0), np.float32(80.0), np.float32(85.0),
            np.float32(90.0), np.float32(95.0), np.float32(100.), np.float32(110.),
            np.float32(120.), np.float32(140.), np.float32(160.), np.float32(180.), np.float32(200.), np.float32(225.),
            np.float32(250.), np.float32(275.), np.float32(300.), np.float32(350.),
            np.float32(400.), np.float32(450.), np.float32(500.), np.float32(550.), np.float32(600.), np.float32(650.),
            np.float32(700.), np.float32(750.), np.float32(800.), np.float32(850.),
            np.float32(900.), np.float32(950.), np.float32(1000.),
            ]
# IONISATION CO2+ ( INCLUDING EXCITED STATES A2PIu and B2SIGMA+u )

YION1G12 = [np.float32(0.00), np.float32(.056), np.float32(.100), np.float32(.139), np.float32(.179), np.float32(.221),
            np.float32(.263), np.float32(.302), np.float32(.343), np.float32(.384),
            np.float32(.441), np.float32(.466), np.float32(.594), np.float32(.642), np.float32(.696), np.float32(.749),
            np.float32(.800), np.float32(.853), np.float32(.906), np.float32(1.05),
            np.float32(1.21), np.float32(1.32), np.float32(1.40), np.float32(1.47), np.float32(1.55), np.float32(1.63),
            np.float32(1.70), np.float32(1.84), np.float32(1.94), np.float32(2.00),
            np.float32(2.06), np.float32(2.10), np.float32(2.13), np.float32(2.15), np.float32(2.19), np.float32(2.20),
            np.float32(2.22), np.float32(2.23), np.float32(2.25), np.float32(2.23),
            np.float32(2.23), np.float32(2.19), np.float32(2.12), np.float32(2.08), np.float32(2.01), np.float32(1.95),
            np.float32(1.87), np.float32(1.83), np.float32(1.75), np.float32(1.62),
            np.float32(1.54), np.float32(1.43), np.float32(1.35), np.float32(1.27), np.float32(1.21), np.float32(1.16),
            np.float32(1.10), np.float32(1.06), np.float32(1.01), np.float32(.964),
            np.float32(.941), np.float32(.909), np.float32(.876),
            ]
# IONISATION EXCITATION CO2+(A2PIu) 17.314ev

# ITIKAWA THEN SCALED CO2+ BY 38.5% ABOVE 400EV

XION2G12 = [np.float32(17.314), np.float32(18.8), np.float32(19.9), np.float32(21.1), np.float32(22.4),
            np.float32(23.7), np.float32(25.1), np.float32(26.6), np.float32(28.2), np.float32(29.8),
            np.float32(31.6), np.float32(33.5), np.float32(35.4), np.float32(37.5), np.float32(39.8), np.float32(42.1),
            np.float32(44.6), np.float32(47.2), np.float32(50.0), np.float32(53.0),
            np.float32(56.1), np.float32(59.5), np.float32(63.0), np.float32(66.7), np.float32(70.7), np.float32(74.8),
            np.float32(79.3), np.float32(88.9), np.float32(94.2), np.float32(99.8),
            np.float32(106.), np.float32(112.), np.float32(119.), np.float32(126.), np.float32(133.), np.float32(141.),
            np.float32(149.), np.float32(158.), np.float32(167.), np.float32(177.),
            np.float32(188.), np.float32(199.), np.float32(211.), np.float32(223.), np.float32(236.), np.float32(250.),
            np.float32(265.), np.float32(281.), np.float32(298.), np.float32(315.),
            np.float32(334.), np.float32(354.), np.float32(375.), np.float32(397.), np.float32(450.), np.float32(500.),
            np.float32(550.), np.float32(600.), np.float32(650.), np.float32(700.),
            np.float32(750.), np.float32(800.), np.float32(850.), np.float32(900.), np.float32(950.), np.float32(1000.),
            ]

YION2G12 = [np.float32(0.0), np.float32(.0314), np.float32(.0494), np.float32(.0682), np.float32(.0873),
            np.float32(.107), np.float32(.128), np.float32(.150), np.float32(.168), np.float32(.191),
            np.float32(.214), np.float32(.233), np.float32(.256), np.float32(.280), np.float32(.304), np.float32(.331),
            np.float32(.356), np.float32(.388), np.float32(.416), np.float32(.445),
            np.float32(.476), np.float32(.508), np.float32(.541), np.float32(.579), np.float32(.615), np.float32(.646),
            np.float32(.675), np.float32(.723), np.float32(.740), np.float32(.754),
            np.float32(.767), np.float32(.776), np.float32(.784), np.float32(.790), np.float32(.796), np.float32(.796),
            np.float32(.798), np.float32(.796), np.float32(.796), np.float32(.791),
            np.float32(.784), np.float32(.775), np.float32(.763), np.float32(.750), np.float32(.734), np.float32(.718),
            np.float32(.702), np.float32(.687), np.float32(.671), np.float32(.656),
            np.float32(.640), np.float32(.624), np.float32(.609), np.float32(.593), np.float32(.551), np.float32(.520),
            np.float32(.489), np.float32(.466), np.float32(.447), np.float32(.423),
            np.float32(.408), np.float32(.389), np.float32(.371), np.float32(.362), np.float32(.350), np.float32(.337),
            ]
# ITIKAWA THEN SCALED CO2+ BY 22.0% ABOVE 400EV
#IONISATION EXCITATION CO2+(B2SIGMA+u) 18.077ev
XION3G12 = [np.float32(18.077), np.float32(18.8), np.float32(19.9), np.float32(21.1), np.float32(22.4),
            np.float32(23.7), np.float32(25.1), np.float32(26.6), np.float32(28.2), np.float32(29.8),
            np.float32(31.6), np.float32(33.5), np.float32(35.4), np.float32(37.5), np.float32(39.8), np.float32(42.1),
            np.float32(44.6), np.float32(47.2), np.float32(50.0), np.float32(53.0),
            np.float32(56.1), np.float32(59.5), np.float32(63.0), np.float32(66.7), np.float32(70.7), np.float32(74.8),
            np.float32(79.3), np.float32(88.9), np.float32(94.2), np.float32(99.8),
            np.float32(106.), np.float32(112.), np.float32(119.), np.float32(126.), np.float32(133.), np.float32(141.),
            np.float32(149.), np.float32(158.), np.float32(167.), np.float32(177.),
            np.float32(188.), np.float32(199.), np.float32(211.), np.float32(223.), np.float32(236.), np.float32(250.),
            np.float32(265.), np.float32(281.), np.float32(298.), np.float32(315.),
            np.float32(334.), np.float32(354.), np.float32(375.), np.float32(397.), np.float32(450.), np.float32(500.),
            np.float32(550.), np.float32(600.), np.float32(650.), np.float32(700.),
            np.float32(750.), np.float32(800.), np.float32(850.), np.float32(900.), np.float32(950.), np.float32(1000.),
            ]
YION3G12 = [np.float32(0.0), np.float32(.0121), np.float32(.0247), np.float32(.0384), np.float32(.0517),
            np.float32(.0653), np.float32(.0797), np.float32(.0932), np.float32(.106),
            np.float32(.120),
            np.float32(.134), np.float32(.147), np.float32(.162), np.float32(.176), np.float32(.191), np.float32(.207),
            np.float32(.222), np.float32(.239), np.float32(.256), np.float32(.272),
            np.float32(.288), np.float32(.304), np.float32(.321), np.float32(.337), np.float32(.353), np.float32(.371),
            np.float32(.386), np.float32(.415), np.float32(.425), np.float32(.434),
            np.float32(.443), np.float32(.451), np.float32(.457), np.float32(.462), np.float32(.466), np.float32(.468),
            np.float32(.469), np.float32(.467), np.float32(.466), np.float32(.462),
            np.float32(.457), np.float32(.449), np.float32(.441), np.float32(.432), np.float32(.423), np.float32(.414),
            np.float32(.404), np.float32(.395), np.float32(.386), np.float32(.377),
            np.float32(.368), np.float32(.357), np.float32(.348), np.float32(.339), np.float32(.315), np.float32(.297),
            np.float32(.279), np.float32(.266), np.float32(.255), np.float32(.242),
            np.float32(.233), np.float32(.222), np.float32(.212), np.float32(.207), np.float32(.200), np.float32(.193),
            ]
# IONISATION O+

XION4G12 = [np.float32(19.07), np.float32(25.0), np.float32(30.0), np.float32(35.0), np.float32(40.0), np.float32(45.0),
            np.float32(50.0), np.float32(55.0), np.float32(60.0), np.float32(65.0),
            np.float32(70.0), np.float32(75.0), np.float32(80.0), np.float32(85.0), np.float32(90.0), np.float32(95.0),
            np.float32(100.), np.float32(110.), np.float32(120.), np.float32(140.),
            np.float32(160.), np.float32(180.), np.float32(200.), np.float32(225.), np.float32(250.), np.float32(275.),
            np.float32(300.), np.float32(350.), np.float32(400.), np.float32(450.),
            np.float32(500.), np.float32(550.), np.float32(600.), np.float32(650.), np.float32(700.), np.float32(750.),
            np.float32(800.), np.float32(850.), np.float32(900.), np.float32(950.),
            np.float32(1000.),
            ]
YION4G12 = [np.float32(0.0), np.float32(.0419), np.float32(.0986), np.float32(.150), np.float32(.195), np.float32(.245),
            np.float32(.299), np.float32(.352), np.float32(.407), np.float32(.452),
            np.float32(.485), np.float32(.526), np.float32(.556), np.float32(.584), np.float32(.606), np.float32(.622),
            np.float32(.640), np.float32(.663), np.float32(.671), np.float32(.680),
            np.float32(.670), np.float32(.647), np.float32(.631), np.float32(.606), np.float32(.572), np.float32(.553),
            np.float32(.524), np.float32(.470), np.float32(.433), np.float32(.388),
            np.float32(.361), np.float32(.339), np.float32(.311), np.float32(.299), np.float32(.283), np.float32(.268),
            np.float32(.252), np.float32(.238), np.float32(.229), np.float32(.222),
            np.float32(.209),
            ]
# IONISATION CO+

XION5G12 = [np.float32(19.47), np.float32(25.0), np.float32(30.0), np.float32(35.0), np.float32(40.0), np.float32(45.0),
            np.float32(50.0), np.float32(55.0), np.float32(60.0), np.float32(65.0),
            np.float32(70.0), np.float32(75.0), np.float32(80.0), np.float32(85.0), np.float32(90.0), np.float32(95.0),
            np.float32(100.), np.float32(110.), np.float32(120.), np.float32(140.),
            np.float32(160.), np.float32(180.), np.float32(200.), np.float32(225.), np.float32(250.), np.float32(275.),
            np.float32(300.), np.float32(350.), np.float32(400.), np.float32(450.),
            np.float32(500.), np.float32(550.), np.float32(600.), np.float32(650.), np.float32(700.), np.float32(750.),
            np.float32(800.), np.float32(850.), np.float32(900.), np.float32(950.),
            np.float32(1000.),
            ]
YION5G12 = [np.float32(0.0), np.float32(.0279), np.float32(.139), np.float32(.247), np.float32(.281), np.float32(.299),
            np.float32(.319), np.float32(.339), np.float32(.362), np.float32(.369),
            np.float32(.379), np.float32(.380), np.float32(.386), np.float32(.389), np.float32(.390), np.float32(.390),
            np.float32(.389), np.float32(.386), np.float32(.378), np.float32(.365),
            np.float32(.340), np.float32(.333), np.float32(.314), np.float32(.300), np.float32(.278), np.float32(.269),
            np.float32(.250), np.float32(.226), np.float32(.211), np.float32(.193),
            np.float32(.178), np.float32(.165), np.float32(.154), np.float32(.145), np.float32(.139), np.float32(.132),
            np.float32(.124), np.float32(.119), np.float32(.113), np.float32(.110),
            np.float32(.103),
            ]
# IONISATION C+

XION6G12 = [np.float32(27.82), np.float32(30.0), np.float32(35.0), np.float32(40.0), np.float32(45.0), np.float32(50.0),
            np.float32(55.0), np.float32(60.0), np.float32(65.0), np.float32(70.0),
            np.float32(75.0), np.float32(80.0), np.float32(85.0), np.float32(90.0), np.float32(95.0), np.float32(100.),
            np.float32(110.), np.float32(120.), np.float32(140.), np.float32(160.),
            np.float32(180.), np.float32(200.), np.float32(225.), np.float32(250.), np.float32(275.), np.float32(300.),
            np.float32(350.), np.float32(400.), np.float32(450.), np.float32(500.),
            np.float32(550.), np.float32(600.), np.float32(650.), np.float32(700.), np.float32(750.), np.float32(800.),
            np.float32(850.), np.float32(900.), np.float32(950.), np.float32(1000.),
            ]
YION6G12 = [np.float32(0.0), np.float32(.0024), np.float32(.028), np.float32(.0782), np.float32(.121), np.float32(.149),
            np.float32(.178), np.float32(.208), np.float32(.229), np.float32(.246),
            np.float32(.261), np.float32(.278), np.float32(.285), np.float32(.296), np.float32(.306), np.float32(.310),
            np.float32(.322), np.float32(.323), np.float32(.331), np.float32(.321),
            np.float32(.309), np.float32(.301), np.float32(.288), np.float32(.273), np.float32(.260), np.float32(.245),
            np.float32(.215), np.float32(.202), np.float32(.183), np.float32(.169),
            np.float32(.154), np.float32(.145), np.float32(.136), np.float32(.127), np.float32(.123), np.float32(.116),
            np.float32(.108), np.float32(.105), np.float32(.101), np.float32(.0964),
            ]
# IONISATION CO2++

XION7G12 = [np.float32(37.4), np.float32(45.0), np.float32(50.0), np.float32(55.0), np.float32(60.0), np.float32(65.0),
            np.float32(70.0), np.float32(75.0), np.float32(80.0), np.float32(85.0),
            np.float32(90.0), np.float32(95.0), np.float32(100.), np.float32(110.), np.float32(120.), np.float32(140.),
            np.float32(160.), np.float32(180.), np.float32(200.), np.float32(225.),
            np.float32(250.), np.float32(275.), np.float32(300.), np.float32(350.), np.float32(400.), np.float32(450.),
            np.float32(500.), np.float32(550.), np.float32(600.), np.float32(650.),
            np.float32(700.), np.float32(750.), np.float32(800.), np.float32(850.), np.float32(900.), np.float32(950.),
            np.float32(1000.),
            ]
YION7G12 = [np.float32(0.0), np.float32(.00166), np.float32(.00399), np.float32(.00686), np.float32(.0106),
            np.float32(.0126), np.float32(.0159), np.float32(.0172), np.float32(.0206),
            np.float32(.0219),
            np.float32(.0227), np.float32(.0246), np.float32(.0265), np.float32(.0285), np.float32(.0290),
            np.float32(.0294), np.float32(.0290), np.float32(.0285), np.float32(.0272), np.float32(.0257),
            np.float32(.0232), np.float32(.0231), np.float32(.0203), np.float32(.0183), np.float32(.0175),
            np.float32(.0165), np.float32(.0141), np.float32(.0128), np.float32(.0125), np.float32(.0113),
            np.float32(.0106), np.float32(.00986), np.float32(.00961), np.float32(.00883), np.float32(.00823),
            np.float32(.00741), np.float32(.00723),
            ]
# IONISATION C++

XION8G12 = [np.float32(72.0), np.float32(80.0), np.float32(85.0), np.float32(90.0), np.float32(95.0), np.float32(100.),
            np.float32(110.), np.float32(120.), np.float32(140.), np.float32(160.),
            np.float32(180.), np.float32(200.), np.float32(225.), np.float32(250.), np.float32(275.), np.float32(300.),
            np.float32(350.), np.float32(400.), np.float32(450.), np.float32(500.),
            np.float32(550.), np.float32(600.), np.float32(650.), np.float32(700.), np.float32(750.), np.float32(800.),
            np.float32(850.), np.float32(900.), np.float32(950.), np.float32(1000.),
            ]
YION8G12 = [np.float32(0.0), np.float32(.000179), np.float32(.000215), np.float32(.000311), np.float32(.000506),
            np.float32(.000520), np.float32(.000751),
            np.float32(.00108), np.float32(.00157), np.float32(.00186),
            np.float32(.00249), np.float32(.00279), np.float32(.00256), np.float32(.00291), np.float32(.00247),
            np.float32(.00252), np.float32(.00216), np.float32(.00224), np.float32(.00198),
            np.float32(.00177),
            np.float32(.00184), np.float32(.00145), np.float32(.00169), np.float32(.00147), np.float32(.00157),
            np.float32(.00139), np.float32(.00129), np.float32(.000965), np.float32(.000897),
            np.float32(.000984),
            ]
# IONISATION O++

XION9G12 = [np.float32(74.0), np.float32(95.0), np.float32(100.), np.float32(110.), np.float32(120.), np.float32(140.),
            np.float32(160.), np.float32(180.), np.float32(200.), np.float32(225.),
            np.float32(250.), np.float32(275.), np.float32(300.), np.float32(350.), np.float32(400.), np.float32(450.),
            np.float32(500.), np.float32(550.), np.float32(600.), np.float32(650.),
            np.float32(700.), np.float32(750.), np.float32(800.), np.float32(850.), np.float32(900.), np.float32(950.),
            np.float32(1000.),
            ]
YION9G12 = [np.float32(0.0), np.float32(.000169), np.float32(.000197), np.float32(.000324), np.float32(.000721),
            np.float32(.00133), np.float32(.00159),
            np.float32(.00217), np.float32(.00233), np.float32(.00271),
            np.float32(.00286), np.float32(.00304), np.float32(.00276), np.float32(.00249), np.float32(.00215),
            np.float32(.00193), np.float32(.00192), np.float32(.00168), np.float32(.00156),
            np.float32(.00142),
            np.float32(.00176), np.float32(.00147), np.float32(.00127), np.float32(.00127), np.float32(.00100),
            np.float32(.00116), np.float32(.00103),
            ]
# CARBON K-SHELL IONISATION X-SECTION

XKSHCG12 = [np.float32(285.), np.float32(298.), np.float32(307.), np.float32(316.), np.float32(325.), np.float32(335.),
            np.float32(345.), np.float32(365.), np.float32(398.), np.float32(422.),
            np.float32(447.), np.float32(473.), np.float32(501.), np.float32(531.), np.float32(613.), np.float32(668.),
            np.float32(708.), np.float32(750.), np.float32(817.), np.float32(917.),
            np.float32(1000.), np.float32(1122.), np.float32(1296.), np.float32(1496.), np.float32(1679.),
            np.float32(1884.), np.float32(2054.), np.float32(2238.), np.float32(2512.), np.float32(2985.),
            np.float32(3981.), np.float32(5012.), np.float32(7079.), 1.0e4, 1.50e4, 2.05e4, 2.51e4, 3.07e4, 4.10e4,
            5.01e4,
            6.13e4, 7.08e4, 8.18e4, 1.0e5, 1.54e5, 2.05e5, 2.99e5, 4.10e5, 5.01e5,
            6.13e5,
            7.08e5, 8.18e5, 1.0e6, 1.26e6, 1.5e6, 2.05e6, 3.07e6, 4.10e6, 5.01e6,
            6.13e6,
            7.08e6, 8.18e6, 1.0e7, 1.26e7, 1.5e7, 2.05e7, 3.07e7, 4.10e7, 5.01e7,
            6.13e7,
            7.08e7, 8.18e7, 1.0e8, 1.26e8, 1.5e8, 2.05e8, 3.07e8, 4.10e8, 5.01e8,
            6.13e8,
            7.08e8, 8.18e8, 1.0e9,
            ]
YKSHCG12 = [np.float32(0.00), 1.66e-4, 3.48e-4, 5.25e-4, 6.96e-4, 8.63e-4, 1.02e-3,
            1.33e-3, 1.75e-3, 2.01e-3,
            2.24e-3, 2.46e-3, 2.66e-3, 2.84e-3, 3.21e-3, 3.38e-3, 3.47e-3, 3.55e-3,
            3.65e-3, 3.72e-3,
            3.75e-3, 3.74e-3, 3.68e-3, 3.57e-3, 3.45e-3, 3.31e-3, 3.19e-3, 3.07e-3,
            2.91e-3, 2.66e-3,
            2.25e-3, 1.95e-3, 1.55e-3, 1.21e-3, 8.97e-4, 7.07e-4, 6.07e-4, 5.21e-4,
            4.21e-4, 3.63e-4,
            3.14e-4, 2.84e-4, 2.57e-4, 2.25e-4, 1.74e-4, 1.50e-4, 1.28e-4, 1.15e-4,
            1.09e-4, 1.05e-4,
            1.03e-4, 1.02e-4, 1.01e-4, 1.005e-4, 1.01e-4, 1.03e-4, 1.07e-4, 1.11e-4,
            1.14e-4, 1.17e-4,
            1.20e-4, 1.22e-4, 1.25e-4, 1.29e-4, 1.32e-4, 1.38e-4, 1.45e-4, 1.50e-4,
            1.54e-4, 1.58e-4,
            1.60e-4, 1.63e-4, 1.67e-4, 1.71e-4, 1.74e-4, 1.80e-4, 1.87e-4, 1.92e-4,
            1.96e-4, 2.00e-4,
            2.02e-4, 2.05e-4, 2.09e-4,
            ]
# OXYGEN K-SHELL IONISATION X-SECTION (MULTIPLY BY 2 FOR MOLECULE)

XKSHOG12 = [np.float32(532.), np.float32(541.), np.float32(557.), np.float32(574.), np.float32(591.), np.float32(609.),
            np.float32(627.), np.float32(646.), np.float32(665.), np.float32(685.),
            np.float32(706.), np.float32(727.), np.float32(749.), np.float32(793.), np.float32(841.), np.float32(891.),
            np.float32(944.), np.float32(1000.), np.float32(1090.), np.float32(1188.),
            np.float32(1296.), np.float32(1496.), np.float32(1679.), np.float32(1884.), np.float32(2054.),
            np.float32(2238.), np.float32(2512.), np.float32(2985.), np.float32(3981.), np.float32(5012.),
            np.float32(7079.), 1.00e4, 1.50e4, 2.05e4, 2.51e4, 3.07e4, 4.10e4, 5.01e4, 6.13e4,
            7.08e4,
            8.18e4, 1.00e5, 1.54e5, 2.05e5, 2.99e5, 4.10e5, 5.01e5, 6.13e5, 7.08e5,
            8.18e5,
            1.00e6, 1.25e6, 1.50e6, 2.05e6, 3.07e6, 4.10e6, 5.01e6, 6.13e6, 7.08e6,
            8.18e6,
            1.00e7, 1.26e7, 1.50e7, 2.05e7, 3.07e7, 4.10e7, 5.01e7, 6.13e7, 7.08e7,
            8.18e7,
            1.00e8, 1.26e8, 1.50e8, 2.05e8, 3.07e8, 4.10e8, 5.01e8, 6.13e8, 7.08e8,
            8.18e8,
            1.00e9,
            ]
YKSHOG12 = [np.float32(0.00), 3.31e-5, 8.86e-5, 1.42e-4, 1.95e-4, 2.45e-4, 2.94e-4,
            3.41e-4, 3.87e-4, 4.31e-4,
            4.73e-4, 5.14e-4, 5.53e-4, 6.27e-4, 6.95e-4, 7.56e-4, 8.13e-4, 8.63e-4,
            9.29e-4, 9.84e-4,
            1.03e-3, 1.08e-3, 1.10e-3, 1.11e-3, 1.11e-3, 1.10e-3, 1.08e-3, 1.03e-3,
            9.24e-4, 8.27e-4,
            6.81e-4, 5.49e-4, 4.18e-4, 3.35e-4, 2.90e-4, 2.50e-4, 2.04e-4, 1.77e-4,
            1.53e-4, 1.39e-4,
            1.26e-4, 1.11e-4,
            8.62e-5, 7.45e-5, 6.36e-5, 5.75e-5, 5.48e-5, 5.29e-5, 5.20e-5, 5.13e-5,
            5.08e-5, 5.08e-5, 5.12e-5, 5.24e-5, 5.47e-5, 5.68e-5, 5.84e-5, 6.00e-5,
            6.13e-5, 6.26e-5,
            6.44e-5, 6.65e-5, 6.81e-5, 7.11e-5, 7.50e-5, 7.78e-5, 7.97e-5, 8.17e-5,
            8.31e-5, 8.45e-5,
            8.65e-5, 8.87e-5, 9.04e-5, 9.36e-5, 9.75e-5, 1.00e-4, 1.02e-4, 1.04e-4,
            1.06e-4, 1.07e-4,
            1.09e-4,
            ]
# BREMSSTRAHLUNG X-SECTION WITH CUT OFF UNITS 10**-24 CM**2

Z6TG12 = [np.float32(298.), np.float32(178.), np.float32(85.2), np.float32(47.5), np.float32(26.3), np.float32(12.2),
          np.float32(7.06), np.float32(4.45), np.float32(3.06), np.float32(2.82),
          np.float32(2.89), np.float32(2.99), np.float32(3.08), np.float32(3.13), np.float32(3.18), np.float32(3.25),
          np.float32(3.31), np.float32(3.39), np.float32(3.44), np.float32(3.49),
          np.float32(3.52), np.float32(3.54), np.float32(3.55), np.float32(3.57), np.float32(3.57),
          ]
Z8TG12 = [np.float32(477.), np.float32(294.), np.float32(145.), np.float32(81.6), np.float32(45.8), np.float32(21.2),
          np.float32(12.2), np.float32(7.69), np.float32(5.22), np.float32(4.76),
          np.float32(4.84), np.float32(4.99), np.float32(5.10), np.float32(5.20), np.float32(5.27), np.float32(5.38),
          np.float32(5.46), np.float32(5.58), np.float32(5.65), np.float32(5.72),
          np.float32(5.77), np.float32(5.80), np.float32(5.81), np.float32(5.83), np.float32(5.84),
          ]
EBRMG12 = [np.float32(1000.), np.float32(2000.), np.float32(5000.), np.float32(1.E4), np.float32(2.E4),
           np.float32(5.E4), np.float32(1.E5), np.float32(2.E5), np.float32(5.E5), np.float32(1.E6),
           np.float32(2.E6), np.float32(3.E6), np.float32(4.E6), np.float32(5.E6), np.float32(6.E6), np.float32(8.E6),
           np.float32(1.E7), np.float32(1.5E7), np.float32(2.E7), np.float32(3.E7),
           np.float32(4.E7), np.float32(5.E7), np.float32(6.E7), np.float32(8.E7), np.float32(1.E8),
           ]
EBRMG12 = [1000., 2000., 5000., 1.E4, 2.E4, 5.E4, 1.E5, 2.E5, 5.E5, 1.E6,
           2.E6, 3.E6, 4.E6, 5.E6, 6.E6, 8.E6, 1.E7, 1.5E7, 2.E7, 3.E7,
           4.E7, 5.E7, 6.E7, 8.E7, 1.E8]
EING12 = np.zeros(250)
B0G12 = 4.838e-5
# CALC ROTATIONAL TRANSITION ENERGIES
for J in range(0, 60, 2):
    EING12[J] = B0G12 * (4 * (J + 1) + 2)
    EING12[J + 1] = -1 * EING12[J]

EING12[60:144] = [np.float32(-0.08275), np.float32(0.08275), np.float32(-0.15937), np.float32(0.15937),
                  np.float32(-0.17211), np.float32(0.17211), np.float32(-0.251), np.float32(0.251),
                  np.float32(-0.29126), np.float32(0.29126), np.float32(0.335), np.float32(0.422), np.float32(0.505),
                  np.float32(0.685), np.float32(0.825), np.float32(0.995), np.float32(1.160), np.float32(1.320),
                  np.float32(2.500), np.float32(6.50), np.float32(6.75), np.float32(7.00), np.float32(7.25),
                  np.float32(7.50), np.float32(7.75), np.float32(8.00), np.float32(8.25), np.float32(8.50),
                  np.float32(8.75), np.float32(8.89), np.float32(8.90), np.float32(9.15), np.float32(9.40),
                  np.float32(9.65), np.float32(9.90), np.float32(10.15), np.float32(10.7), np.float32(11.048),
                  np.float32(11.3), np.float32(11.385), np.float32(11.543), np.float32(11.608), np.float32(11.683),
                  np.float32(11.758), np.float32(11.826), np.float32(11.971), np.float32(12.142), np.float32(12.301),
                  np.float32(12.469), np.float32(12.627), np.float32(12.75), np.float32(12.901), np.float32(13.01),
                  np.float32(13.15), np.float32(13.28), np.float32(13.39), np.float32(13.51), np.float32(13.68),
                  np.float32(13.78), np.float32(14.0), np.float32(14.25), np.float32(14.5), np.float32(14.75),
                  np.float32(15.0), np.float32(15.25), np.float32(15.5), np.float32(15.75), np.float32(16.0),
                  np.float32(16.25), np.float32(16.5), np.float32(16.75), np.float32(17.0), np.float32(17.25),
                  np.float32(17.5), np.float32(17.75), np.float32(18.0), np.float32(18.25), np.float32(18.50),
                  np.float32(18.75), np.float32(19.0), np.float32(19.25), np.float32(19.50), np.float32(19.75),
                  np.float32(25.0)]
gd['gas12/XEN'] = XENG12
gd['gas12/YMOM'] = YMOMG12
gd['gas12/YEL'] = YELG12
gd['gas12/YVBMOM'] = YVBMOMG12
gd['gas12/YVBEL'] = YVBELG12
gd['gas12/YEPS'] = YEPSG12
gd['gas12/XION1'] = XION1G12
gd['gas12/YION1'] = YION1G12
gd['gas12/XION2'] = XION2G12
gd['gas12/YION2'] = YION2G12
gd['gas12/XION3'] = XION3G12
gd['gas12/YION3'] = YION3G12
gd['gas12/XION4'] = XION4G12
gd['gas12/YION4'] = YION4G12
gd['gas12/XION5'] = XION5G12
gd['gas12/YION5'] = YION5G12
gd['gas12/XION6'] = XION6G12
gd['gas12/YION6'] = YION6G12
gd['gas12/XION7'] = XION7G12
gd['gas12/YION7'] = YION7G12
gd['gas12/XION8'] = XION8G12
gd['gas12/YION8'] = YION8G12
gd['gas12/XION9'] = XION9G12
gd['gas12/YION9'] = YION9G12
gd['gas12/XATT'] = XATTG12
gd['gas12/YATT'] = YATTG12
gd['gas12/XV2'] = XV2G12
gd['gas12/YV2'] = YV2G12
gd['gas12/X2V2'] = X2V2G12
gd['gas12/Y2V2'] = Y2V2G12
gd['gas12/XV1'] = XV1G12
gd['gas12/YV1'] = YV1G12
gd['gas12/X3V2'] = X3V2G12
gd['gas12/Y3V2'] = Y3V2G12
gd['gas12/XV3'] = XV3G12
gd['gas12/YV3'] = YV3G12
gd['gas12/XVPD3'] = XVPD3G12
gd['gas12/YVPD3'] = YVPD3G12
gd['gas12/XV130'] = XV130G12
gd['gas12/YV130'] = YV130G12
gd['gas12/XVPD4'] = XVPD4G12
gd['gas12/YVPD4'] = YVPD4G12
gd['gas12/XVPD5'] = XVPD5G12
gd['gas12/YVPD5'] = YVPD5G12
gd['gas12/XVPD6'] = XVPD6G12
gd['gas12/YVPD6'] = YVPD6G12
gd['gas12/XVPD7'] = XVPD7G12
gd['gas12/YVPD7'] = YVPD7G12
gd['gas12/XVPD8'] = XVPD8G12
gd['gas12/YVPD8'] = YVPD8G12
gd['gas12/XVPD9'] = XVPD9G12
gd['gas12/YVPD9'] = YVPD9G12
gd['gas12/XVPDH'] = XVPDHG12
gd['gas12/YVPDH'] = YVPDHG12
gd['gas12/XTRP1'] = XTRP1G12
gd['gas12/YTRP1'] = YTRP1G12
gd['gas12/XTRP2'] = XTRP2G12
gd['gas12/YTRP2'] = YTRP2G12
gd['gas12/XKSHC'] = XKSHCG12
gd['gas12/YKSHC'] = YKSHCG12
gd['gas12/XKSHO'] = XKSHOG12
gd['gas12/YKSHO'] = YKSHOG12
gd['gas12/Z6T'] = Z6TG12
gd['gas12/Z8T'] = Z8TG12
gd['gas12/EBRM'] = EBRMG12
gd['gas12/EIN'] = EING12

# ENERGY LEVELS OF WATER ( UP TO J=9) IN MILLIVOLTS

ELEVG14 = [0.0, 2.950, 4.604, 5.253, 8.690, 9.856, 11.800, 16.726, 16.882,
           16.956, 17.640, 21.946, 25.578, 26.304, 35.363, 35.387, 27.531, 27.876,
           34.157, 37.240, 39.152, 47.426, 47.590, 60.518, 60.521, 40.338, 40.496,
           49.526, 51.603, 55.360, 62.484, 63.085, 75.645, 75.673, 92.005, 92.006,
           55.383, 55.452, 67.312, 68.552, 74.734, 80.463, 82.022, 93.822, 93.953,
           110.172, 110.176, 129.571, 129.571, 72.685, 72.714, 87.311, 87.98, 97.006,
           101.26, 104.44, 115.03, 115.46, 131.38, 131.40, 150.79, 150.79, 172.94,
           172.94, 92.252, 92.264, 109.46, 109.80, 121.87, 124.74, 130.20, 139.20,
           140.32, 155.62, 155.71, 175.02, 175.02, 197.22, 197.22, 221.81, 221.81,
           114.09, 114.09, 133.79, 133.95, 149.02, 150.79, 159.06, 166.25, 168.65,
           182.87, 183.16, 202.25, 202.27, 224.48, 224.48, 249.18, 249.18, 275.92,
           275.92]
#  J VALUE OF WATER LEVELS

AJLG14 = [0.0, 1.0, 1.0, 1.0, 2.0, 2.0, 2.0, 2.0, 2.0,
          3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 4.0, 4.0,
          4.0, 4.0, 4.0, 4.0, 4.0, 4.0, 4.0, 5.0, 5.0,
          5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0,
          6.0, 6.0, 6.0, 6.0, 6.0, 6.0, 6.0, 6.0, 6.0,
          6.0, 6.0, 6.0, 6.0, 7.0, 7.0, 7.0, 7.0, 7.0,
          7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0,
          7.0, 8.0, 8.0, 8.0, 8.0, 8.0, 8.0, 8.0, 8.0,
          8.0, 8.0, 8.0, 8.0, 8.0, 8.0, 8.0, 8.0, 8.0,
          9.0, 9.0, 9.0, 9.0, 9.0, 9.0, 9.0, 9.0, 9.0,
          9.0, 9.0, 9.0, 9.0, 9.0, 9.0, 9.0, 9.0, 9.0,
          9.0]
#  TRANSITION AMPLITUeES FOR 210 TRANSITIONS

SALPHAG14 = [1.50, 1.259, 1.092, 1.088, 1.101, 2.074, 2.543, 2.166, 2.066,
             2.181,
             3.655, 3.446, 2.037, 4.224, 1.899, 4.218, 5.660, 1.841, 4.140, 1.850,
             .8333, 1.036, 1.083, 1.297, 1.850, 2.025, 2.085, 1.566, 2.494, 2.881,
             1.709, 2.965, 1.778, 1.860, 1.000, 1.500, 2.157, 3.007, 3.977, 4.984,
             5.970, 6.980, 7.990, 1.500, 1.667, 1.971, 2.445, 3.131, 3.970, 4.940,
             2.395, 2.319, 2.322, 2.449, 2.800, 3.290, 3.393, 3.270, 3.153, 3.090,
             3.100, 4.397, 4.267, 4.120, 4.000, 5.400, 5.250, 5.120, 1.244, 2.336,
             3.390, 4.397, 5.400, 6.400, .9225, 2.165, 3.251, 4.265, 5.250, .6050,
             1.840, 3.068, 4.090, .3804, 1.402, 2.750, .2494, 1.090, 0.197, .7557,
             1.744, 2.837, 3.918, 4.965, 5.960, 6.980, 7.990, .3003, .8347, 1.641,
             2.681, 3.710, 4.820, 5.900, 1.550]
# TRANSITION J(INITIAL) VALUES FOR 210 TRANSITIONS

AJING14 = [1.0, 1.0, 2.0, 2.0, 3.0, 3.0, 4.0, 4.0, 5.0, 5.0,
           2.0, 2.0, 3.0, 3.0, 4.0, 4.0, 5.0, 5.0, 3.0, 3.0,
           4.0, 4.0, 5.0, 5.0, 4.0, 4.0, 5.0, 5.0, 5.0, 5.0,
           6.0, 6.0, 7.0, 7.0, 6.0, 6.0, 7.0, 7.0, 7.0, 7.0,
           2.0, 2.0, 3.0, 3.0, 4.0, 4.0, 3.0, 3.0, 4.0, 4.0,
           5.0, 5.0, 6.0, 6.0, 4.0, 4.0, 5.0, 5.0, 6.0, 6.0,
           5.0, 5.0, 6.0, 6.0, 6.0, 6.0, 6.0, 6.0, 0.0, 1.0,
           1.0, 2.0, 2.0, 3.0, 3.0, 4.0, 4.0, 5.0, 5.0, 6.0,
           6.0, 7.0, 7.0, 8.0, 8.0, 9.0, 1.0, 2.0, 2.0, 3.0,
           3.0, 4.0, 4.0, 5.0, 5.0, 6.0, 6.0, 7.0, 7.0, 8.0,
           2.0, 3.0, 3.0, 4.0, 4.0, 5.0, 5.0, 6.0, 6.0, 7.0,
           7.0, 8.0, 3.0, 4.0, 4.0, 5.0, 5.0, 6.0, 6.0, 7.0,
           7.0, 8.0, 4.0, 5.0, 5.0, 6.0, 6.0, 7.0, 7.0, 8.0,
           5.0, 6.0, 6.0, 7.0, 7.0, 8.0, 1.0, 2.0, 2.0, 3.0,
           3.0, 4.0, 4.0, 5.0, 5.0, 6.0, 6.0, 7.0, 2.0, 3.0,
           3.0, 4.0, 4.0, 5.0, 5.0, 6.0, 6.0, 7.0, 3.0, 4.0,
           4.0, 5.0, 5.0, 6.0, 6.0, 7.0, 4.0, 5.0, 5.0, 6.0,
           6.0, 7.0, 5.0, 6.0, 6.0, 7.0, 6.0, 7.0, 1.0, 2.0,
           2.0, 3.0, 3.0, 4.0, 4.0, 5.0, 5.0, 6.0, 6.0, 7.0,
           7.0, 8.0, 8.0, 9.0, 2.0, 3.0, 3.0, 4.0, 4.0, 5.0,
           5.0, 6.0, 6.0, 7.0, 7.0, 8.0, 8.0, 9.0, 6.0, 7.0]
# TRANSITION ENERGIES FOR 210 TRANSITIONS IN MILIVOLTS

EROTG14 = [2.303, 5.082, 9.083, 12.93, 16.33, 3.110, 4.809, 8.439, 12.59,
           4.538,
           4.994, 7.724, 6.626, 5.834, 9.188, 7.423, 7.433, 11.93, 9.695, 14.63,
           6.869, 9.785, 13.09, 7.938, 10.19, 13.16, 16.35, 9.364, 10.88, 13.36,
           11.11, 11.91, 13.10, 17.54, 4.604, 6.906, 8.950, 10.92, 12.97, 15.11,
           17.33, 19.58, 21.84, 11.47, 13.78, 15.75, 17.45, 19.03, 20.67, 22.49,
           18.48, 21.12, 23.33, 25.10, 26.52, 27.74, 25.13, 28.05, 30.74, 33.00,
           34.76, 31.48, 34.50, 37.43, 40.16, 37.56, 40.61, 43.62, 12.28, 18.66,
           25.16, 31.49, 37.57, 43.36, 16.45, 22.01, 28.25, 34.53, 40.62, 21.51,
           25.84, 31.47, 37.58, 27.48, 30.42, 35.00, 34.24, 35.89, 41.55, 4.086,
           7.100, 9.891, 12.46, 14.89, 17.23, 19.54, 21.82, 4.769, 8.579, 12.29,
           15.71, 18.76, 21.48, 23.99, 16.54]
# MAP OF TRANSITION NO TO LEVEL POPULATION

IMAPG14 = [2, 4, 7, 9, 14, 16, 23, 25, 34, 36, 5, 7, 12, 14, 21, 23, 32, 34, 10, 12,
           19, 21, 30, 32, 17, 19, 28, 30, 26, 28, 39, 41, 54, 56, 37, 39, 52, 54, 50, 52,
           6, 8, 13, 15, 22, 24, 11, 13, 20, 22, 31, 33, 44, 46, 18, 20, 29, 31, 42, 44,
           27, 29, 40, 42, 38, 40, 66, 68, 1, 3, 2, 6, 5, 11, 10, 18, 17, 27, 26, 38,
           37, 51, 50, 66, 65, 83, 4, 8, 7, 13, 12, 20, 19, 29, 28, 40, 39, 53, 52, 68,
           9, 15, 14, 22, 21, 31, 30, 42, 41, 55, 54, 70, 16, 24, 23, 33, 32, 44, 43, 57,
           56, 72, 25, 35, 34, 46, 45, 59, 58, 74, 36, 48, 47, 61, 60, 76, 3, 9, 8, 16,
           15, 25, 24, 36, 35, 49, 48, 64, 6, 14, 13, 23, 22, 34, 33, 47, 46, 62, 11, 21,
           20, 32, 31, 45, 44, 60, 18, 30, 29, 43, 42, 58, 27, 41, 40, 56, 38, 54, 3, 5,
           6, 10, 11, 17, 18, 26, 27, 37, 38, 50, 51, 65, 66, 82, 8, 12, 13, 19, 20, 28,
           29, 39, 40, 52, 53, 67, 68, 84, 42, 54]
# ELASTIC MOMENTUM TRANSFER ( NO ROTATION EXCEPT ABOVE 2000EV)

XMTG14 = [.0001, .001, .002, .003, .004, .005, .006, .007, .008, .009,
          0.01, 0.02, 0.03, 0.04, 0.05, 0.06, 0.07, 0.08, 0.09, 0.10,
          0.15, 0.20, 0.25, 0.30, 0.40, 0.50, 0.60, 0.70, 0.80, 0.90,
          1.00, 1.30, 1.50, 2.00, 2.50, 3.00, 4.00, 5.00, 6.00, 7.00,
          8.00, 9.00, 10.0, 12.0, 15.0, 20.0, 25.0, 30.0, 40.0, 60.0,
          80.0, 100., 125., 150., 175., 200., 250., 300., 400., 500.,
          600., 700., 800., 900., 1000., 1250., 1500., 1750., 2000.,
          # ABOVE 2000 EV USE SUM OF ROTATION ANe ELASTIC
          2000.0001,
          2500., 3000., 3500., 4000., 4500., 5000., 6000., 7000., 8000., 9000.,
          1.e4, 1.25e4, 1.5e4, 1.75e4, 2.e4, 2.5e4, 3.e4, 3.5e4, 4.e4, 4.5e4,
          5.e4, 6.e4, 7.e4, 8.e4, 9.e4, 1.e5, 1.25e5, 1.5e5, 1.75e5, 2.e5,
          2.5e5, 3.e5, 3.5e5, 4.e5, 4.5e5, 5.e5, 6.e5, 7.e5, 8.e5, 9.e5,
          1.e6, 1.25e6, 1.5e6, 1.75e6, 2.e6, 2.5e6, 3.e6, 3.5e6, 4.e6, 4.5e6,
          5.e6, 6.e6, 7.e6, 8.e6, 9.e6, 1.e7, 1.25e7, 1.5e7, 1.75e7, 2.e7,
          2.5e7, 3.e7, 3.5e7, 4.e7, 4.5e7, 5.e7, 6.e7, 7.e7, 8.e7, 9.e7,
          1.e8, 1.25e8, 1.5e8, 1.75e8, 2.e8, 2.5e8, 3.e8, 3.5e8, 4.e8, 4.5e8,
          5.e8, 6.e8, 7.e8, 8.e8, 9.e8, 1.e9
          ]
YMTG14 = [38000., 35880., 17360., 11167., 8216., 6392., 5418., 4361.,
          3706., 3237.,
          2842., 1151., 671., 465., 353., 287., 224., 178., 146., 125.,
          70.6, 45.2, 31.0, 22.0, 12.8, 8.30, 6.00, 3.80, 2.70, 2.00,
          1.50, 0.85, 0.85, 1.02, 1.45, 1.95, 2.80, 3.60, 4.30, 4.85,
          5.30, 5.65, 5.95, 6.20, 5.95, 5.15, 4.55, 4.00, 3.30, 2.35,
          1.88, 1.47, 1.21, .951, .772, .642, .466, .356, .228, .160,
          .118, .0908, .0718, .0581, .0479, .0314, .0219, .0159, .0119,
          # ABOVE 2000EV USE SUM OF ROTATION ANe ELASTIC
          .0200,
          .0136, .00990, .00755, .00596, .00484, .00401, .00290, .00220, .00173,
          .00140,
          .00116, 7.74e-4, 5.56e-4, 4.21e-4, 3.31e-4, 2.21e-4, 1.59e-4, 1.21e-4,
          9.5e-5, 7.70e-5,
          6.38e-5, 4.61e-5, 3.51e-5, 2.78e-5, 2.26e-5, 1.88e-5, 1.28e-5, 9.41e-6,
          7.27e-6, 5.82e-6,
          4.04e-6, 3.01e-6, 2.36e-6, 1.91e-6, 1.59e-6, 1.35e-6, 1.02e-6, 8.06e-7,
          6.58e-7, 5.50e-7,
          4.68e-7, 3.35e-7, 2.53e-7, 1.99e-7, 1.61e-7, 1.13e-7, 8.38e-8, 6.51e-8,
          5.21e-8, 4.27e-8,
          3.58e-8, 2.62e-8, 2.01e-8, 1.59e-8, 1.29e-8, 1.07e-8, 7.19e-9, 5.18e-9,
          3.92e-9, 3.07e-9,
          2.04e-9, 1.45e-9, 1.09e-9, 8.49e-10, 6.80e-10, 5.57e-10, 3.94e-10,
          2.93e-10, 2.26e-10, 1.80e-10,
          1.47e-10, 9.46e-11, 6.60e-11, 4.86e-11, 3.73e-11, 2.39e-11, 1.66e-11,
          1.22e-11, 9.36e-12, 7.40e-12,
          5.99e-12, 4.16e-12, 3.06e-12, 2.34e-12, 1.85e-12, 1.50e-12]
# ELASTIC X-SECTION (WITHOUT ROTATION)

XELG14 = [.0001, .001, .002, .003, .004, .005, .006, .007, .008, .009,
          0.01, 0.02, 0.03, 0.04, 0.05, 0.06, 0.07, 0.08, 0.09, 0.10,
          0.15, 0.20, 0.25, 0.30, 0.40, 0.50, 0.60, 0.70, 0.80, 0.90,
          1.00, 1.30, 1.50, 2.00, 2.50, 3.00, 4.00, 5.00, 6.00, 7.00,
          8.00, 9.00, 10.0, 12.0, 15.0, 20.0, 25.0, 30.0, 40.0, 50.0,
          60.0, 70.0, 80.0, 90.0, 100., 125., 150., 175., 200., 250.,
          300., 400., 500., 600., 700., 800., 900., 1000., 1250., 1500.,
          1750., 2000.,
          # ABOVE 2000EV USE ELASTIC + ROTATION
          2000.0001, 2500., 3000., 3500., 4000., 4500., 5000.,
          6000., 7000., 8000., 9000., 1.e4, 1.25e4, 1.5e4, 1.75e4, 2.e4, 2.5e4,
          3.e4, 3.5e4, 4.e4, 4.5e4, 5.e4, 6.e4, 7.e4, 8.e4, 9.e4, 1.e5,
          1.25e5, 1.5e5, 1.75e5, 2.e5, 2.5e5, 3.e5, 3.5e5, 4.e5, 4.5e5, 5.e5,
          6.e5, 7.e5, 8.e5, 9.e5, 1.e6, 1.25e6, 1.5e6, 1.75e6, 2.e6, 2.5e6,
          3.e6, 3.5e6, 4.e6, 4.5e6, 5.e6, 6.e6, 7.e6, 8.e6, 9.e6, 1.e7,
          1.25e7, 1.5e7, 1.75e7, 2.e7, 2.5e7, 3.e7, 3.5e7, 4.e7, 4.5e7, 5.e7,
          6.e7, 7.e7, 8.e7, 9.e7, 1.e8, 1.25e8, 1.5e8, 1.75e8, 2.e8, 2.5e8,
          3.e8, 3.5e8, 4.e8, 4.5e8, 5.e8, 6.e8, 7.e8, 8.e8, 9.e8, 1.e9
          ]
YELG14 = [38000., 35880., 17360., 11200., 8700., 7000., 6000., 5000.,
          4300., 3800.,
          3600., 1630., 1010., 780., 640., 530., 460., 405., 365., 317.,
          215., 150., 112., 83.0, 52.7, 37.0, 28.5, 21.5, 17.0, 13.5,
          10.9, 6.50, 5.00, 2.65, 2.45, 2.60, 3.60, 5.00, 6.00, 7.00,
          8.00, 8.70, 9.20, 9.90, 9.50, 8.80, 7.80, 6.80, 5.60, 4.50,
          4.00, 3.55, 3.20, 2.85, 2.50, 2.05, 1.75, 1.55, 1.40, 1.20,
          1.00, .795, .655, .570, .505, .450, .415, .385, .325, .285,
          .250, .226,
          # ABOVE 2000EV USE ELASTIC + ROTATION
          .336, .275, .234, .203, .180, .161, .146,
          .123, .107, .0940, .0841, .0761, .0617, .0519, .0450, .0397, .0323,
          .0273, .0238, .0211, .0190, .0174, .0149, .0131, .0117, .0107, .00987,
          .00837, .00738, .00667, .00614, .00541, .00493, .00459, .00433, .00414,
          .00399,
          .00377, .00361, .00350, .00342, .00336, .00324, .00318, .00313, .00310,
          .00306,
          .00304, .00302, .00301, .00300, .00300, .00299, .00299, .00298, .00298,
          .00298]
for i in range(30):
    YELG14.append(0.00297)
#
#  OKHRIMOVSKY                 1.0 - EPSILON
#  ANGULAR eISTRIBUTION FUNCTION FOR ELASTIC

XEPSG14 = [.0001, .001, .002, .003, .004, .005, .006, .007, .008, .009,
           0.01, 0.02, 0.03, 0.04, 0.05, 0.06, 0.07, 0.08, 0.09, 0.10,
           0.15, 0.20, 0.25, 0.30, 0.40, 0.50, 0.60, 0.70, 0.80, 0.90,
           1.00, 1.30, 1.50, 2.00, 2.50, 3.00, 4.00, 5.00, 6.00, 7.00,
           8.00, 9.00, 10.0, 12.0, 15.0, 20.0, 25.0, 30.0, 40.0, 60.0,
           80.0, 100., 125., 150., 175., 200., 250., 300., 400., 500.,
           600., 700., 800., 900., 1000., 1250., 1500., 1750., 2000.,
           #
           2000.0001, 2500., 3000., 3500., 4000., 4500., 5000., 6000., 7000.,
           8000., 9000., 1.e4, 1.25e4, 1.5e4, 1.75e4, 2.e4, 2.5e4, 3.e4, 3.5e4,
           4.e4, 4.5e4, 5.e4, 6.e4, 7.e4, 8.e4, 9.e4, 1.e5, 1.25e5, 1.5e5,
           1.75e5, 2.e5, 2.5e5, 3.e5, 3.5e5, 4.e5, 4.5e5, 5.e5, 6.e5, 7.e5,
           8.e5, 9.e5, 1.e6, 1.25e6, 1.5e6, 1.75e6, 2.e6, 2.5e6, 3.e6, 3.5e6,
           4.e6, 4.5e6, 5.e6, 6.e6, 7.e6, 8.e6, 9.e6, 1.e7, 1.25e7, 1.5e7,
           1.75e7, 2.e7, 2.5e7, 3.e7, 3.5e7, 4.e7, 4.5e7, 5.e7, 6.e7, 7.e7,
           8.e7, 9.e7, 1.e8, 1.25e8, 1.5e8, 1.75e8, 2.e8, 2.5e8, 3.e8, 3.5e8,
           4.e8, 4.5e8, 5.e8, 6.e8, 7.e8, 8.e8, 9.e8, 1.e9
           ]
YEPSG14 = [1.00, 1.00, 1.00, .99565, .91672, .87009, .85511, .80970,
           .79461, .77988,
           .69030, .57574, .52106, .43613, .38391, .37247, .31332, .26543, .22829,
           .22313,
           .16735, .14647, .12863, .12046, .10559, .09376, .08536, .06614, .05674,
           .05139,
           .04633, .04315, .06256, .21475, .43086, .63530, .67397, .59438, .58994,
           .55822,
           .51861, .50188, .49846, .47289, .47289, .42300, .42075, .42656, .42787,
           .42573,
           .42573, .42633, .42609, .37461, .32511, .28396, .21779, .18960, .13624,
           .10619,
           .08339, .06771, .05713, .04747, 4.025e-2, 2.844e-2, 2.100e-2, 1.628e-2,
           1.273e-2,
           #
           1.497e-2, 1.172e-2, 9.620e-3, 8.153e-3, 7.066e-3, 6.235e-3, 5.577e-3,
           4.601e-3, 3.914e-3,
           3.404e-3, 3.011e-3, 2.699e-3, 2.141e-3, 1.772e-3, 1.510e-3, 1.315e-3,
           1.043e-3, 8.624e-4, 7.336e-4,
           6.375e-4, 5.631e-4, 5.035e-4, 4.143e-4, 3.507e-4, 3.035e-4, 2.667e-4,
           2.374e-4, 1.848e-4, 1.501e-4,
           1.255e-4, 1.073e-4, 8.205e-5, 6.555e-5, 5.398e-5, 4.540e-5, 3.900e-5,
           3.390e-5, 2.646e-5, 2.135e-5,
           1.765e-5, 1.487e-5, 1.273e-5, 9.143e-6, 6.867e-6, 5.363e-6, 4.309e-6,
           2.967e-6, 2.169e-6, 1.656e-6,
           1.308e-6, 1.059e-6, 8.748e-7, 6.267e-7, 4.711e-7, 3.671e-7, 2.942e-7,
           2.408e-7, 1.574e-7, 1.109e-7,
           8.227e-8, 6.344e-8, 4.103e-8, 2.866e-8, 2.112e-8, 1.620e-8, 1.281e-8,
           1.038e-8, 7.187e-9, 5.257e-9,
           4.004e-9, 3.147e-9, 2.533e-9, 1.596e-9, 1.093e-9, 7.92e-10, 5.99e-10,
           3.76e-10, 2.57e-10, 1.86e-10,
           1.41e-10, 1.10e-10, 8.8e-11, 6.0e-11, 4.4e-11, 3.3e-11, 2.6e-11, 2.1e-11]
# INELASTIC ANGULAR eISTRIBUTION  eIPOLE FORM
# ENERGY IN UNITS OF THE ROTATIONAL ENERGY LEVEL.
# ENRTS FOR SUPER ELASTIC
# ENROT FOR NORMAL ELASTIC

ENRTSG14 = [0.00, 0.01, 0.02, 0.03, 0.04, 0.05, 0.06, 0.07, 0.08, 0.09,
            0.10, 0.11, 0.12, 0.13, 0.14, 0.16, 0.18, 0.20, 0.22, 0.25,
            0.28, 0.31, 0.34, 0.37, 0.40, 0.44, 0.48, 0.52, 0.56, 0.60,
            0.65, 0.70, 0.75, 0.80, 0.90, 1.00, 1.10, 1.20, 1.30, 1.40,
            1.60, 1.80, 2.00, 2.20, 2.40, 2.60, 2.80, 3.00, 3.50, 4.00,
            4.50, 5.00, 5.50, 6.00, 7.00, 8.00, 9.00, 10.0, 11.0, 12.0,
            14.0, 16.0, 18.0, 20.0, 22.0, 25.0, 30.0, 35.0, 40.0, 45.0,
            50.0, 60.0, 70.0, 80.0, 90.0, 100., 120., 140., 160., 180.,
            200., 250., 300., 350., 400., 500., 600., 700., 800., 1000.,
            1200., 1400., 1600., 1800., 2000., 2500., 3000., 3500., 4000., 5000.,
            6000., 7000., 8000., 9000., 10000., 12000., 14000., 16000., 18000., 20000.,
            25000., 30000., 35000., 40000., 50000., 60000., 80000., 1.0e5, 1.5e5,
            2.0e5,
            2.5e5, 3.0e5, 3.5e5, 4.0e5, 5.0e5, 6.0e5, 7.0e5, 8.0e5, 9.0e5, 1.0e6,
            1.2e6, 1.4e6, 1.6e6, 1.8e6, 2.0e6, 2.5e6, 3.0e6, 3.5e6, 4.0e6, 5.0e6,
            6.0e6, 7.0e6, 8.0e6, 9.0e6, 1.0e7
            ]
ENROTG14 = [1.0, 1.01, 1.02, 1.03, 1.04, 1.05, 1.06, 1.07, 1.08, 1.09,
            1.10, 1.11, 1.12, 1.13, 1.14, 1.16, 1.18, 1.20, 1.22, 1.25,
            1.28, 1.31, 1.34, 1.37, 1.40, 1.44, 1.48, 1.52, 1.56, 1.60,
            1.65, 1.70, 1.75, 1.80, 1.90, 2.00, 2.10, 2.20, 2.30, 2.40,
            2.60, 2.80, 3.00, 3.20, 3.40, 3.60, 3.80, 4.00, 4.50, 5.00,
            5.50, 6.00, 6.50, 7.00, 8.00, 9.00, 10.0, 11.0, 12.0, 13.0,
            15.0, 17.0, 19.0, 21.0, 23.0, 26.0, 31.0, 36.0, 41.0, 46.0,
            51.0, 61.0, 71.0, 81.0, 91.0, 101., 121., 141., 161., 181.,
            201., 251., 301., 351., 401., 501., 601., 701., 801., 1001.,
            1201., 1401., 1601., 1801., 2001., 2501., 3001., 3501., 4001., 5001.,
            6001., 7001., 8001., 9001., 10001., 12001., 14001., 16001., 18001., 20001.,
            25001., 30001., 35001., 40001., 50001., 60001., 80001., 1.0e5, 1.5e5,
            2.0e5,
            2.5e5, 3.0e5, 3.5e5, 4.0e5, 5.0e5, 6.0e5, 7.0e5, 8.0e5, 9.0e5, 1.0e6,
            1.2e6, 1.4e6, 1.6e6, 1.8e6, 2.0e6, 2.5e6, 3.0e6, 3.5e6, 4.0e6, 5.0e6,
            6.0e6, 7.0e6, 8.0e6, 9.0e6, 1.0e7]
# OKRIMOVSKKY   1.0-EPSILON

YEPSRG14 = [1.0, .90060, .86030, .83000, .80486, .78309, .76390, .74641,
            .73054, .71571,
            .70205, .68931, .67720, .66584, .65510, .63516, .61705, .60056, .58510,
            .56417,
            .54521, .52802, .51233, .49782, .48448, .46818, .45320, .43962, .42704,
            .41555,
            .40221, .39009, .37891, .36854, .35015, .33409, .32004, .30760, .29649,
            .28657,
            .26933, .25493, .24266, .23212, .22286, .21483, .20763, .20114, .18760,
            .17674,
            .16791, .16044, .15403, .14857, .13951, .13226, .12637, .12143, .11718,
            .11346,
            .10742, .10255, .09859, .09519, .09234, .08867, .08387, .08017, .07716,
            .07465,
            .07252, .06913, .06641, .06426, .06240, .06087, .05833, .05628, .05467,
            .05327,
            .05208, .04973, .04794, .04652, .04534, .04347, .04210, .04096, .04001,
            .03854,
            .03740, .03648, .03570, .03506, .03450, .03336, .03248, .03173, .03115,
            .03021,
            .02946, .02886, .02835, .02792, .02754, .02692, .02641, .02597, .02561,
            .02529,
            .02463, .02411, .02369, .02334, .02277, .02232, .02165, .02115, .02030,
            .01973,
            .01931, .01898, .01870, .01847, .01810, .01780, .01756, .01735, .01718,
            .01702,
            .01675, .01654, .01635, .01620, .01606, .01576, .01553, .01534, .01518,
            .01490,
            .01472, .01456, .01440, .01427, .01418]
# RATIO OF MT/TOT

YMTRTG14 = [0.0, .9336, .9065, .8860, .8689, .8540, .8408, .8287, .8176,
            .8073,
            .7977, .7887, .7801, .7720, .7643, .7499, .7367, .7245, .7131, .6974,
            .6830, .6698, .6576, .6462, .6356, .6225, .6103, .5991, .5886, .5789,
            .5675, .5570, .5472, .5380, .5214, .5066, .4934, .4815, .4707, .4609,
            .4435, .4286, .4156, .4042, .3940, .3850, .3768, .3693, .3533, .3401,
            .3291, .3196, .3113, .3041, .2919, .2819, .2736, .2665, .2603, .2548,
            .2457, .2382, .2320, .2266, .2220, .2160, .2080, .2017, .1965, .1921,
            .1883, .1822, .1772, .1732, .1697, .1668, .1619, .1579, .1547, .1519,
            .1495, .1447, .1410, .1380, .1355, .1315, .1285, .1260, .1239, .1206,
            .1180, .1159, .1141, .1126, .1113, .1086, .1065, .1047, .1033, .1010,
            .09915, .09766, .09640, .09532, .09437, .09277, .09147, .09036, .08941,
            .08858,
            .08686, .08550, .08439, .08345, .08193, .08072, .07889, .07752, .07516,
            .07357,
            .07238, .07144, .07066, .07000, .06892, .06807, .06736, .06676, .06624,
            .06578,
            .06500, .06436, .06381, .06334, .06292, .06204, .06133, .06078, .06027,
            .05944,
            .05889, .05839, .05790, .05749, .05723]
# VIBRATION
#  BENe MOeE 010

XVIB1G14 = [.1977, 0.30, 0.34, 0.39, 0.60, 0.86, 1.00, 2.00, 2.20, 3.00,
            4.00, 5.00, 6.00, 8.00, 10.0, 15.0, 20.0
            ]
YVIB1G14 = [0.00, 1.47, 1.56, 1.51, 0.68, .344, .318, .172, .163, .138,
            .129, .135, .140, .146, .155, .112, .086]
# SUM OF STRETCH MOeES 001 ANe 100

XVIB2G14 = [.4535, 0.53, 0.58, 0.63, 0.80, 1.00, 2.10, 3.00, 4.00, 5.00,
            6.00, 7.00, 7.50, 8.00, 9.00, 10.0, 15.0, 20.0
            ]
YVIB2G14 = [0.00, 1.93, 2.00, 1.95, .516, .430, .275, .267, .331, .370,
            .421, .447, .455, .426, .361, .280, .163, .069]
# SUM OF VIBRATION HARMONICS

XVIB3G14 = [.919, 2.00, 3.00, 4.00, 5.00, 6.00, 7.00, 8.00, 9.00, 10.0,
            15.0, 20.0
            ]
YVIB3G14 = [0.00, .001, .009, .017, .034, .040, .042, .042, .039, .034,
            .017, .009]
#
# IONISATION    ABOVE 5000 EV USE IONISATION OSCILLATOR STRENGTH
#

XIONG14 = [12.617, 13.5, 15.0, 17.5, 20.0, 22.5, 25.0, 30.0, 35.0, 40.0,
           45.0, 50.0, 60.0, 70.0, 80.0, 90.0, 100., 110., 125., 150.,
           175., 200., 250., 300., 400., 500., 600., 700., 800., 900.,
           1000., 1100., 1200., 1300., 1400., 1500., 1600., 1700., 1800., 1900.,
           2000., 2100., 2200., 2300., 2400., 2500., 2600., 2700., 2800., 2900.,
           3000., 3500., 4000., 4500., 5000.]
# COUNTING IONISATION

YIONCG14 = [0.0, .028, .124, .271, .427, .600, .752, 1.017, 1.248, 1.431,
            1.577, 1.701, 1.865, 1.964, 2.052, 2.082, 2.104, 2.094, 2.069, 1.994,
            1.931, 1.860, 1.691, 1.534, 1.315, 1.138, 1.005, 0.893, 0.811, 0.744,
            0.681, 0.634, 0.595, 0.559, 0.528, 0.501, 0.476, 0.454, 0.434, 0.416,
            0.399, 0.384, 0.369, 0.356, 0.344, 0.333, 0.323, 0.313, 0.304, 0.295,
            0.287, 0.253, 0.226, 0.205, 0.1873]
# GROSS IONISATION

YIONGG14 = [0.0, .028, .124, .271, .427, .600, .752, 1.017, 1.248, 1.431,
            1.579, 1.705, 1.875, 1.981, 2.076, 2.111, 2.138, 2.132, 2.111, 2.037,
            1.975, 1.903, 1.732, 1.571, 1.346, 1.163, 1.028, 0.913, 0.829, 0.761,
            0.696, 0.648, 0.608, 0.571, 0.540, 0.512, 0.486, 0.464, 0.444, 0.425,
            0.408, 0.392, 0.377, 0.364, 0.352, 0.340, 0.330, 0.320, 0.311, 0.301,
            0.293, 0.259, 0.231, 0.210, 0.1914]
# IONISATION TO H2O +           ELOSS=12.617 EV

XION1G14 = [12.617, 13.5, 15.0, 17.5, 20.0, 22.5, 25.0, 30.0, 35.0, 40.0,
            45.0, 50.0, 60.0, 70.0, 80.0, 90.0, 100., 110., 125., 150.,
            175., 200., 250., 300., 400., 500., 600., 700., 800., 900.,
            1000.
            ]
YION1G14 = [0.0, .028, .124, .271, .410, .542, .646, .811, .948, 1.047,
            1.117, 1.176, 1.241, 1.271, 1.302, 1.304, 1.305, 1.288, 1.266, 1.214,
            1.168, 1.129, 1.022, 0.932, 0.803, 0.702, 0.625, 0.555, 0.504, 0.466,
            0.429]
# IONISATION TO OH +            ELOSS=18.1 EV

XION2G14 = [18.1, 20.0, 22.5, 25.0, 30.0, 35.0, 40.0, 45.0, 50.0, 60.0,
            70.0, 80.0, 90.0, 100., 110., 125., 150., 175., 200., 250.,
            300., 400., 500., 600., 700., 800., 900., 1000.
            ]
YION2G14 = [0.0, .0145, .0493, .0847, .159, .220, .263, .298, .325, .355,
            .374, .388, .388, .392, .389, .384, .367, .358, .342, .315,
            .294, .253, .216, .191, .173, .159, .145, .132]
# IONISATION TO H +             ELOSS=18.72 EV

XION3G14 = [18.72, 20.0, 22.5, 25.0, 30.0, 35.0, 40.0, 45.0, 50.0, 60.0,
            70.0, 80.0, 90.0, 100., 110., 125., 150., 175., 200., 250.,
            300., 400., 500., 600., 700., 800., 900., 1000.
            ]
YION3G14 = [.0, .0021, .0089, .0194, .0433, .0724, .1068, .1398, .169, .220,
            .255, .284, .301, .312, .317, .315, .309, .303, .291, .265,
            .229, .195, .165, .143, .124, .112, .0997, .0904]
# IONISATION TO O +             ELOSS=21.0 EV

XION4G14 = [21.0, 25.0, 30.0, 35.0, 40.0, 45.0, 50.0, 60.0, 70.0, 80.0,
            90.0, 100., 110., 125., 150., 175., 200., 250., 300., 400.,
            500., 600., 700., 800., 900., 1000.
            ]
YION4G14 = [0.0, .0022, .0037, .0069, .0132, .0206, .0273, .0383, .0456,
            .0538,
            .0587, .0594, .0619, .0617, .0596, .0576, .0550, .0481, .0418, .0332,
            .0282, .0237, .0203, .0181, .0165, .0145]
# IONISATION TO H2 +            ELOSS=23.0

XION5G14 = [23.0, 30.0, 35.0, 40.0, 45.0, 50.0, 60.0, 70.0, 80.0, 90.0,
            100., 110., 125., 150., 175., 200., 250., 300., 400., 500.,
            600., 700., 800., 900., 1000.
            ]
YION5G14 = [0.0, .00018, .00039, .00057, .00070, .00065, .00066, .00069,
            .00063, .00078,
            .00075, .00073, .00064, .00077, .00071, .00054, .00050, .00045, .00040,
            .00032,
            .00029, .00033, .00022, .00032, .00024]
# IONISATION TO (H + ,OH +)     ELOSS=35.4 EV  eOUBLE IONISATION

XION6G14 = [35.4, 40.0, 45.0, 50.0, 60.0, 70.0, 80.0, 90.0, 100., 110.,
            125., 150., 175., 200., 250., 300., 400., 500., 600., 700.,
            800., 900., 1000.
            ]
YION6G14 = [0.0, .00045, .0013, .0034, .0091, .0145, .0188, .0216, .0244,
            .0254,
            .0268, .0266, .0258, .0244, .0226, .0211, .0182, .0155, .0137, .0124,
            .0114, .0105, .0095]
# IONISATION TO (H + ,O +)      ELOSS=45.0 EV  eOUBLE IONISATION

XION7G14 = [45.0, 50.0, 60.0, 70.0, 80.0, 90.0, 100., 110., 125., 150.,
            175., 200., 250., 300., 400., 500., 600., 700., 800., 900.,
            1000.
            ]
YION7G14 = [0.0, .0001, .0011, .0028, .0052, .0076, .0098, .0118, .0144,
            .0158,
            .0160, .0163, .0161, .0139, .0111, .0094, .0079, .0068, .0060, .0055,
            .0048]
# IONISATION TO O ++             ELOSS=70.0 EV  eOUBLE IONISATION

XION8G14 = [70.0, 90.0, 100., 110., 125., 150., 175., 200., 250., 300.,
            400., 500., 600., 700., 800., 900., 1000.
            ]
YION8G14 = [0.0, .00010, .00022, .00049, .00068, .00106, .00165, .00173,
            .00180, .00172,
            .00128, .00108, .00090, .00078, .00069, .00061, .00058]
# OXYGEN ATOM K-SHELL IONISATION X-SECTION

XKSHG14 = [532., 541., 557., 574., 591., 609., 627., 646., 665., 685.,
           706., 727., 749., 793., 841., 891., 944., 1000., 1090., 1188.,
           1296., 1496., 1679., 1884., 2054., 2238., 2512., 2985., 3981., 5012.,
           7079., 1.00e4, 1.50e4, 2.05e4, 2.51e4, 3.07e4, 4.10e4, 5.01e4, 6.13e4,
           7.08e4,
           8.18e4, 1.00e5, 1.54e5, 2.05e5, 2.99e5, 4.10e5, 5.01e5, 6.13e5, 7.08e5,
           8.18e5,
           1.00e6, 1.25e6, 1.50e6, 2.05e6, 3.07e6, 4.10e6, 5.01e6, 6.13e6, 7.08e6,
           8.18e6,
           1.00e7, 1.26e7, 1.50e7, 2.05e7, 3.07e7, 4.10e7, 5.01e7, 6.13e7, 7.08e7,
           8.18e7,
           1.00e8, 1.26e8, 1.50e8, 2.05e8, 3.07e8, 4.10e8, 5.01e8, 6.13e8, 7.08e8,
           8.18e8,
           1.00e9
           ]
YKSHG14 = [0.00, 3.31e-5, 8.86e-5, 1.42e-4, 1.95e-4, 2.45e-4, 2.94e-4,
           3.41e-4, 3.87e-4, 4.31e-4,
           4.73e-4, 5.14e-4, 5.53e-4, 6.27e-4, 6.95e-4, 7.56e-4, 8.13e-4, 8.63e-4,
           9.29e-4, 9.84e-4,
           1.03e-3, 1.08e-3, 1.10e-3, 1.11e-3, 1.11e-3, 1.10e-3, 1.08e-3, 1.03e-3,
           9.24e-4, 8.27e-4,
           6.81e-4, 5.49e-4, 4.18e-4, 3.35e-4, 2.90e-4, 2.50e-4, 2.04e-4, 1.77e-4,
           1.53e-4, 1.39e-4,
           1.26e-4, 1.11e-4,
           8.62e-5, 7.45e-5, 6.36e-5, 5.75e-5, 5.48e-5, 5.29e-5, 5.20e-5, 5.13e-5,
           5.08e-5, 5.08e-5, 5.12e-5, 5.24e-5, 5.47e-5, 5.68e-5, 5.84e-5, 6.00e-5,
           6.13e-5, 6.26e-5,
           6.44e-5, 6.65e-5, 6.81e-5, 7.11e-5, 7.50e-5, 7.78e-5, 7.97e-5, 8.17e-5,
           8.31e-5, 8.45e-5,
           8.65e-5, 8.87e-5, 9.04e-5, 9.36e-5, 9.75e-5, 1.00e-4, 1.02e-4, 1.04e-4,
           1.06e-4, 1.07e-4,
           1.09e-4]
#
# ALL ATTACHMENT  SCALEe BY 10(21)
#    H-  + OH     FEeOR eATA WITH THRESHOLe AT 5.6EV ANe SCALEe TO FIT
#                   THE EXPERIMENTAL ATTACHMENT RATE

XATT1G14 = [5.60, 5.75, 6.00, 6.25, 6.40, 6.50,
            6.75, 7.00, 7.25, 7.50, 7.75, 8.00, 8.25, 8.40, 8.50, 8.75,
            9.00, 9.25, 9.50, 9.75, 10.0, 10.25, 10.5, 10.75, 11.0, 11.25,
            11.50, 11.75, 12.00, 12.25, 12.5, 12.75, 13.0, 13.5, 14.0, 14.5,
            15.0, 15.5
            ]
YATT1G14 = [8.7, 383., 2262., 5368., 5742., 5629.,
            4019., 2314., 1192., 655., 572., 727., 930.9, 1018., 1001., 878.7,
            690., 435., 231., 127., 66.3, 49.0, 43.2, 47.1, 47.1, 49.0,
            47.1, 45.1, 43.2, 41.2, 37.2, 33.5, 27.8, 19.6, 15.5, 11.7,
            8.79, 0.59]
# O-  + H  + H    FEeOR eATA SCALEe TO MELTON ANe CHRISTOPHOROU

XATT2G14 = [6.00, 6.25, 6.50, 6.75, 7.00, 7.25, 7.50, 7.75, 8.00, 8.25,
            8.50, 9.00, 9.50, 10.0, 10.25, 10.5, 10.75, 11.0, 11.25, 11.50,
            11.75, 12.0, 12.25, 12.5, 12.75, 13.0, 13.5, 14.0, 14.5, 15.0
            ]
YATT2G14 = [2.50, 7.20, 17.8, 35.0, 59.0, 45.0, 16.8, 11.5, 22.1, 46.5,
            80.0, 142., 128., 113., 112., 141., 180., 213., 240., 260.,
            269., 268., 243., 221., 188., 151., 81.0, 39.0, 18.5, 4.5]
#  OH-  +   H     FEeOR NORMALISEe TO MELTON

XATT3G14 = [6.00, 6.25, 6.50, 6.75, 7.00, 7.25, 7.50, 7.75, 8.00, 8.25,
            8.50, 8.75, 9.00, 9.25, 9.50, 9.75, 10.0, 10.25, 10.5, 10.75,
            11.0, 11.25, 11.50, 11.75, 12.0, 12.25, 12.5, 12.75
            ]
YATT3G14 = [0.30, 0.70, 1.00, 1.50, 1.45, 0.90, 0.40, 0.30, 0.40, 0.58,
            0.70, 0.70, 0.50, 0.40, 0.25, 0.10, 0.10, 0.30, 0.45, 0.58,
            0.72, 0.80, 0.80, 0.75, 0.65, 0.50, 0.42, 0.25]
# TRIPLET EXCITATIONS

XTRP1G14 = [7.04, 7.50, 8.00, 8.50, 9.00, 10.0, 12.0, 15.0, 20.0, 25.0,
            30.0
            ]
YTRP1G14 = [.0001, .075, 0.15, 0.24, 0.33, 0.23, 0.16, 0.14, 0.11, .087,
            .070
            ]
XTRP2G14 = [9.10, 10.0, 11.0, 12.0, 15.0, 20.0, 25.0, 30.0, 40.0, 50.0
            ]
YTRP2G14 = [.0001, 0.06, 0.12, 0.16, 0.18, 0.15, .122, 0.10, .075, .055
            ]
XTRP3G14 = [9.95, 11.5, 13.0, 15.0, 17.5, 20.0, 25.0, 30.0, 40.0, 50.0
            ]
YTRP3G14 = [.0001, 0.10, .190, .235, .250, .235, .205, .170, .130, .100
            ]
XTRP4G14 = [13.0, 15.0, 16.0, 18.0, 22.0, 26.0, 30.0, 40.0, 50.0
            ]
YTRP4G14 = [.0002, .242, .420, .525, .557, .536, .504, .389, .284]
# BREMSSTRAHLUNG X-SECTION WITH CUT OFF UNITS 10**-24 CM**2

Z8TG14 = [477., 294., 145., 81.6, 45.8, 21.2, 12.2, 7.69, 5.22, 4.76,
          4.84, 4.99, 5.10, 5.20, 5.27, 5.38, 5.46, 5.58, 5.65, 5.72,
          5.77, 5.80, 5.81, 5.83, 5.84
          ]
EBRMG14 = [1000., 2000., 5000., 1.E4, 2.E4, 5.E4, 1.E5, 2.E5, 5.E5, 1.E6,
           2.E6, 3.E6, 4.E6, 5.E6, 6.E6, 8.E6, 1.E7, 1.5E7, 2.E7, 3.E7,
           4.E7, 5.E7, 6.E7, 8.E7, 1.E8]
# FOLLOWING ARE NULL COLLISIONS:
# OH PROeUCTION FROM HARB ET AL J.CHEM.PHYS. 115(2001)5507

XNUL1G14 = [6.60, 10.0, 15.0, 20.0, 30.0, 50.0, 75.0, 100., 150., 200.,
            250., 300.]

YNUL1G14 = [0.0, 0.15, 0.48, 0.75, 1.32, 1.90, 2.10, 2.05, 1.98, 1.75,
            1.60, 1.40]
# OH(A-X) 306-350 NM EMISSION  BEENAKKER ET AL CHEM.PHYS.6(1974)445

XNUL2G14 = [9.20, 10.0, 12.5, 15.0, 17.5, 20.0, 22.5, 25.0, 27.5, 30.0,
            35.0, 40.0, 50.0, 60.0, 70.0, 80.0, 90.0, 100., 120., 140.,
            170., 200., 250., 300., 350., 400., 450., 500., 600., 700.,
            800., 900., 1000.
            ]
YNUL2G14 = [0.00, .0187, .0733, .0919, .0932, .0911, .0845, .0797, .0767,
            .0745,
            .0698, .0663, .0603, .0566, .0535, .0508, .0483, .0464, .0432, .0400,
            .0364, .0339, .0297, .0266, .0240, .0224, .0206, .0196, .0179, .0158,
            .0149, .0131, .0121]
# H ALPHA 3-2   656.3 NM MOHLMANN ANe eEHEER  CHEM.PHYS. 40(1979)157

XNUL3G14 = [18.0, 20.0, 30.0, 40.0, 50.0, 60.0, 70.0, 80.0, 90.0, 100.,
            150., 200., 300., 400., 500., 600., 700., 800., 900., 1000.
            ]
YNUL3G14 = [0.0, .00204, .0105, .0169, .0224, .0291, .0326, .0346, .0354,
            .0355,
            .0311, .0269, .0204, .0162, .0132, .0114, .0101, .00892, .00814, .00734]
# H ALPHA 2-1 121.6 NM ITIKAWA ANe MASON  J.PHYS.CHEM.REF.eATA 34(2005)1
# MORGAN ANe MENTAL BELOW 24 EV

XNUL4G14 = [15.4, 15.6, 24.0, 25.0, 37.5, 50.0, 62.5, 75.0, 87.5, 100.,
            112.5, 125., 137.5, 150., 175., 200., 225., 250.
            ]
YNUL4G14 = [0.0, .0030, .0040, .00601, .0227, .0405, .059, .0727, .0823,
            .0845,
            .0839, .0829, .0812, .0799, .0764, .0733, .0698, .0665]

gd['gas14/XEL'] = XELG14
gd['gas14/YEL'] = YELG14
gd['gas14/XMT'] = XMTG14
gd['gas14/YMT'] = YMTG14
gd['gas14/XEPS'] = XEPSG14
gd['gas14/YEPS'] = YEPSG14
gd['gas14/XVIB1'] = XVIB1G14
gd['gas14/YVIB1'] = YVIB1G14
gd['gas14/XVIB2'] = XVIB2G14
gd['gas14/YVIB2'] = YVIB2G14
gd['gas14/XVIB3'] = XVIB3G14
gd['gas14/YVIB3'] = YVIB3G14
gd['gas14/XION'] = XIONG14
gd['gas14/YIONC'] = YIONCG14
gd['gas14/YIONG'] = YIONGG14
gd['gas14/XION1'] = XION1G14
gd['gas14/YION1'] = YION1G14
gd['gas14/XION2'] = XION2G14
gd['gas14/YION2'] = YION2G14
gd['gas14/XION3'] = XION3G14
gd['gas14/YION3'] = YION3G14
gd['gas14/XION4'] = XION4G14
gd['gas14/YION4'] = YION4G14
gd['gas14/XION5'] = XION5G14
gd['gas14/YION5'] = YION5G14
gd['gas14/XION6'] = XION6G14
gd['gas14/YION6'] = YION6G14
gd['gas14/XION7'] = XION7G14
gd['gas14/YION7'] = YION7G14
gd['gas14/XION8'] = XION8G14
gd['gas14/YION8'] = YION8G14
gd['gas14/XKSH'] = XKSHG14
gd['gas14/YKSH'] = YKSHG14
gd['gas14/XATT1'] = XATT1G14
gd['gas14/YATT1'] = YATT1G14
gd['gas14/XATT2'] = XATT2G14
gd['gas14/YATT2'] = YATT2G14
gd['gas14/XATT3'] = XATT3G14
gd['gas14/YATT3'] = YATT3G14
gd['gas14/XTRP1'] = XTRP1G14
gd['gas14/YTRP1'] = YTRP1G14
gd['gas14/XTRP2'] = XTRP2G14
gd['gas14/YTRP2'] = YTRP2G14
gd['gas14/XTRP3'] = XTRP3G14
gd['gas14/YTRP3'] = YTRP3G14
gd['gas14/XTRP4'] = XTRP4G14
gd['gas14/YTRP4'] = YTRP4G14
gd['gas14/XNUL1'] = XNUL1G14
gd['gas14/YNUL1'] = YNUL1G14
gd['gas14/XNUL2'] = XNUL2G14
gd['gas14/YNUL2'] = YNUL2G14
gd['gas14/XNUL3'] = XNUL3G14
gd['gas14/YNUL3'] = YNUL3G14
gd['gas14/XNUL4'] = XNUL4G14
gd['gas14/YNUL4'] = YNUL4G14
gd['gas14/ENROT'] = ENROTG14
gd['gas14/ENRTS'] = ENRTSG14
gd['gas14/YEPSR'] = YEPSRG14
gd['gas14/YMTRT'] = YMTRTG14
gd['gas14/Z8T'] = Z8TG14
gd['gas14/EBRM'] = EBRMG14
gd['gas14/EROT'] = EROTG14
gd['gas14/AJL'] = AJLG14
gd['gas14/ELEV'] = ELEVG14
gd['gas14/SALPHA'] = SALPHAG14
gd['gas14/AJIN'] = AJING14
gd['gas14/IMAP'] = IMAPG14

#  ELASTIC  X-SECTIONS  ASSUMEe ISOTROPIC BELOW 2.0EV

XELAG15 = [0.00, .001, .003, .005, .007, .010, .015, .020, .025, 0.03,
           0.04, 0.05, 0.06, 0.07, 0.08, 0.09, 0.10, 0.11, 0.12, 0.14,
           0.17, 0.20, 0.30, 0.40, 0.50, 0.60, 0.80, 1.00, 1.20, 1.50,
           2.00, 2.50, 3.00, 4.00, 5.00, 6.00, 8.00, 10.0, 12.0, 15.0,
           20.0, 25.0, 30.0, 40.0, 50.0, 60.0, 80.0, 100., 125., 150.,
           175., 200., 250., 300., 350., 400., 450., 500., 600., 700.,
           800., 900., 1000., 1250., 1500., 1750., 2000., 2500., 3000., 3500.,
           4000., 4500., 5000., 6000., 7000., 8000., 9000., 1.0e4, 1.25e4, 1.5e4,
           1.75e4, 2.0e4, 2.5e4, 3.0e4, 3.5e4, 4.0e4, 4.5e4, 5.0e4, 6.0e4, 7.0e4,
           8.0e4, 9.0e4, 1.0e5, 1.25e5, 1.5e5, 1.75e5, 2.0e5, 2.5e5, 3.0e5, 3.5e5,
           4.0e5, 4.5e5, 5.0e5, 6.0e5, 7.0e5, 8.0e5, 9.0e5, 1.0e6, 1.25e6, 1.5e6,
           1.75e6, 2.0e6, 2.5e6, 3.0e6, 3.5e6, 4.0e6, 4.5e6, 5.0e6, 6.0e6, 7.0e6,
           8.0e6, 9.0e6, 1.0e7, 1.25e7, 1.5e7, 1.75e7, 2.0e7, 2.5e7, 3.0e7, 3.5e7,
           4.0e7, 4.5e7, 5.0e7, 6.0e7, 7.0e7, 8.0e7, 9.0e7, 1.0e8, 1.25e8, 1.5e8,
           1.75e8, 2.0e8, 2.5e8, 3.0e8, 3.5e8, 4.0e8, 4.5e8, 5.0e8, 6.0e8, 7.0e8,
           8.0e8, 9.0e8, 1.0e9
           # ELASTIC MOMENTUM TRANSFER
           ]
YMOMG15 = [0.15, 0.17, 0.18, 0.19, 0.21, 0.24, 0.31, 0.45, 0.70, 1.20,
           2.35, 3.00, 3.40, 3.60, 3.65, 3.70, 3.73, 3.77, 3.79, 3.83,
           3.86, 3.90, 3.95, 4.00, 4.02, 4.21, 4.86, 5.74, 6.44, 6.80,
           6.58, 6.37, 6.05, 5.80, 5.70, 5.65, 5.60, 5.55, 5.50, 5.45,
           5.40, 5.30, 5.15, 4.85, 4.50, 4.10, 3.55, 3.05, 2.43, 1.94,
           1.60, 1.34, .991, .768, .616, .507, .426, .364, .275, .216,
           .175, .145, .122, .0847, .0625, .0481, .0383, .0261, .0190, .0145,
           .0114, .00929, .00770, .00556, .00422, .00332, .00269, .00222, .00149,
           .00107,
           8.10e-4, 6.37e-4, 4.26e-4, 3.07e-4, 2.32e-4, 1.83e-4, 1.48e-4, 1.23e-4,
           8.88e-5, 6.77e-5,
           5.35e-5, 4.36e-5, 3.63e-5, 2.47e-5, 1.81e-5, 1.40e-5, 1.12e-5, 7.79e-6,
           5.81e-6, 4.55e-6,
           3.69e-6, 3.07e-6, 2.61e-6, 1.97e-6, 1.56e-6, 1.27e-6, 1.06e-6, 9.04e-7,
           6.46e-7, 4.88e-7,
           3.84e-7, 3.11e-7, 2.18e-7, 1.62e-7, 1.26e-7, 1.01e-7, 8.26e-8, 6.91e-8,
           5.06e-8, 3.88e-8,
           3.07e-8, 2.50e-8, 2.07e-8, 1.39e-8, 1.00e-8, 7.57e-9, 5.93e-9, 3.94e-9,
           2.81e-9, 2.11e-9,
           1.64e-9, 1.31e-9, 1.08e-9, 7.61e-10, 5.66e-10, 4.38e-10, 3.48e-10,
           2.83e-10, 1.83e-10, 1.27e-10,
           9.39e-11, 7.20e-11, 4.62e-11, 3.21e-11, 2.36e-11, 1.81e-11, 1.43e-11,
           1.16e-11, 8.04e-12, 5.91e-12,
           4.52e-12, 3.57e-12, 2.90e-12]
# ELASTIC

YELAG15 = [0.15, 0.17, 0.18, 0.19, 0.21, 0.24, 0.31, 0.45, 0.70, 1.20,
           2.35, 3.00, 3.40, 3.60, 3.65, 3.70, 3.73, 3.77, 3.79, 3.83,
           3.86, 3.90, 3.95, 4.00, 4.02, 4.21, 4.86, 5.74, 6.44, 6.80,
           6.58, 6.37, 6.21, 6.58, 7.03, 7.48, 7.96, 8.82, 9.31, 9.34,
           9.11, 9.36, 9.15, 8.46, 7.66, 6.85, 5.96, 5.20, 4.50, 3.92,
           3.56, 3.27, 2.84, 2.53, 2.29, 2.09, 1.93, 1.80, 1.59, 1.42,
           1.29, 1.18, 1.09, .910, .784, .689, .614, .506, .430, .374,
           .331, .297, .269, .227, .197, .174, .155, .141, .114, .0961,
           .0832, .0735, .0598, .0506, .0440, .0391, .0352, .0322, .0275, .0242,
           .0217, .0198, .0183, .0155, .0137, .0124, .0114, .0100, .00913, .00850,
           .00803, .00767, .00739, .00698, .00670, .00649, .00634, .00622, .00601,
           .00588,
           .00580, .00574, .00567, .00562, .00560, .00558, .00556, .00555, .00554,
           .00553,
           .00552, .00552, .00552, .00551, .00551, .00551, .00551, .00551, .00551,
           .00551,
           .00551]
for J in range(22):
    YELAG15.append(0.00550)
YEPSG15 = []
for J in range(30):
    YEPSG15.append(1.0)
YEPSG15.extend([1.0000, 1.0000, .96137, .82331, .72073, .64268, .57229, .47655, .42962,
                .42099,
                .43201, .40075, .39681, .40896, .42569, .43895, .43546, .42459, .37079,
                .32162,
                .27516, .23726, .18398, .14816, .12316, .10538, .09155, .08026, .06441,
                .05351,
                .04563, .03969, .03507, .02705, .02196, .01844, .01587, .01240, .010154,
                .008595,
                .007441, .006561, .005865, .004834, .004110, .003572, .003159, .002830,
                .002244, .001857,
                .001582, .001378, .001092, .0009027, .0007678, .0006671, .0005892,
                5.269e-4, 4.335e-4, 3.669e-4,
                3.176e-4, 2.790e-4, 2.484e-4, 1.933e-4, 1.571e-4, 1.313e-4, 1.122e-4,
                8.584e-5, 6.857e-5, 5.647e-5,
                4.759e-5, 4.079e-5, 3.547e-5, 2.768e-5, 2.233e-5, 1.847e-5, 1.556e-5,
                1.331e-5, 9.559e-6, 7.186e-6,
                5.613e-6, 4.510e-6, 3.105e-6, 2.270e-6, 1.734e-6, 1.369e-6, 1.108e-6,
                9.156e-7, 6.559e-7, 4.931e-7,
                3.842e-7, 3.079e-7, 2.520e-7, 1.648e-7, 1.161e-7, 8.6108e-8, 6.6395e-8,
                4.2939e-8, 2.9994e-8, 2.2104e-8,
                1.6952e-8, 1.3407e-8, 1.0856e-8, 7.519e-9, 5.500e-9, 4.188e-9, 3.290e-9,
                2.648e-9, 1.669e-9, 1.142e-9,
                8.28e-10, 6.26e-10, 3.93e-10, 2.68e-10, 1.94e-10, 1.47e-10, 1.15e-10,
                9.1e-11, 6.3e-11, 4.5e-11,
                3.4e-11, 2.7e-11, 2.2e-11])

XROT13G15 = [.00178301, .001986, .002055, .002191, .002395, .002558,
             .002871, .003116, .003442, .003796,
             .004082, .004368, .004626, .004966, .005347, .005823, .006422, .007334,
             .008164, .009524,
             .01088, .01225, .01361, .01497, .01633, .01769, .01905, .02041, .02177,
             .02313,
             .02449, .02585, .02721, .02993, .03265, .03538, .03810, .04082, .04762,
             .05442,
             .06123, .06803, .08164, .09524, .1088, .1225, .1361, .1537, .1796, .2027,
             .2340, .2721, .3129, .3578, .4177, .4830, .5810, .6626, .7837, .9279,
             1.029, 1.105, 1.361]
# NOTE ALL ROTATIONAL X-SECTIONS IN eATA ARRAYS BELOW ARE
#             SCALEe BY 0.75 IN SUBROUTINE

YROT13G15 = [1.e-5, .00476, .00505, .00536, .00545, .00550, .00550,
             .00545, .00524, .00505,
             .00485, .00462, .00481, .00550, .00677, .00944, .0129, .0191, .0235, .0308,
             .0392, .0462, .0532, .0616, .0728, .0826, .0924, .1022, .1148, .1260,
             .1400, .1540, .1680, .1904, .2184, .2464, .2856, .3304, .4200, .5180,
             .6160, .7140, .8960, 1.064, 1.232, 1.358, 1.498, 1.646, 1.826, 1.957,
             2.055, 2.204, 2.248, 2.299, 2.299, 2.220, 2.094, 1.982, 1.851, 1.728,
             1.610, 1.534, 1.263]

XROT35G15 = [.00320941, .003333, .003470, .004055, .004544, .005048,
             .005497, .005769, .006368, .007143,
             .008014, .009347, .01088, .01225, .01361, .01497, .01633, .01769, .01905,
             .02041,
             .02177, .02313, .02449, .02585, .02721, .02993, .03265, .03538, .03810,
             .04082,
             .04762, .05442, .06123, .06803, .08164, .09524, .1088, .1225, .1361, .1537,
             .1796, .2027, .2340, .2721, .3129, .3578, .4177, .4830, .5810, .6626,
             .7837, .9279, 1.029, 1.105, 1.361
             ]
YROT35G15 = [1.e-5, .00196, .00415, .00411, .00407, .00411, .00454,
             .00540, .00767, .01146,
             .01658, .02407, .02940, .03556, .04200, .04900, .05600, .06300, .07000,
             .07700,
             .08540, .09380, .1022, .1120, .1232, .1372, .1568, .1848, .2128, .2324,
             .2940, .3640, .4396, .5236, .6440, .7700, .8820, .9940, 1.064, 1.170,
             1.299, 1.394, 1.462, 1.568, 1.602, 1.635, 1.635, 1.579, 1.490, 1.411,
             1.316, 1.229, 1.145, 1.092, .8988
             ]
XROT57G15 = [.00463581, .004762, .004898, .005170, .005442, .005783,
             .006123, .006803, .007483, .008164,
             .008844, .009524, .01088, .01225, .01361, .01497, .01633, .01769, .01905,
             .02041,
             .02177, .02313, .02449, .02585, .02721, .02993, .03265, .03538, .03810,
             .04082,
             .04762, .05442, .06123, .06803, .08164, .09524, .1088, .1225, .1361, .1537,
             .1796, .2027, .2340, .2721, .3129, .3578, .4177, .4830, .5810, .6626,
             .7837, .9279, 1.029, 1.105, 1.361
             ]
YROT57G15 = [1.e-5, .00280, .00286, .00308, .00330, .00356, .00420,
             .00588, .00812, .01092,
             .01344, .01680, .02296, .02884, .03416, .03920, .04536, .05180, .05880,
             .06580,
             .07280, .08120, .0882, .0952, .1036, .1232, .1400, .1596, .1932, .2100,
             .2839, .3500, .4144, .4844, .6048, .7196, .8316, .9184, 1.011, 1.112,
             1.235, 1.322, 1.389, 1.490, 1.520, 1.554, 1.554, 1.501, 1.414, 1.338,
             1.252, 1.168, 1.089, 1.036, .8540
             ]
XROT79G15 = [.00606221, .006259, .006803, .007483, .008164, .008844,
             .009524, .01088, .01225, .01361,
             .01497, .01633, .01769, .01905, .02041, .02177, .02313, .02449, .02585,
             .02721,
             .02993, .03265, .03538, .03810, .04082, .04762, .05442, .06123, .06803,
             .08164,
             .09524, .1088, .1225, .1361, .1537, .1796, .2027, .2340, .2721, .3129,
             .3578, .4177, .4830, .5810, .6626, .7837, .9279, 1.029, 1.105, 1.361
             ]
YROT79G15 = [1.e-5, .00280, .00350, .00490, .00658, .00840, .01064,
             .01596, .02156, .02632,
             .03080, .03696, .04340, .04900, .05600, .06160, .06860, .07560, .08260,
             .0896,
             .1050, .1260, .1512, .1764, .1988, .2688, .3321, .3940, .4578, .5743,
             .6821, .7899, .8705, .9601, 1.055, 1.170, 1.255, 1.319, 1.413, 1.442,
             1.474, 1.474, 1.423, 1.343, 1.271, 1.186, 1.107, 1.032, .9836, .8095
             ]
XROT911G15 = [.00748861, .007619, .008164, .008844, .009524, .01088,
              .01225, .01361, .01497, .01633,
              .01769, .01905, .02041, .02177, .02313, .02449, .02585, .02721, .02993,
              .03265,
              .03538, .03810, .04082, .04762, .05442, .06123, .06803, .08164, .09524,
              .1088,
              .1225, .1361, .1537, .1796, .2027, .2340, .2721, .3129, .3578, .4177,
              .4830, .5810, .6626, .7837, .9279, 1.029, 1.105, 1.361
              ]
YROT911G15 = [1.e-5, .00280, .00336, .00420, .00546, .00910, .01316,
              .01764, .02100, .02632,
              .03136, .04077, .04200, .04760, .05600, .06160, .06720, .07560, .09240,
              .1148,
              .1344, .1568, .1820, .2436, .3136, .3780, .4379, .5496, .6524, .7557,
              .8330, .9190, 1.010, 1.120, 1.201, 1.261, 1.352, 1.379, 1.410, 1.410,
              1.362, 1.285, 1.216, 1.135, 1.060, .9878, .9411, .7748
              ]
XROT1113G15 = [.00891501, .009456, .009524, .01088, .01225, .01361,
               .01497, .01633, .01769, .01905,
               .02041, .02177, .02313, .02449, .02585, .02721, .02993, .03265, .03538,
               .03810,
               .04082, .04762, .05442, .06123, .06803, .08164, .09524, .1088, .1225,
               .1361,
               .1537, .1796, .2027, .2340, .2721, .3129, .3578, .4177, .4830, .5810,
               .6626, .7837, .9279, 1.029, 1.105, 1.361
               ]
YROT1113G15 = [1.e-5, .00280, .00308, .00616, .01036, .01372, .01736,
               .02156, .02604, .03080,
               .03724, .04200, .04760, .05320, .06020, .06720, .08120, .1036, .1232,
               .1456,
               .1680, .2296, .2884, .3461, .4012, .5034, .5978, .6922, .7630, .8585,
               .9248, 1.026, 1.100, 1.155, 1.238, 1.263, 1.291, 1.291, 1.247, 1.177,
               1.114, 1.040, .9705, .9044, .8621, .7095
               ]
XROT1315G15 = [.01034141, .01061, .01088, .01225, .01361, .01497, .01633,
               .01769, .01905, .02041,
               .02177, .02313, .02449, .02585, .02721, .02993, .03265, .03538, .03810,
               .04082,
               .04762, .05442, .06123, .06803, .08164, .09524, .1088, .1225, .1361, .1537,
               .1796, .2027, .2340, .2721, .3129, .3578, .4177, .4830, .5810, .6626,
               .7837, .9279, 1.029, 1.105, 1.361
               ]
YROT1315G15 = [1.e-5, .00280, .00364, .00700, .01036, .01344, .01708,
               .02100, .02576, .03024,
               .03500, .04060, .04620, .05096, .05712, .07420, .09240, .1120, .1316,
               .1512,
               .2100, .2660, .3192, .3699, .4642, .5513, .6384, .7036, .7762, .8532,
               .9458, 1.014, 1.065, 1.142, 1.165, 1.191, 1.191, 1.151, 1.085, 1.027,
               .9590, .8952, .8341, .7949, .6544
               ]
XROT1517G15 = [.01176781, .01197, .01225, .01361, .01497, .01633, .01769,
               .01905, .02041, .02177,
               .02313, .02449, .02585, .02721, .02993, .03265, .03538, .03810, .04082,
               .04762,
               .05442, .06123, .06803, .08164, .09524, .1088, .1225, .1361, .1537, .1796,
               .2027, .2340, .2721, .3129, .3578, .4177, .4830, .5810, .6626, .7837,
               .9279, 1.029, 1.105, 1.361
               ]
YROT1517G15 = [1.e-5, .00280, .00350, .00560, .00840, .01148, .01512,
               .02044, .02464, .02968,
               .03416, .03780, .04340, .04900, .06300, .08120, .09880, .1176, .1372,
               .1904,
               .2436, .2962, .3433, .4308, .5115, .5923, .6529, .7202, .7916, .8778,
               .9411, .9881, 1.060, 1.081, 1.105, 1.105, 1.068, 1.007, .9531, .8898,
               .8305, .7739, .7378, .6070
               ]
XROT1719G15 = [.01319421, .01333, .01361, .01497, .01633, .01769, .01905,
               .02041, .02177, .02313,
               .02449, .02585, .02721, .02993, .03265, .03538, .03810, .04082, .04762,
               .05442,
               .06123, .06803, .08164, .09524, .1088, .1225, .1361, .1537, .1796, .2027,
               .2340, .2721, .3129, .3578, .4177, .4830, .5810, .6626, .7837, .9279,
               1.029, 1.105, 1.361
               ]
YROT1719G15 = [1.e-5, .00280, .00336, .00518, .00770, .01022, .01400,
               .01764, .02128, .02548,
               .03080, .03556, .04200, .05460, .07000, .08680, .1064, .1274, .1736,
               .2226,
               .2762, .3202, .4018, .4771, .5525, .6090, .6717, .7383, .8187, .8777,
               .9216, .9881, 1.008, 1.031, 1.031, .9957, .9392, .8890, .8299, .7747,
               .7220, .6881, .5663
               ]
XROT1921G15 = [.01462061, .01497, .01633, .01769, .01905, .02041, .02177,
               .02313, .02449, .02585,
               .02721, .02993, .03265, .03538, .03810, .04082, .04762, .05442, .06123,
               .06803,
               .08164, .09524, .1088, .1225, .1361, .1537, .1796, .2027, .2340, .2721,
               .3129, .3578, .4177, .4830, .5810, .6626, .7837, .9279, 1.029, 1.105,
               1.361
               ]
YROT1921G15 = [1.e-5, .00280, .00476, .00678, .01036, .01358, .01680,
               .01988, .02492, .03080,
               .03640, .04760, .06300, .07980, .09800, .1190, .1652, .2128, .2588,
               .3000,
               .3765, .4470, .5176, .5706, .6294, .6918, .7671, .8224, .8635, .9259,
               .9447, .9659, .9659, .9329, .8800, .8329, .7776, .7259, .6765, .6447,
               .5306
               ]
XROT2123G15 = [.01604701, .01633, .01769, .01905, .02041, .02177, .02313,
               .02449, .02585, .02721,
               .02993, .03265, .03538, .03810, .04082, .04762, .05442, .06123, .06803,
               .08164,
               .09524, .1088, .1225, .1361, .1537, .1796, .2027, .2340, .2721, .3129,
               .3578, .4177, .4830, .5810, .6626, .7837, .9279, 1.029, 1.105, 1.361
               ]
YROT2123G15 = [1.e-5, .00280, .00448, .00700, .00980, .01288, .01624,
               .02016, .02464, .02940,
               .03920, .05320, .06720, .08960, .1106, .1554, .2017, .2435, .2822,
               .3541,
               .4206, .4869, .5368, .5921, .6507, .7216, .7736, .8123, .8711, .8887,
               .9086, .9086, .8775, .8280, .7834, .7316, .6829, .6364, .6065, .4992
               ]
XROT2325G15 = [.01747341, .01769, .01905, .02041, .02177, .02313, .02449,
               .02585, .02721, .02993,
               .03265, .03538, .03810, .04082, .04762, .05442, .06123, .06803, .08164,
               .09524,
               .1088, .1225, .1361, .1537, .1796, .2027, .2340, .2721, .3129, .3578,
               .4177, .4830, .5810, .6626, .7837, .9279, 1.029, 1.105, 1.361
               ]
YROT2325G15 = [1.e-5, .00280, .00504, .00784, .01064, .01456, .01904,
               .02380, .02884, .03836,
               .05209, .06580, .08792, .1084, .1523, .1977, .2388, .2768, .3472,
               .4124,
               .4774, .5264, .5807, .6381, .7076, .7585, .7966, .8540, .8714, .8910,
               .8910, .8607, .8117, .7683, .7174, .6695, .6241, .5947, .4894
               ]
XROT2527G15 = [.01889981, .01905, .02041, .02177, .02313, .02449, .02585,
               .02721, .02993, .03265,
               .03538, .03810, .04082, .04762, .05442, .06123, .06803, .08164, .09524,
               .1088,
               .1225, .1361, .1537, .1796, .2027, .2340, .2721, .3129, .3578, .4177,
               .4830, .5810, .6626, .7837, .9279, 1.029, 1.105, 1.361
               ]
YROT2527G15 = [1.e-5, .00280, .00504, .00868, .01288, .01568, .02072,
               .02576, .03752, .05096,
               .06468, .08624, .1064, .1495, .1939, .2342, .2715, .3408, .4046, .4684,
               .5163, .5696, .6261, .6941, .7442, .7815, .8378, .8548, .8742, .8742,
               .8442, .7963, .7538, .7036, .6569, .6121, .5835, .4802
               ]
XROT2729G15 = [.02032621, .02041, .02177, .02313, .02449, .02585, .02721,
               .02993, .03265, .03538,
               .03810, .04082, .04762, .05442, .06123, .06803, .08164, .09524, .1088,
               .1225,
               .1361, .1537, .1796, .2027, .2340, .2721, .3129, .3578, .4177, .4830,
               .5810, .6626, .7837, .9279, 1.029, 1.105, 1.361
               ]
YROT2729G15 = [1.e-5, .00280, .00490, .00980, .01344, .01904, .02296,
               .03360, .04900, .06300,
               .08459, .1044, .1467, .1903, .2299, .2664, .3343, .3970, .4598, .5068,
               .5589, .6143, .6812, .7302, .7669, .8224, .8389, .8576, .8576, .8285,
               .7815, .7398, .6905, .6446, .6009, .5726, .4712
               ]
XROT2931G15 = [.02175261, .02177, .02313, .02449, .02585, .02721, .02993,
               .03265, .03538, .03810,
               .04082, .04762, .05442, .06123, .06803, .08164, .09524, .1088, .1225,
               .1361,
               .1537, .1796, .2027, .2340, .2721, .3129, .3578, .4177, .4830, .5810,
               .6626, .7837, .9279, 1.029, 1.105, 1.361
               ]
YROT2931G15 = [1.e-5, .00280, .00378, .01008, .01456, .01904, .03136,
               .04704, .06104, .08305,
               .1025, .1440, .1868, .2257, .2615, .3282, .3898, .4514, .4976, .5488,
               .6031, .6686, .7168, .7529, .8072, .8235, .8420, .8420, .8134, .7672,
               .7260, .6779, .6328, .5897, .5620, .4626
               ]
XROT3133G15 = [.02317901, .02449, .02585, .02721, .02993, .03265, .03538,
               .03810, .04082, .04762,
               .05442, .06123, .06803, .08164, .09524, .1088, .1225, .1361, .1537, .1796,
               .2027, .2340, .2721, .3129, .3578, .4177, .4830, .5810, .6626, .7837,
               .9279, 1.029, 1.105, 1.361
               ]
YROT3133G15 = [1.e-5, .00280, .00784, .01232, .03080, .04620, .05995,
               .08156, .1007, .1414,
               .1835, .2216, .2568, .3223, .3828, .4432, .4886, .5390, .5922, .6566,
               .7039, .7392, .7927, .8086, .8268, .8268, .7988, .7535, .7132, .6658,
               .6213, .5790, .5519, .4542
               ]
XROT3335G15 = [.02460541, .02585, .02721, .02993, .03265, .03538, .03810,
               .04082, .04762, .05442,
               .06123, .06803, .08164, .09524, .1088, .1225, .1361, .1537, .1796, .2027,
               .2340, .2721, .3129, .3578, .4177, .4830, .5810, .6626, .7837, .9279,
               1.029, 1.105, 1.361
               ]
YROT3335G15 = [1.e-5, .00280, .00518, .02800, .04480, .05656, .07700,
               .09887, .1389, .1802,
               .2177, .2523, .3167, .3760, .4355, .4799, .5258, .5818, .6451, .6916,
               .7263, .7787, .7944, .8123, .8123, .7846, .7400, .7006, .6541, .6104,
               .5690, .5421, .4463
               ]
XROT3537G15 = [.02603181, .02721, .02993, .03265, .03538, .03810, .04082,
               .04762, .05442, .06123,
               .06803, .08164, .09524, .1088, .1225, .1361, .1537, .1796, .2027, .2340,
               .2721, .3129, .3578, .4177, .4830, .5810, .6626, .7837, .9279, 1.029,
               1.105, 1.361
               ]
YROT3537G15 = [1.e-5, .00280, .02576, .04200, .05488, .07566, .09717,
               .1365, .1771, .2139,
               .2479, .3111, .3696, .4278, .4715, .5167, .5718, .6339, .6796, .7137,
               .7652, .7806, .7983, .7983, .7708, .7272, .6882, .6427, .5998, .5592,
               .5328, .4385
               ]
XROT3739G15 = [.02745821, .02857, .02993, .03265, .03538, .03810, .04082,
               .04762, .05442, .06123,
               .06803, .08164, .09524, .1088, .1225, .1361, .1537, .1796, .2027, .2340,
               .2721, .3129, .3578, .4177, .4830, .5810, .6626, .7837, .9279, 1.029,
               1.105, 1.361
               ]
YROT3739G15 = [1.e-5, .00280, .02532, .04127, .05396, .07437, .09551,
               .1342, .1741, .2103,
               .2437, .3058, .3632, .4206, .4634, .5079, .5620, .6230, .6681, .7014,
               .7521, .7675, .7846, .7846, .7577, .7148, .6765, .6317, .5897, .5494,
               .5236, .4309
               ]
XROT3941G15 = [.02888461, .02993, .03265, .03538, .03810, .04082, .04762,
               .05442, .06123, .06803,
               .08164, .09524, .1088, .1225, .1361, .1537, .1796, .2027, .2340, .2721,
               .3129, .3578, .4177, .4830, .5810, .6626, .7837, .9279, 1.029, 1.105,
               1.361
               ]
YROT3941G15 = [1.e-5, .00280, .03780, .05306, .07311, .09391, .1320,
               .1712, .2067, .2396,
               .3007, .3570, .4136, .4556, .4995, .5524, .6126, .6569, .6896, .7395,
               .7546, .7714, .7714, .7451, .7028, .6653, .6210, .5796, .5404, .5149,
               .4236
               ]
XROT4143G15 = [.03031101, .03129, .03265, .03538, .03810, .04082, .04762,
               .05442, .06123, .06803,
               .08164, .09524, .1088, .1225, .1361, .1537, .1796, .2027, .2340, .2721,
               .3129, .3578, .4177, .4830, .5810, .6626, .7837, .9279, 1.029, 1.105,
               1.361
               ]
YROT4143G15 = [1.e-5, .00280, .03500, .05219, .07190, .09237, .1298,
               .1683, .2033, .2357,
               .2957, .3511, .4068, .4480, .4914, .5435, .6026, .6460, .6782, .7272,
               .7420, .7588, .7588, .7328, .6913, .6544, .6110, .5701, .5314, .5065,
               .4166
               ]
XROT4345G15 = [.03173741, .03265, .03538, .03810, .04082, .04762, .05442,
               .06123, .06803, .08164,
               .09524, .1088, .1225, .1361, .1537, .1796, .2027, .2340, .2721, .3129,
               .3578, .4177, .4830, .5810, .6626, .7837, .9279, 1.029, 1.105, 1.361
               ]
YROT4345G15 = [1.e-5, .00280, .05040, .07073, .09086, .1277, .1656,
               .2000, .2318, .2909,
               .3455, .4001, .4407, .4836, .5345, .5928, .6353, .6672, .7154, .7300,
               .7465, .7465, .7210, .6801, .6437, .6009, .5608, .5228, .4981, .4099
               ]
XROT4547G15 = [.03316381, .03402, .03538, .03810, .04082, .04762, .05442,
               .06123, .06803, .08164,
               .09524, .1088, .1225, .1361, .1537, .1796, .2027, .2340, .2721, .3129,
               .3578, .4177, .4830, .5810, .6626, .7837, .9279, 1.029, 1.105, 1.361
               ]
YROT4547G15 = [1.e-5, .00280, .04760, .06961, .08940, .1256, .1630,
               .1968, .2281, .2862,
               .3399, .3937, .4337, .4757, .5261, .5832, .6252, .6566, .7039, .7182,
               .7344, .7344, .7095, .6692, .6334, .5914, .5519, .5144, .4903, .4035
               ]
XROT4749G15 = [.03459021, .03538, .03810, .04082, .04762, .05442, .06123,
               .06803, .08164, .09524,
               .1088, .1225, .1361, .1537, .1796, .2027, .2340, .2721, .3129, .3578,
               .4177, .4830, .5810, .6626, .7837, .9279, 1.029, 1.105, 1.361
               ]
YROT4749G15 = [1.e-5, .00280, .04480, .08800, .1236, .1604, .1937,
               .2246, .2817, .3346,
               .3875, .4270, .4682, .5177, .5740, .6154, .6462, .6930, .7070, .7230,
               .7230, .6983, .6586, .6233, .5821, .5432, .5062, .4824, .3970
               ]
XVIBG15 = [.193, 0.20, 0.21, 0.23, 0.32, 0.33, 0.35, 0.44, 0.45, 0.47,
           0.56, 0.57, 0.59, 0.68, 0.69, 0.71, 0.79, 0.80, 0.82, 0.90,
           0.91, 0.93, 1.02, 1.03, 1.05, 1.13, 1.14, 1.16, 1.23, 1.24,
           1.26, 1.34, 1.35, 1.37, 1.44, 1.45, 1.47, 1.54, 1.55, 1.57,
           1.63, 1.65, 1.67, 3.00, 4.00, 5.00, 6.00, 7.00, 8.00, 9.00,
           9.50, 10.0, 11.0, 12.0, 13.0, 14.0, 15.0, 16.0, 17.0, 18.0
           #
           ]
YVIB1G15 = [0.00, .050, .050, 0.00, 0.00, .800, 0.00, 0.00, 1.00, 0.00,
            0.00, 1.35, 0.00, 0.00, 1.32, 0.00, 0.00, 1.02, 0.00, 0.00,
            .611, 0.00, 0.00, .290, 0.00, 0.00, .115, 0.00, 0.00, .049,
            0.00, 0.00, .017, 0.00, 0.00, .0056, 0.00, 0.00, .0019, 0.00,
            0.00, .0006, 0.00, .027, .033, .055, .115, .220, .321, .412,
            .458, .458, .366, .266, .179, .119, .078, .046, .023, .011
            ]
YVIB2G15 = [0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00,
            0.00, .142, 0.00, 0.00, .422, 0.00, 0.00, .544, 0.00, 0.00,
            .473, 0.00, 0.00, .321, 0.00, 0.00, .204, 0.00, 0.00, .097,
            0.00, 0.00, .041, 0.00, 0.00, .018, 0.00, 0.00, .008, 0.00,
            0.00, .003, 0.00, .0110, .0128, .0220, .0458, .0879, .128, .165,
            .183, .183, .147, .106, .071, .048, .032, .018, .0092, .0046
            ]
YVIB3G15 = [0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00,
            0.00, 0.00, 0.00, 0.00, .0038, 0.00, 0.00, .0219, 0.0, 0.0,
            .092, 0.00, 0.00, .122, 0.00, 0.00, .117, 0.00, 0.00, .097,
            0.00, 0.00, .056, 0.00, 0.00, .031, 0.00, 0.00, .0168, 0.00,
            0.00, .008, 0.00, .0043, .0063, .0108, .0224, .0429, .0627, .0806,
            .090, .090, .0716, .0519, .0349, .0233, .0153, .0090, .0047, .0022
            ]
YVIB4G15 = [0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00,
            0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, .0015, 0.00, 0.0,
            .0056, 0.00, 0.0, .0097, 0.00, 0.0, .0168, 0.00, 0.0, .0321,
            0.00, 0.00, .0341, 0.0, 0.00, .0290, 0.00, 0.0, .0219, 0.00,
            0.00, .0168, 0.00, .00258, .00376, .00645, .0134, .0257, .0376, .0483,
            .0537, .0537, .0429, .0311, .0210, .0139, .0092, .00537, .00269, .00134
            ]
YVIB5G15 = []
for J in range(40):
    YVIB5G15.append(0.0)
YVIB5G15.extend([0.00, 0.00, 0.00, .00172, .00250, .00429, .00895, .0172, .0250, .0323,
                 .0358, .0358, .0287, .0208, .0139, .00931, .00608, .00358, .00179, .00090])
YVIB6G15 = [0.0 for J in range(40)]
YVIB6G15.extend([
    0.0, 0.0, 0.0, .00108, .00157, .00269, .00560, .0108, .0157, .0201,
    .0224, .0224, .0179, .0130, .00873, .00582, .00381, .00224, .00112, .00056
])
YVIB7G15 = [0.0 for J in range(40)]
YVIB7G15.extend([0.0, 0.0, 0.0, .000738, .00108, .00184, .00385, .00738, .0108, .0138,
                 .0154, .0154, .0123, .00891, .00599, .00400, .00261, .00154, .000768,
                 .000385
                 ])
YVIB8G15 = [0.0 for J in range(40)]
YVIB8G15.extend([
    0.0, 0.0, 0.0, .000572, .000833, .00142, .00298, .00572, .00833, .0107,
    .0119, .0119, .00952, .00691, .00464, .00309, .00202, .00119, .000595,
    .000297
])
YVIB9G15 = [0.0 for J in range(40)]
YVIB9G15.extend([
    0.0, 0.0, 0.0, .000459, .000670, .00115, .00239, .00459, .00670, .00858,
    .00956, .00956, .00765, .00555, .00373, .00248, .00163, .000956, .000478,
    .000239
])
YVIB10G15 = [0.0 for J in range(40)]
YVIB10G15.extend([
    0.0, 0.0, 0.0, .000368, .000537, .000921, .00192, .00368, .00537, .00691,
    .00767, .00767, .00614, .00445, .00299, .00199, .00130, .000767, .000384,
    .000192
])
YVIB11G15 = [0.0 for J in range(40)]
YVIB11G15.extend([
    0.0, 0.0, 0.0, .000209, .000304, .000521, .00109, .00209, .00304, .00391,
    .00434, .00434, .00348, .00252, .00170, .00113, .000739, .000434, .000218,
    .000109
])
YVIB12G15 = [0.0 for J in range(40)]
YVIB12G15.extend([
    0.0, 0.0, 0.0, .000153, .000224, .000384, .000799, .00154, .00224, .00288,
    .00319, .00319, .00255, .00185, .00124, .000830, .000543, .000319,
    .000160, .0000799
])
YVIB13G15 = [0.0 for J in range(40)]
YVIB13G15.extend([
    0.0, 0.0, 0.0, .000123, .000179, .000306, .000638, .00122, .00179, .00230,
    .00255, .00255, .00205, .00149, .000996, .000664, .000434, .000255,
    .000127, .0000639
])
YVIB14G15 = [0.0 for J in range(40)]
YVIB14G15.extend([
    0.0, 0.0, 0.0, .000086, .000125, .000215, .000448, .000860, .00125, .00161,
    .00179, .00179, .00143, .00104, .000698, .000466, .000304, .000179,
    .000090, .000045
])
YVIB15G15 = [0.0 for J in range(40)]
YVIB15G15.extend([
    .0, 0.0, 0.0, 6.16e-5, 8.97e-5, .000154, .000321, .000616, .000897, .00115,
    .00128, .00128, .00103, .000744, .000500, .000334, .000218, .000128,
    .000064, .0000321
])
YVIB16G15 = [0.0 for J in range(40)]
YVIB16G15.extend([
    .0, 0.0, 0.0, 5.51e-5, 8.05e-5, .000138, .000287, .000551, .000805, .00104,
    .00115, .00115, .000920, .000666, .000449, .000299, .000195, .000115,
    .0000575, .0000288
])
YVIB17G15 = [0.0 for J in range(40)]
YVIB17G15.extend([
    .0, .0, 0.0, 4.93e-5, 7.19e-5, .000123, .000257, .000493, .000719, .000925,
    .00103, .00103, .000822, .000596, .000401, .000268, .000175, .000103,
    .0000514, .0000257
])
YVIB18G15 = [0.0 for J in range(40)]
YVIB18G15.extend([
    .0, .0, 0.0, 4.34e-5, 6.34e-5, .000109, .000227, .000434, .000634, .000815,
    .000906, .000906, .000724, .000525, .000353, .000235, .000154, .0000906,
    .0000453, .0000226
])
YVIB19G15 = [0.0 for J in range(40)]
YVIB19G15.extend([
    .0, .0, 0.0, 3.66e-5, 5.34e-5, 9.16e-5, .000191, .000366, .000534, .000687,
    .000763, .000763, .000611, .000443, .000297, .000198, .000129, .0000763,
    .0000382, .0000191
])
YVIB20G15 = [0.0 for J in range(40)]
YVIB20G15.extend([
    .0, .0, 0.0, 3.07e-5, 4.49e-5, 7.69e-5, .000160, .000307, .000449, .000577,
    .000641, .000641, .000513, .000371, .000250, .000167, .000109, .0000641,
    .0000321, .0000160
])
YVIB21G15 = [0.0 for J in range(40)]
YVIB21G15.extend([
    0.0, 0.0, 0.0, .000116, .000170, .000292, .000607, .00117, .00170, .00219,
    .00243, .00243, .00194, .00141, .000948, .000632, .000413, .000243,
    .000121, .0000607])
# USEe RAPP NORMALISEe TO LINeSAY AT MAXIMUM (110EV)  THEN ABOVE
# MAXIMUM USEe LINeSAY TO 1KEV THEN NORMALISEe SCHRAM TO 16KEV
# THEN MATRIX ELEMENTS FROM RIEKE ANe BERKOWITZ ANALYSIS
# NB.ALL CROSS SECTIONS AeJUSTEe TO GIVE COUNTING IONISATION.
XIONCG15 = [12.071, 12.5, 13.0, 13.5, 14.0, 14.5, 15.0, 15.5, 16.0, 16.5,
            17.0, 17.5, 18.0, 18.5, 19.0, 19.5, 20.0, 20.5, 21.0, 21.5,
            22.0, 24.0, 26.0, 28.0, 30.0, 32.0, 34.0, 36.0, 40.0, 45.0,
            50.0, 55.0, 60.0, 65.0, 70.0, 75.0, 80.0, 85.0, 90.0, 95.0,
            100., 108., 118., 138., 158., 178., 198., 223., 248., 273.,
            298., 348., 398., 448., 498., 548., 598., 648., 698., 748.,
            798., 848., 898., 948., 998., 1200., 1400., 1600., 1800., 2000.,
            2500., 3000., 3500., 4000., 4500., 5000., 5500., 6000., 7000., 8000.,
            9000., 10000., 12000., 14000., 16000]
# COUNTING IONISATION

YIONCG15 = [0.0, .0052, .0117, .024, .034, .047, .061, .073, .087, .105,
            .124, .143, .164, .184, .205, .225, .247, .269, .290, .312,
            .336, .435, .538, .641, .754, .873, .981, 1.09, 1.26, 1.49,
            1.69, 1.84, 1.97, 2.07, 2.16, 2.23, 2.28, 2.34, 2.37, 2.40,
            2.42, 2.45, 2.45, 2.42, 2.40, 2.34, 2.28, 2.19, 2.12, 2.01,
            1.94, 1.80, 1.68, 1.56, 1.46, 1.38, 1.30, 1.24, 1.19, 1.12,
            1.06, 1.03, .987, .950, .922, .805, .718, .645, .587, .540,
            .457, .393, .347, .310, .284, .262, .240, .224, .196, .178,
            .162, .149, .127, .112, .101]
# IONISATION TO O2+   ASYMPTOTIC 64.75% OF COUNTING IONISATION

XION1G15 = [12.071, 12.5, 13.0, 13.5, 14.0, 14.5, 15.0, 15.5, 16.0, 16.5,
            17.0, 17.5, 18.0, 18.5, 19.0, 19.5, 20.0, 20.5, 21.0, 21.5,
            22.0, 24.0, 26.0, 28.0, 30.0, 32.0, 34.0, 36.0, 40.0, 45.0,
            50.0, 55.0, 60.0, 65.0, 70.0, 75.0, 80.0, 85.0, 90.0, 95.0,
            100., 108., 118., 138., 158., 178., 198., 223., 248., 273.,
            298., 348., 398., 448., 498., 548., 598., 648., 698., 748.,
            798., 848., 898., 948., 998., 1200., 1400., 1600., 1800., 2000.,
            2500., 3000., 3500., 4000., 4500., 5000., 5500., 6000., 7000., 8000.,
            9000., 10000., 12000., 14000., 16000.
            ]
YION1G15 = [0.0, .0052, .0117, .024, .034, .047, .061, .073, .087, .105,
            .124, .143, .164, .184, .205, .225, .247, .269, .288, .306,
            .326, .406, .486, .563, .640, .723, .795, .872, .980, 1.12,
            1.25, 1.32, 1.39, 1.43, 1.47, 1.50, 1.51, 1.53, 1.53, 1.53,
            1.54, 1.54, 1.53, 1.50, 1.48, 1.53, 1.39, 1.34, 1.31, 1.24,
            1.20, 1.13, 1.05, .983, .923, .882, .827, .800, .761, .720,
            .686, .671, .643, .617, .597, .522, .465, .418, .380, .350,
            .296, .255, .225, .201, .184, .170, .155, .145, .127, .115,
            .105, .0965, .0823, .0726, .0654]
# SINGLE IONISATION TO O+ ASYMPTOTIC 29.93% OF COUNTING IONISATION

XION2G15 = [20.701, 21.0, 21.5, 22.0, 22.5, 23.0, 24.0, 26.0, 28.0, 30.0,
            32.0, 34.0, 36.0, 40.0, 45.0, 50.0, 55.0, 60.0, 65.0, 70.0,
            75.0, 80.0, 85.0, 90.0, 95.0, 100., 108., 118., 138., 158.,
            178., 198., 223., 248., 273., 298., 348., 398., 448., 498.,
            548., 598., 648., 698., 748., 798., 848., 898., 948., 998.,
            1200., 1400., 1600., 1800., 2000., 2500., 3000., 3500., 4000., 4500.,
            5000., 5500., 6000., 7000., 8000., 9000., 10000., 12000., 14000., 16000.
            ]
YION2G15 = [0.0, .00218, .00582, .0094, .0131, .0167, .0287, .0531, .0781,
            .114,
            .151, .186, .222, .281, .353, .428, .486, .541, .593, .633,
            .661, .692, .723, .741, .758, .767, .785, .786, .780, .770,
            .759, .736, .709, .680, .648, .620, .570, .530, .490, .459,
            .426, .398, .376, .361, .338, .321, .309, .292, .284, .276,
            .241, .215, .193, .176, .162, .137, .118, .104, .0928, .0850,
            .0784, .0718, .0670, .0587, .0533, .0485, .0446, .0380, .0335, .0302]
# eOUBLE IONISATION TO O+ + O+ FROM  TIAN ANe VIeAL
# ASYMPTOTIC EXTENSION  4.46% OF COUNTING IONISATION.

XION3G15 = [38.46, 45.0, 50.0, 60.0, 70.0, 80.0, 90.0, 100., 125., 150.,
            175., 200., 225., 250., 275., 300., 350., 400., 450., 500.,
            550., 600., 650., 700., 750., 800., 850., 900., 950., 1000.,
            1200., 1400., 1600., 1800., 2000., 2500., 3000., 3500., 4000., 4500.,
            5000., 5500., 6000., 7000., 8000., 9000., 10000., 12000., 14000., 16000.
            ]
YION3G15 = [0.0, .0099, .0207, .0409, .0615, .0793, .0966, .110, .129, .136,
            .132, .128, .121, .113, .106, .100, .0885, .0804, .0718, .0667,
            .0607, .0592, .0560, .0538, .0504, .0478, .0460, .0435, .0423, .0411,
            .0359, .0320, .0288, .0262, .0241, .0204, .0176, .0155, .0138, .0127,
            .0117, .0107, .00998, .00875, .00794, .00723, .00665, .00566, .00499,
            .00450]
# eOUBLE IONISATION TO O++ + O   FROM TIAN ANe VIeAL ANe LINeSAY
# ASYMTOTIC EXTENSION 0.61% OF COUNTING IONISATION

XION4G15 = [68.0, 70.0, 80.0, 90.0, 100., 125., 150., 175., 200., 225.,
            250., 275., 300., 350., 400., 450., 500., 550., 600., 650.,
            700., 750., 800., 850., 900., 950., 1000., 1200., 1400., 1600.,
            1800., 2000., 2500., 3000., 3500., 4000., 4500., 5000., 5500., 6000.,
            7000., 8000., 9000., 10000., 12000., 14000., 16000.
            ]
YION4G15 = [0.0, .000561, .00176, .00453, .00568, .0106, .0128, .0141,
            .0152, .0149,
            .0144, .0140, .0129, .0122, .0113, .0103, .00932, .00837, .00805, .00762,
            .00732, .00685, .00650, .00626, .00592, .00575, .00559, .00488, .00435,
            .00392,
            .00356, .00328, .00277, .00239, .00211, .00188, .00173, .00159, .00146,
            .00136,
            .00119, .00108, .000983, .000904, .000770, .000679, .000612]
# TREBLE IONISATION TO  O++ + O+  FROM TIAN ANe VIeAL
# ASYMPTOTIC EXTENSION 0.25% OF COUNTING IONISATION

XION5G15 = [90.0, 100., 125., 150., 175., 200., 225., 250., 275., 300.,
            350., 400., 450., 500., 550., 600., 650., 700., 750., 800.,
            850., 900., 950., 1000., 1200., 1400., 1600., 1800., 2000., 2500.,
            3000., 3500., 4000., 4500., 5000., 5500., 6000., 7000., 8000., 9000.,
            10000., 12000., 14000., 16000.
            ]
YION5G15 = [0.0, .000565, .00248, .00466, .00619, .00712, .00761, .00763,
            .00733, .00711,
            .00627, .00554, .00477, .00414, .00371, .00329, .00311, .00299, .00280,
            .00266,
            .00256, .00242, .00235, .00228, .00199, .00178, .00160, .00145, .00134,
            .00113,
            .000977, .000862, .000768, .000707, .000650, .000597, .000556, .000486,
            .000441, .000402,
            .000369, .000315, .000278, .000250]
# OXYGEN K-SHELL IONISATION X-SECTION (MULTIPLY BY 2 FOR MOLECULE)

XKSHG15 = [532., 541., 557., 574., 591., 609., 627., 646., 665., 685.,
           706., 727., 749., 793., 841., 891., 944., 1000., 1090., 1188.,
           1296., 1496., 1679., 1884., 2054., 2238., 2512., 2985., 3981., 5012.,
           7079., 1.00e4, 1.50e4, 2.05e4, 2.51e4, 3.07e4, 4.10e4, 5.01e4, 6.13e4,
           7.08e4,
           8.18e4, 1.00e5, 1.54e5, 2.05e5, 2.99e5, 4.10e5, 5.01e5, 6.13e5, 7.08e5,
           8.18e5,
           1.00e6, 1.25e6, 1.50e6, 2.05e6, 3.07e6, 4.10e6, 5.01e6, 6.13e6, 7.08e6,
           8.18e6,
           1.00e7, 1.26e7, 1.50e7, 2.05e7, 3.07e7, 4.10e7, 5.01e7, 6.13e7, 7.08e7,
           8.18e7,
           1.00e8, 1.26e8, 1.50e8, 2.05e8, 3.07e8, 4.10e8, 5.01e8, 6.13e8, 7.08e8,
           8.18e8,
           1.00e9
           ]
YKSHG15 = [0.00, 3.31e-5, 8.86e-5, 1.42e-4, 1.95e-4, 2.45e-4, 2.94e-4,
           3.41e-4, 3.87e-4, 4.31e-4,
           4.73e-4, 5.14e-4, 5.53e-4, 6.27e-4, 6.95e-4, 7.56e-4, 8.13e-4, 8.63e-4,
           9.29e-4, 9.84e-4,
           1.03e-3, 1.08e-3, 1.10e-3, 1.11e-3, 1.11e-3, 1.10e-3, 1.08e-3, 1.03e-3,
           9.24e-4, 8.27e-4,
           6.81e-4, 5.49e-4, 4.18e-4, 3.35e-4, 2.90e-4, 2.50e-4, 2.04e-4, 1.77e-4,
           1.53e-4, 1.39e-4,
           1.26e-4, 1.11e-4,
           8.62e-5, 7.45e-5, 6.36e-5, 5.75e-5, 5.48e-5, 5.29e-5, 5.20e-5, 5.13e-5,
           5.08e-5, 5.08e-5, 5.12e-5, 5.24e-5, 5.47e-5, 5.68e-5, 5.84e-5, 6.00e-5,
           6.13e-5, 6.26e-5,
           6.44e-5, 6.65e-5, 6.81e-5, 7.11e-5, 7.50e-5, 7.78e-5, 7.97e-5, 8.17e-5,
           8.31e-5, 8.45e-5,
           8.65e-5, 8.87e-5, 9.04e-5, 9.36e-5, 9.75e-5, 1.00e-4, 1.02e-4, 1.04e-4,
           1.06e-4, 1.07e-4,
           1.09e-4]
# BREMSSTRAHLUNG X-SECTION WITH CUT OFF UNITS 10**-24 CM**2

Z8TG15 = [477., 294., 145., 81.6, 45.8, 21.2, 12.2, 7.69, 5.22, 4.76,
          4.84, 4.99, 5.10, 5.20, 5.27, 5.38, 5.46, 5.58, 5.65, 5.72,
          5.77, 5.80, 5.81, 5.83, 5.84
          ]
EBRMG15 = [1000., 2000., 5000., 1.E4, 2.E4, 5.E4, 1.E5, 2.E5, 5.E5, 1.E6,
           2.E6, 3.E6, 4.E6, 5.E6, 6.E6, 8.E6, 1.E7, 1.5E7, 2.E7, 3.E7,
           4.E7, 5.E7, 6.E7, 8.E7, 1.E8]
#  THREE BOeY ATTACHMENT
#  TABLE IN UNITS OF 10**-16 FOR P=760 TORR ANe T=20 CELSIUS

X3ATTG15 = [0.058, .065, .073, .083, .089, .095, .103, .109, 0.20, 0.21,
            0.23, 0.32, 0.33, 0.35, 0.44, 0.45, 0.47, 0.56, 0.57, 0.59,
            0.68, 0.69, 0.71, 0.79, 0.80, 0.82, 0.90, 0.91, 0.93, 1.02,
            1.03, 1.05
            ]
Y3ATTG15 = [.000, .0704, .1394, .4477, .1042, .2091, .4477, .000, .000,
            .0934,
            .000, .000, .0602, .000, .000, .0380, .000, .000, .0288, .000,
            .000, .0210, .000, .000, .0184, .000, .000, .0144, .000, .000,
            .0110, .000]
#  eISSOCIATIVE ATTACHMENT    RAPP ANe BRIGLIA
#    SCALEe BY *0.72 ANe ENERGY OFFSET BY -0.3EV

XATTG15 = [3.90, 4.10, 4.30, 4.50, 4.70, 4.90, 5.10, 5.30, 5.50, 5.70,
           5.90, 6.00, 6.10, 6.20, 6.30, 6.40, 6.50, 6.70, 6.90, 7.10,
           7.30, 7.50, 7.70, 7.90, 8.10, 8.30, 8.50, 8.70, 9.10, 9.70,
           11.7
           ]
YATTG15 = [0.00, .000187, .000504, .000950, .00158, .00259, .00386,
           .00538, .00690, .00821,
           .00943, .00979, .01008, .01015, .01008, .00986, .00965, .00864, .00763,
           .00646,
           .00531, .00411, .00323, .00240, .00171, .00120, .000886, .000634, .000382,
           .000202, .000072
           #  EXCITATION TO VIBRATIONALLY SUMMEe A1 eELTA G   ALLAN 1995
           # SCALEe BY 1/E**2 ABOVE 40 EV
           ]
XEXC1G15 = [.977, 0.982, 1.20, 1.50, 2.00, 2.50, 3.00, 3.50, 4.00, 4.50,
            5.00, 5.50, 6.00, 6.50, 7.00, 7.50, 8.00, 8.50, 9.00, 9.50,
            10.0, 10.5, 11.0, 11.5, 12.0, 12.5, 13.0, 13.5, 14.0, 15.0,
            16.0, 17.0, 18.0, 20.0, 22.0, 25.0, 28.0, 31.0, 35.0, 40.0
            ]
YEXC1G15 = [0.00, .00102, .00407, .00712, .0122, .0168, .0265, .0397,
            .0539, .0661,
            .0783, .0906, .0977, .0997, .0987, .0967, .0936, .0906, .0865, .0834,
            .0794, .0763, .0743, .0722, .0692, .0682, .0651, .0621, .0605, .0539,
            .0488, .0448, .0407, .0346, .0305, .0249, .0214, .0188, .0153, .0122]
#  EXCITATION TO VIBRATIONALLY SUMMEe  B1 SIGMA G+  ALLAN 1995
# SCALEe BY 1/E**2 ABOVE 17 EV

XEXC2G15 = [1.627, 1.640, 2.00, 2.50, 3.00, 3.50, 4.00, 4.50, 5.00, 5.50,
            6.00, 6.50, 7.00, 7.50, 8.00, 8.50, 9.00, 9.50, 10.0, 10.5,
            11.0, 12.0, 13.0, 14.0, 15.0, 17.0, 20.0, 25.0, 30.0, 35.0,
            40.0
            ]
YEXC2G15 = [0.0, .00102, .00214, .00407, .00651, .00916, .0116, .0153,
            .0198, .0234,
            .0254, .0244, .0224, .0214, .0204, .0193, .0188, .0183, .0178, .0173,
            .0168, .0163, .0153, .0148, .0142, .0132, .0112, .00906, .00733, .00631,
            .00519]
# EXCITATION SUM OF C1SIGMA A!3eELTA ANe A3SIGMA  HERZBERG CONTINUUM
# SPLIT INTO THREE ENERGY LOSSES AT 5.5 6.0 ANe 6.5 EV
# PART1

XEXC3G15 = [5.50, 6.00, 6.50, 7.00, 7.50, 8.00, 9.00, 10.0, 11.0, 12.0,
            14.0, 16.0, 18.0, 20.0, 30.0, 45.0
            ]
YEXC3G15 = [0.00, .0224, .0224, .0244, .0285, .0305, .0356, .0366, .0366,
            .0356,
            .0326, .0305, .0295, .0265, .0163, .0116]
# PART 2

XEXC4G15 = [6.00, 6.50, 7.00, 7.50, 8.00, 9.00, 10.0, 11.0, 12.0, 14.0,
            16.0, 18.0, 20.0, 30.0, 45.0
            ]
YEXC4G15 = [0.00, .0448, .0549, .0560, .0611, .0712, .0733, .0733, .0733,
            .0672,
            .0631, .0590, .0539, .0315, .0234]
# PART 3

XEXC5G15 = [6.50, 7.00, 7.50, 8.00, 9.00, 10.0, 11.0, 12.0, 14.0, 16.0,
            18.0, 20.0, 30.0, 45.0
            ]
YEXC5G15 = [0.00, .0183, .0254, .0305, .0356, .0366, .0366, .0356, .0326,
            .0305,
            .0295, .0265, .0163, .0116]
# SUM OF TRIPLET STATES AT 8.20 EV ANe RESONANT PART OF S-R CONTINUUM

XEXC6G15 = [8.20, 10.0, 11.0, 12.0, 13.0, 15.0, 17.0, 20.0, 23.0, 27.0,
            30.0, 40.0, 50.0, 80.0
            ]
YEXC6G15 = [0.00, 0.21, 0.36, 0.46, 0.50, 0.52, 0.52, 0.46, 0.39, 0.32,
            0.29, 0.24, .205, .135]
# RESONANT PART OF LONG BANe

XEXC7G15 = [9.972, 11.0, 12.0, 14.0, 16.0, 18.0, 20.0, 24.0, 28.0, 32.0,
            36.0, 40.0, 60.0, 80.0
            ]
YEXC7G15 = [0.00, .022, .038, .050, .053, .055, .056, .051, .042, .035,
            .030, .026, .017, .013]
# TRIPLET STATE SUM BELOW IONISATION

XEXC8G15 = [10.6, 12.0, 13.0, 14.0, 16.0, 18.0, 20.0, 24.0, 28.0, 32.0,
            36.0, 40.0, 50.0, 60.0, 80.0
            ]
YEXC8G15 = [0.0, .0878, .130, .145, .159, .169, .173, .156, .135, .111,
            .097, .087, .067, .055, .040]
# TRIPLET STATE SUM ABOVE IONISATION

XEXC9G15 = [13.1, 14.0, 15.0, 16.0, 18.0, 20.0, 24.0, 28.0, 32.0, 36.0,
            40.0, 50.0, 60.0, 80.0
            ]
YEXC9G15 = [0.0, .0658, .122, .142, .157, .169, .174, .163, .146, .125,
            .111, .087, .073, .054]
# ROTATIONAL RESONANCE FROM VIBRATIONS (PHELPS)

XROTG15 = [.020, .021, .025, 0.07, 0.08, 0.10, 0.20, 0.21, 0.22, 0.32,
           0.33, 0.35, 0.44, 0.45, 0.47, 0.56, 0.57, 0.59, 0.68, 0.69,
           0.71, 0.79, 0.80, 0.82, 0.90, 0.91, 0.93, 1.02, 1.03, 1.05,
           1.13, 1.14, 1.16, 1.23, 1.24, 1.26, 1.34, 1.35, 1.37, 1.44,
           1.45, 1.47, 1.54, 1.55, 1.57, 1.64, 1.65, 1.67
           ]
YROTG15 = [0.00, 0.00, 0.00, 0.00, .0054, .00, 0.00, .0216, .00, .000,
           .0384, .00, 0.00, .054, 0.00, 0.00, .067, 0.00, 0.00, 0.08,
           0.00, 0.00, .094, 0.00, 0.00, .084, 0.00, 0.00, .072, 0.00,
           0.00, .047, 0.00, 0.00, .040, 0.00, 0.00, .036, 0.00, 0.00,
           .024, 0.00, 0.00, .012, 0.00, 0.00, .0048, 0.00]

B0 = 1.783e-4
EING15 = np.zeros(250)
EING15[0] = -10 * B0
EING15[24] = -1 * EIN[0]
for J in range(2, 25):
    EING15[J + 24 - 1] = EING15[24] + J * 8.0 * B0
    EING15[J - 1] = -1 * EING15[J + 24 - 1]
EING15[48:148] = [-0.193, 0.193, 0.385, 0.568, 0.749, 0.929, 0.977, 1.108, 1.282, 1.458, 1.627, 1.629, 1.798, 1.965,
                  2.127,
                  2.283, 2.430, 2.585, 2.739, 2.883, 3.023, 3.168, 3.316, 3.46, 5.50, 6.00, 6.50, 6.98, 7.08, 7.25,
                  7.35,
                  7.45, 7.55, 7.65, 7.75, 7.85, 7.95, 8.05, 8.15, 8.20, 8.25, 8.35, 8.45, 8.55, 8.65, 8.75, 8.85, 8.95,
                  9.05,
                  9.15, 9.25, 9.35, 9.45, 9.55, 9.675, 9.972, 10.288, 10.570, 10.60, 10.665, 10.760, 10.915, 11.05,
                  11.25,
                  11.46, 11.56, 11.65, 11.83, 11.98, 12.2, 12.4, 12.6, 12.8, 13.0, 13.1, 13.2, 13.4, 13.6, 13.8, 14.0,
                  14.2,
                  14.4, 14.6, 14.8, 15.0, 15.2, 15.4, 15.6, 15.8, 16.0, 16.2, 16.4, 16.6, 16.8, 17.0, 17.2, 17.4, 17.6,
                  17.8,
                  18.0]
gd['gas15/XELA'] = XELAG15
gd['gas15/YELA'] = YELAG15
gd['gas15/YMOM'] = YMOMG15
gd['gas15/YEPS'] = YEPSG15
gd['gas15/XROT13'] = XROT13G15
gd['gas15/YROT13'] = YROT13G15
gd['gas15/XROT35'] = XROT35G15
gd['gas15/YROT35'] = YROT35G15
gd['gas15/XROT57'] = XROT57G15
gd['gas15/YROT57'] = YROT57G15
gd['gas15/XROT79'] = XROT79G15
gd['gas15/YROT79'] = YROT79G15
gd['gas15/XROT911'] = XROT911G15
gd['gas15/YROT911'] = YROT911G15
gd['gas15/XROT1113'] = XROT1113G15
gd['gas15/YROT1113'] = YROT1113G15
gd['gas15/XROT1315'] = XROT1315G15
gd['gas15/YROT1315'] = YROT1315G15
gd['gas15/XROT1517'] = XROT1517G15
gd['gas15/YROT1517'] = YROT1517G15
gd['gas15/XROT1719'] = XROT1719G15
gd['gas15/YROT1719'] = YROT1719G15
gd['gas15/XROT1921'] = XROT1921G15
gd['gas15/YROT1921'] = YROT1921G15
gd['gas15/XROT2123'] = XROT2123G15
gd['gas15/YROT2123'] = YROT2123G15
gd['gas15/XROT2325'] = XROT2325G15
gd['gas15/YROT2325'] = YROT2325G15
gd['gas15/XROT2527'] = XROT2527G15
gd['gas15/YROT2527'] = YROT2527G15
gd['gas15/XROT2729'] = XROT2729G15
gd['gas15/YROT2729'] = YROT2729G15
gd['gas15/XROT2931'] = XROT2931G15
gd['gas15/YROT2931'] = YROT2931G15
gd['gas15/XROT3133'] = XROT3133G15
gd['gas15/YROT3133'] = YROT3133G15
gd['gas15/XROT3335'] = XROT3335G15
gd['gas15/YROT3335'] = YROT3335G15
gd['gas15/XROT3537'] = XROT3537G15
gd['gas15/YROT3537'] = YROT3537G15
gd['gas15/XROT3739'] = XROT3739G15
gd['gas15/YROT3739'] = YROT3739G15
gd['gas15/XROT3941'] = XROT3941G15
gd['gas15/YROT3941'] = YROT3941G15
gd['gas15/XROT4143'] = XROT4143G15
gd['gas15/YROT4143'] = YROT4143G15
gd['gas15/XROT4345'] = XROT4345G15
gd['gas15/YROT4345'] = YROT4345G15
gd['gas15/XROT4547'] = XROT4547G15
gd['gas15/YROT4547'] = YROT4547G15
gd['gas15/XROT4749'] = XROT4749G15
gd['gas15/YROT4749'] = YROT4749G15
gd['gas15/XVIB'] = XVIBG15
gd['gas15/YVIB1'] = YVIB1G15
gd['gas15/YVIB2'] = YVIB2G15
gd['gas15/YVIB3'] = YVIB3G15
gd['gas15/YVIB4'] = YVIB4G15
gd['gas15/YVIB5'] = YVIB5G15
gd['gas15/YVIB6'] = YVIB6G15
gd['gas15/YVIB7'] = YVIB7G15
gd['gas15/YVIB8'] = YVIB8G15
gd['gas15/YVIB9'] = YVIB9G15
gd['gas15/YVIB10'] = YVIB10G15
gd['gas15/YVIB11'] = YVIB11G15
gd['gas15/YVIB12'] = YVIB12G15
gd['gas15/YVIB13'] = YVIB13G15
gd['gas15/YVIB14'] = YVIB14G15
gd['gas15/YVIB15'] = YVIB15G15
gd['gas15/YVIB16'] = YVIB16G15
gd['gas15/YVIB17'] = YVIB17G15
gd['gas15/YVIB18'] = YVIB18G15
gd['gas15/YVIB19'] = YVIB19G15
gd['gas15/YVIB20'] = YVIB20G15
gd['gas15/YVIB21'] = YVIB21G15
gd['gas15/X3ATT'] = X3ATTG15
gd['gas15/Y3ATT'] = Y3ATTG15
gd['gas15/XATT'] = XATTG15
gd['gas15/YATT'] = YATTG15
gd['gas15/XEXC1'] = XEXC1G15
gd['gas15/YEXC1'] = YEXC1G15
gd['gas15/XEXC2'] = XEXC2G15
gd['gas15/YEXC2'] = YEXC2G15
gd['gas15/XEXC3'] = XEXC3G15
gd['gas15/YEXC3'] = YEXC3G15
gd['gas15/XEXC4'] = XEXC4G15
gd['gas15/YEXC4'] = YEXC4G15
gd['gas15/XEXC5'] = XEXC5G15
gd['gas15/YEXC5'] = YEXC5G15
gd['gas15/XEXC6'] = XEXC6G15
gd['gas15/YEXC6'] = YEXC6G15
gd['gas15/XEXC7'] = XEXC7G15
gd['gas15/YEXC7'] = YEXC7G15
gd['gas15/XEXC8'] = XEXC8G15
gd['gas15/YEXC8'] = YEXC8G15
gd['gas15/XEXC9'] = XEXC9G15
gd['gas15/YEXC9'] = YEXC9G15
gd['gas15/XROT'] = XROTG15
gd['gas15/YROT'] = YROTG15
gd['gas15/XIONC'] = XIONCG15
gd['gas15/YIONC'] = YIONCG15
gd['gas15/XION1'] = XION1G15
gd['gas15/YION1'] = YION1G15
gd['gas15/XION2'] = XION2G15
gd['gas15/YION2'] = YION2G15
gd['gas15/XION3'] = XION3G15
gd['gas15/YION3'] = YION3G15
gd['gas15/XION4'] = XION4G15
gd['gas15/YION4'] = YION4G15
gd['gas15/XION5'] = XION5G15
gd['gas15/YION5'] = YION5G15
gd['gas15/XKSH'] = XKSHG15
gd['gas15/YKSH'] = YKSHG15
gd['gas15/Z8T'] = Z8TG15
gd['gas15/EBRM'] = EBRMG15
gd['gas15/EIN'] = EING15
B0 = 2.4668e-4

# CALC ROTATIONAL TRANSITION ENERGIES
EING16 = np.zeros(250)
for J in range(1, 39):
    I = J - 1
EING16[J + 38 - 1] = B0 * (4.0 * I + 6.0)
EING16[J - 1] = -1 * EING16[J + 38 - 1]

EING16[76:128] = [-0.2889, 0.2889, 0.5742, 0.8559, 1.1342, 1.4088, 1.6801, 1.9475, 2.2115, 2.4718, 2.7284,
                  2.9815, 3.2310, 3.4769, 3.7191, 3.9576, 6.725, 7.360, 7.744, 8.050, 8.217, 8.451, 8.729,
                  8.950, 8.974, 9.191, 9.562, 9.590, 9.665, 9.933, 10.174, 10.536, 11.188, 11.875, 12.289,
                  12.781, 13.000, 13.001, 13.076, 13.174, 13.338, 13.385, 13.628, 14.090, 14.232, 14.36, 14.45,
                  14.839, 15.2, 15.6, 16.6, 0.0]

gd['gas16/EIN'] = EING16
XELAG16 = [0.00, .001, .0015, .0018, .002, .0025, .003, .004, .005, .006,
           .007, .008, .009, .010, .012, .015, .018, .020, .025, .030,
           0.04, 0.05, 0.06, 0.07, 0.08, 0.09, 0.10, 0.12, 0.15, 0.18,
           0.20, 0.25, 0.30, 0.40, 0.50, 0.60, 0.70, 0.80, 0.90, 1.00,
           1.10, 1.20, 1.30, 1.40, 1.50, 1.60, 1.70, 1.80, 1.85, 1.90,
           1.95, 2.00, 2.05, 2.10, 2.15, 2.20, 2.25, 2.30, 2.35, 2.40,
           2.45, 2.50, 2.55, 2.60, 2.65, 2.70, 2.75, 2.80, 2.85, 2.90,
           2.95, 3.00, 3.05, 3.10, 3.15, 3.20, 3.25, 3.30, 3.35, 3.40,
           3.45, 3.50, 3.60, 3.70, 3.80, 3.90, 4.00, 4.50, 5.00, 5.50,
           6.00, 6.50, 7.00, 8.00, 9.00, 10.0, 12.0, 15.0, 17.0, 20.0,
           25.0, 30.0, 35.0, 40.0, 45.0, 50.0, 60.0, 70.0, 80.0, 90.0,
           100., 125., 150., 175., 200., 250., 300., 350., 400., 450.,
           500., 600., 700., 800., 900., 1000., 1250., 1500., 1750., 2000.,
           2500., 3000., 3500., 4000., 4500., 5000., 6000., 7000., 8000., 9000.,
           10000., 1.25e4, 1.5e4, 1.75e4, 2.0e4, 2.5e4, 3.0e4, 3.5e4, 4.0e4, 4.5e4,
           5.0e4, 6.0e4, 7.0e4, 8.0e4, 9.0e4, 1.0e5, 1.25e5, 1.5e5, 1.75e5, 2.0e5,
           2.5e5, 3.0e5, 3.5e5, 4.0e5, 4.5e5, 5.0e5, 6.0e5, 7.0e5, 8.0e5, 9.0e5,
           1.0e6, 1.25e6, 1.5e6, 1.75e6, 2.0e6, 2.5e6, 3.0e6, 3.5e6, 4.0e6, 4.5e6,
           5.0e6, 6.0e6, 7.0e6, 8.0e6, 9.0e6, 1.0e7, 1.25e7, 1.5e7, 1.75e7, 2.0e7,
           2.5e7, 3.0e7, 3.5e7, 4.0e7, 4.5e7, 5.0e7, 6.0e7, 7.0e7, 8.0e7, 9.0e7,
           1.0e8, 1.25e8, 1.5e8, 1.75e8, 2.0e8, 2.5e8, 3.0e8, 3.5e8, 4.0e8, 4.5e8,
           5.0e8, 6.0e8, 7.0e8, 8.0e8, 9.0e8, 1.0e9]
# ELASTIC +ROTATION X-SECTION

YELAG16 = [1.12, 1.377, 1.446, 1.484, 1.510, 1.570, 1.640, 1.738, 1.830,
           1.928,
           2.020, 2.082, 2.151, 2.210, 2.362, 2.570, 2.780, 2.900, 3.170, 3.430,
           3.850, 4.170, 4.480, 4.750, 5.000, 5.250, 5.450, 5.850, 6.300, 6.800,
           7.000, 7.600, 8.000, 8.600, 9.000, 9.200, 9.300, 9.450, 9.650, 9.840,
           10.00, 10.24, 10.48, 10.67, 11.05, 11.71, 12.90, 14.90, 16.10, 17.60,
           17.40, 17.10, 16.30, 17.10, 20.30, 24.10, 21.70, 18.80, 17.90, 22.20,
           24.90, 21.70, 18.00, 16.80, 20.90, 22.45, 20.30, 17.00, 16.80, 18.70,
           18.70, 16.50, 15.30, 15.70, 16.00, 15.40, 14.60, 14.50, 14.70, 14.30,
           13.50, 13.80, 13.60, 13.30, 13.15, 13.00, 12.90, 11.90, 11.60, 11.40,
           11.20, 11.10, 11.10, 10.90, 10.80, 11.20, 11.40, 11.80, 11.80, 11.30,
           10.70, 9.660, 8.740, 8.090, 7.530, 7.130, 6.380, 5.840, 5.330, 4.940,
           4.650, 4.100, 3.600, 3.300, 2.990, 2.620, 2.320, 2.100, 1.930, 1.780,
           1.660, 1.470, 1.300, 1.200, 1.110, 1.030, 0.870, 0.765, 0.670, 0.600,
           0.496, 0.420, 0.364, 0.321, 0.288, 0.261, 0.219, 0.189, 0.167, 0.149,
           0.135, 0.109, .0919, .0795, .0702, .0570, .0483, .0420, .0372, .0336,
           .0306, .0262, .0231, .0207, .0189, .0174, .0148, .0130, .0118, .0108,
           .00953, .00868, .00808, .00764, .00730, .00703, .00664, .00637, .00617,
           .00602,
           .00591, .00572, .00560, .00552, .00546, .00539, .00535, .00532, .00530,
           .00529,
           .00528, .00527, .00525, .00525, .00525, .00524, .00524, .00524, .00524,
           .005236]
for i in range(26):
    YELAG16.append(.005234)

# ELASTIC+ROTATION MOMENTUM TRANSFER X-SECTION

YMOMG16 = [1.12, 1.377, 1.446, 1.484, 1.510, 1.570, 1.640, 1.738, 1.830,
           1.928,
           2.020, 2.082, 2.151, 2.210, 2.362, 2.570, 2.780, 2.900, 3.170, 3.430,
           3.900, 4.350, 4.750, 5.100, 5.410, 5.690, 5.950, 6.450, 7.100, 7.590,
           7.900, 8.500, 9.000, 9.700, 10.30, 10.90, 11.25, 11.40, 11.30, 11.10,
           10.90, 10.65, 10.45, 10.65, 10.80, 11.85, 13.60, 16.00, 17.40, 19.00,
           18.80, 18.60, 17.80, 18.50, 21.70, 25.50, 23.10, 20.20, 19.30, 23.50,
           26.20, 23.00, 19.30, 18.10, 22.20, 23.70, 21.50, 18.10, 17.80, 19.60,
           19.40, 17.10, 15.70, 15.90, 15.90, 15.10, 14.00, 13.50, 13.30, 12.50,
           11.40, 11.40, 11.00, 10.60, 10.20, 10.00, 9.900, 9.100, 8.900, 8.700,
           8.500, 8.400, 8.300, 8.200, 8.200, 8.300, 8.400, 8.500, 8.500, 8.300,
           7.800, 7.200, 6.700, 6.310, 5.950, 5.600, 4.700, 4.000, 3.500, 3.000,
           2.650, 2.100, 1.650, 1.370, 1.179, 0.861, 0.662, 0.527, 0.431, 0.360,
           0.306, 0.230, 0.179, 0.144, 0.119, 0.100, .0687, .0504, .0387, .0307,
           .0208, .0151, .0115, .00904, .00733, .00607, .00438, .00332, .00261,
           .00211,
           .00174, .00116, 8.37e-4, 6.33e-4, 4.97e-4, 3.32e-4, 2.39e-4, 1.81e-4,
           1.43e-4, 1.15e-4,
           9.56e-5, 6.91e-5, 5.26e-5, 4.16e-5, 3.39e-5, 2.82e-5, 1.92e-5, 1.41e-5,
           1.09e-5, 8.71e-6,
           6.04e-6, 4.50e-6, 3.52e-6, 2.86e-6, 2.38e-6, 2.02e-6, 1.52e-6, 1.20e-6,
           9.83e-7, 8.21e-7,
           6.99e-7, 5.00e-7, 3.77e-7, 2.97e-7, 2.40e-7, 1.68e-7, 1.25e-7, 9.72e-8,
           7.78e-8, 6.38e-8,
           5.34e-8, 3.91e-8, 2.99e-8, 2.37e-8, 1.93e-8, 1.60e-8, 1.07e-8, 7.73e-9,
           5.84e-9, 4.58e-9,
           3.04e-9, 2.17e-9, 1.63e-9, 1.27e-9, 1.01e-9, 8.31e-10, 5.88e-10,
           4.37e-10, 3.38e-10, 2.69e-10,
           2.19e-10, 1.41e-10, 9.86e-11, 7.27e-11, 5.57e-11, 3.57e-11, 2.48e-11,
           1.83e-11, 1.40e-11, 1.11e-11,
           8.96e-12, 6.22e-12, 4.57e-12, 3.50e-12, 2.77e-12, 2.24e-12]
# ELASTIC ANISOTROPY FUNCTION EPSILON
# EPSILON=1.0-YEPS
YEPSG16 = []
for J in range(20):
    YEPSG16.append(1.0)
YEPSG16.extend([1.01974, 1.06500, 1.09085, 1.11025, 1.12263, 1.12532, 1.13709, 1.15311,
                1.18909, 1.17321,
                1.19143, 1.17651, 1.18619, 1.19046, 1.21464, 1.27297, 1.30840, 1.30369,
                1.25314, 1.19066,
                1.13451, 1.06001, 0.99571, 0.99719, 0.96607, 1.01794, 1.08128, 1.11047,
                1.12077, 1.11898,
                1.12034, 1.13112, 1.13750, 1.12243, 1.10323, 1.08700, 1.09660, 1.11142,
                1.11699, 1.08770,
                1.07822, 1.08972, 1.10807, 1.11576, 1.09314, 1.08340, 1.08852, 1.09688,
                1.08914, 1.07212,
                1.05611, 1.05451, 1.03920, 1.01911, 0.99063, 0.97078, 0.93840, 0.89677,
                0.85772, 0.81253,
                0.76918, 0.74264, 0.71789, 0.70105, 0.67098, 0.66198, 0.65948, 0.65567,
                0.65920, 0.65352,
                0.64764, 0.64463, 0.63220, 0.63846, 0.64810, 0.62303, 0.61725, 0.59484,
                0.59484, 0.61407,
                0.60653, 0.62889, 0.65829, 0.67702, 0.69139, 0.68467, 0.61702, 0.54773,
                0.51113, 0.44953,
                0.40500, 0.34012, 0.28400, 0.24224, 0.22315, 0.16753, 0.13474, 0.11089,
                0.09315, 0.08049,
                0.07031, 0.05555, 0.04637, 0.03828, 0.03277, 0.02863, 0.02168, 0.01705,
                0.01436, 0.01227,
                0.00951, 0.00782, 0.00665, 0.00576, 0.00508, 0.00454, 0.00377, 0.00322,
                0.00279, 0.00248,
                .002212, .001759, .001461, .001246, .001084, 8.62e-4, 7.12e-4, 6.07e-4,
                5.31e-4, 4.64e-4,
                4.18e-4, 3.44e-4, 2.91e-4, 2.52e-4, 2.21e-4, 1.97e-4, 1.53e-4, 1.249e-4,
                1.042e-4, 8.95e-5,
                6.83e-5, 5.45e-5, 4.49e-5, 3.79e-5, 3.25e-5, 2.83e-5, 2.20e-5, 1.77e-5,
                1.47e-5, 1.24e-5,
                1.062e-5, 7.65e-6, 5.73e-6, 4.48e-6, 3.60e-6, 2.48e-6, 1.81e-6, 1.38e-6,
                1.09e-6, 8.85e-7,
                7.32e-7, 5.24e-7, 3.94e-7, 3.07e-7, 2.46e-7, 2.02e-7, 1.32e-7, 9.28e-8,
                6.89e-8, 5.31e-8,
                3.44e-8, 2.40e-8, 1.77e-8, 1.36e-8, 1.07e-8, 8.70e-9, 6.03e-9, 4.41e-9,
                3.36e-9, 2.64e-9,
                2.13e-9, 1.34e-9, 9.19e-10, 6.67e-10, 5.04e-10, 3.16e-10, 2.16e-10,
                1.57e-10, 1.18e-10, 9.3e-11,
                7.4e-11, 5.1e-11, 3.7e-11, 2.8e-11, 2.2e-11, 1.7e-11])
# ROTATIONAL RESONANCE FUNCTION

XROTG16 = [0.00, 1.00, 1.10, 1.20, 1.30, 1.40, 1.50, 1.60, 1.70, 1.80,
           1.85, 1.90, 1.95, 1.98, 2.00, 2.05, 2.10, 2.15, 2.20, 2.25,
           2.30, 2.35, 2.40, 2.45, 2.50, 2.55, 2.60, 2.65, 2.69, 2.70,
           2.75, 2.80, 2.85, 2.90, 2.95, 3.00, 3.05, 3.10, 3.15, 3.20,
           3.25, 3.30, 3.35, 3.40, 3.45, 3.50, 3.60, 3.70, 3.80, 3.90,
           4.00, 4.10, 4.20, 4.30, 4.40, 4.50, 4.60, 4.70, 4.80, 4.90,
           5.00, 5.10, 5.20, 5.30, 5.40, 5.50, 5.60, 5.70, 5.80, 5.90
           ]
YROTG16 = [0.00, 0.00, 0.00, 0.10, 0.20, 0.30, 0.40, 1.10, 2.30, 4.30,
           5.50, 7.00, 6.80, 7.10, 6.50, 5.70, 6.50, 9.70, 13.5, 11.1,
           8.20, 7.30, 11.6, 14.3, 11.1, 7.40, 6.20, 10.2, 12.0, 11.8,
           9.60, 6.30, 6.10, 8.00, 8.00, 5.80, 4.60, 5.00, 5.30, 4.70,
           3.90, 3.80, 4.00, 3.50, 2.70, 3.00, 2.80, 2.50, 2.40, 2.20,
           2.10, 1.90, 1.70, 1.50, 1.20, 1.00, 0.80, 0.70, 0.60, 0.50,
           0.40, 0.30, 0.20, 0.10, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00]
# ALLAN ANe VICIC  FROM 1.6 EV TO 4.5 EV FOR VIBRATIONS

XVB1G16 = [.2889, .289, .290, .292, .293, .295, .300, .310, .320, .330,
           .340, .360, .380, 0.40, 0.50, 0.60, 0.70, 0.80, 0.90, 1.00,
           1.10, 1.20, 1.30, 1.35, 1.40, 1.45, 1.50, 1.55, 1.60, 1.65,
           1.70, 1.75, 1.80, 1.85, 1.90, 1.95, 2.00, 2.05, 2.10, 2.15,
           2.20, 2.25, 2.30, 2.35, 2.40, 2.45, 2.50, 2.55, 2.60, 2.65,
           2.70, 2.75, 2.80, 2.85, 2.90, 2.95, 3.00, 3.05, 3.10, 3.15,
           3.20, 3.25, 3.30, 3.35, 3.40, 3.45, 3.50, 3.55, 3.60, 3.65,
           3.70, 3.75, 3.80, 3.90, 4.00, 4.50, 5.00, 7.50, 10.0, 15.0,
           18.0, 20.0, 22.5, 25.0, 30.0, 50.0, 80.0]
# V1

YVB1G16 = [.00, .00018, .00045, .00072, .00082, .00099, .00131,
           .00174, .00203, .00225,
           .00242, .00267, .00283, .00294, .00340, .00360, .0039, .0044, .0054, .0066,
           .0086, .0125, .0182, .0230, .0295, .0370, .0475, .0580, .0750, .103,
           .178, .320, .600, 1.20, 2.40, 4.35, 4.40, 2.71, 1.67, 2.40,
           3.62, 4.90, 4.46, 3.31, 2.26, 1.74, 2.90, 4.15, 4.25, 2.95,
           1.61, 1.97, 2.95, 3.43, 2.30, 1.41, 1.63, 2.30, 2.01, 1.54,
           1.12, 1.27, 1.37, 1.27, 0.96, 0.84, .820, .768, .648, .600,
           .624, .528, .432, .390, .330, .230, .075, .025, .012, .031,
           .061, .156, .101, .066, .022, .012, .006]
# V2

XVB2G16 = [.5742, .600, .700, .800, .900, 1.00, 1.10, 1.20, 1.30, 1.40,
           1.50, 1.55, 1.60, 1.65, 1.70, 1.75, 1.80, 1.85, 1.90, 1.95,
           2.00, 2.05, 2.10, 2.15, 2.20, 2.25, 2.30, 2.35, 2.40, 2.45,
           2.50, 2.55, 2.60, 2.65, 2.70, 2.75, 2.80, 2.85, 2.90, 2.95,
           3.00, 3.05, 3.10, 3.15, 3.20, 3.25, 3.30, 3.35, 3.40, 3.45,
           3.50, 3.55, 3.60, 3.70, 3.80, 3.90, 4.00, 4.50, 5.00, 7.50,
           10.0, 15.0, 18.0, 20.0, 22.5, 25.0, 30.0, 50.0, 80.0
           ]
YVB2G16 = [.0, 1.e-5, 4.e-5, 9.e-5, 1.5e-4, 2.0e-4, 2.8e-4, 3.2e-4, 5.e-4,
           8.1e-4,
           .0026, .0059, .0115, .026, .051, .123, .236, .491, 0.94, 2.26,
           2.90, 2.55, 2.20, 1.45, .856, .682, 1.33, 2.40, 3.05, 2.78,
           1.70, .672, .800, 1.48, 1.61, 1.25, .805, .501, .670, .890,
           .890, .650, .444, .428, .539, .491, .364, .225, .285, .238,
           .200, .168, .156, .127, .101, .085, .072, .042, .014, .004,
           .002, .006, .012, .030, .020, .012, .004, .002, .001]
# V3

XVB3G16 = [.8559, .900, 1.00, 1.10, 1.20, 1.30, 1.40, 1.50, 1.60, 1.65,
           1.70, 1.75, 1.80, 1.85, 1.90, 1.95, 2.00, 2.05, 2.10, 2.15,
           2.16, 2.20, 2.25, 2.30, 2.35, 2.40, 2.45, 2.50, 2.55, 2.60,
           2.65, 2.70, 2.75, 2.80, 2.85, 2.90, 2.95, 3.00, 3.05, 3.10,
           3.15, 3.20, 3.25, 3.30, 3.35, 3.40, 3.45, 3.50, 3.55, 3.60,
           3.65, 3.70, 3.75, 3.80, 3.85, 3.90, 3.95, 4.00, 4.50, 5.00,
           7.50, 10.0, 15.0, 18.0, 20.0, 22.5, 25.0, 30.0, 50.0, 80.0
           ]
YVB3G16 = [.0, 1.e-5, 3.7e-5, 7.e-5, 9.8e-5, 1.3e-4, 1.8e-4, 4.1e-4,
           .0021, .0050,
           .012, .028, .071, .160, .300, .807, 1.30, 1.87, 2.11, 2.55,
           2.57, 2.35, 1.52, .617, .438, .656, 1.46, 1.75, 1.81, 1.38,
           .630, .250, .409, .747, 1.00, .682, .309, .144, .263, .412,
           .360, .212, .131, .148, .183, .200, .157, .114, .079, .101,
           .101, .079, .057, .053, .058, .053, .044, .035, .023, .008,
           .0023, .001, .003, .007, .017, .011, .006, .002, .001, .0005]
# V4

XVB4G16 = [1.1342, 1.80, 1.85, 1.90, 1.95, 2.00, 2.05, 2.10, 2.15, 2.20,
           2.22, 2.25, 2.30, 2.35, 2.40, 2.45, 2.50, 2.55, 2.60, 2.65,
           2.70, 2.75, 2.80, 2.85, 2.90, 2.95, 3.00, 3.05, 3.10, 3.15,
           3.20, 3.25, 3.30, 3.35, 3.40, 3.50, 3.60, 3.80, 4.00, 4.50,
           5.00, 7.50, 10.0, 15.0, 18.0, 20.0, 22.5, 30.0, 50.0, 80.0
           ]
YVB4G16 = [0.0, 0.00, 9.e-5, .064, .170, .269, .465, .743, 1.29, 1.76,
           1.79, 1.72, 1.41, 1.04, .600, .234, .168, .439, .797, .994,
           .806, .474, .215, .104, .197, .385, .394, .260, .198, .063,
           .098, .151, .205, .089, .070, .078, .061, .044, .035, .026,
           .009, .0026, .00105, .0016, .003, .008, .005, .003, .001, .0005]
# V5

XVB5G16 = [1.4088, 1.90, 1.95, 2.00, 2.05, 2.10, 2.15, 2.20, 2.25, 2.30,
           2.35, 2.40, 2.45, 2.50, 2.55, 2.60, 2.65, 2.70, 2.75, 2.80,
           2.85, 2.90, 2.95, 3.00, 3.05, 3.10, 3.15, 3.20, 3.25, 3.30,
           3.35, 3.40, 3.45, 3.50, 4.00, 4.50, 5.00, 7.50, 10.0, 20.0
           ]
YVB5G16 = [0.00, 0.00, .0009, .0118, .0531, .136, .313, .490, .655, .791,
           1.04, 1.18, 1.01, .631, .295, .101, .068, .195, .395, .502,
           .519, .313, .106, .024, .101, .195, .183, .112, .068, .018,
           .035, .065, .065, .024, .014, .0096, .0032, .00096, .00024, .00012]
# V6

XVB6G16 = [1.6801, 2.05, 2.10, 2.15, 2.20, 2.25, 2.30, 2.35, 2.40, 2.45,
           2.50, 2.55, 2.60, 2.65, 2.70, 2.75, 2.80, 2.85, 2.90, 2.95,
           3.00, 3.05, 3.10, 3.15, 3.20, 3.25, 3.30, 3.35, 3.40, 3.45,
           3.50, 3.55, 3.60, 3.65, 3.70, 4.00, 4.50, 5.00, 7.50, 10.0,
           20.0]

YVB6G16 = [0.00, 0.00, 9.e-5, .0117, .0463, .124, .192, .344, .487, .602,
           .615, .602, .577, .527, .307, .124, .050, .103, .193, .270,
           .270, .180, .084, .0372, .0527, .103, .128, .096, .062, .0248,
           .0186, .0312, .0372, .0372, .0155, .010, .052, .017, .0052, .0021,
           .00105]
# V7

XVB7G16 = [1.9475, 2.25, 2.30, 2.35, 2.40, 2.45, 2.50, 2.55, 2.60, 2.65,
           2.68, 2.70, 2.75, 2.80, 2.85, 2.90, 2.95, 3.00, 3.05, 3.10,
           3.15, 3.20, 3.25, 3.30, 3.35, 3.40, 3.45, 3.50, 3.55, 3.60,
           3.65, 3.70, 3.75, 3.80, 3.85, 3.90, 4.00, 4.50, 5.00, 7.50,
           10.0, 20.0
           ]
YVB7G16 = [0.00, 0.00, .0009, .0255, .0526, .089, .133, .178, .232, .303,
           .318, .304, .231, .159, .119, .0542, .0239, .0255, .0796, .113,
           .108, .0812, .0413, .0112, .0064, .0207, .0334, .0366, .0224, .0128,
           .0128, .0157, .0183, .0166, .0096, .0074, .0057, .0039, .0013, .00039,
           .00015, .000075]
# V8

XVB8G16 = [2.2115, 2.40, 2.45, 2.50, 2.55, 2.60, 2.65, 2.70, 2.75, 2.80,
           2.85, 2.88, 2.90, 2.95, 3.00, 3.05, 3.10, 3.15, 3.20, 3.25,
           3.30, 3.35, 3.40, 3.45, 3.50, 3.55, 3.60, 3.65, 3.70, 3.75,
           3.80, 3.85, 3.90, 3.95, 4.00, 4.50, 5.00, 7.50, 10.0, 20.0
           ]
YVB8G16 = [0.00, 0.00, 9.e-6, .003, .011, .017, .042, .0656, .0739, .098,
           .135, .140, .128, .084, .035, .014, .003, .007, .028, .0460,
           .0460, .028, .011, .003, .0018, .011, .0123, .0140, .0084, .0035,
           .0018, .0018, .0026, .0029, .0014, .0010, .0003, .00010, .00004, .00002]
# V9

XVB9G16 = [2.4718, 2.65, 2.70, 2.75, 2.80, 2.85, 2.90, 2.95, 3.00, 3.05,
           3.07, 3.10, 3.15, 3.20, 3.25, 3.30, 3.35, 3.40, 3.45, 3.50,
           3.55, 3.60, 3.65, 3.70, 3.75, 3.80, 3.85, 3.90, 3.95, 4.00,
           4.50, 5.00, 7.50, 10.0, 20.0]

YVB9G16 = [0.00, .0011, .0028, .0069, .0132, .0264, .0412, .0474, .0438,
           .0496,
           .0528, .0438, .0247, .0739, .00295, .00581, .0159, .0232, .0264, .0206,
           .0116, .00296, .00296, .00581, .00739, .00739, .00528, .00295, .00147,
           .00070,
           .00039, .00013, .000039, .0000157, .0000079]
# V10

XVB10G16 = [2.7284, 2.90, 2.95, 3.00, 3.05, 3.10, 3.15, 3.20, 3.25, 3.30,
            3.35, 3.40, 3.45, 3.50, 3.55, 3.60, 3.65, 3.70, 3.75, 3.80,
            3.85, 3.90, 3.95, 4.00, 4.05, 4.10, 4.15, 4.20, 4.25, 4.30,
            4.50, 5.00, 7.50, 10.0, 20.0]

YVB10G16 = [0.00, .000040, .00170, .00554, .0103, .0154, .0205, .0201,
            .0147, .0103,
            .00677, .00225, .00137, .00452, .00800, .0116, .0119, .00800, .00390,
            .00137,
            .00205, .00390, .00573, .00573, .00452, .00349, .00225, .00116, .00042,
            .00026,
            .00017, 5.8e-5, 1.7e-5, 8.5e-6, 4.2e-6]
# V11

XVB11G16 = [2.9815, 3.10, 3.15, 3.20, 3.25, 3.30, 3.35, 3.40, 3.45, 3.50,
            3.55, 3.60, 3.65, 3.70, 3.75, 3.80, 3.85, 3.90, 3.95, 4.00,
            4.05, 4.10, 4.15, 4.20, 4.25, 4.30, 4.35, 4.40, 4.45, 4.50,
            4.60, 5.00, 7.50, 10.0, 20.0
            ]
YVB11G16 = [0.00, 3.29e-4, .00170, .00291, .00445, .00550, .00462,
            .00291, .00170, 6.04e-4,
            2.20e-4, .00105, .00275, .00344, .00303, .00198, 7.70e-4, 1.65e-4,
            2.75e-4, 4.40e-4,
            .00116, .00110, 3.85e-4, 5.50e-5, 5.50e-5, 3.30e-4, 3.85e-4, 3.30e-4,
            1.65e-4, 8.70e-5,
            2.88e-5, 9.60e-6, 2.88e-6, 1.16e-6, 5.8e-7]
# V12

XVB12G16 = [3.2310, 3.30, 3.35, 3.40, 3.45, 3.50, 3.55, 3.60, 3.65, 3.70,
            3.75, 3.80, 3.85, 3.90, 3.95, 4.00, 4.05, 4.10, 4.15, 4.20,
            4.25, 4.30, 4.35, 4.40, 4.45, 4.50, 4.55, 4.60, 4.65, 5.00,
            7.50, 10.0, 20.0
            ]
YVB12G16 = [0.00, 3.66e-5, 3.78e-4, 6.22e-4, .00107, .00119, .00092,
            4.40e-4, 1.59e-4, 1.10e-4,
            4.52e-4, 8.06e-4, .00122, .00107, 6.96e-4, 3.17e-4, 7.32e-5, 8.55e-5,
            3.05e-4, 3.78e-4,
            3.05e-4, 1.53e-4, 7.33e-5, 1.22e-5, 7.33e-5, 1.46e-4, 8.55e-5, 1.22e-5,
            6.10e-6, 2.04e-6,
            6.10e-7, 2.44e-7, 1.22e-7]
# V13

XVB13G16 = [3.4769, 3.55, 3.60, 3.65, 3.70, 3.75, 3.80, 3.85, 3.90, 3.95,
            4.00, 4.05, 4.10, 4.15, 4.20, 4.25, 4.30, 4.35, 4.40, 4.45,
            4.50, 4.55, 4.60, 4.65, 4.70, 4.75, 4.80, 5.00, 7.50, 10.0,
            20.0
            ]
YVB13G16 = [0.00, 4.90e-5, 1.02e-4, 1.96e-4, 2.16e-4, 1.18e-4, 3.92e-5,
            3.92e-5, 1.46e-4, 2.94e-4,
            3.68e-4, 3.92e-4, 2.72e-4, 1.22e-4, 2.75e-5, 6.28e-5, 9.77e-5, 1.49e-4,
            1.18e-4, 6.28e-5,
            1.57e-5, 1.57e-5, 2.35e-5, 4.71e-5, 3.14e-5, 1.96e-5, 3.93e-6, 1.31e-6,
            3.93e-7, 1.57e-7,
            7.8e-8]
# V14

XVB14G16 = [3.7191, 3.80, 3.85, 3.90, 3.95, 4.00, 4.05, 4.10, 4.15, 4.20,
            4.25, 4.30, 4.35, 4.40, 4.45, 4.50, 4.55, 4.60, 4.65, 4.70,
            4.75, 4.80, 4.85, 4.90, 4.95, 7.50, 10.0, 20.0
            ]
YVB14G16 = [0.00, 9.07e-6, 1.70e-5, 1.70e-5, 6.80e-6, 7.94e-6, 3.51e-5,
            7.83e-5, 1.14e-4, 1.09e-4,
            7.14e-5, 3.51e-5, 6.80e-6, 9.07e-6, 4.31e-5, 5.44e-5, 3.51e-5, 1.70e-5,
            4.54e-6, 6.80e-6,
            1.02e-5, 1.70e-5, 9.07e-6, 5.67e-6, 1.75e-6, 1.75e-7, 6.98e-8, 3.5e-8]
# V15

XVB15G16 = [3.9576, 4.05, 4.10, 4.15, 4.20, 4.25, 4.30, 4.35, 4.40, 4.45,
            4.50, 4.55, 4.60, 4.65, 4.70, 4.75, 4.80, 4.85, 4.90, 4.95,
            5.00, 5.05, 5.10, 5.15, 5.20, 5.25, 5.30, 5.40, 5.50, 7.50,
            10.0, 20.0
            ]
YVB15G16 = [0.00, 9.42e-7, 1.25e-6, 2.51e-6, 5.34e-6, 1.94e-5, 2.89e-5,
            3.14e-5, 2.16e-5, 1.10e-5,
            4.40e-6, 5.96e-6, 1.20e-5, 1.98e-5, 1.64e-5, 9.07e-6, 3.77e-6, 3.77e-6,
            7.22e-6, 7.22e-6,
            6.28e-6, 3.77e-6, 3.46e-6, 4.39e-6, 4.71e-6, 4.71e-6, 3.77e-6, 2.18e-6,
            1.09e-6, 1.09e-7,
            4.36e-8, 2.2e-8]
# A3SIG(V=0-4) (V=0 ENERGY=6.169 EV)  AVERAGE ENERGY LOSS =6.725 EV

XTRP1G16 = [6.725, 7.00, 7.80, 8.50, 9.00, 10.0, 11.0, 12.0, 13.0, 14.0,
            16.0, 17.0, 18.0, 20.0, 22.0, 24.0, 26.0, 30.0, 34.0, 40.0,
            50.0, 70.0, 100.
            ]
YTRP1G16 = [0.00, .0035, .0100, .0440, .0280, .0240, .022, .021, .020, .019,
            .016, .015, .014, .013, .0108, .0099, .0087, .0069, .0057, .0046,
            .0033, .0019, .00094
            ]
YTP1MG16 = [0.92, 0.92, 0.92, 0.92, 0.92, 0.92, 0.93, 0.94, 0.94, 0.95,
            0.97, 1.01, 1.07, 1.12, 1.14, 1.16, 1.18, 1.22, 1.21, 1.20,
            1.18, 1.00, 0.92]
# A3SIG(V=5-9) (V=5 ENERGY=7.023 EV) AVERAGE ENERGY LOSS =7.360 EV

XTRP2G16 = [7.360, 7.50, 7.80, 8.50, 9.00, 10.0, 11.0, 12.0, 13.0, 14.0,
            16.0, 17.0, 18.0, 20.0, 22.0, 24.0, 26.0, 30.0, 34.0, 40.0,
            50.0, 70.0, 100.
            ]
YTRP2G16 = [0.00, .0071, .0180, .072, .108, .096, .094, .092, .085, .081,
            .069, .064, .059, .054, .049, .043, .038, .029, .024, .020,
            .0136, .0076, .0040
            ]
YTP2MG16 = [0.92, 0.92, 0.92, 0.92, 0.92, 0.92, 0.93, 0.94, 0.94, 0.95,
            0.97, 1.01, 1.07, 1.12, 1.14, 1.16, 1.18, 1.22, 1.21, 1.20,
            1.18, 1.00, 0.92]
# B3PI(V=0-3) (V=0 ENERGY=7.353 EV) AVERAGE ENERGY LOSS =7.744 EV

XTRP3G16 = [7.744, 8.00, 9.00, 10.0, 11.0, 12.0, 13.0, 14.0, 15.0, 16.0,
            17.0, 18.0, 20.0, 22.0, 26.0, 30.0, 34.0, 40.0, 50.0, 70.0,
            100.
            ]
YTRP3G16 = [.0, .018, .132, .194, .188, .173, .161, .150, .138, .128,
            .116, .108, .089, .077, .063, .053, .047, .035, .026, .0113,
            .0039
            ]
YTP3MG16 = [1.06, 1.06, 1.06, 1.06, 1.12, 1.18, 1.18, 1.16, 1.14, 1.12,
            1.10, 1.08, 1.06, 1.08, 1.12, 1.16, 1.16, 1.17, 1.18, 1.06,
            0.94]
# W3eEL(V=0-5) (V=0 ENERGY=7.362 EV) AVERAGE ENERGY LOSS = 8.050 EV

XTRP4G16 = [8.050, 8.50, 9.00, 10.0, 11.0, 12.0, 14.0, 15.0, 16.0, 17.0,
            18.0, 20.0, 22.0, 24.0, 26.0, 28.0, 30.0, 34.0, 40.0, 50.0,
            70.0, 100.
            ]
YTRP4G16 = [.0, .0010, .007, .016, .023, .030, .044, .050, .053, .053,
            .052, .047, .039, .032, .027, .023, .020, .015, .0112, .0073,
            .00366, .00183
            ]
YTP4MG16 = [1.20, 1.20, 1.20, 1.20, 1.14, 1.08, 1.08, 1.13, 1.16, 1.19,
            1.21, 1.22, 1.23, 1.24, 1.25, 1.26, 1.27, 1.26, 1.23, 1.19,
            1.11, 0.98]
# A3SIG(V=10-21) (V=10 ENERGY=7.790 EV) AVERAGE ENERGY LOSS=8.217 EV

XTRP5G16 = [8.217, 8.30, 8.50, 8.70, 9.00, 10.0, 11.0, 12.0, 13.0, 14.0,
            16.0, 17.0, 18.0, 20.0, 22.0, 24.0, 26.0, 30.0, 34.0, 40.0,
            50.0, 70.0, 100.
            ]
YTRP5G16 = [0.0, .0069, .0365, .0450, .055, .096, .100, .097, .091, .086,
            .073, .066, .060, .055, .050, .044, .038, .031, .024, .020,
            .0145, .0080, .0043
            ]
YTP5MG16 = [0.92, 0.92, 0.92, 0.92, 0.92, 0.92, 0.93, 0.94, 0.94, 0.95,
            0.97, 1.01, 1.07, 1.12, 1.14, 1.16, 1.18, 1.22, 1.21, 1.20,
            1.18, 1.00, 0.92]
# B3PI(V=4-16) (V=4 ENERGY=8.177 EV) AVERAGE ENERGY LOSS= 8.451 EV

XTRP6G16 = [8.451, 8.50, 9.00, 10.0, 11.0, 12.0, 13.0, 14.0, 15.0, 16.0,
            17.0, 18.0, 20.0, 22.0, 26.0, 30.0, 34.0, 40.0, 50.0, 70.0,
            100.
            ]
YTRP6G16 = [.0, .011, .090, .133, .129, .119, .110, .102, .094, .088,
            .079, .074, .061, .053, .044, .037, .032, .023, .017, .0077,
            .0028
            ]
YTP6MG16 = [1.06, 1.06, 1.06, 1.06, 1.12, 1.18, 1.18, 1.16, 1.14, 1.12,
            1.10, 1.08, 1.06, 1.08, 1.12, 1.16, 1.16, 1.17, 1.18, 1.06,
            0.94]
# W3eEL(V=6-10) (V=6 ENERGY=8.419 EV) AVERAGE ENERGY LOSS= 8.729 EV

XTRP7G16 = [8.729, 9.00, 10.0, 11.0, 12.0, 14.0, 15.0, 16.0, 17.0, 18.0,
            20.0, 22.0, 24.0, 26.0, 28.0, 30.0, 34.0, 40.0, 50.0, 70.0,
            100.
            ]
YTRP7G16 = [.0, 0.004, .032, .048, .064, .092, .105, .110, .110,
            .108,
            .097, .082, .066, .056, .048, .041, .032, .023, .0153, .0076,
            .0038
            ]
YTP7MG16 = [1.20, 1.20, 1.20, 1.14, 1.08, 1.08, 1.13, 1.16, 1.19, 1.21,
            1.22, 1.23, 1.24, 1.25, 1.26, 1.27, 1.26, 1.23, 1.19, 1.11,
            0.98]
# A1PI(V=0-3) (V=0 ENERGY=8.549 EV) AVERAGE ENERGY LOSS= 8.950 EV

XSNG1G16 = [8.950, 10.0, 11.0, 12.0, 13.0, 14.0, 15.0, 16.0, 17.0, 18.0,
            19.0, 20.0, 24.0, 27.0, 30.0, 40.0, 50.0, 70.0, 100.
            ]
YSNG1G16 = [.0, .013, .025, .040, .059, .082, .101, .116, .123, .128,
            .130, .130, .125, .119, .112, .087, .071, .051, .036
            ]
YSG1MG16 = [0.80, 0.80, 0.75, 0.70, 0.66, 0.60, 0.55, 0.53, 0.51, 0.50,
            0.49, 0.48, 0.50, 0.52, 0.54, 0.48, 0.41, 0.34, 0.24]
# B'3SIG(V=0-6) (V=0 ENERGY=8.165 EV) AVERAGE ENERGY LOSS= 8.974 EV

XTRP8G16 = [8.974, 9.50, 10.0, 11.0, 12.0, 13.0, 14.0, 15.0, 16.0, 17.0,
            18.0, 19.0, 20.0, 22.0, 26.0, 30.0, 34.0, 40.0, 50.0, 70.0,
            100.
            ]
YTRP8G16 = [.0, .0002, .0010, .0032, .0081, .0136, .0203, .0252, .0274,
            .0274,
            .0264, .0250, .0236, .0209, .0151, .0114, .0089, .0064, .0041, .0020,
            .0010
            ]
YTP8MG16 = [0.90, 0.90, 0.90, 0.90, 0.90, 0.91, 0.93, 0.97, 1.07, 1.17,
            1.22, 1.22, 1.23, 1.26, 1.32, 1.37, 1.35, 1.32, 1.29, 1.20,
            1.04]
# A'1SIG (V=0-6) (V=0 ENERGY=8.398 EV) AVERAGE ENERGY LOSS= 9.191 EV

XSNG2G16 = [9.191, 10.2, 12.0, 13.0, 14.0, 15.0, 16.0, 17.0, 18.0, 19.0,
            20.0, 24.0, 30.0, 40.0, 50.0, 70.0, 100.
            ]
YSNG2G16 = [.0, .0013, .0071, .0106, .0139, .0146, .0145, .0143, .0139,
            .0135,
            .0132, .0105, .0072, .0045, .0031, .0017, .0010
            ]
YSG2MG16 = [1.00, 1.00, 1.00, 1.00, 1.00, 1.00, 1.07, 1.13, 1.14, 1.15,
            1.16, 1.21, 1.27, 1.17, 1.07, 0.93, 0.7]
# W3eEL(V=11-19) (V=11 ENERGY=9.220 EV) AVERAGE ENERGY LOSS= 9.562 EV

XTRP9G16 = [9.562, 10.0, 11.0, 12.0, 14.0, 15.0, 16.0, 17.0, 18.0, 20.0,
            22.0, 24.0, 26.0, 28.0, 30.0, 34.0, 40.0, 50.0, 70.0, 100.
            ]
YTRP9G16 = [.0, .012, .029, .038, .056, .063, .067, .067, .065,
            .058,
            .049, .040, .034, .029, .024, .019, .0141, .0092, .00461, .00230
            ]
YTP9MG16 = [1.20, 1.20, 1.14, 1.08, 1.08, 1.13, 1.16, 1.19, 1.21, 1.22,
            1.23, 1.24, 1.25, 1.26, 1.27, 1.26, 1.23, 1.19, 1.11, 0.98
            # W1eEL(V=0-5) (V=0 ENERGY=8.895 EV) AVERAGE ENERGY LOSS= 9.590 EV
            ]
XSNG3G16 = [9.590, 10.0, 11.0, 12.0, 13.0, 14.0, 15.0, 16.0, 17.0, 18.0,
            20.0, 24.0, 30.0, 40.0, 50.0, 70.0, 100.
            ]
YSNG3G16 = [.0, .0002, .003, .009, .0109, .0144, .0141, .0138, .0134, .013,
            .012, .0094, .0074, .0054, .0043, .0030, .0020
            ]
YSG3MG16 = [1.08, 1.08, 1.08, 1.08, 1.05, 1.00, 0.08, 0.97, 0.96, 0.95,
            0.92, 0.90, 0.86, 0.76, 0.66, 0.55, 0.36]
# A1PI(V=4-15) (V=4 ENERGY=9.355 EV) AVERAGE ENERGY LOSS= 9.665 EV

XSNG4G16 = [9.665, 10.0, 11.0, 12.0, 13.0, 14.0, 15.0, 16.0, 17.0, 18.0,
            19.0, 20.0, 24.0, 27.0, 30.0, 40.0, 50.0, 70.0, 100.
            ]
YSNG4G16 = [.0, .009, .023, .039, .057, .077, .097, .109, .117, .121,
            .123, .124, .119, .112, .106, .083, .067, .048, .034
            ]
YSG4MG16 = [0.80, 0.80, 0.75, 0.70, 0.66, 0.60, 0.55, 0.53, 0.51, 0.50,
            0.49, 0.48, 0.50, 0.52, 0.54, 0.48, 0.41, 0.34, 0.24
            # B'3SIG(V=7-18) (V=7 ENERGY=9.399 EV) AVERAGE ENERGY LOSS= 9.933 EV
            ]
XTRP10G16 = [9.933, 10.2, 11.0, 12.0, 13.0, 14.0, 15.0, 16.0, 17.0, 18.0,
             19.0, 20.0, 22.0, 26.0, 30.0, 34.0, 40.0, 50.0, 70.0, 100.
             ]
YTRP10G16 = [.0, .0010, .0068, .0169, .0284, .0427, .0528, .0575, .0575,
             .0552,
             .0524, .0495, .0438, .0316, .0236, .0187, .0133, .0086, .0041, .0020
             ]
YTP10MG16 = [0.90, 0.90, 0.90, 0.90, 0.90, 0.91, 0.93, 0.97, 1.07, 1.17,
             1.22, 1.22, 1.23, 1.26, 1.32, 1.37, 1.35, 1.32, 1.29, 1.20]
# A'1SIG (V=7-19) (V=7 ENERGY=9.645 EV) AVERAGE ENERGY LOSS= 10.174 EV

XSNG5G16 = [10.174, 10.5, 12.0, 13.0, 14.0, 15.0, 16.0, 17.0, 18.0, 19.0,
            20.0, 24.0, 30.0, 40.0, 50.0, 70.0, 100.
            ]
YSNG5G16 = [.0, .0013, .0129, .0194, .0252, .0267, .0265, .0260, .0253,
            .0247,
            .0240, .0192, .0133, .0081, .0055, .0032, .0017
            ]
YSG5MG16 = [1.00, 1.00, 1.00, 1.00, 1.00, 1.00, 1.07, 1.13, 1.14, 1.15,
            1.16, 1.21, 1.27, 1.17, 1.07, 0.93, 0.72]
# W1eEL(V=6-18) (V=6 ENERGY=9.994 EV) AVERAGE ENERGY LOSS= 10.536 EV

XSNG6G16 = [10.536, 11.0, 12.0, 13.0, 14.0, 15.0, 16.0, 17.0, 18.0, 20.0,
            24.0, 30.0, 40.0, 50.0, 70.0, 100.
            ]
YSNG6G16 = [.0, .003, .009, .0242, .032, .032, .031, .030, .029, .026,
            .021, .0164, .0121, .0096, .0066, .0046
            ]
YSG6MG16 = [1.08, 1.08, 1.08, 1.05, 1.00, 0.08, 0.97, 0.96, 0.95, 0.92,
            0.90, 0.86, 0.76, 0.66, 0.55, 0.36]
# C3PI(V=0-4) (V=0 ENERGY=11.032 EV) AVERAGE ENERGY LOSS= 11.188 EV

XTRP11G16 = [11.188, 12.0, 12.5, 13.0, 13.5, 14.0, 14.5, 15.0, 16.0, 17.0,
             18.0, 19.0, 20.0, 24.0, 30.0, 40.0, 50.0, 70.0, 100.
             ]
YTRP11G16 = [.0, .057, .089, .130, .180, .225, .235, .225, .205, .190,
             .170, .155, .140, .105, .074, .044, .031, .015, .0057
             ]
YTP11MG16 = [1.03, 1.03, 1.03, 1.03, 1.03, 1.03, 1.03, 1.03, 1.02, 1.01,
             1.00, 0.99, 0.99, 1.06, 1.14, 1.11, 1.09, 0.93, 0.70
             # E3SIG  V=0
             ]
XTRP12G16 = [11.875, 11.9, 11.95, 12.0, 12.5, 13.0, 14.0, 15.0, 16.0, 17.0,
             18.0, 19.0, 20.0, 21.0, 25.0, 30.0, 35.0, 40.0, 45.0, 50.0,
             70.0, 100.
             ]
YTRP12G16 = [.0, .157, .127, .101, .031, .021, .009, .003, .002, .004,
             .008, .011, .013, .013, .010, .008, .005, .0037, .0027, .002,
             .0010, .0004
             ]
YTP12MG16 = [1.0 for i in range(22)]
# A''1SIG(V=0-1) (V=0 ENERGY=12.255 EV)  AVERAGE ENERGY LOSS= 12.289 EV

XSNG7G16 = [12.289, 13.0, 14.0, 15.0, 17.5, 20.0, 24.0, 30.0, 40.0, 50.0,
            70.0, 100.
            ]
YSNG7G16 = [.0, .002, .005, .011, .022, .034, .037, .036, .031, .028,
            .020, .0125
            ]
YSG7MG16 = [0.86, 0.86, 0.86, 0.86, 0.86, 0.91, 0.94, 0.99, 0.94, 0.89,
            0.73, 0.50
            # B1PI (V=0-6) (V=0 ENERGY=12.500 EV) AVERAGE ENERGY LOSS= 12.781 EV
            #  USE BEF SCALING ABOVE 100EV                   F=0.1855
            ]
XSNG8G16 = [12.781, 17.5, 20.0, 30.0, 40.0, 50.0, 70.0, 100.
            ]
YSNG8G16 = [0.0, .0640, .0855, .145, .160, .163, .160, .152
            ]
YSG8MG16 = [0.76, 0.76, 0.67, 0.46, 0.34, 0.22, 0.13, 0.05
            # C'1SIG (V=0-3) (V=0 ENERGY=12.934 EV) AVERAGE ENERGY LOSS= 13.000 EV
            #  USE BEF SCALING ABOVE 500EV                  F=0.15
            ]
XSNG9G16 = [13.000, 17.5, 20.0, 30.0, 40.0, 50.0, 70.0, 100., 150., 200.,
            250., 300., 350., 400., 450., 500.
            ]
YSNG9G16 = [0.0, .0300, .0440, .067, .086, .093, .102, .100, .091, .083,
            .075, .069, .063, .059, .054, .052
            ]
YSG9MG16 = [0.72, 0.72, 0.47, 0.41, 0.32, 0.23, 0.13, 0.05, 0.04, 0.03,
            .028, .025, .022, .020, .018, .016
            # G3 PI (V=0-3) (V=0 ENERGY=12.810 EV) AVERAGE ENERGY LOSS=13.001 EV
            ]
XTRP13G16 = [13.001, 17.5, 20.0, 23.0, 26.0, 30.0, 40.0, 50.0, 70.0, 100.
             ]
YTRP13G16 = [.0, .0133, .0178, .0204, .0207, .0199, .0174, .0152, .0115,
             .0065
             ]
YTP13MG16 = [0.74, 0.74, 0.73, 0.72, 0.71, 0.69, 0.61, 0.53, 0.47, 0.40
             # C3 1PI ( V=0-3) V=0 ENERGY=12.912 AVERAGE ENERGY LOSS= 13.076 EV
             #  USE BEF SCALING ABOVE 100EV        F=0.15
             ]
XSNG10G16 = [13.076, 17.5, 20.0, 30.0, 40.0, 50.0, 70.0, 100.
             ]
YSNG10G16 = [0.0, .0470, .060, .100, .118, .124, .124, .118
             ]
YSG10MG16 = [0.69, 0.69, 0.55, 0.40, 0.28, 0.16, 0.11, 0.05
             # F3 PI (V=0-3) (V=0 ENERGY=12.985 EV) AVERAGE ENERGY LOSS=13.174 EV
             ]
XTRP14G16 = [13.174, 17.5, 20.0, 23.0, 26.0, 30.0, 40.0, 50.0, 70.0, 100.
             ]
YTRP14G16 = [.0, .0062, .0091, .0129, .0140, .0136, .0119, .0102, .0074,
             .0040
             ]
YTP14MG16 = [0.74, 0.74, 0.76, 0.71, 0.65, 0.63, 0.53, 0.43, 0.40, 0.34
             # B1PI (V=7-14) (V=7 ENERGY=13.156 EV) AVERAGE ENERGY LOSS= 13.338 EV
             # USE BEF SCALING ABOVE 100EV      F=0.0663
             ]
XSNG11G16 = [13.338, 17.5, 20.0, 30.0, 40.0, 50.0, 70.0, 100.
             ]
YSNG11G16 = [0.0, .0120, .0288, .047, .052, .055, .054, .0503
             ]
YSG11MG16 = [0.76, 0.76, 0.67, 0.46, 0.34, 0.22, 0.13, 0.05
             # B! 1SIG (V=0-10) V=0 ENERGY=12.854 AVERAGE ENERGY LOSS= 13.385 EV
             #  USE BEF SCALING ABOVE 100EV             F=0.0601
             ]
XSNG12G16 = [13.385, 17.5, 20.0, 30.0, 40.0, 50.0, 70.0, 100.
             ]
YSNG12G16 = [0.0, .0156, .027, .037, .046, .048, .048, .046
             ]
YSG12MG16 = [0.81, 0.81, 0.71, 0.47, 0.33, 0.20, 0.15, 0.09
             # O3 1PI (V=0-5) (V=0 ENERGY=13.103 EV) AVERAGE ENERGY LOSS= 13.628 EV
             # USE BEF SCALING ABOVE 100EV      F=0.0828
             ]
XSNG13G16 = [13.628, 17.5, 20.0, 30.0, 40.0, 50.0, 70.0, 100.
             ]
YSNG13G16 = [0.0, .0140, .028, .051, .060, .063, .065, .061
             ]
YSG13MG16 = [0.86, 0.86, 0.77, 0.60, 0.45, 0.30, 0.19, 0.08
             # C! 1SIG (V=4-6)  (V=4 ENERGY=13.982 EV)  AVERAGE ENERGY LOSS=14.090
             # USE BEF SCALING ABOVE 100EV     F=0.139
             ]
XSNG14G16 = [14.090, 17.5, 20.0, 30.0, 40.0, 50.0, 70.0, 100.
             ]
YSNG14G16 = [0.0, .030, .045, .081, .096, .102, .103, .097
             ]
YSG14MG16 = [0.85, 0.85, 0.75, 0.55, 0.40, 0.25, 0.17, 0.08
             # B! 1SIG (V=11-INF) (V=11 ENERGY=13.84 EV)
             #  AVERAGE ENERGY LOSS=14.232 EV      (CONSISTENT WITH BERKOWITZ)
             #  USE BEF SCALING ABOVE 100EV            F=0.265
             #  TOTAL TRANSITION STRENGTH FOR B! 1SIG= 0.265 + 0.0601=0.3301
             ]
XSNG15G16 = [14.232, 17.5, 20.0, 30.0, 40.0, 50.0, 70.0, 100.
             ]
YSNG15G16 = [0.0, .055, .083, .151, .180, .191, .194, .182
             ]
YSG15MG16 = [0.81, 0.81, 0.71, 0.47, 0.33, 0.20, 0.15, 0.09]
#
# E! 1SIG  ENERGY LOSS=14.36EV        F=0.0108  (BERKOWITZ)
#  USE BEF SCALING IN SUBROUTINE
#
# E 1PI   ENERGY LOSS=14.45EV         F=0.0237   (BERKOWITZ)
# USE BEF SCALING IN SUBROUTINE
#
# SINGLET  ENERGY LOSS=14.839EV       F=0.0117  (BERKOWITZ)
# USE BEF SCALING IN SUBROUTINE
#
#  SUM OF HIGH ENERGY SINGLETS   ENERGY LOSS=15.2  F=0.1152
# USE BEF SCALING IN SUBROUTINE
#
# SUM OF EXCITATIONS TO EXCITEe IONS ANe MOLECULAR BREAKUP.
#    ENERGY LOSS=15.5EV
# USE BEF SCALING                F=1.30
#
# RAP UP TO 100 EV THEN LINeSAY TO 1KEV THEN SCHRAM TO 20KEV
# ABOVE 20KEV USE MATRIX ELEMENTS COMPATIBLE WITH RIEKE ANe BERKOWITZ

XIONG16 = [15.581, 16.0, 16.5, 17.0, 17.5, 18.0, 18.5, 19.0, 19.5, 20.0,
           20.5, 21.0, 21.5, 22.0, 22.5, 23.0, 23.5, 24.0, 24.5, 25.0,
           25.5, 26.0, 28.0, 30.0, 32.0, 34.0, 36.0, 38.0, 40.0, 45.0,
           50.0, 55.0, 60.0, 65.0, 70.0, 75.0, 80.0, 85.0, 90.0, 95.0,
           100., 110., 120., 140., 160., 180., 200., 225., 250., 275.,
           300., 350., 400., 450., 500., 550., 600., 650., 700., 750.,
           800., 850., 900., 950., 1000., 1200., 1400., 1600., 1800., 2000.,
           2500., 3000., 3500., 4000., 4500., 5000., 5500., 6000., 7000., 8000.,
           9000., 10000., 12000., 14000., 16000., 18000., 20000.]
# COUNTING IONISATION

YIONG16 = [0.00, .0211, .0466, .0713, .0985, .129, .164, .199, .230, .270,
           .308, .344, .380, .418, .455, .492, .528, .565, .603, .640,
           .677, .714, .875, 1.03, 1.15, 1.27, 1.38, 1.49, 1.57, 1.78,
           1.94, 2.07, 2.18, 2.27, 2.33, 2.39, 2.44, 2.46, 2.49, 2.51,
           2.51, 2.50, 2.48, 2.45, 2.36, 2.28, 2.19, 2.08, 1.98, 1.89,
           1.82, 1.68, 1.56, 1.45, 1.36, 1.28, 1.20, 1.12, 1.07, 1.01,
           .971, .936, .907, .879, .847, .728, .649, .585, .534, .491,
           .408, .351, .310, .280, .255, .233, .217, .200, .178, .159,
           .144, .132, .113, .0998, .0898, .0824, .0752]
# IONISATION TO N2+    ASYMPTOTIC 79.73% OF COUNTING IONISATION

XION1G16 = [15.581, 16.0, 16.5, 17.0, 17.5, 18.0, 18.5, 19.0, 19.5, 20.0,
            20.5, 21.0, 21.5, 22.0, 22.5, 23.0, 23.5, 24.0, 24.5, 25.0,
            25.5, 26.0, 28.0, 30.0, 32.0, 34.0, 36.0, 38.0, 40.0, 45.0,
            50.0, 55.0, 60.0, 65.0, 70.0, 75.0, 80.0, 85.0, 90.0, 95.0,
            100., 110., 120., 140., 160., 180., 200., 225., 250., 275.,
            300., 350., 400., 450., 500., 550., 600., 650., 700., 750.,
            800., 850., 900., 950., 1000., 1200., 1400., 1600., 1800., 2000.,
            2500., 3000., 3500., 4000., 4500., 5000., 5500., 6000., 7000., 8000.,
            9000., 10000., 12000., 14000., 16000., 18000., 20000.
            ]
YION1G16 = [0.00, .0211, .0466, .0713, .0985, .129, .164, .199, .230, .270,
            .308, .344, .380, .418, .455, .492, .528, .565, .603, .640,
            .677, .714, .865, .929, 1.03, 1.12, 1.20, 1.29, 1.37, 1.52,
            1.60, 1.66, 1.72, 1.74, 1.78, 1.80, 1.81, 1.82, 1.83, 1.85,
            1.85, 1.83, 1.81, 1.78, 1.72, 1.67, 1.61, 1.55, 1.48, 1.41,
            1.37, 1.28, 1.20, 1.11, 1.05, .998, .943, .880, .844, .796,
            .765, .738, .719, .698, .676, .580, .517, .466, .426, .391,
            .325, .280, .247, .223, .203, .186, .173, .159, .142, .127,
            .115, .105, .0901, .0796, .0716, .0657, .0600]
# IONISATION TO N+   ASYMPTOTIC 19.70% OF COUNTING IONISATION

XION2G16 = [24.294, 28.0, 30.0, 35.0, 40.0, 45.0, 50.0, 55.0, 60.0, 65.0,
            70.0, 75.0, 80.0, 85.0, 90.0, 95.0, 100., 110., 120., 140.,
            160., 180., 200., 225., 250., 275., 300., 350., 400., 450.,
            500., 550., 600., 650., 700., 750., 800., 850., 900., 950.,
            1000., 1200., 1400., 1600., 1800., 2000., 2500., 3000., 3500., 4000.,
            4500., 5000., 5500., 6000., 7000., 8000., 9000., 10000., 12000., 14000.,
            16000., 18000., 20000.
            ]
YION2G16 = [0.0, .010, .0325, .0904, .166, .245, .319, .390, .438, .482,
            .523, .561, .587, .605, .632, .645, .656, .660, .661, .652,
            .633, .595, .566, .516, .493, .458, .438, .393, .351, .324,
            .299, .274, .248, .234, .217, .205, .200, .192, .183, .176,
            .167, .143, .128, .115, .105, .0967, .0804, .0691, .0611, .0552,
            .0502, .0459, .0427, .0394, .0351, .0313, .0284, .0260, .0223, .0197,
            .0177, .0162, .0148]
# IONISATION TO N+ + N+  NORMALISEe TIAN ANe VIeAL
#  ASYMPTOTIC 3.38% OF COUNTING IONISATION

XION3G16 = [38.8, 45.0, 50.0, 60.0, 70.0, 80.0, 90.0, 100., 125., 150.,
            175., 200., 225., 250., 275., 300., 350., 400., 450., 500.,
            550., 600., 700., 800., 900., 1000., 1200., 1400., 1600., 1800.,
            2000., 2500., 3000., 3500., 4000., 4500., 5000., 5500., 6000., 7000.,
            8000., 9000., 10000., 12000., 14000., 16000., 18000., 20000.
            ]
YION3G16 = [0.0, .00917, .0199, .0378, .0617, .0827, .0991, .109, .119,
            .117,
            .112, .105, .0982, .0917, .0842, .0778, .0676, .0596, .0533, .0475,
            .0439, .0426, .0373, .0343, .0314, .0287, .0246, .0220, .0197, .0180,
            .0166, .0138, .0119, .0105, .00948, .00862, .00788, .00733, .00676, .00603,
            .00537, .00488, .00446, .00383, .00338, .00304, .00278, .0025]
# IONISATION TO N++  ASYMPTOTIC  0.57% OF COUNTING IONISATION

XION4G16 = [65.0, 70.0, 75.0, 80.0, 85.0, 90.0, 95.0, 100., 110., 120.,
            140., 160., 180., 200., 225., 250., 275., 300., 350., 400.,
            450., 500., 550., 600., 650., 700., 750., 800., 850., 900.,
            950., 1000., 1200., 1400., 1600., 1800., 2000., 2500., 3000., 3500.,
            4000., 4500., 5000., 5500., 6000., 7000., 8000., 9000., 10000., 12000.,
            14000., 16000., 18000., 20000.
            ]
YION4G16 = [0.0, .000171, .000658, .00122, .00204, .00328, .00439, .00495,
            .00725, .00927,
            .0122, .0137, .0154, .0154, .0154, .0142, .0141, .0128, .0117, .0103,
            .00940, .00808, .00796, .00760, .00701, .00649, .00587, .00594, .00543,
            .00522,
            .00505, .00485, .00415, .00370, .00333, .00304, .00280, .00233, .00200,
            .00177,
            .00160, .00145, .00133, .00124, .00114, .00101, .000906, .000821, .000752,
            .000644,
            .000569, .000512, .000470, .000429]
# NITROGEN K-SHELL IONISATION (MULTIPLY BY 2 FOR MOLECULE)

XKSHG16 = [401.6, 407., 419., 431., 444., 457., 471., 485., 499., 515.,
           530., 546., 562., 596., 631., 668., 708., 750., 794., 841.,
           891., 944., 1000., 1090., 1188., 1296., 1496., 1679., 1884., 2054.,
           2238., 2512., 2985., 3758., 4467., 5158., 5957., 7079., 1.0e4, 1.26e4,
           1.50e4, 2.05e4, 2.51e4, 3.07e4, 4.10e4, 5.01e4, 6.13e4, 7.08e4, 8.18e4,
           1.0e5,
           1.54e5, 2.05e5, 2.99e5, 4.10e5, 5.01e5, 6.13e5, 7.08e5, 8.18e5, 1.00e6,
           1.25e6,
           1.50e6, 2.05e6, 3.07e6, 4.10e6, 5.01e6, 6.13e6, 7.08e6, 8.18e6, 1.00e7,
           1.22e7,
           1.50e7, 1.88e7, 2.24e7, 2.82e7, 3.76e7, 4.87e7, 6.31e7, 8.66e7, 1.00e8,
           1.22e8,
           1.50e8, 1.88e8, 2.24e8, 2.82e8, 3.76e8, 4.87e8, 6.31e8, 8.66e8, 1.00e9]

YKSHG16 = [0.00, 4.11e-5, 1.38e-4, 2.32e-4, 3.23e-4, 4.12e-4, 4.98e-4,
           5.81e-4, 6.61e-4, 7.38e-4,
           8.13e-4, 8.85e-4, 9.54e-4, 1.08e-3, 1.20e-3, 1.31e-3, 1.41e-3, 1.50e-3,
           1.58e-3, 1.65e-3,
           1.72e-3, 1.77e-3, 1.82e-3, 1.87e-3, 1.91e-3, 1.94e-3, 1.95e-3, 1.93e-3,
           1.89e-3, 1.86e-3,
           1.81e-3, 1.74e-3, 1.63e-3, 1.45e-3, 1.32e-3, 1.22e-3, 1.12e-3, 1.00e-3,
           7.95e-4, 6.77e-4,
           5.98e-4, 4.74e-4, 4.09e-4, 3.52e-4, 2.85e-4, 2.47e-4, 2.14e-4, 1.94e-4,
           1.76e-4, 1.54e-4,
           1.19e-4, 1.03e-4, 8.77e-5, 7.92e-5, 7.54e-5, 7.27e-5, 7.14e-5, 7.04e-5,
           6.97e-5, 6.96e-5,
           7.00e-5, 7.16e-5, 7.47e-5, 7.74e-5, 7.95e-5, 8.17e-5, 8.34e-5, 8.51e-5,
           8.75e-5, 9.00e-5,
           9.25e-5, 9.54e-5, 9.76e-5, 1.01e-4, 1.04e-4, 1.08e-4, 1.11e-4, 1.15e-4,
           1.17e-4, 1.20e-4,
           1.22e-4, 1.25e-4, 1.27e-4, 1.31e-4, 1.34e-4, 1.38e-4, 1.41e-4, 1.45e-4,
           1.47e-4]
# BREMSSTRAHLUNG X-SECTION WITH CUT OFF UNITS 10**-24 M**2

Z7TG16 = [385., 234., 113., 63.5, 35.5, 16.4, 9.48, 5.96, 4.07, 3.73,
          3.81, 3.93, 4.04, 4.11, 4.18, 4.26, 4.33, 4.42, 4.48, 4.55,
          4.59, 4.61, 4.63, 4.64, 4.65]

EBRMG16 = [1000., 2000., 5000., 1.E4, 2.E4, 5.E4, 1.E5, 2.E5, 5.E5, 1.E6,
           2.E6, 3.E6, 4.E6, 5.E6, 6.E6, 8.E6, 1.E7, 1.5E7, 2.E7, 3.E7,
           4.E7, 5.E7, 6.E7, 8.E7, 1.E8
           ]

gd['gas16/XELA'] = XELAG16
gd['gas16/YELA'] = YELAG16
gd['gas16/YMOM'] = YMOMG16
gd['gas16/YEPS'] = YEPSG16
gd['gas16/XROT'] = XROTG16
gd['gas16/YROT'] = YROTG16
gd['gas16/XVB1'] = XVB1G16
gd['gas16/YVB1'] = YVB1G16
gd['gas16/XVB2'] = XVB2G16
gd['gas16/YVB2'] = YVB2G16
gd['gas16/XVB3'] = XVB3G16
gd['gas16/YVB3'] = YVB3G16
gd['gas16/XVB4'] = XVB4G16
gd['gas16/YVB4'] = YVB4G16
gd['gas16/XVB5'] = XVB5G16
gd['gas16/YVB5'] = YVB5G16
gd['gas16/XVB6'] = XVB6G16
gd['gas16/YVB6'] = YVB6G16
gd['gas16/XVB7'] = XVB7G16
gd['gas16/YVB7'] = YVB7G16
gd['gas16/XVB8'] = XVB8G16
gd['gas16/YVB8'] = YVB8G16
gd['gas16/XVB9'] = XVB9G16
gd['gas16/YVB9'] = YVB9G16
gd['gas16/XVB10'] = XVB10G16
gd['gas16/YVB10'] = YVB10G16
gd['gas16/XVB11'] = XVB11G16
gd['gas16/YVB11'] = YVB11G16
gd['gas16/XVB12'] = XVB12G16
gd['gas16/YVB12'] = YVB12G16
gd['gas16/XVB13'] = XVB13G16
gd['gas16/YVB13'] = YVB13G16
gd['gas16/XVB14'] = XVB14G16
gd['gas16/YVB14'] = YVB14G16
gd['gas16/XVB15'] = XVB15G16
gd['gas16/YVB15'] = YVB15G16
gd['gas16/XTRP1'] = XTRP1G16
gd['gas16/YTRP1'] = YTRP1G16
gd['gas16/YTP1M'] = YTP1MG16
gd['gas16/XTRP2'] = XTRP2G16
gd['gas16/YTRP2'] = YTRP2G16
gd['gas16/YTP2M'] = YTP2MG16
gd['gas16/XTRP3'] = XTRP3G16
gd['gas16/YTRP3'] = YTRP3G16
gd['gas16/YTP3M'] = YTP3MG16
gd['gas16/XTRP4'] = XTRP4G16
gd['gas16/YTRP4'] = YTRP4G16
gd['gas16/YTP4M'] = YTP4MG16
gd['gas16/XTRP5'] = XTRP5G16
gd['gas16/YTRP5'] = YTRP5G16
gd['gas16/YTP5M'] = YTP5MG16
gd['gas16/XTRP6'] = XTRP6G16
gd['gas16/YTRP6'] = YTRP6G16
gd['gas16/YTP6M'] = YTP6MG16
gd['gas16/XTRP7'] = XTRP7G16
gd['gas16/YTRP7'] = YTRP7G16
gd['gas16/YTP7M'] = YTP7MG16
gd['gas16/XTRP8'] = XTRP8G16
gd['gas16/YTRP8'] = YTRP8G16
gd['gas16/YTP8M'] = YTP8MG16
gd['gas16/XTRP9'] = XTRP9G16
gd['gas16/YTRP9'] = YTRP9G16
gd['gas16/YTP9M'] = YTP9MG16
gd['gas16/XTRP10'] = XTRP10G16
gd['gas16/YTRP10'] = YTRP10G16
gd['gas16/YTP10M'] = YTP10MG16
gd['gas16/XTRP11'] = XTRP11G16
gd['gas16/YTRP11'] = YTRP11G16
gd['gas16/YTP11M'] = YTP11MG16
gd['gas16/XTRP12'] = XTRP12G16
gd['gas16/YTRP12'] = YTRP12G16
gd['gas16/YTP12M'] = YTP12MG16
gd['gas16/XTRP13'] = XTRP13G16
gd['gas16/YTRP13'] = YTRP13G16
gd['gas16/YTP13M'] = YTP13MG16
gd['gas16/XTRP14'] = XTRP14G16
gd['gas16/YTRP14'] = YTRP14G16
gd['gas16/YTP14M'] = YTP14MG16
gd['gas16/XSNG1'] = XSNG1G16
gd['gas16/YSNG1'] = YSNG1G16
gd['gas16/YSG1M'] = YSG1MG16
gd['gas16/XSNG2'] = XSNG2G16
gd['gas16/YSNG2'] = YSNG2G16
gd['gas16/YSG2M'] = YSG2MG16
gd['gas16/XSNG3'] = XSNG3G16
gd['gas16/YSNG3'] = YSNG3G16
gd['gas16/YSG3M'] = YSG3MG16
gd['gas16/XSNG4'] = XSNG4G16
gd['gas16/YSNG4'] = YSNG4G16
gd['gas16/YSG4M'] = YSG4MG16
gd['gas16/XSNG5'] = XSNG5G16
gd['gas16/YSNG5'] = YSNG5G16
gd['gas16/YSG5M'] = YSG5MG16
gd['gas16/XSNG6'] = XSNG6G16
gd['gas16/YSNG6'] = YSNG6G16
gd['gas16/YSG6M'] = YSG6MG16
gd['gas16/XSNG7'] = XSNG7G16
gd['gas16/YSNG7'] = YSNG7G16
gd['gas16/YSG7M'] = YSG7MG16
gd['gas16/XSNG8'] = XSNG8G16
gd['gas16/YSNG8'] = YSNG8G16
gd['gas16/YSG8M'] = YSG8MG16
gd['gas16/XSNG9'] = XSNG9G16
gd['gas16/YSNG9'] = YSNG9G16
gd['gas16/YSG9M'] = YSG9MG16
gd['gas16/XSNG10'] = XSNG10G16
gd['gas16/YSNG10'] = YSNG10G16
gd['gas16/YSG10M'] = YSG10MG16
gd['gas16/XSNG11'] = XSNG11G16
gd['gas16/YSNG11'] = YSNG11G16
gd['gas16/YSG11M'] = YSG11MG16
gd['gas16/XSNG12'] = XSNG12G16
gd['gas16/YSNG12'] = YSNG12G16
gd['gas16/YSG12M'] = YSG12MG16
gd['gas16/XSNG13'] = XSNG13G16
gd['gas16/YSNG13'] = YSNG13G16
gd['gas16/YSG13M'] = YSG13MG16
gd['gas16/XSNG14'] = XSNG14G16
gd['gas16/YSNG14'] = YSNG14G16
gd['gas16/YSG14M'] = YSG14MG16
gd['gas16/XSNG15'] = XSNG15G16
gd['gas16/YSNG15'] = YSNG15G16
gd['gas16/YSG15M'] = YSG15MG16
gd['gas16/XKSH'] = XKSHG16
gd['gas16/YKSH'] = YKSHG16
gd['gas16/XION'] = XIONG16
gd['gas16/YION'] = YIONG16
gd['gas16/XION1'] = XION1G16
gd['gas16/YION1'] = YION1G16
gd['gas16/XION2'] = XION2G16
gd['gas16/YION2'] = YION2G16
gd['gas16/XION3'] = XION3G16
gd['gas16/YION3'] = YION3G16
gd['gas16/XION4'] = XION4G16
gd['gas16/YION4'] = YION4G16
gd['gas16/Z7T'] = Z7TG16
gd['gas16/EBRM'] = EBRMG16

# ELASTIC MT

XELMG21 = [0.00, .001, .0012, .0015, .0018, .002, .0025, .003, .004, .005,
           .006, .007, .008, .009, .010, .012, .015, .018, .020, .025,
           0.03, 0.04, 0.05, 0.06, 0.07, 0.08, 0.09, 0.10, 0.12, 0.15,
           0.18, 0.20, 0.25, 0.30, 0.40, 0.50, 0.60, 0.70, 0.80, 0.90,
           1.00, 1.20, 1.50, 1.80, 2.00, 2.50, 3.00, 4.00, 5.00, 6.00,
           7.00, 8.00, 9.00, 10.0, 12.0, 15.0, 18.0, 20.0, 25.0, 30.0,
           40.0, 50.0, 60.0, 70.0, 80.0, 90.0, 100., 125., 150., 175.,
           200., 250., 300., 350., 400., 450., 500., 600., 700., 800.,
           900., 1000., 1250., 1500., 1750., 2000., 2500., 3000., 3500., 4000.,
           4500., 5000., 6000., 7000., 8000., 9000., 1.0e4, 1.25e4, 1.5e4, 1.75e4,
           2.0e4, 2.5e4, 3.0e4, 3.5e4, 4.0e4, 4.5e4, 5.0e4, 6.0e4, 7.0e4, 8.0e4,
           9.0e4, 1.0e5, 1.25e5, 1.5e5, 1.75e5, 2.0e5, 2.5e5, 3.0e5, 3.5e5, 4.0e5,
           4.5e5, 5.0e5, 6.0e5, 7.0e5, 8.0e5, 9.0e5, 1.0e6, 1.25e6, 1.5e6, 1.75e6,
           2.0e6, 2.5e6, 3.0e6, 3.5e6, 4.0e6, 4.5e6, 5.0e6, 6.0e6, 7.0e6, 8.0e6,
           9.0e6, 1.0e7, 1.25e7, 1.5e7, 1.75e7, 2.0e7, 2.5e7, 3.0e7, 3.5e7, 4.0e7,
           4.5e7, 5.0e7, 6.0e7, 7.0e7, 8.0e7, 9.0e7, 1.0e8, 1.25e8, 1.5e8, 1.75e8,
           2.0e8, 2.5e8, 3.0e8, 3.5e8, 4.0e8, 4.5e8, 5.0e8, 6.0e8, 7.0e8, 8.0e8,
           9.0e8, 1.0e9
           ]
YELMG21 = [7.24, 7.25, 7.26, 7.26, 7.27, 7.28, 7.30, 7.35, 7.38, 7.45,
           7.48, 7.54, 7.59, 7.64, 7.70, 7.78, 7.90, 8.04, 8.14, 8.33,
           8.56, 8.93, 9.27, 9.54, 9.79, 10.04, 10.25, 10.47, 10.86, 11.35,
           11.78, 12.02, 12.54, 13.00, 13.81, 14.52, 15.16, 15.66, 16.17, 16.58,
           17.01, 17.70, 18.05, 18.05, 17.70, 16.60, 15.35, 12.85, 10.90, 9.450,
           8.20, 7.20, 6.30, 5.60, 4.45, 3.275, 2.529, 2.154, 1.476, 1.100,
           .702, .505, .375, .295, .238, .195, .170, .116, .0868, .0662,
           .0524, .0353, .0256, .0195, .0154, .0125, .0103, .00747, .00567, .00446,
           .00361, .00299, .0020, .00144, .00109, 8.53e-4, 5.69e-4, 4.08e-4, 3.08e-4,
           2.41e-4,
           1.94e-4, 1.60e-4, 1.15e-4, 8.65e-5, 6.77e-5, 5.45e-5, 4.49e-5, 2.98e-5,
           2.13e-5, 1.60e-5,
           1.26e-5, 8.34e-6, 5.97e-6, 4.51e-6, 3.54e-6, 2.86e-6, 2.36e-6, 1.70e-6,
           1.29e-6, 1.02e-6,
           8.26e-7, 6.86e-7, 4.65e-7, 3.40e-7, 2.62e-7, 2.09e-7, 1.44e-7, 1.07e-7,
           8.37e-8, 6.76e-8,
           5.62e-8, 4.76e-8, 3.58e-8, 2.82e-8, 2.30e-8, 1.92e-8, 1.63e-8, 1.15e-8,
           8.67e-9, 6.80e-9,
           5.49e-9, 3.83e-9, 2.84e-9, 2.20e-9, 1.76e-9, 1.44e-9, 1.20e-9, 8.79e-10,
           6.72e-10, 5.31e-10,
           4.31e-10, 3.57e-10, 2.39e-10, 1.72e-10, 1.30e-10, 1.02e-10, 6.74e-11,
           4.81e-11, 3.61e-11, 2.81e-11,
           2.25e-11, 1.85e-11, 1.31e-11, 9.76e-12, 7.57e-12, 6.04e-12, 4.93e-12,
           3.20e-12, 2.24e-12, 1.66e-12,
           1.27e-12, 8.18e-13, 5.70e-13, 4.19e-13, 3.21e-13, 2.54e-13, 2.06e-13,
           1.43e-13, 1.05e-13, 8.06e-14,
           6.37e-14, 5.16e-14]
# ELASTIC ANGULAR eISTRIBUTION FUNCTION EPSILON
# EPSILON =1-YEPS

YEPSG21 = [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.00204, 1.00406, 1.00403,
           1.00402, 1.00799, 1.01195, 1.01587, 1.01974, 1.02548, 1.03497, 1.04613,
           1.05537, 1.07162,
           1.09485, 1.11355, 1.13538, 1.15360, 1.16779, 1.18516, 1.19550, 1.20711,
           1.22691, 1.25186,
           1.27686, 1.29241, 1.29958, 1.33194, 1.36128, 1.39254, 1.42965, 1.43614,
           1.42939, 1.42749,
           1.44093, 1.43942, 1.39970, 1.34691, 1.29121, 1.15375, 1.03498, 0.81607,
           0.68293, 0.59997,
           0.53826, 0.48433, 0.43796, 0.41063, 0.36112, 0.31690, 0.28482, 0.26105,
           0.20648, 0.18652,
           0.14951, 0.13589, 0.11425, 0.10223, 0.09743, 0.08175, 0.08042, 0.06877,
           0.06127, 0.05204,
           0.04596, 0.03674, 0.02996, 0.02695, 0.02487, 0.02173, 0.01973, 0.01733,
           0.01536, 0.01371,
           .012395, .011378, .009183, .007832, .006527, .005948, .004772, .004142,
           .003545, .003086,
           .002742, .002452, .002049, .001748, .001525, .001351, .001215, .0009666,
           .0007993, .0006810,
           5.977e-4, 4.724e-4, 3.896e-4, 3.326e-4, 2.893e-4, 2.544e-4, 2.282e-4,
           1.866e-4, 1.581e-4, 1.370e-4,
           1.199e-4, 1.066e-4, 8.29e-5, 6.72e-5, 5.63e-5, 4.80e-5, 3.65e-5, 2.91e-5,
           2.40e-5, 2.02e-5,
           1.73e-5, 1.50e-5, 1.17e-5, 9.40e-6, 7.77e-6, 6.54e-6, 5.59e-6, 3.98e-6,
           2.99e-6, 2.33e-6,
           1.87e-6, 1.28e-6, 9.38e-7, 7.15e-7, 5.64e-7, 4.56e-7, 3.77e-7, 2.70e-7,
           2.02e-7, 1.57e-7,
           1.26e-7, 1.03e-7, 6.74e-8, 4.74e-8, 3.52e-8, 2.72e-8, 1.76e-8, 1.23e-8,
           9.05e-9, 6.95e-9,
           5.50e-9, 4.46e-9, 3.10e-9, 2.28e-9, 1.74e-9, 1.37e-9, 1.11e-9, 7.04e-10,
           4.85e-10, 3.53e-10,
           2.67e-10, 1.68e-10, 1.15e-10, 8.3e-11, 6.3e-11, 4.9e-11, 4.0e-11,
           2.7e-11, 2.0e-11, 1.5e-11,
           1.2e-11, 9.0e-12]
# ELASTIC FROM 100EV

YELTG21 = [7.24, 7.25, 7.26, 7.26, 7.27, 7.28, 7.30, 7.36, 7.40, 7.43,
           7.46, 7.50, 7.53, 7.56, 7.60, 7.65, 7.72, 7.80, 7.85, 7.95,
           8.05, 8.30, 8.50, 8.65, 8.80, 8.93, 9.06, 9.19, 9.42, 9.70,
           9.92, 10.03, 10.42, 10.60, 11.07, 11.43, 11.68, 12.02, 12.46, 12.79,
           13.02, 13.56, 14.15, 14.59, 14.78, 15.05, 15.00, 14.66, 13.90, 13.05,
           12.10, 11.33, 10.54, 9.744, 8.375, 6.678, 5.508, 4.952, 3.931, 3.125,
           2.299, 1.760, 1.465, 1.241, 1.034, 0.954, 0.841, 0.639, 0.518, 0.443,
           .383, .303, .255, .210, .176, .158, .140, .112, .0932, .0800,
           .070, .062, .049, .040, .035, .0295, .0235, .0189, .0162, .0142,
           .0126, .0114, .00951, .00817, .00717, .00639, .00576, .00464, .00390,
           .00336,
           .00296, .00240, .00203, .00176, .00156, .00141, .00128, .00110,
           9.66e-4, 8.67e-4,
           7.90e-4, 7.28e-4, 6.17e-4, 5.44e-4, 4.91e-4, 4.52e-4, 3.98e-4, 3.63e-4,
           3.38e-4, 3.19e-4,
           3.05e-4, 2.94e-4, 2.77e-4, 2.66e-4, 2.58e-4, 2.52e-4, 2.47e-4, 2.39e-4,
           2.34e-4, 2.31e-4,
           2.28e-4, 2.25e-4, 2.23e-4, 2.22e-4, 2.22e-4, 2.21e-4, 2.21e-4, 2.20e-4,
           2.20e-4, 2.20e-4,
           2.19e-4, 2.19e-4, 2.19e-4, 2.19e-4, 2.19e-4]
for i in range(27):
    YELTG21.append(2.188e-4)
# -----------------------------------------------------------------------
# ROTATION J=0-2
# SCALEe BY 1/E ABOVE 20 EV IN SUBROUTINE

XROT0G21 = [.043928, .046, .047, .048, .049, .050, .051, .054, .055, .060,
            .065, .070, .080, .090, 0.10, 0.11, 0.12, 0.13, 0.14, 0.15,
            0.20, 0.25, 0.30, 0.35, 0.40, 0.45, 0.50, 0.55, 0.60, 0.65,
            0.70, 0.80, 0.90, 1.00, 1.10, 1.20, 1.35, 1.50, 1.75, 2.00,
            2.50, 3.00, 3.50, 4.00, 4.50, 5.00, 6.00, 7.00, 8.00, 9.00,
            10.0, 15.0, 20.0
            ]
YROT0G21 = [0.00, .0206, .0276, .0286, .0297, .0308, .0310, .0330, .0340,
            .0394,
            .0452, .0507, .0614, .0680, .0740, .0790, .0835, .088, .0925, .0970,
            .115, .132, .152, .175, .200, .228, .260, .291, .323, .359,
            .394, .469, .555, .636, .716, .796, .916, 1.036, 1.203, 1.370,
            1.585, 1.704, 1.755, 1.758, 1.732, 1.689, 1.579, 1.462, 1.350, 1.248,
            1.156, 0.730, 0.47]
# -----------------------------------------------------------------------
# ROTATION J=1-3
# SCALEe BY 1/E ABOVE 20 EV IN SUBROUTINE

XROT1G21 = [0.072741, .075, .080, .085, .090, .095, 0.10, 0.11, 0.12, 0.13,
            0.15, 0.20, 0.25, 0.30, 0.35, 0.40, 0.45, 0.50, 0.56, 0.60,
            0.66, 0.70, 0.80, 0.90, 1.01, 1.20, 1.40, 1.60, 1.80, 2.00,
            2.50, 3.00, 3.50, 4.00, 4.50, 5.00, 6.00, 7.00, 8.00, 9.00,
            10.0, 15.0, 20.0
            ]
YROT1G21 = [0.00, .0085, .0149, .0203, .0238, .0266, .0282, .0351, .0403,
            .0449,
            .0520, .0604, .0719, .0870, .1029, .1191, .1361, .1543, .1773, .1944,
            .2212, .2396, .2839, .3328, .3842, .489, .569, .658, .743, .818,
            .952, 1.020, 1.046, 1.050, 1.036, 1.011, .946, .876, .809, .748,
            .694, .440, .288]
# -----------------------------------------------------------------------
# ROTATION J=2-4
# SCALEe BY 1/E ABOVE 20 EV IN SUBROUTINE

XROT2G21 = [0.10085, 0.15, 0.20, 0.25, 0.30, 0.35, 0.40, 0.45, 0.50, 0.60,
            0.70, 0.80, 0.90, 1.00, 1.50, 2.00, 2.50, 3.00, 3.50, 4.00,
            4.50, 5.00, 5.50, 6.00, 7.00, 8.00, 10.0, 20.0
            ]
YROT2G21 = [0.00, .0249, .0367, .0475, .0577, .0694, .0834, .1003, .1192,
            .145,
            .178, .216, .256, .299, .436, .543, .600, .649, .670, .672,
            .662, .646, .627, .605, .561, .517, .444, 0.20]
# ROTATION J=4-6 USE X-SECTION FOR J=2-4 SCALEe BY 0.8
# ROTATION J=6-8 USE X-SECTION FOR J=2-4 SCALEe BY 0.5
# -----------------------------------------------------------------------
# ROTATION J=3-5
# SCALEe BY 1/E ABOVE 20 EV IN SUBROUTINE

XROT3G21 = [0.12797, 0.15, 0.20, 0.25, 0.30, 0.35, 0.40, 0.45, 0.50, 0.60,
            0.70, 0.80, 0.90, 1.00, 1.50, 2.00, 2.50, 3.00, 3.50, 4.00,
            4.50, 5.00, 5.50, 6.00, 7.00, 8.00, 10.0, 20.0
            ]
YROT3G21 = [0.00, .019, .033, .043, .050, .058, .066, .075, .085, .104,
            .128, .154, .185, .214, .334, .565, .700, .750, .825, .828,
            .818, .797, .774, .747, .692, .640, .548, 0.24]
# ROTATION J=5-7 USE X-SECTION FOR J=3-5 SCALEe BY 0.8
# ROTATION J=7-9 USE X-SECTION FOR J=3-5 SCALEe BY 0.5
# -----------------------------------------------------------------------
# VIBRATION V=0-1 eELTAJ=0  ROTATIONALLY ELASTIC
# SCALE AS 1/E ABOVE 100 EV

XVIB1G21 = [.515916, 0.56, 0.58, 0.60, 0.65, 0.75, 0.85, 0.95, 1.00, 1.05,
            1.10, 1.15, 1.20, 1.30, 1.40, 1.60, 1.80, 2.20, 2.40, 2.60,
            3.00, 3.50, 4.00, 4.50, 5.00, 6.00, 7.00, 8.00, 9.00, 10.0,
            11.0, 12.0, 13.0, 14.0, 15.0, 20.0, 25.0, 30.0, 40.0, 50.0,
            60.0, 80.0, 100.
            ]
YVIB1G21 = [0.00, .0005, .0031, .0064, .0071, .0106, .0170, .0279, .0342,
            .0399,
            .0451, .0501, .0545, .0651, .0735, .0964, .1216, .1624, .1677, .1719,
            .1916, .2008, .1860, .1630, .1460, .1160, .0876, .0655, .0510, .0430,
            .0366, .0318, .0280, .0241, .0222, .0143, .0104, .0073, .0048, .00416,
            .00351, .00262, .00194]
# -----------------------------------------------------------------------
# VIBRATION V=0-1 eELTAJ=2  ROTATIONALLY INELASTIC
# SCALE AS 1/E ABOVE 100 EV

XVIB2G21 = [.568, .575, 0.60, 0.65, 0.75, 0.85, 0.95, 1.00, 1.05, 1.10,
            1.15, 1.20, 1.30, 1.40, 1.60, 1.80, 2.20, 2.40, 2.60, 3.00,
            3.50, 4.00, 4.50, 5.00, 6.00, 7.00, 8.00, 9.00, 10.0, 11.0,
            12.0, 13.0, 14.0, 15.0, 20.0, 25.0, 30.0, 40.0, 50.0, 60.0,
            80.0, 100.
            ]
YVIB2G21 = [0.00, .0002, .0016, .0028, .0058, .0110, .0204, .0264, .0316,
            .0369,
            .0423, .0477, .0602, .0697, .0994, .1334, .1910, .2008, .2141, .2494,
            .2672, .2540, .2270, .2040, .1640, .1224, .0905, .0690, .0570, .0484,
            .0422, .0370, .0319, .0294, .0189, .0138, .0097, .0064, .00552, .00466,
            .00347, .00257]
# -----------------------------------------------------------------------
#  VIBRATION V=0-2

XVIB3G21 = [1.00265, 1.40, 1.50, 2.00, 2.50, 3.00, 4.00, 5.00, 6.00, 8.00,
            10.0, 15.0, 20.0
            ]
YVIB3G21 = [0.00, .001, .002, .011, .025, .033, .035, .032, .027, .021,
            .016, .0092, .0066]
# -----------------------------------------------------------------------
#  VIBRATION V=0-3

XVIB4G21 = [1.46083, 1.80, 2.00, 2.50, 3.00, 4.00, 5.00, 6.00, 8.00,
            10.0, 15.0, 20.0
            ]
YVIB4G21 = [.0, .0003, .001, .0025, .0033, .0035, .0032, .0027, .0021,
            .0016, .00092, .00066]
# B3 SIGMA+ 100% eISSOCIATIVE SPLIT INTO 4 ENERGY LOSSES
# SCALEe BY1/E**3 ABOVE 50.0EV

XB3S1G21 = [8.00, 9.20, 9.20001
            ]
YB3S1G21 = [0.00, .109, 0.00
            ]
XB3S2G21 = [9.00, 9.20, 9.20001, 10.2, 12.2, 12.20001
            ]
YB3S2G21 = [0.00, 0.00, .109, .187, .445, 0.00
            ]
XB3S3G21 = [9.50, 12.2, 12.20001, 15.2, 15.20001
            ]
YB3S3G21 = [0.00, 0.00, .445, 0.63, 0.00
            ]
XB3S4G21 = [10.0, 15.2, 15.20001, 17.2, 20.2, 30.0, 40.0, 50.0
            ]
YB3S4G21 = [0.00, 0.00, 0.63, .516, .353, .153, .069, .035]
# C3 PI V=0-18 SUMMEe VIBRATIONS METASTABLE LEVEL
# SCALEe BY 1/E**3 ABOVE 30 EV

XC3PIG21 = [11.779, 15.0, 17.5, 20.0, 30.0
            ]
YC3PIG21 = [0.00, 0.09, .126, .135, .072]
# A3 SIGMA V=0-17 SUMMEe VIBRATIONS
# SCALEe BY 1/E**3 ABOVE 30 EV

XA3SGG21 = [11.793, 15.0, 17.5, 20.0, 30.0]

YA3SGG21 = [0.00, .072, .081, 0.09, .027]
# E3 SIGMA V=0-10 SUMMEe VIBRATIONS
# SCALEe BY 1/E**3 ABOVE 30 EV

XE3SGG21 = [13.253, 15.0, 17.5, 20.0, 30.0
            ]
YE3SGG21 = [0.00, .0108, .018, .0225, .0117]
# EF1 SIGMA V=0-19 SUMMEe VIBRATIONS
#  BORN SCALEe ABOVE XEFSG(NEFSG)  EV

XEFSGG21 = [12.301, 15.0, 16.0, 17.0, 17.5, 19.0, 20.0, 21.0, 23.5, 26.0,
            30.0, 40.0, 50.0, 60.0, 70.0, 80.0, 100., 120., 140., 160.,
            180., 200., 220., 240., 260., 280., 300., 400., 500., 600.,
            700., 800., 900., 1000.
            ]
YEFSGG21 = [0.00, .028, .033, .037, .038, .039, .040, .040, .040, .040,
            .040, .041, .041, .039, .036, .034, .029, .026, .024, .022,
            .021, .020, .019, .018, .017, .016, .015, .012, .0096, .0080,
            .0069, .0061, .0054, .0049]
# GROUNe STATE CONTINUUM FRACTIONS FROM STEPHENS ANe eALGARNO:
# NEUTRAL eISSOCIATION FRACTION FOR LYMAN BANe - GROUNe STATE CONTINUUM

DISLYG21 = [3.01e-9, 6.58e-9, 1.35e-5, 1.16e-4, 1.48e-3, .0171,
            .0309, .211, .291, .415,
            .410, .407, .523, .511, .542, .558, .554, .601, .608, .634,
            .637, .643, .651, .659, .677, .691, .712, .730, .753, .774,
            .795, .816, .842, .873, .911, .956, .995
            # NEUTRAL eISSOCIATION FRACTION FOR WERNER BANe - GROUNe STATE CONTINUUM
            ]
DISWRG21 = [1.57e-11, 1.10e-10, 2.40e-9, 2.03e-8, 2.04e-6, 7.44e-6,
            6.75e-4, 1.45e-3, .0372, .0643,
            .377, .425, .642, .825]
# eISSOCIATION FRACTIONS FROM GLASS-MAUJEAN:
# B!1SIGMA

DISB1SG21 = [1.41e-8, 4.77e-8, 5.82e-8, 1.99e-7, 1.05e-6, 4.24e-5,
             .065, .152, .451]
#  e1PI

DISD1PG21 = [5.95e-9, 1.39e-8, 1.85e-8, 3.96e-8, 2.47e-6, 2.02e-5,
             7.74e-4, .0039, .0371, .103,
             .357, .481, .527, .638, .859, .870]
#
# NEUTRAL
# B1 SIGMA                  OSCILLATOR SUM V=0-36   F=0.310770
# C1 PI                     OSCILLATOR SUM V=0-13   F=0.355995
# B!1 SIGMA                 OSCILLATOR SUM V=0-8    F=0.044610
# e1 PI                     OSCILLATOR SUM V=0-15   F=0.074070
# B!!1 SIGMA                OSCILLATOR SUM V=0-6    F=0.022300
# e!1 PI                    OSCILLATOR SUM V=0-3    F=0.014500
# B!!!1 SIGMA + e!!1 PI     OSCILLATOR SUM          F=0.014500
# B!!!!1 SIGMA + e!!!1 PI   OSCILLATOR SUM          F=0.010100
# B!!!!!1 SIGMA + e!!!!1 PI OSCILLATOR SUM          F=0.005000
# CONTINUUM EXCITATION                              F=0.026800
# PREeISSOCIATION                                   F=0.017000
#
#                 SUM EXCITATION OSCILLATOR         F=0.895645
#                 SUM IONISATION OSCILLATOR         F=1.1219
#           TOTAL OSCILLATOR SUM           F=2.017545
# -----------------------------------------------------------------------
#  ATTACHMENT GIVEN AS TABLES ANe AS A TEMPERATURE eEPENeENT FUNCTION
#
# TABLES FOR 2SIGMAg  ATTACHMENT

XATTG21 = [7.00, 7.50, 8.00, 8.50, 9.00, 9.50, 10.0, 10.4, 11.0, 11.5,
           12.0, 12.5, 13.0, 13.5, 14.0, 14.5, 15.0, 15.5
           ]
YATTG21 = [0.00, 2.8e-6, 1.18e-5, 3.08e-5, 5.88e-5, 1.01e-4, 1.18e-4,
           1.29e-4, 1.18e-4, 1.01e-4,
           7.28e-5, 4.48e-5, 2.66e-5, 1.26e-5, 6.72e-6, 3.20e-6, 8.0e-7, 0.0]
# TOTAL IONISATION
# SEE NOTES BELOW ON eERIVATION OF TOTAL IONISATION X-SECTION

XIONG21 = [15.418, 16.0, 16.5, 17.0, 17.5, 18.0, 18.5, 19.0, 19.5, 20.0,
           20.5, 21.0, 21.5, 22.0, 22.5, 23.0, 23.5, 24.0, 24.5, 25.0,
           25.5, 26.0, 28.0, 30.0, 32.0, 34.0, 36.0, 38.0, 40.0, 45.0,
           50.0, 55.0, 60.0, 65.0, 70.0, 75.0, 80.0, 85.0, 90.0, 95.0,
           100., 105., 110., 115., 120., 125., 130., 135., 140., 145.,
           150., 160., 180., 200., 225., 250., 275., 300., 350., 400.,
           450., 500., 550., 600., 650., 700., 750., 800., 850., 900.,
           950., 1000., 1200., 1400., 1600., 1800., 2000., 2500., 3000., 3500.,
           4000., 4500., 5000., 5500., 6000., 7000., 8000., 9000., 10000., 12000.,
           14000., 16000.
           ]
YIONG21 = [0.00, .0295, .0598, .0910, .121, .154, .184, .217, .245, .276,
           .305, .331, .357, .384, .407, .433, .454, .477, .498, .516,
           .536, .555, .623, .678, .725, .765, .800, .828, .853, .900,
           .927, .945, .954, .957, .957, .956, .950, .944, .934, .920,
           .910, .902, .890, .878, .865, .851, .840, .832, .818, .809,
           .801, .776, .725, .687, .645, .605, .565, .537, .484, .443,
           .404, .379, .343, .322, .307, .287, .276, .261, .251, .239,
           .226, .214, .199, .165, .146, .133, .121, .101, .0865, .0754,
           .0675, .0610, .0558, .0515, .0480, .0422, .0375, .0340, .0310, .0265,
           .0234, .0208]
# eISSOCIATIVE IONISATION X-SECTION STRAUB WITH EXTENSION TO 16KEV
#  USE CONSTANT RATIO FOR H2+ ANe H+ ABOVE 1KEV

XIONDG21 = [18.076, 25.0, 30.0, 35.0, 40.0, 45.0, 50.0, 55.0, 60.0, 65.0,
            70.0, 75.0, 80.0, 85.0, 90.0, 95.0, 100., 110., 120., 140.,
            160., 180., 200., 225., 250., 275., 300., 350., 400., 450.,
            500., 550., 600., 650., 700., 750., 800., 850., 900., 950.,
            1000., 1200., 1400., 1600., 1800., 2000., 2500., 3000., 3500., 4000.,
            4500., 5000., 5500., 6000., 7000., 8000., 9000., 10000., 12000., 14000.,
            16000.
            ]
YIONDG21 = [0.00, .00422, .00856, .0176, .0287, .0408, .0482, .0572, .0625,
            .0682,
            .0705, .0737, .0739, .0751, .0754, .0761, .0759, .0744, .0724, .0671,
            .0639, .0592, .0545, .0505, .0450, .0412, .0392, .0339, .0294, .0260,
            .0241, .0211, .0197, .0181, .0171, .0159, .0149, .0137, .0135, .0125,
            .0117, .0109, .00902, .00798, .00727, .00662, .00552, .00473, .00412,
            .00369,
            .00333, .00305, .00282, .00262, .00231, .00205, .00186, .00169, .00145,
            .00128,
            .00114]
# BREMSSTRAHLUNG X-SECTION WITH CUT OFF  UNITS 10**-24

Z1TG21 = [11.3, 6.18, 2.80, 1.54, .858, .407, .251, .176, .145, .150,
          .167, .178, .187, .193, .198, .205, .210, .218, .222, .228,
          .231, .233, .234, .235, .235
          ]
EBRMG21 = [1000., 2000., 5000., 1.E4, 2.E4, 5.E4, 1.E5, 2.E5, 5.E5, 1.E6,
           2.E6, 3.E6, 4.E6, 5.E6, 6.E6, 8.E6, 1.E7, 1.5E7, 2.E7, 3.E7,
           4.E7, 5.E7, 6.E7, 8.E7, 1.E8]
EING21 = [-.043928, -.072741, -.10085, -.12797, 0.043928, 0.072741, 0.10085, 0.12797, 0.515916, 0.568, 1.00265, 1.46083,
          8.0, 9.0, 9.5, 10.0, 11.189, 11.353, 11.512, 11.666, 11.817, 11.963, 12.105, 12.244, 12.378, 12.509, 12.636,
          12.759, 12.878, 12.994, 13.106, 13.215, 13.320, 13.422, 13.521, 13.617, 13.709, 13.798, 13.884, 13.967,
          14.047, 14.124, 14.197, 14.268, 14.335, 14.399, 14.458, 14.514, 14.564, 14.608, 14.644, 14.668, 14.678,
          12.285, 12.571, 12.840, 13.094, 13.332, 13.553, 13.758, 13.947, 14.119, 14.273, 14.408, 14.522, 14.611,
          14.672, 11.779, 13.100, 11.793, 12.684, 13.253, 12.301, 12.841, 13.698, 13.931, 14.144, 14.333, 14.494,
          14.613, 14.651, 14.664, 14.672, 13.994, 14.270, 14.530, 14.775, 15.003, 15.218, 15.418, 15.602, 15.772,
          15.928, 16.068, 16.191, 16.299, 16.390, 16.462, 16.516, 14.491, 14.609, 14.899, 15.060, 15.150, 15.300,
          15.800, 32.0, 0.0]
for i in range(250 - 108):
    EING21.append(0.0)

gd['gas21/XELM'] = XELMG21
gd['gas21/YELM'] = YELMG21
gd['gas21/YELT'] = YELTG21
gd['gas21/YEPS'] = YEPSG21
gd['gas21/XROT0'] = XROT0G21
gd['gas21/YROT0'] = YROT0G21
gd['gas21/XROT1'] = XROT1G21
gd['gas21/YROT1'] = YROT1G21
gd['gas21/XROT2'] = XROT2G21
gd['gas21/YROT2'] = YROT2G21
gd['gas21/XROT3'] = XROT3G21
gd['gas21/YROT3'] = YROT3G21
gd['gas21/XVIB1'] = XVIB1G21
gd['gas21/YVIB1'] = YVIB1G21
gd['gas21/XVIB2'] = XVIB2G21
gd['gas21/YVIB2'] = YVIB2G21
gd['gas21/XVIB3'] = XVIB3G21
gd['gas21/YVIB3'] = YVIB3G21
gd['gas21/XVIB4'] = XVIB4G21
gd['gas21/YVIB4'] = YVIB4G21
gd['gas21/XB3S1'] = XB3S1G21
gd['gas21/YB3S1'] = YB3S1G21
gd['gas21/XB3S2'] = XB3S2G21
gd['gas21/YB3S2'] = YB3S2G21
gd['gas21/XB3S3'] = XB3S3G21
gd['gas21/YB3S3'] = YB3S3G21
gd['gas21/XB3S4'] = XB3S4G21
gd['gas21/YB3S4'] = YB3S4G21
gd['gas21/XC3PI'] = XC3PIG21
gd['gas21/YC3PI'] = YC3PIG21
gd['gas21/XA3SG'] = XA3SGG21
gd['gas21/YA3SG'] = YA3SGG21
gd['gas21/XE3SG'] = XE3SGG21
gd['gas21/YE3SG'] = YE3SGG21
gd['gas21/XEFSG'] = XEFSGG21
gd['gas21/YEFSG'] = YEFSGG21
gd['gas21/XATT'] = XATTG21
gd['gas21/YATT'] = YATTG21
gd['gas21/XION'] = XIONG21
gd['gas21/YION'] = YIONG21
gd['gas21/XIOND'] = XIONDG21
gd['gas21/YIOND'] = YIONDG21
gd['gas21/DISLY'] = DISLYG21
gd['gas21/DISWR'] = DISWRG21
gd['gas21/DISD1P'] = DISD1PG21
gd['gas21/DISB1S'] = DISB1SG21
gd['gas21/Z1T'] = Z1TG21
gd['gas21/EBRM'] = EBRMG21
gd['gas21/EIN'] = EING21

XENG22 = [0.00, 0.01, 0.02, 0.03, 0.04, .046, 0.05, 0.06, 0.07, 0.08,
          0.09, 0.10, 0.13, 0.15, 0.20, 0.30, 0.40, 0.50, 0.60, 0.70,
          0.90, 1.00, 1.10, 1.40, 1.50, 1.60, 1.80, 2.00, 2.50, 3.00,
          4.00, 5.00, 6.00, 8.00, 10.0, 15.0, 20.0, 30.0, 40.0, 50.0,
          60.0, 80.0, 100., 150., 200., 300., 400., 500., 600., 800.,
          1000., 10000., 100000.
          ]
YXSECG22 = [6.36, 7.26, 7.95, 8.45, 8.91, 9.05, 9.22, 9.50, 9.79, 10.04,
            10.24, 10.44, 10.93, 11.33, 11.93, 12.92, 13.82, 14.61, 15.51, 16.20,
            16.9, 17.2, 17.3, 17.7, 17.7, 17.8, 17.7, 17.5, 16.8, 16.1,
            14.2, 13.5, 13.2, 12.3, 11.2, 7.30, 4.30, 1.60, 0.77, 0.50,
            0.35, 0.22, 0.15, 0.07, .043, .022, .014, .010, .006, .004,
            .002, .0002, .00002]
# -----------------------------------------------------------------------
# ROTATION J=0-2

XROT0G22 = [.0226, .025, 0.03, 0.04, 0.05, 0.06, 0.07, 0.08, 0.10, 0.15,
            0.20, 0.25, 0.30, 0.40, 0.50, 0.60, 0.70, 0.80, 0.90, 1.00,
            1.20, 1.50, 2.00, 2.50, 3.00, 3.50, 4.00, 4.50, 5.00, 6.00,
            7.00, 8.00, 9.00, 10.0, 15.0, 20.0, 100., 1000., 10000., 100000.
            ]
YROT0G22 = [0.00, .024, .042, .061, .067, .073, .078, .082, .091, .110,
            .129, .144, .170, .215, .264, .323, .394, .469, .555, .636,
            .796, 1.036, 1.370, 1.585, 1.704, 1.755, 1.758, 1.732, 1.689, 1.579,
            1.462, 1.350, 1.248, 1.156, 0.730, 0.44, 0.05, .0015, .00015, .000015]
# -----------------------------------------------------------------------
# ROTATION J=1-3

XROT1G22 = [.0377, 0.04, 0.05, 0.06, 0.07, 0.08, 0.10, 0.15, 0.20, 0.25,
            0.30, 0.40, 0.50, 0.56, 0.60, 0.66, 0.70, 0.80, 0.90, 1.01,
            1.20, 1.40, 1.60, 1.80, 2.00, 2.50, 3.00, 3.50, 4.00, 4.50,
            5.00, 6.00, 7.00, 8.00, 9.00, 10.0, 15.0, 20.0, 100., 1000., 10000., 100000.
            ]
YROT1G22 = [0.00, 0.01, .026, .032, .036, .040, .046, .058, .071, .082,
            .094, .122, .152, .165, .178, .200, .214, .252, .292, .334,
            .420, .510, .610, .700, .786, .937, 1.01, 1.05, 1.05, 1.04,
            1.01, .946, .876, .809, .748, .694, .440, .265, 0.03, .001, .0001, .00001]
# -----------------------------------------------------------------------
# ROTATION J=2-4

XROT2G22 = [.0528, 0.07, 0.10, 0.15, 0.20, 0.30, 0.40, 0.50, 0.60, 0.70,
            0.80, 0.90, 1.00, 1.50, 2.00, 2.50, 3.00, 3.50, 4.00, 4.50,
            5.00, 5.50, 6.00, 7.00, 8.00, 10.0, 20.0, 100., 1000., 10000., 100000.
            ]
YROT2G22 = [0.00, .022, .034, .046, .055, .075, .099, .115, .132, .162,
            .193, .227, .266, .463, .619, .719, .774, .799, .802, .790,
            .771, .748, .721, .669, .617, .529, 0.20, 0.02, .0007, .00007, .000007]
# -----------------------------------------------------------------------
# ROTATION J=3-5

XROT3G22 = [.0679, 0.10, 0.15, 0.20, 0.25, 0.30, 0.40, 0.50, 0.60, 0.70,
            0.80, 0.90, 1.00, 1.50, 2.00, 2.50, 3.00, 3.50, 4.00, 4.50,
            5.00, 5.50, 6.00, 7.00, 8.00, 10.0, 20.0, 100., 1000., 10000., 100000.
            ]
YROT3G22 = [0.00, 0.02, 0.04, 0.05, 0.06, 0.07, .095, .110, .129, .160,
            .194, .233, .271, .478, .637, .742, .799, .825, .828, .818,
            .797, .774, .747, .692, .640, .548, 0.18, 0.02, .0007, .00007, .000007]
# -----------------------------------------------------------------------
# ROTATION J=4-6

XROT4G22 = [.0830, 0.10, 0.15, 0.20, 0.25, 0.30, 0.40, 0.50, 0.60, 0.70,
            0.80, 0.90, 1.00, 1.50, 2.00, 2.50, 3.00, 3.50, 4.00, 4.50,
            5.00, 5.50, 6.00, 7.00, 8.00, 10.0, 20.0, 100., 1000., 10000., 100000.
            ]
YROT4G22 = [0.00, .012, 0.03, .038, .045, .053, .071, .083, .097, .120,
            .146, .175, 0.20, 0.36, 0.48, 0.56, 0.60, 0.62, 0.62, 0.61,
            0.60, 0.58, 0.56, 0.52, 0.48, 0.41, 0.13, .015, .0005, .00005, .000005]
# -----------------------------------------------------------------------
# ROTATION J=5-7

XROT5G22 = [.0981, 0.15, 0.20, 0.25, 0.30, 0.40, 0.50, 0.60, 0.70, 0.80,
            0.90, 1.00, 1.50, 2.00, 2.50, 3.00, 3.50, 4.00, 4.50, 5.00,
            5.50, 6.00, 7.00, 8.00, 10.0, 20.0, 100., 1000., 10000., 100000.
            ]
YROT5G22 = [0.00, .015, .028, .034, 0.04, .053, .062, .073, 0.09, 0.11,
            0.13, 0.15, 0.27, 0.36, 0.42, 0.45, 0.46, 0.46, 0.46, 0.45,
            0.44, 0.42, 0.39, 0.36, 0.31, 0.10, 0.01, .0004, .00004, .000004]
# ----------------------------------------------------------------------
# VIBRATION V=0-1 eELTAJ=0  ROTATIONALLY ELASTIC

XVIB1G22 = [0.371, 0.50, 0.60, 0.65, 0.75, 0.85, 1.00, 1.15, 1.25, 1.50,
            1.75, 2.00, 2.20, 2.40, 2.60, 3.00, 3.50, 4.00, 4.50, 5.00,
            6.00, 7.00, 8.00, 9.00, 10.0, 11.0, 12.0, 13.0, 14.0, 15.0,
            20.0, 100., 1000., 10000., 100000.
            ]
YVIB1G22 = [0.00, .0045, .009, .011, .016, .020, .028, .037, .042, .064,
            .084, .100, .110, .120, .128, .135, .140, .140, .135, .122,
            .100, .077, .060, .046, .035, .027, .021, .017, .015, .013,
            .0085, .0017, .00005, .000005, .0000005]
# -----------------------------------------------------------------------
# VIBRATION V=0-1 eELTAJ=2  ROTATIONALLY INELASTIC

XVIB2G22 = [0.391, 0.50, 0.60, 0.65, 0.75, 0.85, 1.00, 1.15, 1.25, 1.50,
            1.75, 2.00, 2.20, 2.40, 2.60, 3.00, 3.50, 4.00, 4.50, 5.00,
            6.00, 7.00, 8.00, 9.00, 10.0, 11.0, 12.0, 13.0, 14.0, 15.0,
            20.0, 100., 1000., 10000., 100000.
            ]
YVIB2G22 = [0.00, .0025, .0055, .008, .012, .017, .026, .035, .040, .064,
            .088, .115, .135, .150, .160, .176, .188, .188, .185, .172,
            .142, .110, .082, .062, .045, .035, .026, .019, .014, .011,
            .0074, .0015, .00004, .000004, .0000004]
# -----------------------------------------------------------------------
#  VIBRATION V=0-2

XVIB3G22 = [0.735, 1.00, 1.50, 2.00, 3.00, 4.00, 5.00, 6.00, 8.00, 10.0,
            15.0, 20.0, 100., 1000., 10000., 100000.
            ]
YVIB3G22 = [0.00, .0005, .003, .007, .017, .018, .017, .015, .011, .007,
            .001, .0005, .00015, .000005, .0000005, .00000005
            # -----------------------------------------------------------------------
            #  VIBRATION V=0-3
            ]
XVIB4G22 = [1.085, 1.35, 1.50, 2.00, 3.00, 4.00, 5.00, 6.00, 8.00, 10.0,
            15.0, 20.0, 100., 1000., 10000., 100000.
            ]
YVIB4G22 = [0.00, .00015, .0003, .0008, .0016, .0016, .0015, .0012, .001,
            .0015, .0005, .0001, .000025, .0000008, .00000008, .000000008
            # -----------------------------------------------------------------------
            # EXCITATION TO TRIPLET STATES (eISSOCIATION)
            ]
XEXC1G22 = [8.85, 8.92, 9.34, 10.0, 11.0, 12.0, 15.0, 20.0, 25.0, 30.0,
            40.0, 50.0, 60.0, 80.0, 100., 150., 200., 1000., 10000., 100000.
            ]
YEXC1G22 = [0.00, .008, 0.04, 0.08, .184, .336, 0.51, 0.46, 0.28, 0.18,
            0.08, .041, .025, .010, .005, .0012, .0005, .00008, .000008, .0000008
            #  EXCITATION TO SINGLET STATES
            ]
XEXC2G22 = [12.0, 12.13, 13.4, 15.0, 17.0, 20.0, 25.0, 30.0, 40.0, 50.0,
            60.0, 80.0, 100., 150., 200., 300., 400., 500., 600., 800.,
            1000., 10000., 100000.
            ]
YEXC2G22 = [0.00, 0.09, 0.09, 0.24, 0.40, 0.58, 0.86, 1.01, 1.07, 1.11,
            1.13, 1.05, 0.99, 0.79, 0.70, 0.58, 0.50, 0.42, 0.38, 0.31,
            0.24, .024, .0024
            # -----------------------------------------------------------------------
            ]
XATTG22 = [7.40, 8.00, 9.00, 10.0, 11.0, 12.0, 13.0, 14.0, 15.0, 16.0,
           17.0, 18.0, 30.0, 60.0, 100., 1000., 10000., 100000.
           ]
YATTG22 = [0.00, .000005, .000012, .000026, .000027, .00003, .000035,
           .00010, .00008, .00009, .00010, .00011, .00006, .00001, .000001,
           .0000001, .00000001, .000000001
           # -----------------------------------------------------------------------
           ]
XIONG22 = [15.427, 16.0, 16.5, 17.0, 17.5, 18.0, 18.5, 19.0, 19.5, 20.0,
           20.5, 21.0, 21.5, 22.0, 22.5, 23.0, 23.5, 24.0, 24.5, 25.0,
           25.5, 26.0, 28.0, 30.0, 32.0, 34.0, 36.0, 38.0, 40.0, 45.0,
           50.0, 55.0, 60.0, 65.0, 70.0, 75.0, 80.0, 85.0, 90.0, 95.0,
           100., 105., 110., 115., 120., 125., 130., 135., 140., 145.,
           150., 160., 180., 200., 250., 300., 350., 400., 450., 500.,
           550., 600., 650., 700., 750., 800., 850., 900., 950., 1000.,
           10000., 100000.
           ]
YIONG22 = [0.00, .034, .069, .104, .138, .173, .207, .239, .272, .300,
           .328, .355, .383, .406, .429, .454, .475, .498, .518, .537,
           .556, .575, .641, .699, .744, .786, .821, .851, .876, .931,
           .950, .968, .977, .981, .981, .980, .974, .968, .958, .948,
           .939, .925, .913, .907, .889, .877, .866, .853, .839, .827,
           .813, .792, .754, .716, .638, .576, .523, .482, .446, .414,
           .387, .366, .344, .326, .310, .295, .282, .271, .257, .247,
           .0247, .00247]

EING22 = [-.0226, -.0377, -.0528, 0.0226, 0.0377, 0.0528, 0.0679, 0.0830, 0.0981, 0.371, 0.391, 0.735, 1.085, 8.85,
          12.0, ]

for i in range(250 - 15):
    EING22.append(0.0)
gd['gas22/XEN'] = XENG22
gd['gas22/YXSEC'] = YXSECG22
gd['gas22/XROT0'] = XROT0G22
gd['gas22/YROT0'] = YROT0G22
gd['gas22/XROT1'] = XROT1G22
gd['gas22/YROT1'] = YROT1G22
gd['gas22/XROT2'] = XROT2G22
gd['gas22/YROT2'] = YROT2G22
gd['gas22/XROT3'] = XROT3G22
gd['gas22/YROT3'] = YROT3G22
gd['gas22/XROT4'] = XROT4G22
gd['gas22/YROT4'] = YROT4G22
gd['gas22/XROT5'] = XROT5G22
gd['gas22/YROT5'] = YROT5G22
gd['gas22/XVIB1'] = XVIB1G22
gd['gas22/YVIB1'] = YVIB1G22
gd['gas22/XVIB2'] = XVIB2G22
gd['gas22/YVIB2'] = YVIB2G22
gd['gas22/XVIB3'] = XVIB3G22
gd['gas22/YVIB3'] = YVIB3G22
gd['gas22/XVIB4'] = XVIB4G22
gd['gas22/YVIB4'] = YVIB4G22
gd['gas22/XEXC1'] = XEXC1G22
gd['gas22/YEXC1'] = YEXC1G22
gd['gas22/XEXC2'] = XEXC2G22
gd['gas22/YEXC2'] = YEXC2G22
gd['gas22/XATT'] = XATTG22
gd['gas22/YATT'] = YATTG22
gd['gas22/XION'] = XIONG22
gd['gas22/YION'] = YIONG22
gd['gas22/EIN'] = EING22

XENG25 = [0.00, .004, 0.01, 0.02, 0.03, 0.04, 0.05, 0.06, 0.07, 0.08,
          0.09, 0.10, 0.11, 0.12, 0.13, 0.14, 0.16, 0.18, 0.20, 0.24,
          0.30, 0.40, 0.50, 0.60, 0.80, 1.00, 1.40, 2.00, 3.00, 4.00,
          5.00, 6.00, 7.00, 8.00, 9.00, 10.0, 15.0, 20.0, 30.0, 40.0,
          70.0, 100., 140., 200., 250., 300., 500., 1000., 1500., 3000.,
          6000., 10000., 20000., 100000.
          ]
XENG25 = [np.float32(i) for i in XENG25]
YXSECG25 = [235., 235., 235., 233., 225., 215., 205., 190., 175., 160.,
            140., 125., 110., 95.0, 80.0, 74.0, 62.0, 51.0, 43.0, 34.0,
            25.0, 20.0, 18.0, 16.5, 15.7, 15.0, 14.5, 15.0, 17.5, 20.0,
            22.0, 23.5, 24.0, 24.5, 24.0, 22.0, 15.0, 11.5, 8.00, 6.20,
            3.50, 2.60, 1.50, 0.95, 0.70, 0.55, 0.30, 0.14, 0.09, 0.04,
            0.02, .012, .005, .001
            ]
YXSECG25 = [np.float32(i) for i in YXSECG25]
XIONG25 = [10.04, 10.9, 13.4, 18.4, 19.4, 20.4, 23.4, 28.4, 33.4, 38.4,
           43.4, 48.4, 53.4, 58.4, 68.4, 78.4, 88.4, 98.4, 120., 140.,
           200., 300., 500., 700., 1000., 2000., 4000., 10000., 100000.
           ]
XIONG25 = [np.float32(i) for i in XIONG25]
YIONG25 = [0.00, 0.12, 1.12, 2.92, 3.37, 3.70, 4.44, 5.48, 6.17, 6.68,
           7.13, 7.41, 7.52, 7.66, 7.84, 7.89, 7.84, 7.75, 7.53, 7.20,
           6.17, 4.76, 3.30, 2.45, 1.95, 1.15, 0.70, 0.36, .06
           ]
YIONG25 = [np.float32(i) for i in YIONG25]

XATTG25 = [6.85, 7.00, 7.20, 7.50, 8.00, 8.50, 9.00, 9.50, 10.0, 10.5,
           11.0, 11.5, 12.0, 12.5, 13.0, 13.2
           ]
XATTG25 = [np.float32(i) for i in XATTG25]
YATTG25 = [0.00, 0.67, 1.10, 1.65, 2.80, 4.40, 6.60, 10.3, 14.7, 12.3,
           9.70, 6.20, 3.50, 1.30, 0.50, 0.00]
YATTG25 = [np.float32(i) for i in YATTG25]
# V2 ANe V3 eIPOLE PARTS GIVEN ANALYTICALLY
# NB V3 TABLE CONTAINS ONLY RESONANCE PART OF X-SECT.

XVIB3G25 = [.137, 1.00, 2.00, 3.00, 4.00, 5.00, 6.00, 7.00, 8.00, 9.00,
            10.0, 14.0, 20.0, 30.0, 40.0, 100., 1000., 10000., 100000.
            ]
XVIB3G25 = [np.float32(i) for i in XVIB3G25]
YVIB3G25 = [0.00, 0.01, 0.45, 0.75, 1.00, 1.15, 1.20, 1.15, 1.00, 0.90,
            0.80, 0.50, 0.35, 0.21, 0.16, 0.05, .005, .0005, .00005
            ]
YVIB3G25 = [np.float32(i) for i in YVIB3G25]
XVIB4G25 = [.180, 0.19, 0.20, 0.23, 0.25, 0.30, 0.35, 0.40, 0.50, 0.70,
            1.00, 1.50, 2.00, 3.00, 4.00, 5.00, 6.00, 7.50, 8.50, 10.0,
            15.0, 20.0, 30.0, 40.0, 100., 1000., 10000., 100000.
            ]
XVIB4G25 = [np.float32(i) for i in XVIB4G25]
YVIB4G25 = [0.00, 0.17, 0.22, 0.30, 0.32, 0.34, 0.34, 0.32, 0.31, 0.25,
            0.21, 0.19, 0.19, 0.32, 0.47, 0.61, 0.79, 1.03, 1.03, 0.85,
            0.58, 0.33, 0.18, 0.11, 0.03, .003, .0003, .00003
            ]
YVIB4G25 = [np.float32(i) for i in YVIB4G25]
XVIB5G25 = [.349, 0.40, 0.45, 0.50, 0.60, 0.70, 0.80, 1.00, 1.50, 2.00,
            3.00, 4.00, 5.00, 6.00, 7.50, 8.50, 10.0, 15.0, 20.0, 30.0,
            40.0, 100., 1000., 10000., 100000.
            ]
XVIB5G25 = [np.float32(i) for i in XVIB5G25]
YVIB5G25 = [0.00, 0.35, 0.43, 0.47, 0.48, 0.48, 0.46, 0.43, 0.43, 0.47,
            0.69, 1.00, 1.30, 1.75, 1.90, 1.60, 1.20, 0.72, 0.30, 0.17,
            0.10, 0.02, .002, .0002, .00002
            ]
YVIB5G25 = [np.float32(i) for i in YVIB5G25]
XVIB6G25 = [.529, 1.00, 1.50, 2.00, 3.00, 4.00, 5.00, 6.00, 7.50, 8.50,
            10.0, 15.0, 20.0, 30.0, 40.0, 100., 1000., 10000., 100000.
            ]
XVIB6G25 = [np.float32(i) for i in XVIB6G25]
YVIB6G25 = [0.00, .001, 0.01, .016, .035, 0.06, 0.09, 0.12, 0.13, 0.11,
            0.08, .045, 0.02, 0.01, .007, .0016, .00016, .000016, .0000016
            ]
YVIB6G25 = [np.float32(i) for i in YVIB6G25]
XEXCG25 = [7.70, 8.50, 9.00, 9.50, 10.5, 11.5, 13.0, 15.0, 20.0, 25.0,
           30.0, 40.0, 50.0, 60.0, 70.0, 80.0, 100., 150., 200., 300.,
           400., 600., 1000., 2000., 4000., 10000., 100000.
           ]
XEXCG25 = [np.float32(i) for i in XEXCG25]
YEXCG25 = [0.00, 0.11, 0.38, 0.71, 1.26, 1.76, 2.03, 2.36, 2.80, 3.03,
           3.08, 3.19, 3.25, 3.25, 3.20, 3.10, 2.81, 1.93, 1.49, 1.10,
           0.88, 0.66, 0.44, 0.28, .160, .083, .0150
           ]
YEXCG25 = [np.float32(i) for i in YEXCG25]
XEXC1G25 = [8.50, 8.70, 9.30, 9.85, 10.3, 10.8, 11.3, 12.3, 13.3, 14.3,
            15.3, 17.3, 20.0, 22.0, 25.0, 30.0, 35.0, 40.0, 45.0, 50.0,
            60.0, 70.0, 80.0, 100., 150., 200., 300., 400., 500., 600.,
            1000., 2000., 4000., 10000., 100000.
            ]
XEXC1G25 = [np.float32(i) for i in XEXC1G25]
YEXC1G25 = [0.00, 0.077, 0.16, 0.23, 0.29, 0.34, 0.42, 0.64, 0.97, 1.43,
            1.99, 2.91, 3.79, 4.07, 4.73, 5.50, 5.94, 6.16, 6.44, 6.60,
            6.82, 6.82, 6.77, 6.44, 4.79, 3.91, 2.86, 2.20, 1.87, 1.65,
            1.16, 0.68, 0.40, 0.20, .038]
YEXC1G25 = [np.float32(i) for i in YEXC1G25]
EING25 = [-0.051, 0.051, 0.137, 0.180, 0.349, 0.529, 7.70, 8.5, ]
EING25 = [np.float32(i) for i in EING25]
for J in range(250 - 8):
    EING25.append(0.0)
gd['gas25/XEN'] = XENG25
gd['gas25/YXSEC'] = YXSECG25
gd['gas25/XION'] = XIONG25
gd['gas25/YION'] = YIONG25
gd['gas25/XATT'] = XATTG25
gd['gas25/YATT'] = YATTG25
gd['gas25/XVIB3'] = XVIB3G25
gd['gas25/YVIB3'] = YVIB3G25
gd['gas25/XVIB4'] = XVIB4G25
gd['gas25/YVIB4'] = YVIB4G25
gd['gas25/XVIB5'] = XVIB5G25
gd['gas25/YVIB5'] = YVIB5G25
gd['gas25/XVIB6'] = XVIB6G25
gd['gas25/YVIB6'] = YVIB6G25
gd['gas25/XEXC'] = XEXCG25
gd['gas25/YEXC'] = YEXCG25
gd['gas25/XEXC1'] = XEXC1G25
gd['gas25/YEXC1'] = YEXC1G25
gd['gas25/EIN'] = EING25

np.save("gases", gd)