
package Air01;

import java.io.IOException;

import org.apache.hadoop.io.DoubleWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Reducer;

public class Air01Reducer extends Reducer<Text, DoubleWritable, Text, Text>{
    
    @Override
    protected void reduce(Text key, Iterable<DoubleWritable> values, Context context) throws IOException, InterruptedException {
        
        double IAQI_sum = 0;
        double count = 0;
        for (DoubleWritable value : values) {
            IAQI_sum += value.get();
            count += 1;
        }
        double IAQI_average = IAQI_sum / count;

        context.write(new Text(key), new Text(String.valueOf(IAQI_average)));
    }
}
