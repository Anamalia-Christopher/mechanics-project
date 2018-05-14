import math


class Mechanics:
    gravity = 9.81  # m/s^2
    # velocity, spring_k, extension

    def __init__(self, *args, **kwargs):

        self.find = args
        print(self.find)
        self.data = kwargs
        print(self.data)

    def rest_mass(self):
        # necessary that force has to be run

        # This functions calculates the mass of the object on the
        #  launcher when the spring is uncompressed to be launched
        print('Calculate mass of object to be projected using the Force of '
              'gravity and the inlination angle\n of the device\n\n')
        self.force()
        self.rest_m = math.fabs(self.f / (self.gravity*math.sin(self.data['angle'])))
        print('Rest mass is ', self.rest_m, ' kg')

    def launch_vel(self):

        # This function calculates the launch velocity of projectile

        print("Calculates the launch velocity using the spring extension, spring constant and measured mass\n\n'")
        self.velocity = math.sqrt((self.data['spring_k'] * self.data['extension']**2)/self.data['mass'])
        print('Launch velocity is ', self.velocity, ' m/s^2')

    def vel_comp(self):
        # this function calculates the 2 dimensional components of the launch velocity; the vertical component
        vertical_vel = self.data['velocity']*math.cos(math.radians(self.data['angle']))
        print('Vertical component of velocity is',vertical_vel,'m/s')
        horzontal_vel = self.data['velocity']*math.sin(math.radians(self.data['angle']))
        print('Horizontal component of velocity is',horzontal_vel,'m/s')

    def launch_mass(self):
        # This function calculates the mass of the object using the
        # additional compressed extension aside the rest or normal extension

        # ext = additional extension from the additional compression of spring to launch projectile
        print('The extension required is obtained from compressing the spring additionally to launch projectile')
        print('Calculates the mass of the object using the the calcuated launch velocity essentially\n\n')
        self.launch_m = (self.data['spring_k']*self.data['extension']**2)/self.data['velocity']**2
        print('Launch mass is', self.launch_m, ' kg')

    def force(self):
        # Thia function calculates the normal force
        # or weight of mass in newton or when angle is 90 degrees

        self.f = self.data['spring_k'] * self.data['extension']
        print('weight of mass is', self.f, 'newton')

    def launch_force(self):
        self.force()
        launch_f = self.f * math.sin(math.radians(self.data['angle']))
        print(launch_f, 'newton is exerted on spring, launch force is', launch_f, 'newton')
        return launch_f

    def p_range(self):
        # this function calculates the range of the projectile
        self.rangeX = (self.data['velocity']**2 * math.sin(math.radians(2 * self.data['angle'])))/self.gravity
        print('The range of projectile is', self.rangeX, 'meters')

    def max_height(self):
        # This function calculates the maximum height attained by the projectile
        self.max_h = (self.data['velocity']**2 * (math.sin(math.radians(self.data['angle'])))**2)/(2*self.gravity)
        print('Maximum height attaned by projectile is', self.max_h, 'meters')

    # calculated mass disparity

    def mass_calc_disp(self):
        self.rest_mass();self.launch_mass()
        self.mass_disparity = self.rest_m - self.launch_m
        print('rest and launch mass disparity is' ,self.mass_disparity, ' kg')


    # efficiency in calculated masses


    def mass_eff(self):
        self.launch_mass();self.rest_mass()
        print('This function allows you to calculate the effeciency between the calculated mass and the measured mass\n\n')


        option = int(input('Select calculated mass type to find its efficiency\n1.rest mass, 2.launch mass\n:'))

        if option == 1:

            error_percentage = ((self.data['mass'] - self.rest_m)/self.data['mass'])*100
            print('mass percentage error is', error_percentage, '%\n\n')
            efficiency = 100 - error_percentage
            print('The error in the calculated mass relative to measured mass is',self.data['mass'] - self.rest_m,
                  'kg\n The percentage error is', error_percentage, '%')
            return efficiency

        if option == 2:

            error_percentage =( ((self.data['mass'] - self.launch_m))/self.data['mass'])*100
            print('mass percentage error is', error_percentage, '%\n\n')
            efficiency = 100 - error_percentage
            print('The error in the calculated mass relative to measured mass is', self.data['mass'] - self.launch_m,
                  'kg/n The percentage error is', error_percentage,'%')
            return efficiency




    def run_all(self):
        functions = {'mass efficiency': 'self.mass_eff()', 'mass disparity': 'self.mass_calc_disp()', 'maximum height': 'self.max_height()',
                     'range': 'self.p_range()', 'launch force': 'self.launch_force()', 'components of velocity': 'self.vel_comp()', 'launch velocity': 'self.launch_vel()',
                     'launch mass': 'self.launch_mass()', 'rest mass': 'self.rest_mass()', 'force': 'self.force()'}
        print(functions.keys())

        for i in self.find:

            if i in functions.keys():
                try:
                    exec(functions[i])
                except Exception:
                    print(Exception)
                    print('you did not supply a vital variable')
                    quit()






function_available = ['mass efficiency', 'mass disparity', 'maximum height', 'range', 'launch force', 'components of velocity', 'launch velocity', 'launch mass', 'rest mass', 'force']
for i, j in enumerate(function_available):i+=1;print(i,j)
#

# Mechanics('rest mass', 'force','launch velocity', mass= 23, extension= 50, velocity= 34, spring_k= 12,angle=23).run_all()

Mechanics('rest mass','force','launch velocity',mass=34, extension=100, velocity=564, spring_k= 232,angle= 2311).run_all()






"Authors" = "Christopher and William"
