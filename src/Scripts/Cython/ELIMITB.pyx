from Magboltz cimport Magboltz
cimport cython
from Magboltz cimport drand48
from libc.math cimport sin, cos, acos, asin, log, sqrt, pow,log10
from libc.stdlib cimport malloc, free
from libc.string cimport memset
from SORT cimport SORT
@cython.cdivision(True)
@cython.boundscheck(False)
@cython.wraparound(False)
cdef int isNaN(double num):
    return num != num

@cython.cdivision(True)
@cython.boundscheck(False)
@cython.wraparound(False)
cdef double random_uniform(double dummy):
    cdef double r = drand48(dummy)
    return r


@cython.cdivision(True)
@cython.boundscheck(False)
@cython.wraparound(False)
cdef void GERJAN(double RDUM, double API, double *RNMX):
    cdef double RAN1, RAN2, TWOPI
    cdef int J
    for J in range(0, 5, 2):
        RAN1 = random_uniform(RDUM)
        RAN2 = random_uniform(RDUM)
        TWOPI = 2.0 * API
        RNMX[J] = sqrt(-1 * log(RAN1)) * cos(RAN2 * TWOPI)
        RNMX[J + 1] = sqrt(-1 * log(RAN1)) * sin(RAN2 * TWOPI)

@cython.cdivision(True)
@cython.boundscheck(False)
@cython.wraparound(False)
cpdef ELIMITB(Magboltz Object):
    cdef long long I, ISAMP, N4000, IMBPT, J1, KGAS, IE, INTEM
    cdef double SMALL, RDUM, E1, TDASH, CONST9, CONST10, DCZ1, DCX1, DCY1, BP, F1, F2, F4, J2M, R5, TEST1, R1, T, AP, E, CONST6, DCX2, DCY2, DCZ2, R2,
    cdef double VGX, VGY, VGZ, VEX, VEY, VEZ, EOK, CONST11, DXCOM, DYCOM, DZCOM, S1, EI, R9, EXTRA, IPT, S2, R3, R31, F3, RAN, EPSI, R4, PHI0, F8, F9, ARG1
    cdef double D, Q, U, CSQD, F6, F5, ARGZ, CONST12, VXLAB, VYLAB, VZLAB, TEMP[4000],DELTAE,EF100
    TEMP = <double *> malloc(4000 * sizeof(double))
    memset(TEMP, 0, 4000 * sizeof(double))

    Object.SMALL =  1.0e-20
    ISAMP = 20
    EF100 = Object.EFIELD * 100
    RDUM = Object.RSTART
    E1 = Object.ESTART

    INTEM = 8
    TDASH = 0.0
    CONST9 = Object.CONST3 * 0.01

    # INITIAL DIRECTION COSINES
    DCZ1 = cos(Object.THETA)
    DCX1 = sin(Object.THETA) * cos(Object.PHI)
    DCY1 = sin(Object.THETA) * sin(Object.PHI)

    for J in range(4000):
        TEMP[J] = Object.TCFN1[J] + Object.TCF1[J]

    VTOT = CONST9 * sqrt(E1)
    CX1 = DCX1 * VTOT
    CY1 = DCY1 * VTOT
    CZ1 = DCZ1 * VTOT

    F4 = 2 * acos(-1)

    DELTAE = Object.EFINAL / float(INTEM)

    J2M = Object.NMAX / ISAMP

    for J1 in range(int(J2M)):
        if J1 != 0  and not int(str(J1)[-int(log10(J1)):]):
            print('* Num analyzed collisions: {}'.format(J1))
        while True:
            R1 = random_uniform(RDUM)
            I = int(E1 / DELTAE)+1
            I = min(I, INTEM) - 1
            TLIM = Object.TCFMAX1[I]
            T = -1 * log(R1) / TLIM + TDASH
            TDASH = T
            WBT = Object.WB * T
            COSWT = cos(WBT)
            SINWT = sin(WBT)
            DZ = (CZ1 * SINWT + (Object.EOVB - CY1) * (1 - COSWT)) / Object.WB
            E = E1 + DZ * EF100
            IE = int(E / Object.ESTEP)
            IE = min(IE, 3999)
            if TEMP[IE] > TLIM:
                TDASH += log(R1) / TLIM
                Object.TCFMAX1[I] *= 1.05
                continue
            R5 = random_uniform(RDUM)
            TEST1 = Object.TCF1[IE] / TLIM

            # TEST FOR REAL OR NULL COLLISION
            if R5<=TEST1:
                break

        if IE == 3999:
            Object.IELOW = 1
            return

        TDASH = 0.0
        CX2 = CX1
        CY2 = (CY1 - Object.EOVB) * COSWT + CZ1 * SINWT + Object.EOVB
        CZ2 = CZ1 * COSWT - (CY1 - Object.EOVB) * SINWT
        VTOT = sqrt(CX2 ** 2 + CY2 ** 2 + CZ2 ** 2)
        DCX2 = CX2 / VTOT
        DCY2 = CY2 / VTOT
        DCZ2 = CZ2 / VTOT

        # DETERMINATION OF REAL COLLISION TYPE
        R2 = random_uniform(RDUM)

        # FIND LOCATION WITHIN 4 UNITS IN COLLISION ARRAY
        I = SORT(I, R2, IE, Object)
        while Object.CF1[IE][I] < R2:
            I = I + 1

        S1 = Object.RGAS1[I]
        EI = Object.EIN1[I]
        if Object.IPN1[I] > 0:
            R9 = random_uniform(RDUM)
            EXTRA = R9 * (E - EI)
            EI = EXTRA + EI

        # GENERATE SCATTERING ANGLES AND UPDATE  LABORATORY COSINES AFTER
        # COLLISION ALSO UPDATE ENERGY OF ELECTRON.
        IPT = Object.IARRY1[I]
        if E < EI:
            EI = E - 0.0001
        S2 = (S1 * S1) / (S1 - 1.0)
        R3 = random_uniform(RDUM)

        if Object.INDEX1[I] == 1:
            R31 = random_uniform(RDUM)
            F3 = 1.0 - R3 * Object.ANGCT1[IE][I]
            if R31 > Object.PSCT1[IE][I]:
                F3 = -1 * F3
        elif Object.INDEX1[I] == 2:
            EPSI = Object.PSCT1[IE][I]
            F3 = 1 - (2 * R3 * (1 - EPSI) / (1 + EPSI * (1 - 2 * R3)))
        else:
            F3 = 1 - 2 * R3
        THETA0 = acos(F3)
        R4 = random_uniform(RDUM)
        PHI0 = F4 * R4
        F8 = sin(PHI0)
        F9 = cos(PHI0)
        ARG1 = 1 - S1 * EI / E
        ARG1 = max(ARG1, SMALL)

        D = 1 - F3 * sqrt(ARG1)
        E1 = E * (1 - EI / (S1 * E) - 2 * D / S2)
        E1 = max(E1, SMALL)
        Q = sqrt((E / E1) * ARG1) / S1
        Q = min(Q, 1)
        Object.THETA = asin(Q * sin(THETA0))

        F6 = cos(Object.THETA)
        U = (S1 - 1) * (S1 - 1) / ARG1
        CSQD = F3 ** 2

        if F3 < 0 and CSQD > U:
            F6 = -1 * F6
        F5 = sin(Object.THETA)
        DCZ2 = min(DCZ2, 1)
        VTOT = CONST9 * sqrt(E1)
        ARGZ = sqrt(DCX2 * DCX2 + DCY2 * DCY2)
        if ARGZ == 0:
            DCZ1 = F6
            DCX1 = F9 * F5
            DCY1 = F8 * F5
        else:
            DCZ1 = DCZ2 * F6 + ARGZ * F5 * F8
            DCY1 = DCY2 * F6 + (F5 / ARGZ) * (DCX2 * F9 - DCY2 * DCZ2 * F8)
            DCX1 = DCX2 * F6 - (F5 / ARGZ) * (DCY2 * F9 + DCX2 * DCZ2 * F8)
        CX1 = DCX1 * VTOT
        CY1 = DCY1 * VTOT
        CZ1 = DCZ1 * VTOT

    Object.IELOW = 0
    return