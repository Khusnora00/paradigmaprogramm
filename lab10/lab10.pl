% LABORATORY WORK 10
% Individual variant 4 - Consultation

% Students
student(aida).
student(miras).
student(dana).
student(timur).
student(aliya).

% Courses
course(programming_1).
course(programming_2).
course(data_structures).
course(databases).
course(artificial_intelligence).
course(machine_learning).

% Completed courses
completed(aida, programming_1).
completed(aida, programming_2).
completed(aida, data_structures).
completed(aida, databases).

completed(miras, programming_1).
completed(miras, databases).

completed(dana, programming_1).
completed(dana, programming_2).

completed(timur, programming_1).

completed(aliya, programming_1).
completed(aliya, databases).

% Course prerequisites
requires(programming_2, programming_1).
requires(data_structures, programming_2).
requires(artificial_intelligence, data_structures).
requires(artificial_intelligence, databases).
requires(machine_learning, artificial_intelligence).

% Rule 1: AI candidate
ai_candidate(Student) :-
completed(Student, data_structures),
completed(Student, databases).

% Rule 2: Strong student
strong_student(Student) :-
completed(Student, programming_2),
completed(Student, data_structures).

% Rule 3: Direct missing prerequisite
missing_direct(Student, Course, Prerequisite) :-
student(Student),
requires(Course, Prerequisite),
+ completed(Student, Prerequisite).

% Rule 4: Direct eligibility
immediate_eligible(Student, Course) :-
student(Student),
course(Course),
+ missing_direct(Student, Course, _).

% Rule 5: Recursive prerequisite search
prerequisite(Course, Prerequisite) :-
requires(Course, Prerequisite).

prerequisite(Course, Prerequisite) :-
requires(Course, Intermediate),
prerequisite(Intermediate, Prerequisite).

% Rule 6: Find all missing prerequisites
missing_all(Student, Course, Missing) :-
setof(P,
(prerequisite(Course, P),
\+ completed(Student, P)),
Missing).

missing_all(_, _, []).

% Rule 7: Full eligibility
eligible(Student, Course) :-
student(Student),
course(Course),
missing_all(Student, Course, []).

% Rule 8: Individual variant - consultation
needs_advice(Student, Course) :-
student(Student),
course(Course),
missing_all(Student, Course, Missing),
Missing = [].

% Rule 9: Consultation with missing course list
advice_list(Student, Course, Missing) :-
needs_advice(Student, Course),
missing_all(Student, Course, Missing).

% Rule 10: Recommendation
recommendation(Student, Course, eligible, []) :-
eligible(Student, Course).

recommendation(Student, Course, missing, Missing) :-
missing_all(Student, Course, Missing),
Missing = [].

% Rule 11: Safe recursive prerequisite search
safe_prerequisite(Course, Prerequisite) :-
safe_prerequisite(Course, Prerequisite, [Course]).

safe_prerequisite(Course, Prerequisite, _) :-
requires(Course, Prerequisite).

safe_prerequisite(Course, Prerequisite, Visited) :-
requires(Course, Next),
\+ memberchk(Next, Visited),
safe_prerequisite(Next, Prerequisite, [Next|Visited]).