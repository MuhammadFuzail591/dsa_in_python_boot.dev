def last_work_experience(work_experiences):
   if len(work_experiences) == 0:
      return None
   
   num_of_experiences = len(work_experiences)
   
   last_experience = work_experiences[num_of_experiences-1]

   return last_experience