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

    