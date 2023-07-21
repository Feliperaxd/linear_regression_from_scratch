from typing import Optional, Tuple, Union
import matplotlib.pyplot as plt
import random

#  LINEAR REGRESSION FROM SCRATCH!
#  NO NUMPY!
#  But with random and matplotlib (to visualize)

class LinearRegression:
    
    
    def __init__(
        self: 'LinearRegression',
        number_of_rows: Optional[int] = None,
        x_independent: Optional[Tuple[Union[int, float]]] = None,
        y_dependent: Optional[Tuple[Union[int, float]]] = None
    ) -> None:
            
        if not number_of_rows:
            number_of_rows = random.randint(0, 100)
            
        if not x_independent:
            x_independent = tuple(
                random.uniform(a=-100, b=100) for i in range(number_of_rows)
                )
            
        if not y_dependent:
            y_dependent = tuple(
                random.uniform(a=-100, b=100) for i in range(number_of_rows)
                ) 
            
        if len(x_independent) != len(y_dependent):
            raise ValueError("Independent and Dependent variables should have same length!")
        
        self.number_of_rows = len(x_independent)
        self.x_independent = x_independent
        self.y_dependent = y_dependent
        self.estimated_y_values = 0
        self.slope = 0
        self.intercept = 0
        self.sum_xy = 0
        self.sum_x_squared = 0 
    
    #  Calculate slope and intercept!
    def calculate_data(
        self: 'LinearRegression'
    ) -> Tuple[Tuple[float], Tuple[float]]:

        for x, y in zip(self.x_independent, self.y_dependent):
            self.sum_xy += x * y
            self.sum_x_squared += x ** 2
    
        #  Set the slope!
        self.slope = self.number_of_rows * self.sum_xy
        self.slope -= sum(self.x_independent) * sum (self.y_dependent)
        self.slope /= self.number_of_rows * self.sum_x_squared - (sum(self.x_independent) ** 2)
        
        #  Set the intercept
        x_independent_avg = sum(self.x_independent) / len(self.x_independent)
        y_dependent_avg = sum(self.y_dependent) / len(self.y_dependent)
        self.intercept = y_dependent_avg - self.slope * x_independent_avg

        self.estimated_y_values  = tuple(
            [self.slope * x + self.intercept for x in self.x_independent]
        )
        
        return self.x_independent, self.estimated_y_values 

    #  Create and show chart!
    def draw_chart(
        self: 'LinearRegression',
        line: Optional[bool] = True,
        dots: Optional[bool] = True,
        line_color: Optional[str] = 'Red',
        dots_color: Optional[str] = 'Blue',
        x_label: Optional[str] = '-X Axis-',
        y_label: Optional[str] = '-Y Axis-',
        title: Optional[str] = 'Linear Regresss'
    ) -> None:
        
        if line:
            plt.plot(
                self.x_independent,
                self.estimated_y_values,
                color=line_color
            )
            
        if dots:
            for x, y in zip(self.x_independent, self.y_dependent):
                plt.scatter(
                    x=x, y=y,
                    color=dots_color
                    )

        plt.title(title)
        plt.xlabel(x_label)
        plt.ylabel(y_label)
        plt.show()
#:)