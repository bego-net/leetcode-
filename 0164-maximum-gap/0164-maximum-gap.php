<?php

class Solution {

    function maximumGap($nums) {

        $n = count($nums);

        if ($n < 2) {
            return 0;
        }

        $minNum = min($nums);
        $maxNum = max($nums);

        if ($minNum == $maxNum) {
            return 0;
        }

        // Bucket size
        $bucketSize = max(1, intdiv(($maxNum - $minNum), ($n - 1)));

        // Number of buckets
        $bucketCount = intdiv(($maxNum - $minNum), $bucketSize) + 1;

        $bucketMin = array_fill(0, $bucketCount, PHP_INT_MAX);
        $bucketMax = array_fill(0, $bucketCount, PHP_INT_MIN);
        $used = array_fill(0, $bucketCount, false);

        // Put numbers into buckets
        foreach ($nums as $num) {

            $idx = intdiv(($num - $minNum), $bucketSize);

            $bucketMin[$idx] = min($bucketMin[$idx], $num);
            $bucketMax[$idx] = max($bucketMax[$idx], $num);

            $used[$idx] = true;
        }

        $maxGap = 0;
        $prevMax = $minNum;

        // Find maximum gap
        for ($i = 0; $i < $bucketCount; $i++) {

            if (!$used[$i]) {
                continue;
            }

            $maxGap = max($maxGap, $bucketMin[$i] - $prevMax);

            $prevMax = $bucketMax[$i];
        }

        return $maxGap;
    }
}

$solution = new Solution();

$nums = [3, 6, 9, 1];

echo $solution->maximumGap($nums);

?>