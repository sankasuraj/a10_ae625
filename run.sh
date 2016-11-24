python cavity1.py --kernel=CubicSpline --nx=50  --tf=8.0 --openmp -d cavity_output/cs_1.0_50
python cavity1.py --kernel=CubicSpline --nx=100 --tf=8.0 --openmp -d cavity_output/cs_1.0_100
python cavity1.py --kernel=CubicSpline --nx=200 --tf=8.0 --openmp -d cavity_output/cs_1.0_200


python cavity1.py --kernel=Gaussian --nx=50 --tf=8.0 --openmp -d cavity_output/g_1.0_50
python cavity1.py --kernel=Gaussian --nx=100 --tf=8.0 --openmp -d cavity_output/g_1.0_100
python cavity1.py --kernel=Gaussian --nx=200 --tf=8.0 --openmp -d cavity_output/g_1.0_200


python cavity1.py --kernel=QuinticSpline --nx=50 --tf=8.0 --openmp -d cavity_output/qs_1.0_50
python cavity1.py --kernel=QuinticSpline --nx=100 --tf=8.0 --openmp -d cavity_output/qs_1.0_100
python cavity1.py --kernel=QuinticSpline --nx=200 --tf=8.0 --openmp -d cavity_output/qs_1.0_200


python cavity1.py --kernel=WendlandQuintic --nx=50 --tf=8.0 --openmp -d cavity_output/wq_1.0_50
python cavity1.py --kernel=WendlandQuintic --nx=100 --tf=8.0 --openmp -d cavity_output/wq_1.0_100
python cavity1.py --kernel=WendlandQuintic --nx=200 --tf=8.0 --openmp -d cavity_output/wq_1.0_200


python cavity2.py --kernel=CubicSpline --nx=50 --tf=8.0 --openmp -d cavity_output/cs_1.5_50
python cavity2.py --kernel=CubicSpline --nx=100 --tf=8.0 --openmp -d cavity_output/cs_1.5_100
python cavity2.py --kernel=CubicSpline --nx=200 --tf=8.0 --openmp -d cavity_output/cs_1.5_200


python cavity2.py --kernel=Gaussian --nx=50 --tf=8.0 --openmp -d cavity_output/g_1.5_50
python cavity2.py --kernel=Gaussian --nx=100 --tf=8.0 --openmp -d cavity_output/g_1.5_100
python cavity2.py --kernel=Gaussian --nx=200 --tf=8.0 --openmp -d cavity_output/g_1.5_200


python cavity2.py --kernel=QuinticSpline --nx=50 --tf=8.0 --openmp -d cavity_output/qs_1.5_50
python cavity2.py --kernel=QuinticSpline --nx=100 --tf=8.0 --openmp -d cavity_output/qs_1.5_100
python cavity2.py --kernel=QuinticSpline --nx=200 --tf=8.0 --openmp -d cavity_output/qs_1.5_200


python cavity2.py --kernel=WendlandQuintic --nx=50 --tf=8.0 --openmp -d cavity_output/wq_1.5_50
python cavity2.py --kernel=WendlandQuintic --nx=100 --tf=8.0 --openmp -d cavity_output/wq_1.5_100
python cavity2.py --kernel=WendlandQuintic --nx=200 --tf=8.0 --openmp -d cavity_output/wq_1.5_200


python cavity3.py --kernel=CubicSpline --nx=50 --tf=8.0 --openmp -d cavity_output/cs_2.0_50
python cavity3.py --kernel=CubicSpline --nx=100 --tf=8.0 --openmp -d cavity_output/cs_2.0_100
python cavity3.py --kernel=CubicSpline --nx=200 --tf=8.0 --openmp -d cavity_output/cs_2.0_200


python cavity3.py --kernel=Gaussian --nx=50 --tf=8.0 --openmp -d cavity_output/g_2.0_50
python cavity3.py --kernel=Gaussian --nx=100 --tf=8.0 --openmp -d cavity_output/g_2.0_100
python cavity3.py --kernel=Gaussian --nx=200 --tf=8.0 --openmp -d cavity_output/g_2.0_200


python cavity3.py --kernel=QuinticSpline --nx=50 --tf=8.0 --openmp -d cavity_output/qs_2.0_50
python cavity3.py --kernel=QuinticSpline --nx=100 --tf=8.0 --openmp -d cavity_output/qs_2.0_100
python cavity3.py --kernel=QuinticSpline --nx=200 --tf=8.0 --openmp -d cavity_output/qs_2.0_200


python cavity3.py --kernel=WendlandQuintic --nx=50 --tf=8.0 --openmp -d cavity_output/wq_2.0_50
python cavity3.py --kernel=WendlandQuintic --nx=100 --tf=8.0 --openmp -d cavity_output/wq_2.0_100
python cavity3.py --kernel=WendlandQuintic --nx=200 --tf=8.0 --openmp -d cavity_output/wq_2.0_200


cp plots.py cavity_output/
cp report.tex cavity_output/

cd cavity_output/
python plots.py

pdflatex report.tex
pdflatex report.tex

mv report.pdf ../
cd ../

rm -rf cavity_output