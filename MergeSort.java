class MergeSort{
    static void Merge(int[] arr, int left, int mid, int right){
        int n1 = mid - left + 1;
        int n2 = right - mid;
        int[] leftArr = new int[n1];
        int[] rightArr = new int[n2];

        for(int i = 0; i < n1; i++){leftArr[i] = arr[left + 1];}
        for(int j = 0; j < n2; j++){rightArr[j] = arr [mid + 1 + j];}

        int iIndex = 0, jIndex = 0, kIndex = 0;
        while(iIndex < n1 && jIndex < n2){
            if(leftArr[iIndex] <= rightArr[jIndex]){
                arr[kIndex++] = leftArr[iIndex++];
            }else{
                arr[kIndex++] = rightArr[jIndex++];
            }
         }
        while(iIndex < n1){
               arr[kIndex++] = leftArr[iIndex++];
            }
            while(jIndex < n2){
               arr[kIndex++] = rightArr[jIndex++];
            }

    }
    static void MergeSort(int[] arr, int left, int right){
        if(left < right){
            int mid = (left - right) / 2;
            MergeSort(arr, left, mid);
            MergeSort(arr, mid + 1, right);

            Merge(arr, left, mid, right);
        }
    }
    static void print(int[] arr){
        for(int i: arr){
            System.out.print(i + " ");
        }
    }
    public static void main(String[] args){
        int arr[] = {100, 11, 20, 24, 69};
        print(arr);
        System.out.println();
        MergeSort(arr, 0, arr.length - 1);
        print(arr);
    }
}

