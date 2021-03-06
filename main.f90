program Main

implicit none

integer :: i,u,z,x,y,j
real(4), dimension(:,:), allocatable :: m
real(4), dimension(:,:), allocatable :: n
real(4) :: r(5,5)

u=1
z=2
x=3
y=5

!read the M.dat
open(unit=u, file='M.dat', status='old')
allocate( m(y,x))

do i = 1,y
  read(u,*) (m(i,j),j=1,x)
enddo

close(u)

write(*,*) "N="
do i = 1,y
  write(*,'(5f9.2)') (m(i,:))
enddo

!read the N.dat
open(unit=z, file='N.dat', status='old')
allocate( n(x,y))

do i = 1,x
  read(z,*) (n(i,j),j=1,y)
enddo

close(z)

write(*,*) "M="
do i = 1,x
  write(*,'(5f9.2)') (n(i,:))
enddo


!call the subroutine
call Matrix_multip(m,n,r)
write(*,*) "M*N="
write(*,'(5f9.2)') r

deallocate(m,n)

u=50
open(unit=u,file='MN.dat',status='replace')
write(u,'(5f9.2)') r
close(u)

end program Main

