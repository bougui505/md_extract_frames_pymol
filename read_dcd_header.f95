program read_dcd_header
implicit none
character*80 dcdfilename
character*4 HDR
integer ICNTRL(20)
integer NTITL
integer j
integer natoms
character*80 TITLE(100)
real(4) :: delta
write(*,*) "What is your dcd file name?"
read(*,*) dcdfilename
open(unit=243,file=dcdfilename,form='unformatted',status="unknown")
read(243) HDR,(ICNTRL(j),j=1,9),delta,(ICNTRL(j),j=11,20)
read(243) NTITL,(TITLE(j),j=1,NTITL)
read(243) natoms
write(*,*) "# of configurations in dcd file:", ICNTRL(1)
write(*,*) "time step of first configuration:", ICNTRL(2)
write(*,*) "frequency of configurations in dcd file, dcd_freq:", ICNTRL(3)
write(*,*) "last time step in dcd file:", ICNTRL(4)
write(*,*) "timestep of simulation", delta
write(*,*) "natoms in dcd file", natoms
end program
