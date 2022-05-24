import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
nltk.download("punkt")
nltk.download("stopwords")
nltk.download("wordnet")
lemmatizer = WordNetLemmatizer()
from config import CauseOfLossConfig

class causeOfLoss():
    
    def __init__(self, incident_details: str) -> None:
 
        self.incident_details = incident_details
        self.word_list = self.get_word_list_from_incident_details()

    #############################################################################
    def get_word_list_from_incident_details(self) -> list:

        ''' Break incident details into word list, remove stop words and return a list of words.'''

        stop_words_list = set(stopwords.words("english") + CauseOfLossConfig.REMOVED_COMMON_WORDS)
        
        word_list = word_tokenize(self.incident_details)
        
        word_list = [lemmatizer.lemmatize(word).lower() for word in word_list if word.lower() not in stop_words_list]
       
        word_list=" ".join(word_list).replace("-"," ").replace("."," ")
        
        word_list=word_list.split()
       
        return word_list

    ################################################################################
    def get_part_name_from_word_list(self) -> str:

        '''return: list parts name of vehicle if mentioned by customer in incident details''' 

        mentioned_part=[]

        for j in range(len(self.word_list)):
          for k in CauseOfLossConfig.PART_DICT:
              if self.word_list[j] in CauseOfLossConfig.PART_DICT[k]:
                if k == "Tail" and j < (len(self.word_list)-1):    #condition for tail gate
                  if self.word_list[j+1] in ["lamp","light"]:
                    mentioned_part.append("Taillight")
                  elif self.word_list[j+1] == "gate":
                    mentioned_part.append("Tail Gate")
                  else:
                    mentioned_part.append("")

                elif k == "Fog" and j < (len(self.word_list)-1):   #condition for fog light
                  if self.word_list[j+1] in ["lamp" ,"light"]:
                    mentioned_part.append("Fog Light")
                  else:
                    mentioned_part.append("")

                elif (k == "Glass" or k == "Front Glass") and j > 0:     #condition for window glass, back glass and windshield
                  if self.word_list[j-1] in  ["back", "rear", "rare"]:
                    mentioned_part.append("Back Glass")
                  elif self.word_list[j-1]=="window":
                    mentioned_part.append("Window Glass")
                  else:
                    mentioned_part.append("Front Glass")

                else:
                    mentioned_part.append(k)

              elif self.word_list[j] in ["light", "lights"] and j>0:
                if self.word_list[j-1] == "head" :
                  mentioned_part.append("Headlight")
                elif self.word_list[j-1] in ["rear", "back"] :
                  mentioned_part.append("Taillight")

        mentioned_part=list(set(mentioned_part))
       
        if not mentioned_part:
          mentioned_part .append("NA")
        print("salman")
        return mentioned_part

    ###########################################################################
    def get_types_of_damages_from_word_list(self) ->str:

        '''return : list damage types in vehicle if mentioned by customer in incident details'''

        CauseOfLossConfig.DAMAGE_TYPE_DICT
        mentioned_damages=[]
       
        for k in CauseOfLossConfig.DAMAGE_TYPE_DICT:
          damage=set()
          damage=set(CauseOfLossConfig.DAMAGE_TYPE_DICT[k]).intersection(set(self.word_list))
          if damage:
            mentioned_damages=mentioned_damages + list(damage)
        
        if not mentioned_damages:
          mentioned_damages.append("NA")

        return mentioned_damages

    ##################################################################################
    def get_correct_side_keyword(self, word_string: str)->str:

        ''' take a uncorrect side word as a string and search for the correct keyword of that 
            uncorrect word in our SIDE_WORD dictionary return the right keyword'''

        correct_word = ""
        
        for k in CauseOfLossConfig.SIDE_WORD:
          if word_string in CauseOfLossConfig.SIDE_WORD[k]:
            correct_word = k

        return correct_word

    #########################################################################################
    def get_impact_side_from_word_list_preference1(self) ->str:

        ''' this function return impact side form word list by using impact type keywords (e.g. hit, nudged, rubbed)'''

        impact_side_flag = True
        impact_side = ""
       
        if self.word_list:
          copy_word_list = self.word_list.copy()
          imapct_type_in_word = [ element for element in copy_word_list if element in CauseOfLossConfig.IMPACT_TYPE ]
          if imapct_type_in_word:
            for i in imapct_type_in_word:
              forword_word_count = 0
              index_of_impact_type = copy_word_list.index(i)
              for j in range(index_of_impact_type, len(copy_word_list)):
                forword_word_count += 1
                if forword_word_count<6:
                  for k in CauseOfLossConfig.SIDE_WORD:
                    if copy_word_list[j] in CauseOfLossConfig.SIDE_WORD[k]:
                      impact_side = impact_side+" "+k
              if i in copy_word_list:
                copy_word_list.remove(i)
            
            if not impact_side:
              backward_word_count = 0
              for j in reversed(range(index_of_impact_type)):
                backward_word_count += 1
                if backward_word_count < 4:
                  for k in CauseOfLossConfig.SIDE_WORD:
                    if self.word_list[j] in CauseOfLossConfig.SIDE_WORD[k] and impact_side_flag:
                      if j>0 and self.word_list[j-1] in CauseOfLossConfig.All_FOUR_SIDE:
                        if self.word_list[j-1].lower() != k.lower():
                          impact_side = impact_side + self.get_correct_side_keyword(self.word_list[j-1]) + " " + k
                          impact_side_flag = False
                      else:
                        impact_side = impact_side + " " + k
                        impact_side_flag = False

        return impact_side.strip()

    #############################################################################################
    def get_impact_side_from_word_list_preference2(self)-> str:

        ''' this function return impact side form word list by using part position (e.g. if customer mention front 
        glass then impact side will be front)'''

        impact_side = ""
        
        if self.word_list:
          FRONT, BACK, RIGHT, TOP, LEFT, LEFT_RIGHT, DOOR = False, False, False, False, False,False, False
          for j in range(len(self.word_list)):

            if self.word_list[j] in CauseOfLossConfig.BUMPER :
              if j>0 and self.word_list[j-1] in CauseOfLossConfig.REAR_WORD :
                BACK = True
              elif j>0 and self.word_list[j-1] in CauseOfLossConfig.FRONT_WORD :
                FRONT = True
              elif j>0 and self.word_list[j-1] in CauseOfLossConfig.LEFT_WORD :
                LEFT = True
              elif j>0 and self.word_list[j-1] in CauseOfLossConfig.RIGHT_WORD:
                RIGHT = True  
              else:
                FRONT = True
                BACK = True

            if self.word_list[j] in CauseOfLossConfig.GET_FRONT_SIDE_BY_PART and FRONT == False:
              if j>0 and self.word_list[j] in CauseOfLossConfig.GLASS and self.word_list[j-1] == "window":
                if j>1 and (self.word_list[j-1] in CauseOfLossConfig.LEFT_WORD or self.word_list[j-2] in CauseOfLossConfig.LEFT_WORD):
                  LEFT = True
                elif j>1 and (self.word_list[j-1] in CauseOfLossConfig.RIGHT_WORD or self.word_list[j-2] in CauseOfLossConfig.RIGHT_WORD):
                  RIGHT = True
                else:
                  LEFT_RIGHT = True
              elif j>0 and self.word_list[j-1] in CauseOfLossConfig.REAR_WORD :
                BACK = True
              else:
                FRONT = True

            if self.word_list[j] in CauseOfLossConfig.GET_REAR_SIDE_BY_PART and BACK == False:
              if j>0 and self.word_list[j-1] in CauseOfLossConfig.FRONT_WORD:
                FRONT = True
              else:
                BACK = True

            if self.word_list[j] in CauseOfLossConfig.ROOF_WORD and "roof" in self.word_list and  TOP == False:
              TOP = True

            if self.word_list[j] in CauseOfLossConfig.GET_LEFT_RIGHT_SIDE_BY_PART:
              if j>1 and self.word_list[j-1] in CauseOfLossConfig.All_FOUR_SIDE and self.word_list[j-2] in CauseOfLossConfig.All_FOUR_SIDE and  DOOR==False:
                DOOR = True
                side= self.get_correct_side_keyword(self.word_list[j-2]) +" " + self.get_correct_side_keyword(self.word_list[j-1])
              if j>1 and (self.word_list[j-1] in CauseOfLossConfig.LEFT_WORD or self.word_list[j-2] in CauseOfLossConfig.LEFT_WORD) and  LEFT == False:
                LEFT = True
              elif j>1 and (self.word_list[j-1] in CauseOfLossConfig.RIGHT_WORD or self.word_list[j-2] in CauseOfLossConfig.RIGHT_WORD) and  RIGHT == False:
                RIGHT = True
              else: 
                LEFT_RIGHT = True

          if TOP:
            impact_side = impact_side +" "+ "Top"
          if FRONT:
            impact_side = impact_side +" "+ "Front"
          if BACK:
            impact_side = impact_side +" "+ "Rear"
          if DOOR:
            impact_side = impact_side +" "+ side
          elif LEFT_RIGHT:
            impact_side = impact_side+" "+ "Left Right"
          else:
            if RIGHT:
              impact_side = impact_side+" "+ "Right"
            if LEFT:
              impact_side = impact_side+" "+ "Left"     
        
        return impact_side

    #######################################################################################
    def get_impact_side_from_word_list_preference3(self, impact_side: str)->str:
        '''
        NOTE - this function will run if we get empty string from get_impact_side_from_word_list_preference1 
        and get_impact_side_from_word_list_preference2 function.

        it take word list of incident details and impact side (string)  returned from above two function and return
        impact side
        '''
        impact_side_count=0

        if not impact_side:
          if self.word_list:
            for j in range(len(self.word_list)):
              for k in CauseOfLossConfig.SIDE_WORD:
                if self.word_list[j] in CauseOfLossConfig.SIDE_WORD[k] and impact_side_count<2:
                  if j<(len(self.word_list)-1) and self.word_list[j+1] in CauseOfLossConfig.All_FOUR_SIDE:
                    if self.word_list[j+1].lower() != k.lower():
                      impact_side = impact_side + " " + k +" "+ self.get_correct_side_keyword(self.word_list[j+1])
                      impact_side_count += 1
                  else:
                    impact_side = impact_side+ " " +k
              
                    impact_side_count+=1

        return impact_side

    #######################################################################################
    def get_impact_side_from_word_list_preference4(self, impact_side: str)->str: 

        '''
        NOTE - this function will run if we get empty string from get_impact_side_from_word_list_preference1, 
        get_impact_side_from_word_list_preference2 function and get_impact_side_from_word_list_preference3.
        this function is only for "reverse" word, if word list don't have any other impact side key words

        it take impact side (string)  returned from above two function and return impact side
        '''
        if not impact_side:
          if self.word_list:
            for j in range(len(self.word_list)):
              if self.word_list[j] in CauseOfLossConfig.REVERSE:
                impact_side = "Rear"

        return impact_side

    def get_final_impact_side(self) ->str:

        ''' arg : word list of incident details
            return : impact side from all four preference impact side function 
        '''
        impact_side=""  

        impact_side_from_function_preference1 = self.get_impact_side_from_word_list_preference1()

        impact_side_from_function_preference2 = self.get_impact_side_from_word_list_preference2()

        combined_impact_side = impact_side_from_function_preference1 + " " + impact_side_from_function_preference2

        impact_side_from_function_preference3 = self.get_impact_side_from_word_list_preference3(combined_impact_side.strip())
        
        impact_side_from_function_preference4 = self.get_impact_side_from_word_list_preference4( impact_side_from_function_preference3)
        
        impact_side=list(set(impact_side_from_function_preference4.split()))
        
        impact_side=" ".join(impact_side)
        
        if not impact_side:
          impact_side="NA"

        return impact_side

    def get_only_windshield_damaged_flag(self)->bool:

        ''''''
        branch_tree_hail_is_present, chance_for_glass_damage_only, WS_damage_flag = True, False, False
        
        if not set(self.word_list).intersection({"tree", "branch", "hail"}):  #checking for "tree", "branch", "hail" words in word_list
          branch_tree_hail_is_present = False
        
        damage_types_in_cause_of_loss = self.get_types_of_damages_from_word_list()

        impact_side_in_cause_of_loss = self.get_final_impact_side()
        
        parts_name_in_cause_of_loss = self.get_part_name_from_word_list()
        
        if not set(damage_types_in_cause_of_loss).intersection({"spot", "scratch", "dent", "tear", "dislocation"}):
          chance_for_glass_damage_only= True
        
        if parts_name_in_cause_of_loss == ['Front Glass'] and impact_side_in_cause_of_loss == 'Front' and chance_for_glass_damage_only and not branch_tree_hail_is_present:
          WS_damage_flag = True 
        
        return WS_damage_flag
