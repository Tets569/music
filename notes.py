from enum import Enum, IntEnum
from abc import ABC, abstractmethod






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

# KEYS = ['C', 'C+', ...]
# KEYS = ['C', 'B-', ...]


# class Chord:  # but, can be a diff chord in diff key... D: D: D:
# 	def __init__(self, key, notes):
# 		pass



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
C "Major Triad" 	C-E-G 					0-4-7
Cm "Minor Triad" 	C-Eb-G 					0-3-7
Cdim "Diminished" 	C-Eb-Gb 				0-3-6
C+ "Augmented" 	C-E-G# 						0-4-8
Csus "Sustained" 	C-F-G 					0-5-7
C6 "Sixth" 	C-E-G-A 						0-4-7-9
Cm6 "Minor Sixth" 	C-Eb-G-A 				0-3-7-9
C7 "Dominant Seventh" 	C-E-G-Bb 			0-4-7-10
Cmaj7 "Major Seventh" 	C-E-G-B 			0-4-7-11
Cm7 "Minor (Dominant) Seventh" 	C-Eb-G-Bb 	0-3-7-10
Cdim7 "Diminished Seventh" 	C-Eb-Gb-A 		0-3-6-9
C(add9) "Add 9" 	C-E-G-D 				0-4-7-14
C9 "Ninth" 	C-E-G-Bb-D 						0-4-7-10-14
Cmaj9 "Major Ninth" 	C-E-G-B-D 			0-4-7-11-14
Cm9 "Minor Ninth" 	C-Eb-G-Bb-D 			0-3-7-10-14
C11 "Eleventh" 	C-E-G-Bb-D-F 				0-4-7-10-14-17
C13 "Thirteenth" 	C-E-G-Bb-D-A 			0-4-7-10-14-21 

				---> [0-3, 0-4, 0-5] seem to be the things to split into
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

# any()  # use thiiiiis! :P
class MusicNotes:
	#TODO: these need sorted if gonna be tuples so hashable...
	chords = {
		(0,4,7): 'C',
		(0,3,7): 'Cm',
		(0,3,6): 'Cdim',
		(0,4,8): 'C+',
		(0,5,7): 'Csus',
		(0,4,7,9): 'C6',
		(0,3,7,9): 'Cm6',
		(0,4,7,10): 'C7',
		(0,4,7,11): 'Cmaj7',
		(0,3,7,10): 'Cm7',
		(0,3,6,9): 'Cdim7',
		(0,4,7,14): 'Cadd9',
		(0,4,7,10,14): 'C9',
		(0,4,7,11,14): 'Cmaj9',
		(0,3,7,10,14): 'Cm9',
		(0,4,7,10,14,17): 'C11',
		(0,4,7,10,14,21): 'C13'
	}

	chord_desc = {
		'C': 'Major Triad',
		'Cm': 'Minor Triad',
		'Cdim': 'Diminished',
		'C+': 'Augmented',
		'Csus': 'Sustained',
		'C6': 'Sixth',
		'Cm6': 'Minor Sixth',
		'C7': 'Dominant Seventh',
		'Cmaj7': 'Major Seventh',
		'Cm7': 'Minor (Dominant)',
		'Cdim7': 'Diminished Seventh',
		'Cadd9': 'Add 9',
		'C9': 'Ninth',
		'Cmaj9': 'Major Ninth',
		'Cm9': 'Minor Ninth',
		'C11': 'Eleventh',
		'C13': 'Thirteenth'
	}



	def _tones(notes):
		'''
			(G, C, E)  	-->  	(0, 5, 9)G 	--> 	*0-4-7-9  ?	[Seg('G6'), Seg('Gdim7')]
			(C, E, G)	--> 	(0, 4, 7)C 	--> 				[Triad('C')]
			(E, G, C) 	--> 	(0, 3, 8)E 	-- >	* 0-3-7-9 ? [Seg('e6')]

			((((but can  you do this since diff keys for intervals are tech. diff. due to tuning?????))))

			(C, F, A) 	--> 	(0, 5, 9)C <----- xC
						--> 	(0, 4, 7)F <----- IF
		'''


def _permutations(notes):
	perms = []
	n = len(notes)
	repeated_notes = notes * 3

	for i in range(n):
		perms.append(repeated_notes[i:i+n])
	return perms

def _permutations_in_key(notes):
	# TODO: %24 instead of large, jazzy chords?
	# these are ordrerd IFF _permutations are ordered

	perms = _permutations(notes)
	perms_in_key = []

	for perm in perms:
		intvs = []

		for intv in perm:
			intvs.append((intv - perm[0]) % 12)

		perms_in_key.append(intvs)

	return perms_in_key

# TODO: do the above need key mods too then? i guess not since pure interval...



	#### Or just make these into Enums :)
	flat_keys = ['F', 'Bb', 'Eb', 'Ab', 'Db', 'Gb', 'Cb']
	sharp_keys = ['G', 'D', 'A', 'E', 'B', 'F#', 'C#']

	minor_flat_keys = ['d', 'g', 'c', 'f', 'bb', 'eb', 'ab']
	minor_sharp_keys = ['e', 'b', 'f#', 'c#', 'g#', 'd#', 'a#']

	def _key_augment(key):
		if key in (flat_keys, minor_flat_keys):
			return 'flat'
		elif key in (sharp_keys, minor_sharp_keys):
			return 'sharp'
		else:
			return 'neutral'

	def note(key, interval):
		'''
		'''

