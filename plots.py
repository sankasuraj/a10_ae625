from pysph.solver.utils import load
from pysph.tools.interpolator import Interpolator
from pysph.examples.ghia_cavity_data import get_u_vs_y, get_v_vs_x
import numpy as np
import matplotlib.pyplot as plt
import os

cwd = os.getcwd()

def l2_error(theoritical, numerical):
	difference = theoritical - numerical
	temp = sum(difference * difference)
	return np.sqrt(temp) / len(theoritical)

def get_data():
	error_u = {}
	error_v = {}
	for kernel in ['cs', 'g', 'qs', 'wq']:
		for nx in [50, 100, 200]:
			for hdx in [1.0, 1.5, 2.0]:
				sub_dir = kernel + '_' + str(hdx) + '_' + str(nx) 	
				files = []
				for fil in os.listdir(cwd + '/' + sub_dir):
					if fil.endswith(".npz") and fil != 'results.npz':
						files.append(fil)
				f_num = [int(f.split('_')[1].split('.')[0]) for f in files]
				zipped = zip(f_num, files)
				last_file = sorted(zipped)[-1][1]
				data = load(sub_dir + '/' + last_file)
				_x = np.linspace(0,1,nx)
				xx, yy = np.meshgrid(_x, _x)
				interp = Interpolator(list(data['arrays'].values()), x=xx, y=yy)
				ui = np.zeros_like(xx)
				vi = np.zeros_like(xx)
				interp.update_particle_arrays(list(data['arrays'].values()))
				_u = interp.interpolate('u')
				_v = interp.interpolate('v')
				_u.shape = nx, nx
				_v.shape = nx, nx
				ui += _u
				vi += _v
				particle = data['arrays']
				fluid = particle['fluid']
				u = fluid.u
				v = fluid.v
				ui = np.ravel(ui)
				vi = np.ravel(vi)
				error_u[sub_dir] = l2_error(ui, u)
				error_v[sub_dir] = l2_error(vi, v)
	return error_u, error_v

def plot():
	error_u, error_v = get_data()
	for hdx in [1.0, 1.5, 2.0]:
		for nx in [50, 100, 200]:
			plt.figure(figsize=(17.0, 10.0))
			y_axis1 = [error_u['cs_'+str(hdx)+'_'+str(nx)], error_u['g_'+str(hdx)+'_'+str(nx)], 
					error_u['qs_'+str(hdx)+'_'+str(nx)], error_u['wq_'+str(hdx)+'_'+str(nx)]]
			y_axis2 = [error_v['cs_'+str(hdx)+'_'+str(nx)], error_v['g_'+str(hdx)+'_'+str(nx)], 
					error_v['qs_'+str(hdx)+'_'+str(nx)], error_v['wq_'+str(hdx)+'_'+str(nx)]]
			plt.subplot(211)
			plt.bar([1, 2, 3, 4], y_axis1, align = 'center', color='b', width=0.2, label='X-velocity Error')
			plt.xticks([1, 2, 3, 4], ['CubicSpline', 'Gaussian', 'QuinticSpline', 'WendlandQuintic'])
			plt.title('Error in Velocities for each Kernel for hdx=%s and nx=%s'%(hdx, nx), 
				fontweight='bold', fontsize=24)
			plt.ylabel('Error in X-velocity', fontsize=20, fontweight='bold')
			plt.subplot(212)
			plt.bar([1, 2, 3, 4], y_axis2, align = 'center', color='r', width=0.2, label='Y-velocity Error')
			plt.xticks([1, 2, 3, 4], ['CubicSpline', 'Gaussian', 'QuinticSpline', 'WendlandQuintic'])
			plt.ylabel('Error in Y-velocity', fontsize=20, fontweight='bold')
			plt.savefig('kernels_%s_%serror.png'%(int(10*hdx), nx))
			plt.close()

	for kernel in ['cs', 'g', 'qs', 'wq']:
		for hdx in [1.0, 1.5, 2.0]:
			y_axis1 = [error_u[kernel+'_'+str(hdx)+'_50'], error_u[kernel+'_'+str(hdx)+'_100'], 
					error_u[kernel+'_'+str(hdx)+'_200']]
			y_axis2 = [error_v[kernel+'_'+str(hdx)+'_50'], error_v[kernel+'_'+str(hdx)+'_100'], 
					error_v[kernel+'_'+str(hdx)+'_200']]
			plt.figure(figsize=(17.0, 9.0))
			plt.subplot(211)
			plt.bar([1, 2, 3], y_axis1, align='center', color='b', width=0.2, label='X-velocity Error')
			plt.xticks([1, 2, 3], ['nx=50', 'nx=100', 'nx=200'])
			plt.title('Error in Velocities vs nx for hdx='+str(hdx), fontweight='bold', fontsize=24)
			plt.ylabel('Error in X-velocity', fontsize=20, fontweight='bold')
			plt.subplot(212)
			plt.bar([1, 2, 3], y_axis2, align='center', color='r', width=0.2, label='Y-velocity Error')
			plt.xticks([1, 2, 3], ['nx=50', 'nx=100', 'nx=200'])
			plt.ylabel('Error in Y-velocity', fontsize=20, fontweight='bold')
			plt.savefig('nx_%s_%serror.png'%(kernel, int(10*hdx)))
			plt.close()

	for kernel in ['cs', 'g', 'qs', 'wq']:
		for nx in [50, 100, 200]:
			y_axis1 = [error_u[kernel+'_1.0_'+str(nx)], error_u[kernel+'_1.5_'+str(nx)], 
					error_u[kernel+'_2.0_'+str(nx)]]
			y_axis2 = [error_v[kernel+'_1.0_'+str(nx)], error_v[kernel+'_1.5_'+str(nx)], 
					error_v[kernel+'_2.0_'+str(nx)]]
			plt.figure(figsize=(17.0, 9.0))
			plt.subplot(211)
			plt.bar([1, 2, 3], y_axis1, align='center', color='b', width=0.2, label='X-velocity Error')
			plt.xticks([1, 2, 3], ['hdx=1.0', 'hdx=1.5', 'hdx=2.0'])
			plt.title('Error in Velocities vs hdx for nx='+str(nx), fontweight='bold', fontsize=24)
			plt.ylabel('Error in X-velocity', fontsize=20, fontweight='bold')
			plt.subplot(212)
			plt.bar([1, 2, 3], y_axis2, align='center', color='r', width=0.2, label='Y-velocity Error')
			plt.xticks([1, 2, 3], ['hdx=1.0', 'hdx=1.5', 'hdx=2.0'])
			plt.ylabel('Error in Y-velocity', fontsize=20, fontweight='bold')
			plt.savefig('hdx_%s_%serror.png'%(kernel, nx))
			plt.close()



if __name__ == '__main__' :
	plt.ioff()
	plt.clf()
	plot()