# fo76decode
fo76decode is a python tool to decode fallout 76 launch codes
## dependecies
fo76decode depends of the re python library
## funcions:
the original namespace of the class is fo76decode

`fo76decode.pairing(key,number,pairlist)`:

allow you to add nuke codes pairs into a dictionary type list

exemple : `a={"g":2,"h":8,"j":2,"m":4,"o":7,"q":6,"x":5,"b":7}`

G is the letter asosiated to the nuber 2

to insert it like in the exemple using the pairing method

would be `fo76decode.pairing(g,2,a)`

variables: 

![alt text](https://projects.overcorp.net/2022/images/152838.png)

`key`(str) represents the letter of a pair of code

`number`(int) represents the number of a pair of code

`pairlist`(tuple) represents the list which contains the pairs

output a tuple of letters

`fo76decode.findscrambled(keyword,pairlist)`:

finds the scrambled anagram of the code

variables:

`keyword`(str) the keyword guessed on the walls of the white sping bumker

`pairlist`(tuple) the list of pairs of the nuke code (type {letter:number,letter:nuber})

`fo76decode.findcode(scrambled,word,pairs)`:
final step to find the code:

this funcion is used to decode the pairs using the scrambled word, the solved word, and the paris.
note: the scrambled word sould be as the same order of the outputed by findscrambled

variables:

`scrambled`(tuple) the scrambled word ouputed as a tuple

`word`(str) the unscrambled word anagram

`pairlist` the list of code pairs

output:(str) the nuke launch codes for your favorite silo
# bages
doing my best to write quality code !:

[![Maintainability](https://api.codeclimate.com/v1/badges/77fe36c56a8ad2d39a4a/maintainability)](https://codeclimate.com/github/aphshir/fo76decode/maintainability)

I hope improving it soon !
