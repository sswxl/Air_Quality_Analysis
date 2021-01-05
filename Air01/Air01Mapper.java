
package Air01;

import java.io.IOException;

import org.apache.hadoop.io.DoubleWritable;
import org.apache.hadoop.io.LongWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Mapper;

public class Air01Mapper extends Mapper<LongWritable, Text, Text, DoubleWritable>{
	 int[] pollutant_levels = {0, 35, 75, 115, 150, 250, 350, 500};
     int[] IAQI_levels = {0, 50, 100, 150, 200, 300, 400, 500};
     double IAQI;
    @Override
    protected void map(LongWritable key, Text value, Context context) throws IOException, InterruptedException {
        if (key.toString().equals("0")) {
            return;
	}
        String line = value.toString();
        String[] fields = line.split(",");
        double PM25 = Double.parseDouble(fields[3]);
        String city = fields[16];
        
        //计算IAQI
        for (int i = 0; i < 7; i++){
            if (PM25 > pollutant_levels[i] && PM25 < pollutant_levels[i+1]){
                IAQI = (IAQI_levels[i+1] - IAQI_levels[i]) * (PM25 - pollutant_levels[i]) / (pollutant_levels[i+1] - pollutant_levels[i]) + IAQI_levels[i];
            }
        }
        context.write(new Text(city), new DoubleWritable(IAQI));
    }    
}
  
