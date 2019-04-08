F_P = [\
  'kf1',
  'kr1',
  'kf2',
  'kr2',
  'kf3',
  'kr3',
  'V4',
  'K4',
  'kf5',
  'kr5',
  'kf6',
  'kr6',
  'kf7',
  'kr7',
  'kf8',
  'kr8',
  'kf9',
  'kr9',
  'V10',
  'K10',
  'kf11',
  'K11',
  'V12',
  'K12',
  'kf13',
  'K13',
  'kf14',
  'K14',
  'kf15',
  'K15',
  'kf16',
  'K16',
  'kf17',
  'K17',
  'kf18',
  'K18',
  'kf19',
  'K19',
  'kf20',
  'K20',
  'kf21',
  'K21',
  'kf22',
  'K22',
  'kf23',
  'kr23',
  'kf24',
  'kr24',
  'kf25',
  'kr25',
  'V26',
  'K26',
  'kf27',
  'K27',
  'V28',
  'K28',
  'kf29',
  'kr29',
  'V30',
  'K30',
  'kf31',
  'K31',
  'V32',
  'K32',
  'kf33',
  'K33',
  'kf34',
  'kr34'\
]

for i,name in enumerate(F_P):
  exec('%s=%d'%(name,i))

def f_params():
  x = [0]*len(F_P)

  x[kf1] = 1.2e-3
  x[kr1] = 7.6e-4
  x[kf2] = 0.01
  x[kr2] = 0.1
  x[kf3] = 1.0
  x[kr3] = 0.01
  x[V4] = 62.5
  x[K4] = 50.
  x[kf5] = 0.1
  x[kr5] = 1.
  x[kf6] = 20.
  x[kr6] = 5.
  x[kf7] = 60.
  x[kr7] = 546.
  x[kf8] = 2040.
  x[kr8] = 15700.
  x[kf9] = 40.8
  x[kr9] = 0.
  x[V10] = 0.0154
  x[K10] = 340.
  x[kf11] = 0.222
  x[K11] = 0.181
  x[V12] = 0.289
  x[K12] = 0.0571
  x[kf13] = 1.53
  x[K13] = 11.7
  x[kf14] = 6.73e-3
  x[K14] = 8.07
  x[kf15] = 3.5
  x[K15] = 317.
  x[kf16] = 0.058
  x[K16] = 2200.
  x[kf17] = 2.9
  x[K17] = 317.
  x[kf18] = 0.058
  x[K18] = 60.
  x[kf19] = 9.5
  x[K19] = 1.46e+5
  x[kf20] = 0.3
  x[K20] = 160.
  x[kf21] = 16.
  x[K21] = 1.46e+5
  x[kf22] = 0.27
  x[K22] = 60.
  x[kf23] = 0.1
  x[kr23] = 2.
  x[kf24] = 9.85
  x[kr24] = 0.0985
  x[kf25] = 45.8
  x[kr25] = 0.047
  x[V26] = 2620.
  x[K26] = 3680.
  x[kf27] = 16.9
  x[K27] = 39.1
  x[V28] = 17000.
  x[K28] = 9.02
  x[kf29] = 507.
  x[kr29] = 234.
  x[V30] = 2e+4
  x[K30] = 80000.
  x[kf31] = 0.107
  x[K31] = 4.35
  x[V32] = 2e+4
  x[K32] = 80000.
  x[kf33] = 0.211
  x[K33] = 12.
  x[kf34] = 1e-3
  x[kr34] = 0.

  return x