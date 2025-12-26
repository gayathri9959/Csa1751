can_fly(sparrow).
can_fly(pigeon).
can_fly(parrot).

cannot_fly(penguin).
cannot_fly(ostrich).

fly_or_not(Bird, fly) :-
    can_fly(Bird).

fly_or_not(Bird, no_fly) :-
    cannot_fly(Bird).
can_fly(sparrow).
can_fly(pigeon).
can_fly(parrot).

cannot_fly(penguin).
cannot_fly(ostrich).

fly_or_not(Bird, fly) :-
    can_fly(Bird).

fly_or_not(Bird, no_fly) :-
    cannot_fly(Bird).
