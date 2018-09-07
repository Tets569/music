








'''
	Phylogenetic Traits D: D: D:
		Rhythms, 5 notes / 16 slots on spinning wheel



		....STARS IN STARRY NIGHT v MELODY D: D: D:....
		12C3 x4 ... Major chord.. .any other interestings?
		https://www.youtube.com/watch?v=d8s8e8JdGCc
'''


'''
	Phi 1.618~~~ (Golden Ratio)
		Line-> Short + Long s.t. Short/Long == Long/Whole

		...Area Fibonacci???
		Time-based music, so can only tell Fib. in retrospective
		...Words written with Fib-pentameter? (wrong word but whatever)

'''


'''
	Yeah Chopin!
	Prelude in C: Op.23 No.1
'''



# UNIT TESTIIIIING
# Fractals in music? D:
# Connection b/w Fibonacci and Fractals?
# Fib. Tuning with other Phenomena!!!
# Musical Fractal - theme harmonizes with slowed down version of self
# Fugues... (Bach!) -- Harmony between N(notes)(aligned time-wise... Spd Mults.)
# Contrapunctus


'''
	C-maj7 doesn't have as much tension as 7, soooo
	G7 brings back to C more
'''
KEYS = ['C', 'C+', ...]
KEYS = ['C', 'B-', ...]


class Chord:  # but, can be a diff chord in diff key... D: D: D:
	def __init__(self, key, notes):
		pass



'''
	C,G  -> Eb, E -> i, I
	C,Ab -> Eb, F -> VIb, iv
	C,A  -> E, F  -> vi, IV
'''





'''
	You can do a "group" on Intervals/Semitones, but not pitches/Hertz	
'''

# https://arxiv.org/html/1202.4212v1






'''
L ------------[] Volume, not pitch D:
R    ---------[]

?Log(dist) to tell hot/cold
?Each fox note in chord, distance determines interval?
	?Leads to only specific arrangements on field?
	?Does distance stay same-sounding? diff like should??
'''


'''
	Enum of notes, based on semitones?
	Sliding Enum based on Key? :D
'''
'''
C-E-G : 1/1, 5/4, 3/2 : 4/4, 5/4, 6/4 : 4-5-6
			1 : 1.25 : 1.5
			0 : 0.25 : 0.75
C-E:  5/4 (5/4) ((15/12))
C-G:  3/2 (6/4) ((18/12))
E-G:  (3/2-5/4?) ((1/4?))
C-F:  4/3
F-Bb: 

'''

''' 	JUST INTONATION
	C - 1    ( 1/1)  (24/24) 3
	D - 9/8  ( 9/8)  (27/24) 3
	E - 5/4  (10/8)  (30/24) 2
	F - 4/3  (32/24) (32/24) 4
	G - 3/2  (12/8)  (36/24) 4
	A - 5/3  (40/24) (40/24) 5
	B - 15/8 (15/8)  (45/24) 3
	C - 2    ( 8/8)  (48/24) 

	Unison - 	1:1
	Octave - 	2:1
	P5 - 		3
Our new Terms of Service and Privacy Statement are in effect.
Repositories

    Tets569/formal-language

:2
	P4 - 		4:3
	M6 - 		5:3
	M3 - 		5:4
	m6 - 		8:5
	m3 - 		6:5
'''

'''
	Major - 4:5:6					---	x15, 60:75:90
	Minor - 10:12:15				---  x6, 60:72:90
	dim - 160,192,231 ~ 20,24,29	--- 
	7 - 20,25,30,36					---  x9, 180:225:270:324
	m7 -  10,  12,15,18
	M7 - 8,10,12,  15

1/1, 6/5, 3/2 (C->C, C->Eb, C->G)

10, 12, 15
'''



''' 	PYTHAGOREAN INTONATION
	C - 1
	D - 9/8
	E - 81/64
	F - 4/3
	G - 3/2
	A - 27/16
	B - 243/128
	C - 2

	Unison - 	1:1
	Octave - 	2:1
	P5 - 		3:2
	P4 - 		4:3
	M6 - 		5:3
	M3 - 		5:4
	m6 - 		8:5
	m3 - 		6:5
'''





'''
	Cents (12-TET)
	100 cents / semitone, 1200 cents / octave
	n = 1200 * log2( f2 / f1 )
'''



'''
	Name 	Notes in C Major Scale 	Semi-tones from fundamental
C "Major Triad" 	C-E-G 	0-4-7
Cm "Minor Triad" 	C-Eb-G 	0-3-7
Cdim "Diminished" 	C-Eb-Gb 	0-3-6
C+ "Augmented" 	C-E-G# 	0-4-8
Csus "Sustained" 	C-F-G 	0-5-7
C6 "Sixth" 	C-E-G-A 	0-4-7-9
Cm6 "Minor Sixth" 	C-Eb-G-A 	0-3-7-9
C7 "Dominant Seventh" 	C-E-G-Bb 	0-4-7-10
Cmaj7 "Major Seventh" 	C-E-G-B 	0-4-7-11
Cm7 "Minor (Dominant) Seventh" 	C-Eb-G-Bb 	0-3-7-10
Cdim7 "Diminished Seventh" 	C-Eb-Gb-A 	0-3-6-9
C(add9) "Add 9" 	C-E-G-D 	0-4-7-14
C9 "Ninth" 	C-E-G-Bb-D 	0-4-7-10-14
Cmaj9 "Major Ninth" 	C-E-G-B-D 	0-4-7-11-14
Cm9 "Minor Ninth" 	C-Eb-G-Bb-D 	0-3-7-10-14
C11 "Eleventh" 	C-E-G-Bb-D-F 	0-4-7-10-14-17
C13 "Thirteenth" 	C-E-G-Bb-D-A 	0-4-7-10-14-21 
'''

'''
	Pentatonic - 5
	Chromatic - 12
	M/m Diatonic - 7 
	(Dorian, Lydian, etc.)

	BUT we use 7/12 notes of the Chromatic as a Scale/Key . . . 
	We use Log-scaling (step sizes of equal frequency ratios)
	While very rarely some may use steps of equal frequencies themselves
'''

any()  # use thiiiiis! :P