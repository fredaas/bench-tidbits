#!/usr/bin/env bash

set terminal png size 800,600 font 'courier'
set size 1,1
set xtic rotate by 0 right offset 0.5,0
set key r
set grid ytics
set style data lp
set output 'out.png'

set xtic 500
set xlabel 'N'
set ylabel 'Latency'
plot 'stack_out.txt' u 1:2 title 'v1', \
     ''              u 1:3 title 'v2', \