class FlatKeys(IntEnum):
	C = 0
	F = 1
	Bflat = 2
	Eflat = 3
	Aflat = 4
	Dflat = 5
	Gflat = 6
	Cflat = 7
	a = 0
	d = 1
	g = 2
	c = 3
	f = 4
	bflat = 5
	eflat = 6
	aflat = 7
class SharpKeys(IntEnum):
	C = 0
	G = 1
	D = 2
	A = 3
	E = 4
	B = 5
	Fsharp = 6
	Csharp = 7
	a = 0
	e = 1
	b = 2
	fsharp = 3
	csharp = 4
	gsharp = 5
	dsharp = 6
	asharp = 7


class MajorFlatKeys(IntEnum):
	C = 0
	F = 1
	Bflat = 2
	Eflat = 3
	Aflat = 4
	Dflat = 5
	Gflat = 6
	Cflat = 7
class MajorSharpKeys(IntEnum):
	C = 0
	G = 1
	D = 2
	A = 3
	E = 4
	B = 5
	Fsharp = 6
	Csharp = 7

class MinorFlatKeys(IntEnum):
	a = 0
	d = 1
	g = 2
	c = 3
	f = 4
	bflat = 5
	eflat = 6
	aflat = 7
class MinorSharpKeys(IntEnum):
	a = 0
	e = 1
	b = 2
	fsharp = 3
	csharp = 4
	gsharp = 5
	dsharp = 6
	asharp = 7


### Why not just Key(___) with .numFlats, .numSharps, .notes, etc...?
### Then can just do Keys(Enum).A for example to return Key(A) ??


# class Key:
# 	keys = ('C')

# 	def __init__(self, key='C'):
# 		if key not in cls.keys:
# 			raise ValueException()

# 		if key == 'C':
# 			return KeyC



class Key(ABC):

	@abstractmethod
	def __init__(self, key):
		self.key = key

	@abstractmethod
	def notes(self):
		pass

class KeyCMajor(Key):
	def __init__(self):
		super().__init__('Cmajor')

	def notes(self):
		pass



# 1)
class Keys(Enum):
	C = KeyCMajor()
# 2)
KEYS = {
	'C': KeyCMajor()
}
# 3-4)
class Keeys:
	# 3) 
	# TODO: ---if you do this, make sure peeps can't change this class with reference :) ---> return KeyCMajor and have them instantiate on declaration!
	D = KeyCMajor()
	# 4)
	_C = KeyCMajor()
	@property
	def C(self):
		return self._C
	

#def is_sharp(note, key):
	#if note not stripped of mods, error
#	"if key in MajorSharpKeys and val > 2...




if __name__ == '__main__':
	print(_permutations_in_key([0,4,7]))

	# TODO: ERROR CHECKING HERE...
	# k = Key()
	# k = Key('k')
	# a = Key.notes()

	# k = Keys.C.value   # TODO: ...this is why we don't use Enums for instantiation.....
	# print(k)
	# print(dir(k))

	# k = KEYS['C']   # TODO: ...this is why we don't use Enums for instantiation.....
	# print(k)
	# print(dir(k))

	# print('\n\n')  # TODO: --'property object', not KeyCMajor object
	# k = Keeys.C
	# print(k)
	# print(dir(k))

	# print('\n\n')
	# k = Keeys.D
	# print(k)
	# print(dir(k))

	a = Keeys.D
	b = Keeys.D
	a.x = 1
	print(a == b)
	print(b.x)

	# for k,v in intervals.items():
	# 	print(k,v)
	# ''' can't use dict as key for other dict....'''



	# TODO: inifinite sequence generator of notes so that you can go through a scale?
	# TODO: ...does that include C4, C5, etc.... ???? (technically infinite???....)
	# TODO: enharmonic equivalents...

	# TODO: establish Keys vs. Notes vs. Chords, and which can be Major/Minor/Sharp/Flat/Aug./Dim./etc.
	# TODO: Major -> relative minor... through function? Can transform between?
		# TODO: 'add-sharp' or 'add-flat' methods too if allowing transformations?
	# TODO: Theoretical keys with ## or bb sigs?
		# TODO: secondary dominants :3
		# TODO: Tonic -I, Dom -V/-vii, PreDom -IV/-ii, Nothing -iii
		'''
			---key F -> Dom is C---
			C-E-G:      V
			D-F-*Ab: 	iio/V
			*Eb-G-Bb: 	bIII/V
			E-G-*B: 	iii/V
			E-*G#-*B#: 	III+/V
			F-*Ab-C: 	iv/V
			G-*B-D: 	V/V
			*Ab-C-*Eb: 	bVI/V
			A-C-*Eb: 	vio/V
			*B-D-F: 	viio/V
			C-E-G: 		V

			----Changes----
			V - ()
			iio/V - (bb --> bbbbb)
			bIII/V - 1
			iii/V - 1 (V/V)
			III+/V - 4
			iv/V - 2 (iio/V, bVI/V)
			V/V - 1 (iii/V)
			bVI/V - 2 (iio/V, iv/V)
			vio/V - 1
			viio/V - 1 (V/V, iii/V)

			----Equivs----
			ii/V = vi   ***
			IV/V = I    ***
			v/V = ii
			vi/V = iii  ***
			bVII/V = IV

			----notes----
			i76-5 ? -> iio/V
		'''

		# TODO: 
		# TODO: 
		# TODO: 
		# TODO: 