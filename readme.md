# Python Path Tracer

A python implementation of the "Raytracing In One Weekend" minibook (https://www.amazon.com/Ray-Tracing-Weekend-Minibooks-Book-ebook/dp/B01B5AODD8/ref=sr_1_1?ie=UTF8&qid=1524022612&sr=8-1&keywords=raytracing+in+one+weekend).

Performance is ok with Pypy thus far for the small image in the book.  I eventually plan to experiment with multiprocessing
for parallelism as well as profiling and using c foreign functions, possibly with SIMD using intel ispc.