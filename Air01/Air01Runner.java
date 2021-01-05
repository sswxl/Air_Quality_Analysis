
package Air01;

import java.io.IOException;
import org.apache.hadoop.conf.Configuration;
import org.apache.hadoop.fs.Path;
import org.apache.hadoop.io.DoubleWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Job;
import org.apache.hadoop.mapreduce.lib.input.FileInputFormat;
import org.apache.hadoop.mapreduce.lib.output.FileOutputFormat;
import org.apache.log4j.BasicConfigurator;

public class Air01Runner {
    public static void main(String[] args) throws IOException, InterruptedException, ClassNotFoundException {
        
        BasicConfigurator.configure();
        Configuration con = new Configuration();
        Job job = Job.getInstance(con);
        job.setJarByClass(Air01Runner.class);
        
        job.setMapperClass(Air01Mapper.class);
        job.setReducerClass(Air01Reducer.class);
       
        job.setMapOutputKeyClass(Text.class);
        job.setMapOutputValueClass(DoubleWritable.class);
        
        job.setOutputKeyClass(Text.class);
        job.setOutputValueClass(Text.class);
        FileInputFormat.setInputPaths(job, new Path(args[0]));
        FileOutputFormat.setOutputPath(job, new Path(args[1]));
        
        job.waitForCompletion(true);
    }    
}
