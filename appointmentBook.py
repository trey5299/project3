
import .var = util.Collection
import .var =.LinkedList
import .var = util.List

def class AppointmentBook extends AbstractAppointmentBook<Appointment> {
     List<Appointment> appointmentList

    def AppointmentBook(){
        appointmentList = new LinkedList<Appointment>();



     @Override
       String getOwnerName():
       return null;


    @Override
     Collection getAppointments():
        return appointmentList;


    @Override
     addAppointment(Appointment):



