import unittest
from structures import *

class TestWorkoutPlan(unittest.TestCase):
    
    def testWorkoutPlan(self):
        plan = WorkoutPlan("test plan", set(["test", "tag", "plan"]))
        ex1 = Exercise("Test", "Computer")
        block1 = ExerciseBlock(ex1, "A test block", set(["test","tag", "block"]))
        block1.addSet(10, 25)
        block1.addSet(10,35)

        ex2 = Exercise("Test2", "Computer")
        block2 = ExerciseBlock(ex2, "Second test block", set(["test", "block2"]))
        block2.addSet(12, 20)
        block2.addSet(12, 25)
        block2.addSet(10, 30)

        plan.addExerciseBlock(block1)
        plan.addExerciseBlock(block2)

        
        self.assertEqual(len(plan.exercise_blocks), 2)
        self.assertEqual(len(plan.tags), 3)

    def testRemoveExerciseBlock(self):
        plan = WorkoutPlan("test plan", set(["test", "tag", "plan"]))
        ex1 = Exercise("Test", "Computer")
        block1 = ExerciseBlock(ex1, "A test block", set(["test","tag", "block"]))
        block1.addSet(10, 25)
        block1.addSet(10,35)

        ex2 = Exercise("Test2", "Computer")
        block2 = ExerciseBlock(ex2, "Second test block", set(["test", "block2"]))
        block2.addSet(12, 20)
        block2.addSet(12, 25)
        block2.addSet(10, 30)

        plan.addExerciseBlock(block1)
        plan.addExerciseBlock(block2)

        self.assertEqual(len(plan.exercise_blocks), 2)

        plan.removeExerciseBlock(1)
        
        self.assertEqual(len(plan.exercise_blocks), 1)
        self.assertEqual(plan.exercise_blocks[0], block1)

    def testSerializeExercise(self):
        ex1 = Exercise("Test", "Computer")
        actual = ex1._serialize()

        expected = {
            "name": "Test",
            "equipment": "Computer"
        }

        self.assertEqual(expected, actual)

    def testSerializeExerciseSet(self):
        ex1 = Exercise("Test", "Computer")
        s1 = ExerciseSet(ex1, 12, 40, 1)

        actual = s1._serialize()

        expected = {
            "exercise": ex1._serialize(),
            "reps": 12,
            "weight": 40,
            "units": "lbs",
            "set_index": 1,
            "target": "reps"
        }

        self.assertEqual(expected, actual)

    def testSerializeExerciseBlock(self):
        ex1 = Exercise("Test", "Computer")
        block1 = ExerciseBlock(ex1, "A test block", set(["test","tag", "block"]))
        block1.addSet(10, 25)
        block1.addSet(10,35)

        actual = block1._serialize()

        expected = {
            "exercise": ex1._serialize(),
            "description": "A test block",
            "tags": {"test","tag", "block"},
            "sets": [
                {
                    "exercise": ex1._serialize(),
                    "reps": 10,
                    "weight": 25,
                    "units": "lbs",
                    "set_index": 0,
                    "target": "reps"
                },
                {
                    "exercise": ex1._serialize(),
                    "reps": 10,
                    "weight": 35,
                    "units": "lbs",
                    "set_index": 1,
                    "target": "reps"
                }
            ]
        }

        self.maxDiff = None

        self.assertEqual(expected, actual)

    def testSerializeWorkoutPlan(self):
        plan = WorkoutPlan("test plan", set(["test", "tag", "plan"]))
        ex1 = Exercise("Test", "Computer")
        block1 = ExerciseBlock(ex1, "A test block", set(["test","tag", "block"]))
        block1.addSet(10, 25)
        block1.addSet(10,35)

        ex2 = Exercise("Test2", "Computer")
        block2 = ExerciseBlock(ex2, "Second test block", set(["test", "block2"]))
        block2.addSet(12, 20)
        block2.addSet(12, 25)
        block2.addSet(10, 30)

        plan.addExerciseBlock(block1)
        plan.addExerciseBlock(block2)

        actual = plan._serialize()

        expected = {
            "name": "test plan",
            "tags": {"test", "tag", "plan"},
            "exercise_blocks": [
                block1._serialize(),
                block2._serialize()
            ]
        }


        self.maxDiff = None
        self.assertEqual(expected, actual)
    

    