// Checker A (release name check_parts_bb.c): exact clique search with greedy-colouring bound (Tomita style), bitsets, with an optional split of the top-level branches into parts.
// usage: check_parts_bb file r s [part nparts [side]]   side 0 = clique of size r, side 1 = independent set of size s, 2 = both.
// The parts take top-level branches idx with idx % nparts == part of one fixed colouring order, so together the parts cover the whole search.
// Finds K_r in G and K_s in complement(G). Parser: reads all 0/1 tokens inside [[ ]]; checks square, symmetric, zero diagonal.
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdint.h>
#include <time.h>
typedef uint64_t u64;
int n,W; u64 *adj[2];
static int K; static long nodes; static int found; static int PART=0,TOT=1,SIDE=2;
static int pc(u64*a){int c=0;for(int i=0;i<W;i++)c+=__builtin_popcountll(a[i]);return c;}
static void expand(u64*P,int size,u64*A){
  if(found)return; nodes++;
  if(size>=K){found=1;return;}
  int cnt=pc(P); if(size+cnt<K)return;
  int *order=malloc(sizeof(int)*cnt),*col=malloc(sizeof(int)*cnt); int m=0;
  u64*U=malloc(W*8),*Q=malloc(W*8); memcpy(U,P,W*8); int c=0;
  while(1){int any=0;for(int i=0;i<W;i++)if(U[i]){any=1;break;} if(!any)break; c++; memcpy(Q,U,W*8);
    while(1){int v=-1;for(int i=0;i<W;i++)if(Q[i]){v=i*64+__builtin_ctzll(Q[i]);break;} if(v<0)break;
      Q[v>>6]&=~(1ULL<<(v&63));U[v>>6]&=~(1ULL<<(v&63)); for(int i=0;i<W;i++)Q[i]&=~A[(size_t)v*W+i];
      order[m]=v;col[m]=c;m++;}}
  u64*NP=malloc(W*8); memcpy(Q,P,W*8);
  for(int idx=m-1;idx>=0;idx--){ if(size+col[idx]<K)break; int v=order[idx];
    if(size==0 && (idx%TOT)!=PART){ Q[v>>6]&=~(1ULL<<(v&63)); continue; }
    for(int i=0;i<W;i++)NP[i]=Q[i]&A[(size_t)v*W+i];
    expand(NP,size+1,A); if(found)break; Q[v>>6]&=~(1ULL<<(v&63)); }
  free(order);free(col);free(U);free(Q);free(NP);
}
int main(int argc,char**argv){
  if(argc>=6){PART=atoi(argv[4]);TOT=atoi(argv[5]);} if(argc>=7)SIDE=atoi(argv[6]);
  FILE*f=fopen(argv[1],"r"); int r=atoi(argv[2]),s=atoi(argv[3]);
  int cap=1<<24; unsigned char*buf=malloc(cap); int L=0; int ch;
  while((ch=fgetc(f))!=EOF){ if(ch=='['||ch==']'||ch==' '||ch=='\n'||ch=='\r'||ch==','){} else if(ch=='0'||ch=='1'){ if(L>=cap){cap*=2;buf=realloc(buf,cap);} buf[L++]=ch-'0'; } else {fprintf(stderr,"bad char %d\n",ch);return 2;} }
  n=1;while((long)n*n<L)n++; if((long)n*n!=L){fprintf(stderr,"not square %d\n",L);return 2;}
  W=(n+63)/64; adj[0]=calloc((size_t)n*W,8); adj[1]=calloc((size_t)n*W,8); long edges=0;
  for(int i=0;i<n;i++)for(int j=0;j<n;j++){ int a=buf[i*n+j],b=buf[j*n+i]; if(a!=b){printf("ASYM\n");return 1;} if(i==j){if(a){printf("LOOP\n");return 1;}continue;}
    if(a){adj[0][(size_t)i*W+(j>>6)]|=1ULL<<(j&63);edges++;} else adj[1][(size_t)i*W+(j>>6)]|=1ULL<<(j&63);}
  printf("A: n=%d edges=%ld\n",n,edges/2);
  u64*all=calloc(W,8);for(int i=0;i<n;i++)all[i>>6]|=1ULL<<(i&63);
  for(int side=0;side<2;side++){ if(SIDE<2&&side!=SIDE)continue; K=side?s:r;found=0;nodes=0;clock_t t=clock();
    expand(all,0,adj[side]); printf("A[part %d/%d]: %s of size %d exists: %s (nodes %ld, %.1fs)\n",PART,TOT,side?"independent set":"clique",K,found?"YES":"no",nodes,(double)(clock()-t)/CLOCKS_PER_SEC);fflush(stdout);}
  return 0;
}
