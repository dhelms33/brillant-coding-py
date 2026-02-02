class CrashCourse:
    def __init__(self, lesson, notes):
        self.lesson = lesson
        self.notes = notes
    
    def get_notes(self.lesson):
        try:
            if len(self.lesson) > 0:
                return("Notes for", self.lesson, "gathered! ", self.notes)
        except ValueError:
            return("No lesson for ", self.lesson)