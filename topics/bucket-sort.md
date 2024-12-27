# Bucket Sort

Bucket sort, or bin sort, is a sorting algorithm that works by distributing the elements of an array into a number of buckets. Each bucket is then sorted individually, either using a different sorting algorithm or by recursively applying the bucket sorting algorithm. It is a distribution sort, a generalization of pigeonhole sort that allows multiple keys per bucket, and is a cousin of radix sort in the most-to-least significant digit flavor.

Bucket sort is mainly useful when input is uniformly distributed over a range. When the input contains several keys that are close to each other (clustering), those elements are likely to be placed in the same bucket, which results in some buckets containing more elements than others. The worst-case scenario occurs when all the elements are placed in a single bucket.
