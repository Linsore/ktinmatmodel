//create kernel
cl_kernel krnl = clCreateKernel(program, "matmult", NULL);
cl_mem srcBuff = clCreateBuffer(context, CL_MEM_READ_ONLY | CL_MEM_COPY_HOST_PTR, sizeof(float)*size*size, src, NULL);
cl_mem dstBuff = clCreateBuffer(context, CL_MEM_READ_ONLY | CL_MEM_COPY_HOST_PTR, sizeof(float)*size*size, dst, NULL);
//buffer for result
float* res = (float*)malloc(sizeof(float)*size*size);
cl_mem resBuff = clCreateBuffer(context, CL_MEM_WRITE_ONLY, sizeof(float)*size*size, NULL, NULL);
//set kernel args
clSetKernelArg(krnl, 0, sizeof(cl_mem), &srcBuff);
clSetKernelArg(krnl, 1, sizeof(cl_mem), &dstBuff);
clSetKernelArg(krnl, 2, sizeof(cl_mem), &resBuff);
clSetKernelArg(krnl, 3, sizeof(int), &size);
//run
size_t dimSizes[] = { size,size };
clEnqueueNDRangeKernel(commandQueue, krnl, 2, NULL, dimSizes, NULL, NULL, NULL, NULL);
clEnqueueReadBuffer(commandQueue, resBuff, CL_TRUE, 0, sizeof(float)*size*size, res, 0, NULL, NULL);
return res;
__kernel void matmult(__global const float* src, __global const float* dst, 
                           __global float* ret, const int n) {
       int y=get_global_id(0);
       int x=get_global_id(1);
       float sum=0;
       for(int i=0;i<n;i++){
           sum+=src[y*n+i] * dst[i*n+x];
       }
       ret[y*n+x]=sum;
}