class Book:
    '''
    Class: Book contains the detail of the books. It allows comparing 
    two instances accoring to the rank.
    for example b1 < b2 if  b1.rank < b2.rank 
    '''
    def __init__(self, key, title, group, rank, similar):
        self.key = key
        self.title = title
        self.group = group
        self.rank = int(rank) 
        self.similar = similar
    
    def __lt__(self, a) :  
        '''
        This function allows to make direct comparation using the operator <
        '''
        # change this to be title instead of rank
        # make sure all titles being compared are bot lower case
        return str(self.title).lower()<str(a.title).lower()
        # return self.rank < a.rank 

    def __gt__(self, a) :  
        '''
        This function allows to make direct comparation using the operator >
        '''
        return str(self.title).lower()>str(a.title).lower()
        # return self.rank > a.rank

    def __le__(self,a):
        return str(self.title).lower()<=str(a.title).lower()

    def __ge__(self,a):
        return str(self.title).lower()>=str(a.title).lower()

    def __eq__(self,a):
        if(len(self.title)>=len(a.title)):
            return str(self.title).lower().startswith(str(a.title).lower()) or str(self.title).lower() == str(a.title).lower()
        return str(a.title).lower().startswith(str(self.title).lower()) or str(self.title).lower() == str(a.title).lower()
        # return str(self.title).lower() in str(a.title).lower() and self<=a and self>=a


    def __str__(self):
        '''
        function returns a string containting the book information
        '''
        return f"\n\tBook: {self.key}\n\tTitle: {self.title}\n\tGroup: {self.group}\n\tRank: {self.rank}"