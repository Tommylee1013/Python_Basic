class CalValue(object) :
    def __init__(self) :
        self._present = 0
        self._future = 0
        self._interest = 0
        self._period = 0
    
    @property
    def present(self) :
        return self._present
    
    @present.setter
    def present(self, value) :
        self._present = value
    
    @property
    def future(self) :
        return self._future
    
    @future.setter
    def future(self, value) :
        self._future = value
    
    @property
    def interest(self) :
        return self._interest
    
    @interest.setter
    def interest(selt, value) :
        self._interest = value
        
    @property
    def period(self) :
        return self._period
    
    @period.setter
    def period(selt, value) :
        self._period = value
    
    def future_to_present(self) :
        self._present = self._future / (1 + self._interest) ** self._period
        return self._present
    
    def present_to_future(self) :
        self._future = self._present * (1 + self._interest) ** self._period
        return self._present
