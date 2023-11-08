candidate_cv_info_extraction = [
{
   "name":"Candidate_information",
   "description":"extract all the information of the candidate that is available in the cv",
   "parameters":{
      "type":"object",
      "properties":{
         "candidate_personal_info":{
            "name":"candidate_personal_info",
            "description":"Extract personal info like name, address, contact etc from CV",
            "parameters":{
               "type":"object",
               "properties":{
                  "name":{
                     "type":"string",
                     "description":"Name of the candidate"
                  },
                  "contact":{
                     "type":"string",
                     "description":"Contact number of the candidate"
                  },
                  "LinkedIn":{
                     "type":"string",
                     "description":"LinkedIn ID of candidate"
                  },
                  "GitHub_ID":{
                     "type":"string",
                     "description":"GitHub ID of candidate"
                  },
                  "WebSite":{
                     "type":"string",
                     "description":"Portfolio website candidate"
                  },
                  "email":{
                     "type":"string",
                     "description":"Email Id of the candidate"
                  }
               }
            }
         },
         "candidate_past_experience":{
            "name":"candidate_past_experience",
            "description":"Extract past work experiences, employers, roles, responsibilities, duration etc",
            "parameters":{
               "type":"object",
               "properties":{
                  "employers":{
                     "type":"string",
                     "description":"List of past employers"
                  },
                  "positions":{
                     "type":"string",
                     "description":"Past roles/positions held"
                  },
                  "durations":{
                     "type":"string",
                     "description":"Duration of each past appointment"
                  }
               }
            }
         },
         "candidate_education_info":{
            "name":"candidate_education_info",
            "description":"Extract education details, degrees, universities, grades, durations etc from CV",
            "parameters":{
               "type":"object",
               "properties":{
                  "degrees":{
                     "type":"string",
                     "description":"List of degrees"
                  },
                  "universities":{
                     "type":"string",
                     "description":"Universities attended"
                  },
                  "grades":{
                     "type":"string",
                     "description":"Grades or CGPA in each degree/course"
                  },
                  "durations":{
                     "type":"string",
                     "description":"Time period of each degree/course"
                  }
               }
            }
         },
         "candidate_skills":{
            "name":"candidate_skills",
            "description":"Extract skills from CV, IT-technology skills, language skills etc",
            "parameters":{
               "type":"object",
               "properties":{
                  "IT_skills":{
                     "type":"string",
                     "description":"Programming and software skills like Tensorflow, pytorch, MEARN etc"
                  },
                  "Programming_language":{
                     "type":"string",
                     "description":"Programming Language like C, C++, python etc"
                  }
               }
            }
         },
         "candidate_soft_skills":{
            "name":"candidate_soft_skills",
            "description":"Extract soft skills like communication, leadership, business skills,teamwork etc mostely Non technical skills",
            "parameters":{
               "type":"object",
               "properties":{
                  "communication":{
                     "type":"string",
                     "description":"Communication skills"
                  },
                  "language_skills":{
                     "type":"string",
                     "description":"Languages the candidate is fluent in"
                  },
                  "business_skills":{
                     "type":"string",
                     "description":"Business related skills"
                  },
                  "leadership":{
                     "type":"string",
                     "description":"Leadership skills"
                  },
                  "teamwork":{
                     "type":"string",
                     "description":"Teamwork skills"
                  }
               }
            }
         },
         "candidate_achievements":{
            "name":"candidate_achievements",
            "description":"Extract professional and academic achievements, awards, certifications",
            "parameters":{
               "type":"object",
               "properties":{
                  "awards":{
                     "type":"string",
                     "description":"Awards or recognitions received"
                  },
                  "certifications":{
                     "type":"string",
                     "description":"Professional certifications google, amazone-aws, azure, IBM certifications"
                  },
                  "publications":{
                     "type":"string",
                     "description":"Any publications or articles or any libraries on github"
                  }
               }
            }
         }
      }
   }
}
       

]